# Mavzu: For sikli

"""
89.a va b butun sonlari berilgan (a<b). a dan b gacha barcha butun
   sonlarni ko’paytmasini ekranga chiqaruvchi programma tuzilsin.
"""
a= int(input("a ni kriting"))
b =int(input("b ni kriting"))
summa =1
for x in  range(a,b):
    summa*=x

print(f" ko'paytma {summa} ga teng")