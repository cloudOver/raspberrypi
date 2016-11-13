#!/bin/bash

source vars.sh
cp cloudover.list /etc/apt/sources.list.d/

cp core/interfaces /etc/network/interfaces
service networking restart

wget http://packages.cloudover.org/cloudover.key -O - | apt-key add -

sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password cloudover'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password cloudover'

apt-get update
apt-get install corecluster coredhcp coretalk mysql-server htop screen ipython python-mysqldb nfs-kernel-server git dnsmasq hostapd rng-tools --yes
apt-get upgrade --yes

pip install -U thunderscript

mkdir -p /storage/core
chmod 777 /storage/core/

virsh net-destroy default
virsh net-undefine default

echo "/storage/core *(rw,sync,no_subtree_check)" >> /etc/exports

#sed -e "s/127.0.0.1/0.0.0.0/" core/mysqld.cnf > /etc/mysql/mysql.conf.d/mysqld.cnf

sed -e "s/_OSPF_TOKEN/$OSPF_TOKEN/" \
    -e "s/_QUAGGA_PASSWORD/$QUAGGA_PASSWORD/" core/corenetwork_config.py > /etc/corenetwork/config.py

sed -e "s/_SECRET_KEY/$SECRET_KEY/" \
    -e "s/_MYSQL_DB_PASSWORD/$MYSQL_DB_PASSWORD/" \
    -e "s/_MYSQL_LOG_PASSWORD/$MYSQL_LOG_PASSWORD/" \
    -e "s/_INSTALLATION_ID/$INSTALLATION_ID/" core/corecluster_config.py > /etc/corecluster/config.py

rm /var/www/html/index.nginx-debian.html
git clone https://github.com/cloudOver/coreui.git /var/www/html/

cp core/dnsmasq.conf /etc/
cp core/hostname /etc/
cp core/hosts /etc/
cp core/rc.local /etc/
cp core/agent.py /etc/corecluster/
cp core/my.cnf /etc/mysql/my.cnf
cp core/settings.js /var/www/html/
cp core/hostapd /etc/default/
cp core/hostapd.conf /etc/hostapd/

echo "CREATE DATABASE cloudover;" | mysql -u root -pcloudover
echo "GRANT ALL PRIVILEGES ON cloudover.* TO cloudover@'localhost' IDENTIFIED BY '$MYSQL_DB_PASSWORD';" | mysql -u root -pcloudover

cc-admin migrate
cc-admin makemigrations
cc-admin migrate

echo 'from corecluster.models.core import Storage
s = Storage()
s.capacity = 20000
s.transport="netfs"
s.address="192.168.27.254"
s.dir="/storage/core"
s.name="core"
s.save()' | cc-admin shell

echo 'from corecluster.models.core import NetworkPool
n = NetworkPool()
n.address="0.0.0.0"
n.mask=0
n.mode="isolated"
n.access="public"
n.save()' | cc-admin shell

echo 'from corecluster.models.core import NetworkPool
n = NetworkPool()
n.address="192.168.28.0"
n.mask=24
n.mode="public"
n.access="public"
n.save()' | cc-admin shell

echo 'from corecluster.models.core import NetworkPool
n = NetworkPool()
n.address="192.168.128.0"
n.mask=17
n.mode="routed"
n.access="public"
n.save()' | cc-admin shell

echo 'from corecluster.models.core import Template
t = Template()
t.name="small"
t.description="Small template with 1vCPU and 512MB of RAM"
t.cpu=1
t.memory=512
t.hdd=10000
t.points=1
t.save()' | cc-admin shell

echo 'from corecluster.models.core import Template
t = Template()
t.name="medium"
t.description="Medium template with 1vCPU and 1024MB of RAM"
t.cpu=1
t.memory=1024
t.hdd=20000
t.points=2
t.save()' | cc-admin shell

echo 'from corecluster.models.core import Template
t = Template()
t.name="large"
t.description="Large template with 2vCPU and 2048MB of RAM"
t.cpu=2
t.memory=2048
t.hdd=40000
t.points=4
t.save()' | cc-admin shell

ln -s /lib/systemd/system/rpcbind.target /etc/systemd/system/multi-user.target.wants/
cc-manage configure
cc-admin createsuperuser
