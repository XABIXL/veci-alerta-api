from config import get_db_connection

class GrupoService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM grupos")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO grupos (nombre_grupo, descripcion) VALUES (%s, %s)"
        valores = (datos.get('nombre_grupo'), datos.get('descripcion'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id