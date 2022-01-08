"""
By using list comprehension, please write a program to print the list after
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

if __name__ == '__main__':
    lst=[12,24,35,70,88,120,155]
    new_lst=[lst[i] for i in range(len(lst)) if i not in (0,4,5)]
    print(f'{lst}\n{new_lst}')

"""
"""
By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].

if __name__ == '__main__':
    lst=[12,24,35,70,88,120,155]
    new_lst=[i for i in lst if i!=24]
    print(f'{lst}\n{new_lst}')

"""
"""

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
write a program to make a list whose elements are intersection of the above given lists.

list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
set1= set(list1)
set2= set(list2)
intersection = set1 & set2
print(intersection)

"""
"""
With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all duplicate values with original order reserved.

if __name__ == '__main__':
    lst=[12,24,35,24,88,120,155,88,120,155]
    new_lst=[]
    for i in lst:
        if lst.count(i)==1 or new_lst.count(i)==0:
            new_lst.append(i)
    print(f'{lst}\n{new_lst}')

"""

"""
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class person:
    pass

class male(person):
    def getGender(self):
        print('Male')

class female(person):
    def getGender(self):
        print('Female')

if __name__ == '__main__':
    ml=male()
    fml=female()
    ml.getGender()
    fml.getGender()

"""
