# Mavzu: For sikli va shart operatorlari

"""
86. Barcha 2 xonali sonlar ichida raqamlar yig’indisi 12 dan katta bo’lgan
    barcha sonlarni ekranga chiqaring.
"""
for i in range(10,100):
    if i%10+i//10>12 :
        print(i)