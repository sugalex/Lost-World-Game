
from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    create_table_query = """
    CREATE TABLE Kampf_Details (
    Detail_ID INT PRIMARY KEY AUTO_INCREMENT,
    Kampf_ID INT,
    Zugnummer INT,
    Charakter_Schaden INT,
    Monster_Schaden INT,
    Charakter_HP INT,
    Monster_HP INT,
    Aktion VARCHAR(50),  
    Zeitpunkt TIMESTAMP,  
    Aktion_Details VARCHAR(100)  
    );
        """

    execute_query(conn, create_table_query)
    conn.close()