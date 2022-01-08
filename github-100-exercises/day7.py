"""

Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints:

    Consider use class, function and comprehension.



class numgen:

    def num_div_by_seven(self,inp):
        for i in range(0,inp+1):
            if i%7==0:
                yield(i)




if __name__ == '__main__':
    usr_inp=int(input("enter your number: "))
    gnr_obj = numgen()
    gnr=gnr_obj.num_div_by_seven(usr_inp)
    for i in gnr:
        print(f'\n{i}')
"""

"""


A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2

Then, the output of the program should be:

    2

def pos_2d(inp):
    x=0
    y=0
    for i in inp:
        dir,temp=i.split(' ')[0],i.split(' ')[1]
        steps=int(temp)
        if dir=='UP':
            x+=steps
        elif dir=='DOWN':
            x-=steps
        elif dir=='RIGHT':
            y+=steps
        elif dir=='LEFT':
            y-=steps
        else:
            print('Please give direction correctly')
    print(f'(x,y)=({x},{y})')

if __name__ == '__main__':
    usr_inp=[]
    while True:
        usr_str=input("")
        if usr_str:
            usr_inp.append(usr_str)
        else:
            break
    pos_2d(usr_inp)

"""
