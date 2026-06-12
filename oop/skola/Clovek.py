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