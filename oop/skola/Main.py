from oop.skola.Clovek import Clovek
from oop.skola.Trida import Trida

zaci = []        
zaci.append(Clovek("David", "Reschke", "muž", 19))
zaci.append(Clovek("Petr", "Bui", "muž", 19))
zaci.append(Clovek("Natalie", "Mikšovská", "žena", 19))
zaci.append(Clovek("Armin", "Lyavinets", "muž", 18))
zaci.append(Clovek("Nicholas", "Ras", "muž", 18))
zaci.append(Clovek("Samuel", "El Bakri", "muž", 18))

trida3E = Trida("3E", Clovek("Jitka", "Černochová", "žena", 29), zaci, "M5")
print(trida3E)