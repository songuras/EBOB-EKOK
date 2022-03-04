import math
print("EBOB EKOK BULMA \n ")
while True:
    menu = input("EBOB için '1' EKOK için '2' çıkış için '3' : ")
    if menu == "1":
        sayi1 = int(input("ilk sayi : "))
        sayi2 = int(input("ikinci sayi : "))
        ebob = math.gcd(sayi1,sayi2)
        print(sayi1,sayi2,"sayilarının EBOB'U = ",ebob)
    elif menu == "2":
        sayi1 = int(input("ilk sayi : "))
        sayi2 = int(input("ikinci sayi : "))
        ekok = math.lcm(sayi1,sayi2)
        print(sayi1,sayi2,"sayilarının EKOK'U = ",ekok)
    elif menu == "3":
        break
    else: 
        print("geçersiz işlem")