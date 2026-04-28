def nactiCislo(): # nacte z konzole cele cislo
    return int(input("Zadejte číslo"))

prvniCislo = nactiCislo() # nacti prvni cislo
druheCislo = nactiCislo() # nacti druhe cislo
operace = input("Zadejte znak operace")
if (operace == "+"): # proved soucet / rozdil / soucin / podil
    vysledek = prvniCislo + druheCislo
elif (operace == "-"):
    vysledek = prvniCislo - druheCislo
elif (operace == "*"):
    vysledek = prvniCislo * druheCislo
elif (operace == "u"):
    vysledek = prvniCislo ** druheCislo
elif (operace == "o"):
    vysledek = prvniCislo ** (1 / druheCislo)
else:
    vysledek = prvniCislo / druheCislo
# zobraz vysledek
print("Výsledek je", vysledek)

# odmocneni : o
# umocneni : u    ** 