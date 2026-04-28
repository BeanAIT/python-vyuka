sirka = int(input("Zadejte šířku obdélníku"))
vyska = int(input("Zadejte výšku obdélníku"))

for radek in range(0, vyska):
    for sloupec in range(0, sirka):
        print('*', end='')
    print()