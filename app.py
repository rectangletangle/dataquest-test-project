""" Run rodeo with a Docker specific config """

from flask.ext.cdn import CDN
from rodeo import rodeo

if __name__ == '__main__':

    rodeo.app.config['CDN_DOMAIN'] = 'localhost:8000'
    CDN(rodeo.app)

    rodeo.main('/home/data/',
               host='0.0.0.0',
               port=5000,
               browser=False)





