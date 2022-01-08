"""

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

    john@google.com

Then, the output of the program should be:

    google

if __name__ == '__main__':
    id="john@google.com"
    print(f'Welcome {(id.split("@")[0])},You are from {str(id.split("@")[1]).split(".")[0]}')

"""

"""

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program:

    2 cats and 3 dogs.

Then, the output of the program should be:

    ['2', '3']


if __name__ == '__main__':
    id=input("enter your sentence: ")
    lst=[]
    for i in id:
        if i.isdigit():
            lst.append(i)
    print(' '.join(lst))

import re

email = input()
pattern = "\d+"
ans = re.findall(pattern,email)
print(ans)

"""

"""

Print a unicode string "hello world".

unicodeString = u"hello world!"
print(unicodeString)

"""

"""

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

s = input()
u = s.encode('utf-8')
print(u)

"""

"""

Write a special comment to indicate a Python source code file is in unicode.

# -*- coding: utf-8 -*-

"""

"""

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:

    5

Then, the output of the program should be:

    3.55

if __name__ == '__main__':
    usr_inp=int(input("enter your number: "))
    rslt=0
    for i in range(1,usr_inp+1):
        rslt+= i/(i+1)
    print(round(rslt,2))

"""
