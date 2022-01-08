"""
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0

with a given n input by console (n>0).

Example: If the following n is given as input to the program:

    5

Then, the output of the program should be:

    500

def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

n = int(input())
print(f(n))

"""

"""

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

    7

Then, the output of the program should be:

    13

if __name__ == '__main__':
    usr_inp=int(input('enter your number: '))
    fibo=0
    if usr_inp==0:
        fibo=0
        print(fibo)
    elif usr_inp==1 or usr_inp==2:
        fibo=1
        print(fibo)
    elif usr_inp>1:
        fibo=2
        fibo1=1
        for i in range(3,usr_inp):
            temp=fibo
            fibo+=fibo1
            fibo1=temp
        print(fibo)
    else:
        print('please give positive number')

"""
"""
he Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

    7

Then, the output of the program should be:

    0,1,1,2,3,5,8,13

if __name__ == '__main__':
    inp=int(input('enter your number: '))
    first_val=0
    second_val=1
    cnt=0
    fibo_lst=[str(0)]
    if inp==1:
        fibo_lst.append(str(first_val))
        # print(fibo_lst)
    elif inp>1:
        while cnt<inp:
            temp=first_val+second_val
            first_val=second_val
            second_val=temp
            cnt+=1
            fibo_lst.append(str(first_val))
            # print(fibo_lst)
    print(','.join(fibo_lst))

"""

"""


Please write a program using generator to print the even numbers between 0 and n
in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

    10

Then, the output of the program should be:

    0,2,4,6,8,10

def find_even(i):
    if i%2==0:
        print(i,end=',')

if __name__ == '__main__':
    inp=int(input('enter your number: '))
    for num in range(0,inp+1):
        find_even(num)

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(raw_input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print ",".join(values)

"""

"""
Please write a program using generator to print the numbers
which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

    100

Then, the output of the program should be:

    0,35,70

def generate(n):
    for i in range(n+1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i

n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))

"""
