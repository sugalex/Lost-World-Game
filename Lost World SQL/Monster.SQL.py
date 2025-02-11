
from SQL_connection import create_connection, execute_query

conn = create_connection()

if conn:
    create_table_query = """

CREATE TABLE Monster (
    Monster_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Stufe INT NOT NULL,
    Max_HP INT NOT NULL,
    Aktuelle_HP INT NOT NULL,
    Staerke INT NOT NULL,
    Attacke VARCHAR(100) NOT NULL,
    Schadensbereich VARCHAR(20),
    Beschreibung TEXT,
    Monster_spawntime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
        """

    execute_query(conn, create_table_query)
    conn.close()