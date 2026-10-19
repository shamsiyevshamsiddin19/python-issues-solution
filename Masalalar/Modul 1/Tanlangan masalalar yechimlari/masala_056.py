# Mavzu: Shart operatorlari

"""
56. 5 ta son berilgan. Shu sonlarni Ichida faqatgina toq musbat
    sonlarnigina yig’indisini hisoblovchi dastur tuzing.
"""
a= int(input("Kriting:"))
b= int(input("Kriting:"))
c= int(input("Kriting:"))
d= int(input("Kriting:"))
e= int(input("Kriting:"))
jami=0
if a>0 and a%2==1:
    jami +=a
if b>0 and b%2==1:
    jami +=b
if c>0 and c%2==1:
    jami +=c
if d>0 and d%2==1:
    jami +=d
if e>0 and e%2==1:
    jami +=e

    print(jami)
