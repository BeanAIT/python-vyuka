#oblibeneOvoce = ["avokádo", "banán", "jablko", "pomeranč", "víno", "kiwi"]
oblibeneOvoce = []
noveOvoce = ""
while(noveOvoce != "x"):
    noveOvoce = input("Zadejte ovoce, nebo 'x' pro ukončení")
    if(noveOvoce != "x"):
        oblibeneOvoce.append(noveOvoce)
print(oblibeneOvoce)
nejoblibenejsiOvoceIdx = input("Zadejte pořadí v listu, kde je vaše oblíbené ovoce")
nejoblibenejsiOvoce = oblibeneOvoce[int(nejoblibenejsiOvoceIdx) - 1]
print("vaše oblíbené ovoce je: ", nejoblibenejsiOvoce)