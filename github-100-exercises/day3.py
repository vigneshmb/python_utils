"""
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

    hello world and practice makes perfect and hello world again

Then, the output should be:

    again and hello makes perfect practice world


def print_rslt(inp):
    uip_lst=(inp.split(" "))
    ans_lst=[]
    for i in uip_lst:
        if ans_lst.count(i)<=0:
            ans_lst.append(i)
    ans_lst.sort()
    print(" ".join(ans_lst))


if __name__ == '__main__':
    usr_str=input("enter your sentence: ")
    print_rslt(usr_str)

"""

"""

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

    0100,0011,1010,1001

Then the output should be:

    1010


def print_rslt(inp):
    uip_lst=(inp.split(","))
    ans_lst=[]
    for i in uip_lst:
        if int(i,2)%5==0:
            ans_lst.append(i)
    print(",".join(ans_lst))


if __name__ == '__main__':
    usr_str=input("enter your sentence: ")
    print_rslt(usr_str)

"""

"""

Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.


if __name__ == '__main__':
    ans_lst=[]
    for i in range(1000,3001):
        sts=True
        for j in str(i):
            if int(j)%2!=0:
                sts=False
        if sts:
            ans_lst.append(str(i))

    print(",".join(ans_lst))

"""

"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

    hello world! 123

Then, the output should be:

    LETTERS 10
    DIGITS 3

if __name__ == '__main__':
    usr_str=input("enter your sentence: ")
    ltr=0
    dgt=0
    for i in usr_str:
        if i.isalpha():
            ltr+=1
        if i.isdecimal():
            dgt+=1

    print(f"LETTERS {ltr}\n\nDIGITS {dgt}")

"""
