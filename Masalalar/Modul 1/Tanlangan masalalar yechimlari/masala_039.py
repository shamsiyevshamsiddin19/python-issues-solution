# Mavzu: Shart operatorlari

"""
39. Butun son berilgan. Agar son musbat bo’lsa 15 martaga oshiring,
    manfiy bo’lsa absolut qiymatini (ya’ni modulini), aks holda berilgan
    sonning o’zini ekranga chiqaruvchi dastur tuzing.

        Input:                        Output:
     Son = 4                          60
     Son = -50                        50
     Son = 0                          0
"""
a= int(input("Kriting:"))
if a>0:
    print(15*a)
elif a<0:
    print(abs(a))
else:
    print(a)