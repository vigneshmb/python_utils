"""

Please write a program which count and print the numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

    abcdefgabc

Then, the output of the program should be:

    a,2
    c,2
    b,2
    e,1
    d,1
    g,1
    f,1

if __name__ == '__main__':
    lst='abcdefgabc'
    char_lst=[]
    for i in lst:
        if char_lst.count(i)==0:
            char_lst.append(i)
            print(f'{i},{lst.count(i)}')
"""

"""
Please write a program which accepts a string from console and print it in reverse order.

Example: If the following string is given as input to the program:*

    rise to vote sir

Then, the output of the program should be:

    ris etov ot esir


s = input()
s = ''.join(reversed(s))
print(s)

"""

"""
Please write a program which accepts a string from console and print the characters that have even indexes.

Example: If the following string is given as input to the program:

    H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

    Helloworld

s = "H1e2l3l4o5w6o7r8l9d"
ns =''
for i in range(len(s)):
    if i % 2 == 0:
        ns+=s[i]
print(ns)

"""

"""
Please write a program which prints all permutations of [1,2,3]

import itertools
print(list(itertools.permutations([1,2,3])))

"""

"""
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

if __name__ == '__main__':
    heads=35
    legs=94
    chic=0
    rabb=0
    poss_chic=[i for i in range(1,95) if i%2==0]
    poss_rabb=[i for i in range(1,95) if i%4==0]
    for i in poss_chic:
        for j in poss_rabb:
            if (i+j)==legs:
                chic=i/2
                rabb=j/4
                if (chic+rabb)==heads:
                    print(f'{chic} , {rabb}')

"""
