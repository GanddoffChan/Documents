from datetime import *
from pynput import *
from pynput.keyboard import *
from random import *
from time import *

k = Controller()

while True:
    d = datetime.now()
    h = d.hour
    m = d.minute
    s = d.second
    D = d.day
    M = d.strftime('%B')
    Y = d.year

    if h == 4 and m == 20 and s >= 10:
        D = str(D)
        M = str(M)
        Y = str(Y)
        k.type('Dear all please Indicate your temperature by 8:00am ')
        k.type(D)
        k.press(Key.space)
        k.release(Key.space)
        k.type(M)
        k.press(Key.space)
        k.release(Key.space)
        k.type(Y)
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)

        k.type('Jiang Tianyuan:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Wang Xiyu:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Ryan Joo Rui An:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Lim Zheng Yan:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Leong Huen Phun:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)

        k.type('Gordon Chan Lok Hin:')
        x = uniform(36.5,37.0)
        x = str(round(x,1))
        k.type(x)
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)

        k.type('Niu Te:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Zhu Rong:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Tsan Jian Ming:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Chooi Kae Leang:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Zhou Junmin:')
        k.press(Key.shift)
        k.press(Key.enter)
        k.release(Key.enter)
        k.release(Key.shift)
        k.type('Wang Yaxin:')

        k.press(Key.enter)
        k.release(Key.enter)

        break

    sleep(1)
