list = []     # vytvoří nový list (pythoní pole)
vstup = input("Zadejte cislo, q pro ukonceni")  # do promenne 'vstup' to ulozi nacteny vstup
while (vstup != "q"):   # dokud ve vstupu neni 'q'
    list.append(int(vstup))  # do listu pridam to, co uzivatel zadal do vstupu
    vstup = input("Zadejte cislo, q pro ukonceni")  # nactu dalsi vstup
print(list)     # vypisu, co jsem si ulozil do listu
soucet = 0
for i in list:
    soucet += i
print("Soucet cisel je: ", soucet)
