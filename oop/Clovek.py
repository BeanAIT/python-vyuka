class Clovek:
    
    def __init__(self, jmeno="", prijmeni="", pohlavi="", vek=-1):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pohlavi = pohlavi
        self.vek = vek
    
    def __str__(self):
        return f"Clovek => Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Pohlaví: {self.pohlavi}, Věk: {self.vek}"

    def jeMuz(self):
        if (self.pohlavi == "muz" or self.pohlavi == "muž"):
            return True
        else:
            return False

zaci = []        
zaci.append(Clovek("David", "Reschke", "muž", 19))
zaci.append(Clovek("Petr", "Bui", "muž", 19))
zaci.append(Clovek("Natalie", "Mikšovská", "žena", 19))
zaci.append(Clovek("Armin", "Lyavinets", "muž", 18))
zaci.append(Clovek("Nicholas", "Ras", "muž", 18))
zaci.append(Clovek("Samuel", "El Bakri", "muž", 18))

for zak in zaci:
    print(zak)