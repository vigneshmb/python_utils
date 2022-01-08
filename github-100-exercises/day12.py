"""

Write a program which can map() to make a list whose elements are square of
numbers between 1 and 20 (both included).

if __name__ == '__main__':
    sqr_lst=list(map(lambda i:i ** 2,range(1,21)))
    print(sqr_lst)

"""

"""

Define a class named American which has a static method called printNationality.

class American:
    @staticmethod
    def printNationality():
        print("I am American")

if __name__ == '__main__':
    amr=American()
    amr.printNationality()

"""

"""

Define a class named American and its subclass NewYorker.

class American:
    def printNationality(self):
        print("I am American")

class Newyorker(American):
    def printstate(self):
        print("from Newyork")

if __name__ == '__main__':
    amr=Newyorker()
    amr.printNationality()
    amr.printstate()

"""
