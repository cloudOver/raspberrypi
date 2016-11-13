# CloudOver Cloud Starter Kit for Raspberry PI
This is set of scripts to prepare management node on Raspberry PI computer.
Use it to prepare, install and configure your raspberry into the CoreCluster
management with simple storage. This scripts create new templates, define
storage and configure networks for CoreCluster

After installation you should be able to connect to the corecluster.pi wire-
less network and connect with all your machines in the cloud.

# Requirements
To launch your cloud on Raspberry you will need:
* One Raspberry PI 3
* SD Card, at least 16GB
* USB Ethenret adapter
* Micro USB for powering up the Raspberry PI
* At least two ethernet cords (Red and green! :)
* Optionally ethernet switch

... and as many computers as many nodes you want to connect to your cloud.

# Preparation
Retreive the Raspbian image and prepare bootable SD card for your Raspberry.
Then copy whole directory `scripts` into the / on the SD card (or to the /boot
partition, if you don't have access to the ext4 filesystem)

# Installation
Power up your raspberry. When it is ready, log in to the `pi` account with the
`raspberry` password. Go to your scripts directory:
	cd /boot/scripts
and execute installation script as root:
	sudo ./install_core.sh
At the end of the installation you will be asked for the CoreCluster admini-
strator login and password.

# Booting
When installation is done, rebot your raspberry. The wireless network
	corecluster.pi
should be available. Connect to it with the password:
	cloudoverpi
CoreUI interface should be available at the address:
	http://core.pi.cloudover.io

In case of problems feel free to contact us:
	contact@cloudover.io
