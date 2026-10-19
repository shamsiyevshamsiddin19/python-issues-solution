# Mavzu: While sikli

"""
126. Berilgan 2 ta sonning ham EKUBini, ham EKUKini topadigan dastur
     tuzing.
"""
a = int(input("A="))
b = int(input("B="))

kopaytma = a*b

while  a != b:
     if a>b:
          a= a-b
     
     else:
          b=b-a

ekub = a
ekuk = kopaytma // a

print(f"EKUB = {ekub}")
print(f"EKUK = {ekuk}")