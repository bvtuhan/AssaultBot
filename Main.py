from Utils import *
import keyboard

if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('z'):
            aimAt()

        elif keyboard.is_pressed('delete'):
            shutdown()
