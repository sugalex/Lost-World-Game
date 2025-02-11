from Spieler import Spieler

class World:

    def __init__(self):
        self.spieler = Spieler()
        self.schritte = [None] * self.spieler.max_schritte

    def main(self):
        while True:
            eingabe = input("Drücke 'w' für einen Schritt nach vorne: ")
            if eingabe.lower() == "w":
                self.spieler.vorwaerts_gehen()
                if self.spieler.position >= self.spieler.max_schritte -1:
                    break
            else:
                print("Ungültige Eingabe. Drücke 'w'")




if __name__ == "__main__":
    welt = World()
    welt.main()