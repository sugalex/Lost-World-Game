from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    ceate_table_query = """
    
    CREATE TABLE IF NOT EXISTS Ruestung (
        Ruestung_ID INT PRIMARY KEY AUTO_INCREMENT,
        Ruestungsteil VARCHAR(30),
        Seltenheit VARCHAR (20),
        Verteidigung INT,
        Infoblatt TEXT,
        Charakter_ID INT,
    
        FOREIGN KEY (Charakter_ID) REFERENCES Charakter(Charakter_ID)
    );
    

    """

    execute_query(conn, ceate_table_query)
    conn.close()
