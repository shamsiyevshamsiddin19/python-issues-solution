# Mavzu: Shart operatorlari

"""
43.Uchta butun a, b, c sonlar berilgan. Jumlani rostlikka tekshiring: a, b, c
   sonlarning faqat ikkitasi musbat son.
"""
from sympy import false, true


a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))

if a>0 and b>0 and c<0 or a>0 and b<0 and c>0  or a<0 and b>0 and c>0:
    print(true)
elif a>0 and b<0 and c<0 or a<0 and b<0 and c>0  or a<0 and b>0 and c<0 or  a<0 and b<0 and c<0 or a>0 and b>0 and c>0 :
    print(false)
