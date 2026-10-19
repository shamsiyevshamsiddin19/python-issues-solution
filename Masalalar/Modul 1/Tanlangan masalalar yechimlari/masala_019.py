# Mavzu: Arifmetik amallar

"""
19. Qo’shimcha o’zgaruvchidan foydalanmasdan a va b o’zgaruvchilar
    qiymatini almashtirib ekranga chiqaruvchi dastur tuzing.
    Masalan, a=3 va b=4 kiritilsa, u holda ekranga a=4 va b=3 kabi
    chiqarilishi kerak
"""
a = int(input("A="))
b = int(input("B="))
a=a+b
b=a-b
a=a-b
print(f"A={a}")
print(f"B={b}")