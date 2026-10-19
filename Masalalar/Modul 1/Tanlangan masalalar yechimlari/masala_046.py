# Mavzu: Shart operatorlari

"""
46. Uch xonali a sonni berilgan. Shu sondagi eng katta raqamni aniqlovchi
    dastur tuzing.


         Input:                          Output:
      a = 584                            8
      a = 402                            4
      a = 626                            6
      a = 101                            1
"""
a= int(input("Kriting:"))
if a//100 > (a//10)%10 > a%10 or a//100 > (a//10)%10 < a%10:
    print(a//100)
if a//100 < (a//10)%10 < a%10 or a//100 < (a//10)%10 >a%10:
    print(a%10)
if (a//10)%10 > a//100 >a%10 or (a//10)%10 > a//100 <a%10 :
    print((a//10)%10)
