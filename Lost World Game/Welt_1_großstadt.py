class Welt_1_großstadt:

    def kreuzung(self):
        """Wird aufgerufen, wenn der Spieler an der Kreuzung ist (5 Schritte erreicht)."""
        print("\nDu stehst an einer Kreuzung. Es geht nach links oder rechts...\n")

        while True:
            entscheidung = input("\nWillst du nach links gehen ( ein mysteriöser Pfad, der nachhause führt ) oder nach rechts gehen ( in eine angesagte Bar ) ? "
                                 "\nTippe = LINKS = oder "
                                 "\nTippe = RECHTS = ein: ").lower()

            if entscheidung == "links":
                self.geheimer_weg()
                break
            elif entscheidung == "rechts":
                self.geht_in_bar()
                break
            else:
                print("Ungültige Eingabe. Drücke 'a' für den geheimen Weg oder 'd' für die Bar.")

    @staticmethod
    def geheimer_weg():
        print("\nDer dunkle Pfad windet sich durch enge Gassen...")
        print("Es ist ruhig. Zu ruhig. Nur das Echo deiner Schritte hallt in der Ferne.")
        print("Plötzlich... siehst du dein Haus! Ein geheimer Weg hat dich sicher nach Hause gebracht. 🏠")
        print("\nDu hast das Spiel erfolgreich beendet! 🎉\n")

    @staticmethod
    def geht_in_bar():
        print("\nNeonlichter flackern. Musik dröhnt aus der Bar...")
        print("Drinnen lachen Leute, tanzen und trinken. Eine verrauchte, mysteriöse Stimmung liegt in der Luft.")
        print("Du setzt dich an die Bar und bestellst etwas zu trinken. 🍸")
        print("\nWer weiß, was diese Nacht noch bringt...? Fortsetzung folgt!\n")



            eingabe = input("\nDrücke: \n= W = für vorwärts, "
                            "\n'Q' um zu beenden: ").lower()
