from Berles import Berles


class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_felvetele(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        for auto in self.autok:
            print(auto)

    def autoberles(self, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            print("Ez az autó nem bérelhető.")
            return
        berles = Berles(auto, datum)
        self.berlesek.append(berles)
        print(f"Sikeres bérlés! Az autó bérleti díja: {auto.berleti_dij} Ft/nap")
        return auto.berleti_dij

    def berles_lemondasa(self, rendszam):
        berles = next((b for b in self.berlesek if b.auto.rendszam == rendszam), None)
        if not berles:
            print("Nincs ilyen bérlés.")
            return
        self.berlesek.remove(berles)
        print(f"Bérlés lemondva: {rendszam}")

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincsenek aktív bérlések.")
        for berles in self.berlesek:
            print(berles)