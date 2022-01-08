"""

Write a program which accepts a sequence of comma-separated numbers from console and
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')


usr_str=input("enter the sequence: ")
lst_seq=usr_str.split(",")
tup_seq=tuple(lst_seq)
print(lst_seq)
print(tup_seq)

"""
"""

Define a class which has at least two methods:

    getString: to get a string from console input
    printString: to print the string in upper case.

class get_print_upper():
    def __init__(self):
        self.usr_str=""

    def getString(self):
        self.usr_str=input("give your string: ")

    def printString(self):
        print(f"{(self.usr_str).upper()}")

if __name__ == '__main__':
    a = get_print_upper()
    a.getString()
    a.printString()

"""


"""

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

import math

def print_rslt(inp):
    uip_lst=inp.split(",")
    #ans_lst=[]
    C=50
    H=30
    for i in uip_lst:
        D=int(i)
        frml=((2*C*D)/H)
        Q=round(math.sqrt(round(((2*C*D)/H))))
        #ans_lst.append(Q)
        print(Q,end=",")


if __name__ == '__main__':
    usr_str=input("enter your sequence: ")
    print_rslt(usr_str)


"""

"""

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i _ j.*

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


def print_rslt(inp):
    uip_lst=inp.split(",")
    rw=int(uip_lst[0])
    cl=int(uip_lst[1])
    ans_lst=[]
    for i in range(0,rw):
        temp_lst=[]
        for j in range(0,cl):
            temp_lst.append(i*j)
        ans_lst.append(temp_lst)
    print(ans_lst)

if __name__ == '__main__':
    usr_str=input("enter your sequence: ")
    print_rslt(usr_str)

"""

"""


Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.

without,hello,bag,world

bag,hello,without,world


def print_rslt(inp):
    uip_lst=(inp.split(","))
    uip_lst.sort()
    print(",".join(uip_lst))


if __name__ == '__main__':
    usr_str=input("enter your sequence: ")
    print_rslt(usr_str)

"""

"""


Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT


"""


if __name__ == '__main__':
    uip=[]
    while True:
        usr_str=input()
        if len(usr_str)==0:
            break
        uip.append(usr_str.upper())

    print(f"\n".join(uip))
