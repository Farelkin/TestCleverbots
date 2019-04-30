from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()

user = 'root'
group = 'www-data'
directory = '/home/cleverbots'
max_requests = 1000
workers = max_workers()
bind = 'unix:/home/cleverbots/cleverbots.sock'

env = {
    'DJANGO_SETTINGS_MODULE': 'cleverbots.settings',
}

# accesslog = '/home/cleverbots/logs/gunicorn-access.log'
# errorlog = '/home/cleverbots/logs/gunicorn-error.log'
# loglevel = 'info'
# daemon = True

reload = True
name = 'cleverbots'
