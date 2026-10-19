# Mavzu: Ichma-ich for sikli

"""
103. Konsoldan kiritilgan N soni asosida quyidagi shaklga mos harflarni
     chiqaruvchi dastur tuzing. Misol: N=5

      EEEEE
      DDDD
      CCC
      BB
      A
"""
n = int(input("N="))

for i in range(n, 0,-1):
    kod=65+i-1
    harf = chr(kod)
    for j in range(i):
     print(harf, end="")
    print()
    