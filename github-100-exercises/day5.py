"""

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

    1,2,3,4,5,6,7,8,9

Then, the output should be:

    1,9,25,49,81


def print_rslt(inp):
    uip_lst=(inp.split(","))
    ans_lst=[]
    for i in uip_lst:
        a=int(i)
        if a%2!=0:
            ans_lst.append(str(a*a))
    print(",".join(ans_lst))


if __name__ == '__main__':
    usr_str=input("enter your sequence: ")
    print_rslt(usr_str)


"""

"""

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

    D 100
    W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

    D 300
    D 300
    W 200
    D 100

Then, the output should be:

    500



def print_rslt(inp):
    dep_lst=[]
    wth_lst=[]
    for i in inp:
        a=i.split(" ")[0]
        if a=="D":
            dep_lst.append(int(i.split(" ")[1]))
        if a=="W":
            wth_lst.append(int(i.split(" ")[1]))
    print(f"Balance: {(sum(dep_lst))-(sum(wth_lst))}")


if __name__ == '__main__':
    print(f"give your entry of deposit and withdrawal\n\nif you want to exit & see result, give an empty entry")
    usr_ip_lst=[]
    while True:
        usr_str=input("")
        if usr_str:
            usr_ip_lst.append(usr_str)
        else:
            break
    print_rslt(usr_ip_lst)

"""
