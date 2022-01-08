"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys.

def sq_dict(a):
    sqr_value={}
    for i in range(1,a+1):
        sqr_value[i]= i ** 2
    return sqr_value


if __name__ == '__main__':
    num=int(input('please enter your number: '))
    print(sq_dict(num))

"""

"""

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys. The function should just print the keys only.

def sq_dict(a):
    sqr_value={}
    for i in range(1,a+1):
        sqr_value[i]= i ** 2
    #lambda sqr_value: for i in sqr_value.values(): print(i)
    print(sqr_value.keys())


if __name__ == '__main__':
    num=int(input('please enter your number: '))
    sq_dict(num)

"""

"""

Define a function which can generate and print a list where the values are square of numbers
between 1 and 20 (both included).


def sq_list(a):
    sqr_value=[]
    for i in range(1,a+1):
        sqr_value.append(i ** 2)
    print(sqr_value)


if __name__ == '__main__':
    num=int(input('please enter your number: '))
    sq_list(num)
"""

"""

Define a function which can generate a list where the values are square of numbers between 1 and 20
(both included). Then the function needs to print the first 5 elements in the list.

def sq_list(a):
    sqr_value=[]
    for i in range(1,a+1):
        sqr_value.append(i ** 2)
    for i in sqr_value[0:5]:
        print(i)

if __name__ == '__main__':
    num=int(input('please enter your number: '))
    sq_list(num)
"""

"""

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.

def sq_list(a):
    sqr_value=[]
    for i in range(1,a+1):
        sqr_value.append(i ** 2)
    for i in sqr_value[-5:]:
        print(i)

if __name__ == '__main__':
    num=int(input('please enter your number: '))
    sq_list(num)

"""

"""

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.

def sq_list(a):
    sqr_value=[]
    for i in range(1,a+1):
        sqr_value.append(i ** 2)
    for i in sqr_value[5:]:
        print(i)

if __name__ == '__main__':
    num=int(input('please enter your number: '))
    sq_list(num)

"""

"""

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

"""
def sq_list(a):
    sqr_value=tuple([i**2 for i in range(1,a+1)])
    print(sqr_value)

if __name__ == '__main__':
    num=int(input('please enter your number: '))
    sq_list(num)
