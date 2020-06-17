from os import getenv


bind = '0.0.0.0:' + getenv('PORT', '8080')
reload = True
workers = 2
worker_class = 'aiohttp.GunicornWebWorker'

accesslog = '-'
