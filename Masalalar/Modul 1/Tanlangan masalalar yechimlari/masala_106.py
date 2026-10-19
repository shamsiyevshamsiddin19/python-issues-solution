# Mavzu: Ichma-ich for sikli

"""
106. Konsoldan kiritilgan N soni asosida quyidagi shaklga mos diagonal
     ko’rinishida sonlarni chiqaruvchi dastur tuzing, Misol: N=5
      1
              2
                      3
                              4
                                  5
"""
n = int(input("n="))

for i in range(1,n+1):
    print(i)
    for j in range(i):
        print(" " , end="")