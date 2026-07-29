import os
import mysql.connector

def get_db_connection():
    """
    Establece y retorna una conexión a la base de datos MySQL.
    Utiliza variables de entorno (útiles para Railway) y respaldo local si no existen.
    """
    connection = mysql.connector.connect(
        host=os.getenv('MYSQLHOST', 'localhost'),
        user=os.getenv('MYSQLUSER', 'root'),
        password=os.getenv('MYSQLPASSWORD', '242716'),  # Tu contraseña local actual
        database=os.getenv('MYSQLDATABASE', 'veci_alerta_db'),
        port=int(os.getenv('MYSQLPORT', 3306))
    )
    return connection