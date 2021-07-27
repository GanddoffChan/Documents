from random import *

c = 0

for i in range(9999):
    t1 = randint(0,9999)
    t2 = randint(0,9999)
    t3 = randint(0,9999)
    t4 = randint(0,9999)
    t5 = randint(0,9999)
    t6 = randint(0,9999)
    t7 = randint(0,9999)
    t8 = randint(0,9999)
    t9 = randint(0,9999)
    t10 = randint(0,9999)

    if t1 >= 1200 and t2>=1200 and t3>=1200 and t4>=1200 and t5>=1200 and t6>=1200 and t7>=1200 and t8>=1200 and t9>=1200 and t10>=1200:
        c +=1

print(100-c/100)
