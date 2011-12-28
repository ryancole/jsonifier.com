bind = 'unix:/tmp/jsonifier.sock'
proc_name = 'jsonifier'
workers = 3
worker_class = 'gevent'
daemon = True
logfile = '/home/ryan/logs/jsonifier.log'