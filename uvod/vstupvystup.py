jmeno = input("Zadejte své jméno")  # textova promenna
vek = input("Zadejte svůj věk")            
vek = int(vek)          # ciselna promenna
bratr = input("Zadejte, zda máte bratra (True/False)")       # logicka promenna
bratr = bool(bratr)
sestra = input("Zadejte, zda máte sestru (True/False)")
sestra = bool(sestra)

print("Výstup je: ", jmeno, vek, bratr, sestra)
print("Typy proměnných jsou:")
print("jmeno: ", str(type(jmeno)))
print("vek:", str(type(vek)))
print("bratr: ", str(type(bratr)))
print("sestra: ", str(type(sestra)))