# Mavzu: Match/case

"""
66.1-7 gacha butun sonlar berilgan. Kiritilgan songa mos ravishda hafta
   kunlarini ekranga chiqaruvchi programma tuzilsin. (1-Dushanba, 2-
   Seshanba, …)
"""
kun = int(input("hafta kunini kriting 1--7: "))

match kun:
   case 1:
      print("Dushanba")
   case 2:
      print("Seshanba")
   case 3:
      print("Chorshanba")
   case 4:
      print("Payshanba")
   case 5:
      print("Juma")
   case 6:
      print("Shanba")
   case 7:
      print("Yakshanba")
   case _:
      print("Kunni xato kritingiz")
