# flaskr/core.py

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

port = '11211'  # <---- New line
'''
Depending on what operating system you are using, 
the `--network` host option of Docker may not work consistently. 
In particular:
    * If you are using Mac then you will need to use host.docker.internal.
    * If you are in Linux you can use localhost.
'''
#host = 'memcached'      # <---- New line, but what to use as host address?
host = 'localhost'      # <---- New line, but what to use as host address?
memcached_uri = f'memcached://{host}:{port}'  # <--- New line
limiter = Limiter(storage_uri=memcached_uri,  # <---- Line changed
          key_func=get_remote_address)