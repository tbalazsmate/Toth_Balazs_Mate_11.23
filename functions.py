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
    input('tovább...')

def addNewTemp():
    system('cls')
    print('Új nap:\n')
    nap=input('Adja meg a dátumot [hónap.nap]: ')
    temp=int(input('A nap átlaghőmérséklete: '))
    homersekletek[nap]=temp
    saveTempToFile(nap,temp)
    input('Adat sikeresen felvéve. Tovább...')

def saveTempToFile(nap,temp):
    file=open(filename,'a', encoding='utf-8')
    file.write(f'\n{nap};{temp}')
    file.close()
    
def deleteTemp():
    system('cls')
    print('Adat törlése\n')
    nap=input('Adja meg a törlendő adat dátumát [Hónap.Nap]: ')
    if nap in homersekletek:
        homersekletek.pop(nap)
        saveAllToFile()
        input('A megadott dátum adatai törölve. Tovább...')
    else:
        print('Erre a dátumra nincs adat megadva. Tovább...')
        
def saveAllToFile():
    file=open(filename, 'w', encoding='utf-8')
    file.write(cimsor)
    for key,value in homersekletek.items():
        file.write(f'\n{key};{value}')
    file.close()