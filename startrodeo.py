""" Run rodeo with a Docker specific config """

from rodeo import rodeo

if __name__ == '__main__':
    rodeo.main('/home/',
               host='0.0.0.0',
               port=5000,
               browser=False)



