from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Weltitems (
    Item_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50),
    Stufe INT,
    Staerke_Bonus INT,
    Heilwert INT,
    Dauer_in_Zuegen INT,
    Beschreibung TEXT
    );
    """


execute_query(conn, create_table_query)
conn.close()