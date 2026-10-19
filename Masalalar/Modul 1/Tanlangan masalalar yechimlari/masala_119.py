# Mavzu: Ichma-ich for sikli

"""
119. Konsoldan kiritilgan N soni asosida quyidagi shaklga mos sonlarni
     chiqaruvchi dastur tuzing. Masalan: N = 5

      *****
      ****
      ***
      **
      *
"""
n = int(input("N="))

for i in range(n,0,-1):
      for j in range(i):
            print("*",end="")

      print("")
