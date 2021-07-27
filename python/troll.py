from pynput import *
from pynput.keyboard import *
from random import *
from string import *
from time import *

k = Controller()

for t in range(420):
    x = ''.join(choice('chem feg') for _ in range(8))
    k.type(x)
    k.press(Key.enter)
    k.release(Key.enter)
    sleep(0.1)
