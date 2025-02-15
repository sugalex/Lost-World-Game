from Spieler import Spieler
from Welt_1_großstadt import Welt_1_großstadt

class LevelManager:

    def __init__(self):
        self.spieler = Spieler()  # Initialisiert den Spieler
        self.welt_1 = Welt_1_großstadt()  # Erstes Level laden

    def start(self):
        """Startet das Spiel."""
        print("\nWillkommen in Lost World\n")
        print(input("Wähle deinen Namen: "))
        self.spieler.spiel_starten()  # Ruft die Spiellogik in Spieler.py auf

if __name__ == "__main__":
    level_manager = LevelManager()
    level_manager.start()
