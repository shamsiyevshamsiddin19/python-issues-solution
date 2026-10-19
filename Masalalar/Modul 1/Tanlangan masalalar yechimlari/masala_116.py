# Mavzu: Ichma-ich for sikli

"""
116. Konsoldan kiritilgan N soni asosida quyidagi shaklni chiqaruvchi
     dastur tuzing. Bu yerda: N – 3 dan katta toq son deb hisoblansin.
      Misol: N=5

      *               *
          *       *
              *
          *       *
      *               *
"""
n = int(input("N = "))
spacing = 4                      # yulduzlar orasidagi masofa
width = (n - 1) * spacing + 1    # qatorning umumiy kengligi

for i in range(n):               # tashqi loop — qatorlar
    chap = i * spacing                 # chap diagonal pozitsiyasi
    ong = (n - 1 - i) * spacing        # o'ng diagonal pozitsiyasi
    
    for j in range(width):       # ichki loop — har bir ustun
        if j == chap or j == ong:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()                      # qator tugadi, yangi qatorga o't