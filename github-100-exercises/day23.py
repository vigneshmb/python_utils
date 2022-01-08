"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5

Then, the output of the program should be:

5


if __name__ == '__main__':
    usr_scr=list(set(input().split()))
    usr_scr.sort()
    print(usr_scr[-2])
"""

"""
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4

Then, the output of the program should be:

    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ

import textwrap

if __name__ == '__main__':
    usr_inp=input("Enter you string: ")
    wdh=int(input("Enter you width: "))
    print(f'\n'.join(textwrap.wrap(usr_inp,width=wdh)))

"""

"""


You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

    #size 3

    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----

    #size 5

    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------

Hints

First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.

import string
def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

"""

"""
You are given a date. Your task is to find what the day is on that date.

A single line of input containing the space separated month, day and year, respectively,
in MM DD YYYY format.

    08 05 2015

Output the correct day in capital letters.

    WEDNESDAY


import calendar

if __name__ == '__main__':
    usr_inp=input().split(' ')
    daylist=(calendar.weekheader(10)).split()
    dayvalue=calendar.weekday(int(usr_inp[2]),int(usr_inp[0]),int(usr_inp[1]))
    print(f'day is {(daylist[dayvalue]).upper()}')

"""

"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N
but do not exist in both.

The first line of input contains an integer, M.The second line contains M space-separated integers.
The third line contains an integer, N.The fourth line contains N space-separated integers.

    4
    2 4 5 9
    4
    2 4 11 12

Output the symmetric difference integers in ascending order, one per line.

    5
    9
    11
    12

n = int(input())
set1 = set(map(int,input().split()))

m = int(input())
set2 = set(map(int, input().split()))

ans = list(set1 ^ set2)
ans.sort()
for i in ans:
    print(i)

"""
