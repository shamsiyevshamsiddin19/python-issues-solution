# Mavzu: Shart operatorlari

"""
36. Berilgan 3 ta sondan bir xil bo’lmaganini ekranga chiqaradigan dastur
    tuzing. Agar barcha sonlar bir xil bo’lsa ‘=’ belgisi chiqsin.

        Input:                   Output:
     a=2, b=4, c=4               2
     a=0, b=4, c=3               043
     a=2, b=2, c=2               =
"""
a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))
if a!=b and b!=c and c!=a:
    print(a,b,c)
if a==b and b!=c:
    print(c)
if  a==c and b!=c:
    print(b)
if  b==c and b!=a:
    print(a)
if a==b and b==c and c==a:
    print("=")