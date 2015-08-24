""" Run rodeo with a Docker specific config """

from flask.ext.cdn import CDN
from rodeo import rodeo

config = {'static-domain': 'localhost:8000',
          'storage-dir': '/home/data/',
          'dynamic-port': 5000}

if __name__ == '__main__':

    rodeo.app.config['CDN_DOMAIN'] = config['static-domain']
    CDN(rodeo.app)

    rodeo.main(config['storage-dir'],
               host='0.0.0.0',
               port=config['dynamic-port'],
               browser=False)
