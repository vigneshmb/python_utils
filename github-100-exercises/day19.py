"""

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))

"""
"""

Please write a program to print the running time of execution of "1+1" for 100 times.

import datetime

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)

"""
"""

Please write a program to shuffle and print the list [3,6,7,8].

import random

lst = [3,6,7,8]
random.shuffle(lst)
print(lst)

"""
"""

Please write a program to generate all sentences where
subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

if __name__ == '__main__':
    sub=['I','You']
    verb=['Play','Love']
    obj=['Hockey','Football']
    for i in sub:
        for j in verb:
            for k in obj:
                print(f'{i} {j} {k}')

"""
