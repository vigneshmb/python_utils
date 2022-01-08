"""

A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

    ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

    ABd1234@1


import re

if __name__ == '__main__':
    print(f"give your entry of passwords\n\nif you want to exit & see result, give an empty entry")
    reg_str=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$"
    usr_ip_lst=[]
    while True:
        usr_str=input("")
        if usr_str:
            if re.match(reg_str,usr_str):
                usr_ip_lst.append(usr_str)
        else:
            break
    print(",".join(usr_ip_lst))

"""

"""

You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score

The priority is that name > age > score.

If the following tuples are given as input to the program:

    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85

Then, the output of the program should be:

    [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]



def print_rslt(inp):
    ans_lst=[]
    for i in inp:
        a=(i.split(","))
        if a=="D":
            dep_lst.append(int(i.split(" ")[1]))
        if a=="W":
            wth_lst.append(int(i.split(" ")[1]))
    print(f"Balance: {(sum(dep_lst))-(sum(wth_lst))}")


if __name__ == '__main__':
    print(f"give your entry\n\nif you want to exit & see result, give an empty entry")
    usr_ip_lst=[]
    while True:
        usr_str=input("")
        if usr_str:
            usr_ip_lst.append(usr_str)
        else:
            break
    print_rslt(usr_ip_lst)

"""

lst = []
while True:
    s = input().split(',')
    if not s[0]:                          # breaks for blank input
        break
    lst.append(tuple(s))

lst.sort(key= lambda x:(x[0],x[1],x[2]))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)
