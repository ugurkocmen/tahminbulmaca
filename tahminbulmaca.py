import random

tutulan = random.randrange(0,100)

print("Tuttum Bul kanka!")

while True:

    try:
        tahmin = int(input("Buldum Kanka! Sayı : "))
    except:
        print("Sadece sayı gir!")
        continue

    if tahmin == tutulan:
        print("Helal Kanka Buldun :)")
        break
    elif tahmin < tutulan:
        print("Çık Kanka")
        continue
    elif tahmin > tutulan:
        print("Düş Kanka")
        continue
