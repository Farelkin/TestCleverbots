from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()

# user = 'root'
# group = 'www-data'
# directory = '/home/cleverbots'
# bind = 'unix:/home/cleverbots/cleverbots.sock'
# bind = '134.0.119.252:' + environ.get('PORT', '8000')
bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()


env = {
    'DJANGO_SETTINGS_MODULE': 'cleverbots.settings',
}

# accesslog = '/home/cleverbots/logs/gunicorn-access.log'
# errorlog = '/home/cleverbots/logs/gunicorn-error.log'
# loglevel = 'info'
# daemon = True

reload = True
name = 'cleverbots'
