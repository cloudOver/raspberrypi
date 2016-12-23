ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudover',
        'USER': 'cloudover',
        'PASSWORD': '_MYSQL_DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET NAMES utf8",
        }
    },
    'logs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudover',
        'USER': 'cloudover',
        'PASSWORD': '_MYSQL_LOG_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET NAMES utf8",
        }
    },
}

CACHE_URL = 'localhost'

DNS_DOMAIN = 'localdomain'

VNC_ADDRESS = '192.168.26.254'
VNC_PORTS = {
    'START': 5900,
    'EXCLUDE': []
}

AUTOREGISTER_NODE = True

USER_QUOTA = {
    'cpu': 20,
    'memory': 40000,                # in MB
    'storage': 40000*1024*1024,     # in bytes
    'redirections': 1,              # Public IP redirections
    'points': 2000,
    'public_lease': 5,
    'routed_lease': 64,
    'network_isolated': 10
}

ENABLE_ALL_PERMISSIONS = True
CREATE_ADDITIONAL_ROLES = True
CHECK_STATES = False
MAX_UPLOAD_CHUNK_SIZE = 1024*1024*10
NODE_SUSPEND_DURATION = 60 * 60 * 24
NODE_WAKEUP_TIME = 30
SECRET_KEY = '_SECRET_KEY'
API_STATS = False
INSTALLATION_ID = '_INSTALLATION_ID'

APPS = [
    'corecluster.app',
    'corecluster-auth-db.app',
    'corecluster-algorithm-storage-default.app',
    'corecluster-algorithm-node-default.app',
    'corecluster-algorithm-id-uuid.app',
    'corecluster-storage-libvirt.app',
    'corenetwork.app',
    'coredhcp.app',
    'coretalk.app',
    'thunderscript.app',
]

LOG_PREFIX = 'co_'
