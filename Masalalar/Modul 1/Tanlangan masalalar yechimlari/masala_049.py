# Mavzu: Shart operatorlari

"""
49. 4 ta a, b, c, d son berilgan, kattasidan kichigini ayirib ekranga natijani
    chiqaruvchi, agar u sonlar o’zaro teng bo’lsa yig’indisini ekranga
    chiqaruvchi dastur tuzing.
     Input:                            Output:
     a=2, b=2, c=2, d=2                8
     a=9, b=2, c=7, d=2                7
     a=3, b=8, c=2, d=8                6
"""
a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))
d= int(input("Kriting:"))
max = 0
min = 0
if a>b and a>c and a>d:
    max = a
elif b>a and b>c and b>d:
    max = b
elif c>a and c>b and c>d:
    max = c
else:
    max = d


if a<b and a<c and a<d:
    min = a
elif b<a and b<c and b<d:
    min = b
elif  c<a and c<b and c<d:
    min = c
else:
    min =d

print(max-min)