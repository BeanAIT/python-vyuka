rozmer = int(input("rozmer"))

for radek in range(0, rozmer): # výška pyramidy (řádky)
    for sloupec in range(radek, rozmer): # mezery
        print(' ', end='')
    for sloupec in range(0, radek):     # hvězdičky
        print('* ', end='')
    print('')