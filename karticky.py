import json
class Karta:
    def __init__(self, nazev, kategorie):
        self.nazev = nazev
        self.kategorie = kategorie    

    def __str__(self):
        return f"Karta {self.nazev} se vzácností úrovně {self.kategorie}"
    
    def kde_mam_karticku(self, file):
        with open(file) as f:
            data = json.load(f)
            self.kategorie = data["kategorie"]
            self.nazev = data["nazev"]
    
k = Karta("NaPikachu", "Treskyplesky")
print(k)
k.kde_mam_karticku('vkapsicce')
print(k)