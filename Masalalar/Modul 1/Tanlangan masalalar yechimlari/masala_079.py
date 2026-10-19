# Mavzu: For sikli va shart operatorlari

"""
79. Barcha 2 xonali sonlar ichida kamida 1 ta raqami 8 bo’lgan barcha
    sonlarni ekranga chiqaruvchi dastur tuzing.
"""
for i in range(10,100):
    if i%10 ==8 or i//10==8:
        print(i)