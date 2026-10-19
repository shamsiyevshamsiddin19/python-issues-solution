# Mavzu: Raqamlar bilan ishlash

"""
9. Berilgan to'rt xonali sonni o’nlar xonasidagi raqamni aniqlab natijani
   ekranga chiqaradigan dastur tuzing.

       Input:                        Output:
    N = 1452                         5
    N = 4789                         8
"""
a = int(input("4 xonali sonni kriting: "))
n = (a//10)%10
print("o'nlar xonasidagi son" , n)