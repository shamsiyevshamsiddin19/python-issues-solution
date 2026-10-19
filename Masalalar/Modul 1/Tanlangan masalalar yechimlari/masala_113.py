# Mavzu: Ichma-ich for sikli

"""
113. Konsonldan kiritilgan N soni asosida quyidagi shaklni chiqaruvchi
     dastur tuzing. Misol: N=5
     * * * * *
     * * *
     * * * * *
     * * *
     * * * * *
"""
n = int(input("n="))
for i in range(n):
    if i%2==0:
        for j in range(n):
            print("*", end=" ")
        print()
    elif i%2==1:
        for k in range(n-2):
            print("*", end=" ")
        print()