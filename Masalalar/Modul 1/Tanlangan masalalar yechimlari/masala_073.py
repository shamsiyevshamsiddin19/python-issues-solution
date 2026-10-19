# Mavzu: For sikli

"""
73. a va b butun sonlar berilgan (a<b). a dan b gacha bo’lgan barcha
    butun sonlarni ko’paytmasini chiqaruvchi dastur tuzing. (a va b
    ham ko’paytmaga kirsin)


        Input:                  Output:
     a=2, b=4                   24
     a=0, b=4                   0
     a=2, b=5                   120
"""
a= int(input("a ni kriting"))
b =int(input("b ni kriting"))
summa =1
for x in  range(a,b):
    summa*=x

print(f" ko'paytma {summa} ga teng")
