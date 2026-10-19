# Mavzu: Shart operatorlari

"""
63. Uchta son berilgan. Agar berilgan sonlar o’sish tartibida bo’lsa,
    sonlarni ikkilantiring, aks holda sonlarni ishorasi o’zgaritirilsin. Yangi
    sonlarni ekranga chiqaring.
"""
a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))

if a<b<c:
    a=2*a
    b=2*b
    c=2*c
else:
    a=-a
    b=-b
    c=-c

    print(a, b, c)

