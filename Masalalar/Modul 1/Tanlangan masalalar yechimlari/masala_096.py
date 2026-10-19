# Mavzu: While sikli

"""
96. Foydalanuvchi tomonidan butun sonlar kiritilaveradi. Bu jarayon
    manfiy son kiritilguncha davom etadi. Shu sonlarning ichida nechtasi
    5 ga karrali ekanligini aniqlovchi dastur tuzing.
"""

n = int(input("sonni kiritavering:"))
karrali=0
while (n>=0):
    if n%5==0:
        karrali+=1
    n = int(input("sonni kiritavering:"))


print(karrali)