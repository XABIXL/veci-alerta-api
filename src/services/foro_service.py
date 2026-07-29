from config import get_db_connection

class ForoService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM foros ORDER BY fecha_publicacion DESC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def obtener_por_id(id_foro):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM foros WHERE id_foro = %s", (id_foro,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO foros (id_usuario, titulo, contenido, foto_foro) VALUES (%s, %s, %s, %s)"
        valores = (datos.get('id_usuario'), datos.get('titulo'), datos.get('contenido'), datos.get('foto_foro'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id

    @staticmethod
    def actualizar(id_foro, datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE foros SET titulo = %s, contenido = %s, foto_foro = %s WHERE id_foro = %s"
        valores = (datos.get('titulo'), datos.get('contenido'), datos.get('foto_foro'), id_foro)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar(id_foro):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM foros WHERE id_foro = %s", (id_foro,))
        conn.commit()
        cursor.close()
        conn.close()