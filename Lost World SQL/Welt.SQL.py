
from SQL_connection import create_connection, execute_query

# Verbindung zur Datenbank herstellen
conn = create_connection()

if conn:
    # SQL-Befehl zur Erstellung der Tabelle `Welt`
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Welt (
        Welt_ID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(50) NOT NULL,
        Schwierigkeitsgrad INT,
        Beschreibung TEXT,
        Umgebungstyp VARCHAR(20),
        Max_Level INT
    );
    """
    # Abfrage ausführen
    execute_query(conn, create_table_query)

    # Verbindung schließen
    conn.close()