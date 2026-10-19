# Mavzu: For sikli

"""
69. 1 dan 100 gacha bo‘lgan toq sonlarni alohida va juft sonlarni alohida
    qatorda ekranga chiqaruvchi dastur tuzing.
"""
for toq in range(1, 100, 2):
    print(toq, end=", ")
print("\n")
for juft in range(0, 100, 2):
    print(juft, end=", ")