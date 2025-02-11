from SQL_connection import create_connection, execute_query

# Verbindung zur Datenbank herstellen
conn =create_connection()

if conn:
# SQL-Befehl zur Erstellung der Tabelle `Welt`
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Charakter (
        Charakter_ID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(50),
        Klasse VARCHAR(50),
        Level INT,
        Staerke INT,
        Aktuelle_HP INT,
        MAX_HP INT,
        Erfahrungspunkte INT,
        Waffe_ID INT,
        Komplett_Ruestung INT,
        Brust_Ruestung INT,
        Erstelldatum TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (Waffe_ID) REFERENCES Waffe(Waffe_ID),
        FOREIGN KEY (Komplett_Ruestung) REFERENCES Ruestung(Ruestung_ID),
        FOREIGN KEY (Brust_Ruestung) REFERENCES Ruestung(Ruestung_ID)

    );
    """
# Abfrage ausführen
execute_query(conn, create_table_query)

# Verbindung schließen
conn.close()