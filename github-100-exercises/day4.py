"""

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

    Hello world!

Then, the output should be:

    UPPER CASE 1
    LOWER CASE 9


if __name__ == '__main__':
    usr_str=input("enter your sentence: ")
    upr=0
    lwr=0
    for i in usr_str:
        if i.isupper():
            upr+=1
        if i.islower():
            lwr+=1

    print(f"UPPERCASE {upr}\n\nLOWERCASE {lwr}")

"""

"""

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

    9

Then, the output should be:

    11106

if __name__ == '__main__':
    usr_str=input("enter your number: ")
    usr_lst=[]
    for i in range(1,5):
        usr_lst.append(int(usr_str*i))
    print(sum(usr_lst))

"""
