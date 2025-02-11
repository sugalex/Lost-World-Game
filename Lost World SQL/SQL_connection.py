import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        # Verbinde mit der MySQL-Datenbank
        connection = mysql.connector.connect(
            host="127.0.0.1",      # oder die IP deines Servers
            port=3306,
            user="root",
            password="",
            database="The real Lost World"
        )
        if connection.is_connected():
            print("Verbindung zur MySQL-Datenbank erfolgreich.")
        return connection
    except Error as e:
        print(f"Fehler bei der Verbindung: {e}")
        return None

# Beispiel zum Ausführen einer Abfrage
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Abfrage erfolgreich ausgeführt")
    except Error as e:
        print(f"Fehler bei der Abfrage: {e}")


