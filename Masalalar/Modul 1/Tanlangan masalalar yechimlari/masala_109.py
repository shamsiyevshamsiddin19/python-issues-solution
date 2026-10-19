# Mavzu: For sikli va shart operatorlari

"""
109. N natural son berilgan. Uning murakkab yoki murakkab emasligini
     aniqlovchi dastur tuzing. Murakkab son – 1 va o’zidan tashqari yana
     bo’luvchisi mavjud bo’lgan son. Masalan: 4 ning bo’luvchilari - 1,2,4
"""



sana=0
n = int(input("n="))
for i in range(1,n+1):
    if  n%i == 0:
        sana+=1

if sana>2:
     print("Murakkab son")
else:
        print("tub son")
