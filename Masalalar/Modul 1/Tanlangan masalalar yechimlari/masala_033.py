# Mavzu: Shart operatorlari

"""
33. 5 ta butun son berilgan. Shu sonlar orasida nechta musbat va nechta
    manfiy, nechta nol raqami borligini aniqlovchi dastur tuzing.
"""
a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))
d= int(input("Kriting:"))
e= int(input("Kriting:"))
manfiy = 0
nol = 0
musbat = 0

musbat = (a>0 )+(b>0) +( c>0) +(d>0) +(e>0)
nol = (a==0 )+ (b==0) + (c==0 )+( d==0 )+( e==0)
manfiy = (a<0) +(b<0) +( c<0 )+(d<0 )+e<0

print(f" musbat {musbat}\nnol {nol}\n manfiy {manfiy}")
