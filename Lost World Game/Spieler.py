class Spieler:

    def __init__(self):
        self.position = 0
        self.max_schritte = 11

    def vorwaerts_gehen(self):
        self.position += 1
        print(f"Der Spieler ist ein Schritt nach vorne gegangen. Position {self.position}")