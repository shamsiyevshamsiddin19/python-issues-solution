# Mavzu: For sikli va shart operatorlari

"""
83. Barcha 2 xonali sonlar ichida raqamlar yig’indisi 9 ga yoki 15 ga teng
    bo’lgan sonlarni ekranga chiqaring.
"""
for i in range(10,100):
    if i%10+i//10==9 or i%10+i//10==15:
        print(i)