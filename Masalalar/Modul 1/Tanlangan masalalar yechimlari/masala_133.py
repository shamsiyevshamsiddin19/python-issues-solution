# Mavzu: Ichma-ich for sikli

"""
133. Konsoldan kiritilgan N soni asosida quyidagi shaklni chiqaruvchi
     dastur tuzing, Misol: N=5
     * * * * *
      *     *
         *
      *     *
     * * * * *
"""
n = int(input("N="))

for i in range(n):              
    for j in range(n):         
        if i == 0 or i == n - 1 or i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()                    

