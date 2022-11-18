def get_a(b,hypotenuse):
    a_2 = (hypotenuse**2) - (b**2)
    print(f"\n=> {hypotenuse**2} - {b**2} = {a_2} => {a_2**0.5}\n")

def get_b(a, hypotenuse):
    b_2 = (hypotenuse**2) - (a**2)
    print(f"\n=> {hypotenuse**2} - {a**2} = {b_2} => {b_2**0.5}\n")

def get_hypotenuse(a,b):
    hypotenuse_2 = (a**2) + (b**2)
    print(f"\n=> {a**2} + {b**2} = {hypotenuse_2} => {hypotenuse_2**0.5}\n")

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
        print("\n=> Please enter at least two of them\n")
    elif a == "":
        b = float(b)
        c = float(c)
        get_a(b,c)
    elif b == "":
        a = float(a)
        c = float(c)
        get_b(a,c)
    elif c == "":
        a = float(a)
        b = float(b)
        get_hypotenuse(a,b)
    else:
        print("\n=> All variable have been filled\n")
