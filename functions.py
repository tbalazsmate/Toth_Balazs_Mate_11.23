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
