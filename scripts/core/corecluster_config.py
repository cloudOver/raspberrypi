######################################
# Basic setup                        #
######################################

# Should be only UI(s) host(s)
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/cloudOver/logs.sqlite3',
    },
}

CACHE_URL = 'localhost'
DNS_DOMAIN = 'localdomain'
VNC_ADDRESS = '127.0.0.1'
VNC_PORTS = {
    'START': 5900,
    'EXCLUDE': []
}
AUTOREGISTER_NODE = True

######################################
# User accounts                      #
######################################
USER_QUOTA = {
    'cpu': 30,
    'memory': 80000,                # in MB
    'storage': 80*1024*1024*1024,     # in bytes
    'redirections': 5,              # Public IP redirections
    'points': 2000,
    'public_lease': 2,
    'routed_lease': 128,
    'network_isolated': 128,
}

ENABLE_ALL_PERMISSIONS = True
CREATE_ADDITIONAL_ROLES = True
CHECK_STATES = False

######################################
# Advanced options                   #
######################################
MAX_UPLOAD_CHUNK_SIZE = 1024*1024*100
NODE_SUSPEND_DURATION = 60 * 60 * 24
NODE_WAKEUP_TIME = 30
SECRET_KEY = '_SECRET_KEY'

NODE_SELECT_ALGORITHM = 'corecluster.algorithms.node.simple'
STORAGE_SELECT_ALGORITHM = 'corecluster.algorithms.storage.simple'
ID_GENERATOR = 'corecluster.algorithms.id.uuid_gen'
AUTH_METHOD = 'corecluster.algorithms.auth.db'

API_STATS = False
INSTALLATION_ID = '_INSTALLATION_ID'

######################################
# Extensions                         #
######################################
APPS = [
    'corecluster.app',
    'corenetwork.app',
    'coredhcp.app',
    'coretalk.app',
    'thunderscript.app',
]

LOG_PREFIX = 'co_'
