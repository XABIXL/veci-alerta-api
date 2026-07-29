from config import get_db_connection

class ComentarioService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM comentarios ORDER BY fecha_comentario ASC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO comentarios (id_foro, id_usuario, contenido_comentario) VALUES (%s, %s, %s)"
        valores = (datos.get('id_foro'), datos.get('id_usuario'), datos.get('contenido_comentario'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id

    @staticmethod
    def eliminar(id_comentario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM comentarios WHERE id_comentario = %s", (id_comentario,))
        conn.commit()
        cursor.close()
        conn.close()