import random
from Welt_1_großstadt import Welt_1_großstadt

class Spieler:

    def __init__(self):
        self.position = 0  # Schritte nach vorne
        self.max_schritte = 11  # Maximale Schritte im Level
        self.schritte_nach_wurf = 0  # Verbleibende Schritte nach dem Würfeln
        self.welt_1 = Welt_1_großstadt()  # Erstes Level vorbereiten

    def spiel_starten(self):
        """Hauptspiel-Schleife, die das Spiel steuert."""
        while True:
            if self.schritte_nach_wurf == 0:
                input("Drücke = F =, um zu würfeln: ")
                self.wuerfeln()

            eingabe = input("\nDrücke: \n= W = für vorwärts, "
                            "\n= Q = um zu beenden: ").lower()

            if eingabe == "w":
                self.vorwaerts_gehen()
                if self.position == 5:  # Wenn 5 Schritte erreicht sind, rufe Kreuzung in Welt_1 auf
                    self.welt_1.kreuzung()  # Übergibt Kontrolle an Welt_1_großstadt
                continue

            elif eingabe == "q":
                print("Spiel wird beendet.")
                break  # Beende die Schleife

            else:
                print("Ungültige Eingabe oder keine Schritte mehr übrig.")

            print(f"Du bist jetzt auf Position {self.position}, noch {self.schritte_nach_wurf} Schritte übrig.")

    def wuerfeln(self):
        """Würfelt eine Zahl zwischen 1 und 6 und speichert die Schritte."""
        self.schritte_nach_wurf = random.randint(1, 6)
        print(f"Du hast eine {self.schritte_nach_wurf} gewürfelt.")

    def vorwaerts_gehen(self):
        """Bewegt den Spieler einen Schritt nach vorne, wenn noch Schritte übrig sind."""
        if self.schritte_nach_wurf > 0:
            self.position += 1
            self.schritte_nach_wurf -= 1
            print(f"Der Spieler geht einen Schritt nach vorne. Position: {self.position}")
        else:
            print("Keine Schritte mehr übrig! Würfle zuerst.")

    def links_gehen(self):
        """Bewegt den Spieler nach links (kein x/y mehr, nur Story-Ereignis)."""
        print(f"Der Spieler biegt nach links ab.")

    def rechts_gehen(self):
        """Bewegt den Spieler nach rechts (kein x/y mehr, nur Story-Ereignis)."""
        print(f"Der Spieler biegt nach rechts ab.")
