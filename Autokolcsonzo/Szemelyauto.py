from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ajtok_szama = ajtok_szama

    def __str__(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap, Ajtók száma: {self.ajtok_szama}"
