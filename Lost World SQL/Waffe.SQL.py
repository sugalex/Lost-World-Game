from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Waffe (
        Waffe_ID INT PRIMARY KEY AUTO_INCREMENT,
        Klasse VARCHAR(20),
        Name VARCHAR(50),
        Stufe INT,
        Schaden INT,
     Besonderer_Effekt VARCHAR(100)
    );   
    
    """

execute_query(conn, create_table_query)
conn.close()