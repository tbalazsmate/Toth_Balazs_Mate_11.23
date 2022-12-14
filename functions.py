from data import homersekletek
from os import system

filename='Celsius.csv'
cimsor=''

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0 - Kilépés')
    print('1 - Adatok listázása')
    print('2 - Adat felvétele')
    print('3 - Adat törlése')
    print('4 - Átlag hőmérséklet')
    print('5 - Legmelegebb nap')
    print('6 - Leghidegebb nap')
    print('7 - Átváltás Kelvinbe')
    return input('Kérem válasszon: ')

def loadTemp():
    file=open(filename,'r',encoding='utf-8')
    global cimsor
    cimsor=file.readline().strip()
    for row in file:
        splitted=row.strip().split(';')
        homersekletek[splitted[0]]=int(splitted[1])
    file.close

def printAllTemps():
    system('cls')
    print('Hőmérsékletek: \n')
    for key,value in homersekletek.items():
        print(f'{key} - {value}°C')
    input('\ntovább...')

def addNewTemp():
    system('cls')
    print('Új nap:\n')
    nap=input('Adja meg a dátumot [hónap.nap]: ')
    temp=int(input('A nap átlaghőmérséklete: '))
    homersekletek[nap]=temp
    saveTempToFile(nap,temp)
    input('\nAdat sikeresen felvéve. Tovább...')

def saveTempToFile(nap,temp):
    file=open(filename,'a', encoding='utf-8')
    file.write(f'\n{nap};{temp}')
    file.close()
    
def deleteTemp():
    system('cls')
    print('Adat törlése\n')
    print('Hőmérsékletek: \n')
    for key,value in homersekletek.items():
        print(f'{key} - {value}°C')

    nap=input('Adja meg a törlendő adat dátumát [Hónap.Nap]: ')
    if nap in homersekletek:
        homersekletek.pop(nap)
        saveAllToFile()
        input('A megadott dátum adatai törölve. Tovább...')
    else:
        input('Erre a dátumra nincs adat megadva. Tovább...')
        
def saveAllToFile():
    file=open(filename, 'w', encoding='utf-8')
    file.write(cimsor)
    for key,value in homersekletek.items():
        file.write(f'\n{key};{value}')
    file.close()
    
def averageTemp():
    system('cls')
    print('A napok átlaghőmérséklete\n')
    osszeg=sum(homersekletek.values())
    print(f'{len(homersekletek)} napnak átlaghőmérséklete: {round(osszeg/len(homersekletek),2)}°C')
    input('\nTovább...')
    
def hottestDay():
    system('cls')
    print('A legmelegebb napok\n')
    max_value=max(homersekletek.values())
    max_key=[key for key, value in homersekletek.items() if value == max(homersekletek.values())]
    max_days=', '.join(max_key)
    print(f'A legmelegebb nap/napok: {max_days}. \n E napi átlaghőmérséklet: {max_value}')
    input('\nTovább...')
    
def coldestDay():
    system('cls')
    print('A leghidegebb napok\n')
    min_value=min(homersekletek.values())
    min_key=[key for key, value in homersekletek.items() if value == min(homersekletek.values())]
    min_days=', '.join(min_key)
    print(f'A legmelegebb nap/napok: {min_days}. \nE napi átlaghőmérséklet: {min_value}')
    input('\nTovább...')

def tempInKelvin():
    system('cls')
    print('Átváltás Kelvinbe\n')
    
    print('Hőmérsékletek: \n')
    for key,value in homersekletek.items():
        print(f'{key} - {value}°C')
    nap=input('\nMelyik napnak hőmérsékletét szertné átváltani? [hónap.nap]: ')
    Celsius=homersekletek.get(nap,'Ez a nap nem található meg az adatbázisban!')
    if type(Celsius)==int:
        print(f'\n{Celsius}°C az {Celsius+273.15} K')
    else:
        print('\nEz a nap nem található meg az adatbázisban!')
    input('\nTovább...')
    