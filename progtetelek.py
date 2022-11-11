import random as rnd

szamok = []
for x in range(10):
    r_szam = rnd.randint(10, 99)
    szamok.append(r_szam)
print(f'szamok: {szamok}')

# sorozatszámítás (pl. összegzés)
sum:int = 0
for szam in szamok:
    sum += szam
print(f'sorozat elemeinek összege: {sum}')
avg = sum/len(szamok)
print(f'sorozat elemeinek átlaga: {avg}')

# megszámlálás (-> <adott tulajdonságú> elemek száma)
# (pl. páratlan elemek száma)
count = 0
for szam in szamok:
    if szam % 2 == 1:
        count += 1
print(f'páratlan számok száma a sorozatban: {count}')

# szélsőérték hely (-> leg[kisebb/nagyobb] elem indexe a sorozatban)
# (maximum index) 
maxi = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
print(f'legnagyobb elem indexe: {maxi}')
print(f'ez a sorozat {maxi + 1}. eleme')
print(f'a sorozat legnagyobb eleme: {szamok[maxi]}')

# (minimum index)
mini = 0
for i in range(1, len(szamok)):
    if szamok[i] < szamok[mini]:
        mini = 1
print(f'legkisebb elem indexe: {mini}')
print(f'ez a sorozat {mini + 1}. eleme')
print(f'a sorozat legkisebb eleme: {szamok[mini]}')

# kiválasztás
# !!!CSAK!!! akkor alkalmazható, 
# ha kiválasztani kívánt <tulajdonságú> elem
# !!!BIZTOSAN!!! van a sorozatban
# (t: 'a sorozat első olyan eleme,
# amely nagyobb vagy egyenlő a sorozat átlagával)'
i = 0
while szamok[i] < avg:
    i += 1
print(f'a sorozat első ilyan eleme, amely nem kisebb, mint az átlag: {szamok[i]}')

# eldöntés -> van-e a sorozatnak <adott tulajdonságú> eleme
#(van-e 0-ra végződő eleme?)

i = 0
while i < len(szamok) and szamok[i] % 10 != 0:
    i += 1
if i < len(szamok): print('VAN 0-ra végződő eleme a sorozatnak')
else: print('NINCS 0-ra végződő eleme a sorozatnak')

# lineáris keresés -> <adott elem> benne van-e a sorozatban?
# és ha igen, akkor hol (melyik indexen)?

keresett_szam = int(input('keresett szám: '))
i = 0
while i < len(szamok) and szamok[i] != keresett_szam:
    i += 1
if i < len(szamok):
    print(f'a {keresett_szam} indexe: {i}')
else:
    print(f'a {keresett_szam} nincs benne a sorozatban')

# http://info.nytta.hu/temak/prog/Programozasi_tetelek.pdf