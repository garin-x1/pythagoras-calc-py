from math import sqrt

def get_a(b,hypotenuse):
    a_2 = (hypotenuse**2) - (b**2)
    print(f"{hypotenuse**2} - {b**2} = {a_2} => {sqrt(a_2)}\n")

def get_b(a, hypotenuse):
    b_2 = (hypotenuse**2) - (a**2)
    print(f"{hypotenuse**2} - {a**2} = {b_2} => {sqrt(b_2)}\n")

def get_hypotenuse(a,b):
    hypotenuse_2 = (a**2) + (b**2)
    print(f"{a**2} + {b**2} = {hypotenuse_2} => {sqrt(hypotenuse_2)}\n")

while True:
    print("-------------------------------")
    print("Pythagoras Formula:")
    print("a^2 + b^2 = c^2")
    print("*Leave blank if you don't know")
    print("ctrl+c to exit\n")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    if (a == "" and b == "") or (a == "" and c == "") or (b == "" and c == ""):
        print("Please enter at least two of them\n")
    elif a == "":
        b = int(b)
        c = int(c)
        get_a(b,c)
    elif b == "":
        a = int(a)
        c = int(c)
        get_b(a,c)
    elif c == "":
        a = int(a)
        b = int(b)
        get_hypotenuse(a,b)
    else:
        print("All variable have been filled\n")
