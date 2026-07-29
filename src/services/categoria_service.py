from config import get_db_connection

class CategoriaService:
    @staticmethod
    def obtener_todas():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorias (nombre_categoria) VALUES (%s)", (datos.get('nombre_categoria'),))
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id