
import rodeo
import os

def staticpath():
    return os.path.join(os.path.dirname(rodeo.__file__), 'static')

if __name__ == '__main__':
    print(staticpath())
