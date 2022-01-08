"""

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
and the last half values in one line.


def tup_split(a):
    # sqr_value=tuple([i**2 for i in range(1,a+1)])
    print(a[0:5])
    print(a[5:])

if __name__ == '__main__':
    num=(1,2,3,4,5,6,7,8,9,10)
    tup_split(num)

"""

"""
Write a program to generate and print another tuple
whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


def tup_even(a):
    evn_lst=[]
    for i in a:
        if i%2==0:
            evn_lst.append(i)
    evn_tup=tuple(evn_lst)
    print(evn_tup)

if __name__ == '__main__':
    num=(1,2,3,4,5,6,7,8,9,10)
    tup_even(num)

"""

"""

Write a program which accepts a string as input to print "Yes"
if the string is "yes" or "YES" or "Yes", otherwise print "No".

def str_yes_chk(i):
    if i=='yes' or i=='YES' or i=='Yes':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    usr_inp=input('enter your string: ')
    str_yes_chk(usr_inp)
"""

"""

whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
Write a program which can map() to make a list

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
print(list(squaredNumbers))               # converting the object into list

"""

"""

Write a program which can map() and filter() to make a list whose elements are
square of even number in [1,2,3,4,5,6,7,8,9,10].

if __name__ == '__main__':
    lst=[1,2,3,4,5,6,7,8,9,10]
    new_lst=list(filter(lambda i:i%2==0,lst))
    print(new_lst)

"""

"""

Write a program which can filter()
to make a list whose elements are even number between 1 and 20 (both included).

if __name__ == '__main__':
    new_lst=list(filter(lambda i:i%2==0,range(1,21)))
    print(new_lst)
"""
