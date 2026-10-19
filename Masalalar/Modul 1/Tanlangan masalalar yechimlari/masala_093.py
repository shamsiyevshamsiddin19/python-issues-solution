# Mavzu: While sikli

"""
93.n butun soni berilgan. Berilgan son raqamlarini teskari tartibda
   chiqaruvchi programma tuzilsin.
"""



n = int(input("sonni kriting:"))

if n< 0:
   n=abs(n)

while (n>0):
   oxirgi_raqami = n%10
   print(oxirgi_raqami, end="")
   n=n//10