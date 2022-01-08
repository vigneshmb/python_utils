"""
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

if __name__ == '__main__':
    lst=[5,6,77,45,22,12,24]
    new_lst=[i for i in lst if i%2!=0]
    print(new_lst)

"""

"""
By using list comprehension, please write a program to print the list after removing numbers
which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

if __name__ == '__main__':
    lst=[12,24,35,70,88,120,155]
    new_lst=[i for i in lst if i%35==0]
    print(new_lst)

"""

"""
By using list comprehension, please write a program to print the list
after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

if __name__ == '__main__':
    lst=[12,24,35,70,88,120,155]
    new_lst=[i for i in lst if (lst.index(i))%2!=0]
    print(f'{lst}\n{new_lst}')

"""

"""
By using list comprehension, please write a program to print the list
after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i<3 or 4<i]
print(li)

"""

"""
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)

"""
