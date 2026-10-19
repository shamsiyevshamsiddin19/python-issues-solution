# Mavzu: Shart operatorlari

"""
53. 3 ta a, b, c sonlar berilgan. Agar ixtiyoriy 2ta sonni qo’shib, qolgan 3-
    songa teng bo’lsa, ekranga true, aks holda false chiqaring.

     Input:                                  Output:
     a=1, b=2, c=3                           True
     a=3, b=1, c=2                           True
     a=3, b=2, c=2                           Fasle
"""
from sympy import false, true


a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))

if a+b == c or a+c==b or b+c==a:
    print(true)
else:
    print(false)
