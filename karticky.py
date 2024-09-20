import json
class Karta:
    def __init__(self, nazev, kategorie):
        self.nazev = nazev
        self.kategorie = kategorie    

    def __str__(self):
        return f"Karta {self.nazev} se vzácností úrovně {self.kategorie}"
    
    def kde_mam_karticku(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            self.kategorie = Karta['kategorie']
            self.nazev = Karta['nazev']
    

k = Karta("aha", "no nevim hele")
k.kde_mam_karticku("vkapsicce.json")
print(k)