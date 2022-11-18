def cari_a(b,hipotenusa):
    a_2 = (hipotenusa**2) - (b**2)
    print(f"\n=> {hipotenusa**2} - {b**2} = {a_2} => {a_2**0.5}\n")

def cari_b(a, hipotenusa):
    b_2 = (hipotenusa**2) - (a**2)
    print(f"\n=> {hipotenusa**2} - {a**2} = {b_2} => {b_2**0.5}\n")

def cari_hipotenusa(a,b):
    hipotenusa_2 = (a**2) + (b**2)
    print(f"\n=> {a**2} + {b**2} = {hipotenusa_2} => {hipotenusa_2**0.5}\n")

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
        print("\n=> Tolong isi setidaknya dua dari itu\n")
    elif a == "":
        b = float(b)
        c = float(c)
        cari_a(b,c)
    elif b == "":
        a = float(a)
        c = float(c)
        cari_b(a,c)
    elif c == "":
        a = float(a)
        b = float(b)
        cari_hipotenusa(a,b)
    else:
        print("\n=> Semua variabel telah terisi\n")
