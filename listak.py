#                     0       1        2         3
nevek:list[str] = ['Béla', 'Dezső', 'Cecil', 'András']
print(f'lista elemei kezdetben: {nevek}')
print(f'2-es indexű elem a listában: {nevek[2]}')
nevek[0] = input('első elem megváltoztatása erre: ')
print(f'lista elemei módosítás után: {nevek}')
list.sort(nevek)
for n in nevek: print(f'{n}', end=' ')
lista_hossza = len(nevek)
print(f'\nlista elemeinek száma: {lista_hossza}')

uj:str = input('új név hozzáadása a lista végéhez: ')
nevek.append(uj)
print(f'elemek a hozzáadás után: {nevek}')

hely:int = int(input('index, ahová beszúrjunk: '))
uj:str = input('új név, amit beszúrunk: ')
nevek.insert(hely, uj)
print(f'elemek a beszúrás után: {nevek}')

nev:str = input('nev, amit törlünk: ')
nevek.remove(nev)
print(f'{nev} törlése után: {nevek}')

hely:int = int(input('index, ahonnan törlünk: '))
nevek.pop(hely)
print(f'a {hely} indexű elem törlése után: {nevek}')

for i in range(len(nevek)):
    print(f'{i}. indexű elem: {nevek[i]}')