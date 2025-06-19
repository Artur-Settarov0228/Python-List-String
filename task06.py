text = input("matn kiriting :")
sozlar = text.split(',')

palindrom = []

for soz in sozlar :
    if soz == soz[::-1]:
        palindrom.append(soz)

print(palindrom)        