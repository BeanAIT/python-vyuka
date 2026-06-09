class Clovek:
    def __init__(self, jmeno="", prijmeni="", pohlavi="", vek=-1):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pohlavi = pohlavi
        self.vek = vek

honza = Clovek("Honza", "Novák", "muž", 20)
petr = Clovek()
petr.jmeno = "Petr"
petr.prijmeni = "Dostál"
print(honza.jmeno)
print(petr.jmeno)