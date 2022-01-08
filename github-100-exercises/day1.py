"""

    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.


for i in range(2000,3201):
    if ((i % 7)==0) and ((i % 5)!=0):
        #act_range.append(i)
        print(f"{i}",end=",")
"""

"""

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320



user_input=int(input(f"Enter your number:\t"))
i=1
fact=1
while i<=user_input:
    fact=fact*i
    print(fact,end=",")
    i+=1

"""

"""

With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


user_input=int(input(f"Enter your number: "))
ans={}
for i in range(1,user_input+1):
    ans[i]=i*i
print(ans)

"""
