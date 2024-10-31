from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo


kolcsonzo = Autokolcsonzo("Autókölcsönzés")

auto1 = Szemelyauto("AB-CD-123", "BMW M3 competition Touring", 80000, 2)
auto2 = Szemelyauto("EF-GH-456", "Audi Q6 Sportback", 75000, 4)
auto3 = Teherauto("ij-kl-789", "Volkswagen Crafter", 50000, 1300)

kolcsonzo.autok_felvetele(auto1)
kolcsonzo.autok_felvetele(auto2)
kolcsonzo.autok_felvetele(auto3)

kolcsonzo.autoberles("AB-CD-123", "2023-11-01")
kolcsonzo.autoberles("EF-GH-456", "2023-11-02")
kolcsonzo.autoberles("ij-kl-789", "2023-11-03")
kolcsonzo.autoberles("EF-GH-456", "2023-11-04")


def felhasznaloi_menu():
    while True:
        print("\n--- Autókölcsönző Rendszer ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("5. Autók listázása")
        print("6. Kilépés")

        valasztas = input("Válasszon egy lehetőséget: ")

        if valasztas == "1":
            rendszam = input("Adja meg az autó rendszámát: ")
            datum = input("Adja meg a bérlés dátumát (YYYY-MM-DD): ")
            kolcsonzo.autoberles(rendszam, datum)
        elif valasztas == "2":
            rendszam = input("Adja meg a lemondani kívánt autó rendszámát: ")
            kolcsonzo.berles_lemondasa(rendszam)
        elif valasztas == "3":
            rendszam = input("Adja meg a visszahozni kívánt autó rendszámát: ")
            kolcsonzo.auto_visszahozasa(rendszam)
        elif valasztas == "4":
            print("\nAktív bérlések:")
            kolcsonzo.berlesek_listazasa()
        elif valasztas == "5":
            print("\nElérhető autók:")
            kolcsonzo.autok_listazasa()
        elif valasztas == "6":
            print("Kilépés a rendszerből.")
            break
        else:
            print("Érvénytelen választás, próbálja újra.")

felhasznaloi_menu()
