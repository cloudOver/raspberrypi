WORKER_USER = 'cloudover'
WORKER_GROUP = 'cloudover'
MOUNT_NODES = True
CLEANUP_QUEUES_ON_START = True
REMOVE_TASKS_ON_DONE = True
REMOVE_AGENTS_ON_DONE = True
TASK_FETCH_INTERVAL = 5
IGNORE_TASKS = ['ok',
                'canceled',
                'failed',
]
