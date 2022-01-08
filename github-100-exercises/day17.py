"""

Please write assert statements to verify that every number in the list [2,4,6,8] is even.

data = [2,4,5,6]
for i in data:
    assert i%2 == 0, "{} is not an even number".format(i)

"""

"""

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following n is given as input to the program:

    35 + 3

Then, the output of the program should be:

    38

expression = input()
ans = eval(expression)
print(ans)

"""

"""

Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = round((low + high) / 2)

        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

lst = [1,3,5,7,]
print(binary_search(lst, 5))

"""

"""

Please generate a random float where the value is between 10 and 100 using Python module.

import random

print(random.random(10,100))

"""

"""

Please generate a random float where the value is between 5 and 95 using Python module.

import random

print(random.uniform(5,95))

"""
