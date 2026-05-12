for radek in range(1,10):
    for sloupec in range(0,10-radek):
        print(" ", end='')
    for sloupec in range(radek,0,-1):
        print(sloupec,end='')
    print()