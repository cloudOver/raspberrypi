WORKER_USER = 'cloudover'
WORKER_GROUP = 'cloudover'
AGENTS = [
    {'type': 'image', 'module': 'corecluster.agents.image_libvirt', 'count': 4},
    {'type': 'vm', 'module': 'corecluster.agents.vm', 'count': 4},
    {'type': 'network', 'module': 'corecluster.agents.network', 'count': 4},
    {'type': 'node', 'module': 'corecluster.agents.node_libvirt', 'count': 4},
    {'type': 'storage', 'module': 'corecluster.agents.storage_libvirt', 'count': 4},
    {'type': 'console', 'module': 'corecluster.agents.console', 'count': 1},
    {'type': 'dhcp', 'module': 'coredhcp.agents.dhcp', 'count': 1},
]
MOUNT_NODES = True
REMOVE_TASKS_ON_DONE = True
REMOVE_AGENTS_ON_DONE = True
TASK_FETCH_INTERVAL = 1
IGNORE_TASKS = ['ok',
                'canceled',
                'failed',
]
