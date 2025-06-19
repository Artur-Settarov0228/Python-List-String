soz = input("biron bir matn kiritng :")

foalyatlar = soz.split(',')

natija = []
for foalyat in foalyatlar:
    sd = foalyat.strip().lower().replace(' ', ' _ ')
    natija.append(sd)
natijalar = '_'.join(natija)

print(natijalar)
