from math import sqrt

def cari_a(b,hipotenusa):
    a_2 = (hipotenusa**2) - (b**2)
    print(f"{hipotenusa**2} - {b**2} = {a_2} => {sqrt(a_2)}\n")

def cari_b(a, hipotenusa):
    b_2 = (hipotenusa**2) - (a**2)
    print(f"{hipotenusa**2} - {a**2} = {b_2} => {sqrt(b_2)}\n")

def cari_hipotenusa(a,b):
    hipotenusa_2 = (a**2) + (b**2)
    print(f"{a**2} + {b**2} = {hipotenusa_2} => {sqrt(hipotenusa_2)}\n")

while True:
    print("-------------------------------")
    print("Rumus Pythagoras:")
    print("a^2 + b^2 = c^2")
    print("*Kosongkan jika tidak tahu")
    print("ctrl + c untuk keluar\n")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    if (a == "" and b == "") or (a == "" and c == "") or (b == "" and c == ""):
        print("Tolong isi setidaknya dua dari itu\n")
    elif a == "":
        b = int(b)
        c = int(c)
        cari_a(b,c)
    elif b == "":
        a = int(a)
        c = int(c)
        cari_b(a,c)
    else:
        a = int(a)
        b = int(b)
        cari_hipotenusa(a,b)
