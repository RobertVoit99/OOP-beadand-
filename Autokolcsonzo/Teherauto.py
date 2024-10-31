from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherkapacitas):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherkapacitas = teherkapacitas

    def __str__(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap, Teherkapacitás: {self.teherkapacitas} kg"


