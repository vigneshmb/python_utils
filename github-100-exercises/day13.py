"""

Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

class crcl_plot:

    def __init__(self):
        rdus=int(input("please enter your radius for the circle: "))
        self.radius=rdus

    def find_area(self):
        print(f'the area of the circle is {(self.radius**2)*3.14}')

if __name__ == '__main__':
    crcl1=crcl_plot()
    crcl1.find_area()

"""

"""

Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

class rect_plot:

    def __init__(self):
        self.lgth=int(input("please enter your length for the rectangle: "))
        self.bdth=int(input("please enter your breadth for the rectangle: "))

    def find_area(self):
        print(f'the area of the rectangle is {(self.lgth*self.bdth)}')

if __name__ == '__main__':
    rect1=rect_plot()
    rect1.find_area()

"""

"""

Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area of
the shape where Shape's area is 0 by default.

class shape:

    def __init__(self):
        self.area=0

    def find_area(self):
        print(f'the area of the shape is {self.area}')

class square(shape):

    def __init__(self):
        self.lgth=int(input("please enter your length for the square: "))

    def find_area(self):
        print(f'the area of the shape is {self.lgth**2}')


if __name__ == '__main__':
    shp1=shape()
    shp1.find_area()
    sqr1=square()
    sqr1.find_area()

"""

"""

Please raise a RuntimeError exception

if __name__ == '__main__':
    raise RuntimeError

"""
