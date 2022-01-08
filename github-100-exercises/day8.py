"""

Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1

def count_words(inp):
    temp_lst=inp.split(' ')
    temp_lst.sort()
    inp_lst=[]
    for i in temp_lst:
        if inp_lst.count(i)<1:
            print(f'{i} = {temp_lst.count(i)}')
            inp_lst.append(i)

if __name__ == '__main__':
    usr_str=input("")
    count_words(usr_str)

"""

"""

Write a method which can calculate square value of number

Hints:
Using the ** operator which can be written as n**p where means n^p

def sqr_val(inp):
    print(inp**2)


if __name__ == '__main__':
    usr_str=int(input(""))
    sqr_val(usr_str)

"""

"""

Python has many built-in functions, and if you do not know how to use it,
you can read document online or find some books.
But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents,
 such as abs(), int(), raw_input()

And add document for your own function



print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)

"""

"""

Define a class, which have a class parameter and have a same instance parameter.

class car_name:
    def __init__(self,name):
        self.name=name


if __name__ == '__main__':
    car_model=input('Enter your model:')
    car=car_name(car_model)
    print(car.name)

"""
