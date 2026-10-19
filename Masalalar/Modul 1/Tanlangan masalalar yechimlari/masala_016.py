# Mavzu: Raqamlar bilan ishlash

"""
16. Uch xonali son berilgan. Uning raqamlari yig’indisi hisoblovchi dastur
    tuzilsin.
"""
a = int(input(" uch xonali sonni kriting "))
print(f"output {a%10+(a//10)%10+a//100}")