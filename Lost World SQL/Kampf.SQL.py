from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Kampf (
    Kampf_ID INT PRIMARY KEY AUTO_INCREMENT,
    Charakter_ID INT,
    Waffe_ID int, 
    Ruestung_ID int, 
    Level int, 
    Startzeit_Kampf TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Endzeit_Kampf timestamp null,
    WINorLOSE varchar(50)
);
        """

    execute_query(conn, create_table_query)
    conn.close()