from functions import *

loadTemp()

choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        printAllTemps()
    elif choice=='2':
        addNewTemp()
    elif choice=='3':
        deleteTemp()
    elif choice=='4':
        averageTemp()
    elif choice=='5':
        hottestDay()
    elif choice=='6':
        coldestDay()
    elif choice=='7':
        tempInKelvin()