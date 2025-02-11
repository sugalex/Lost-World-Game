from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Inventar (
        Inventar_ID INT PRIMARY KEY AUTO_INCREMENT,
        Charakter_ID INT,
        Item_ID INT,
        Menge INT DEFAULT 1,
        FOREIGN KEY(Charakter_ID) REFERENCES Charakter(Charakter_ID),
        FOREIGN KEY(Item_ID) REFERENCES Weltitems(Item_ID)
    );
    """

execute_query(conn, create_table_query)
conn.close()