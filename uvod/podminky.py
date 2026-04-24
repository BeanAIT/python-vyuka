cisloStr = input("Zadejte číslo")
cislo = int(cisloStr)
if(cislo > 0):
    print(cislo, "je kladné")
    if(cislo == 5):
        print("Zadal jste moje oblíbené číslo!")
elif(cislo < 0):
    print(cislo, "je záporné")
else:
    print(cislo, "je nula")