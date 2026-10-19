# Mavzu: For sikli va shart operatorlari

"""
76. a va b sonlari berilgan. (a<b) a dan b gacha 4 ga karrali sonlarni
    ekranga chiqaruvchi dastur tuzing. (a va b kirmasin)
       Input:                           Output:
    a=12, b=24                          16 20
    a=70, b=90                             72 6 80 84 88
"""
a= int(input("a ni kriting:"))
b =int(input("b ni kriting:"))

for i in range(a+1,b):
    if i % 4 ==0:
        print(i , end=",")
