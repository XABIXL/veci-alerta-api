from config import get_db_connection

class EventoService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM eventos ORDER BY fecha_evento ASC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def obtener_por_id(id_evento):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM eventos WHERE id_evento = %s", (id_evento,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO eventos (id_usuario, titulo, descripcion, fecha_evento, lugar, foto_evento) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (datos.get('id_usuario'), datos.get('titulo'), datos.get('descripcion'), datos.get('fecha_evento'), datos.get('lugar'), datos.get('foto_evento'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id

    @staticmethod
    def actualizar(id_evento, datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE eventos SET titulo = %s, descripcion = %s, fecha_evento = %s, lugar = %s, foto_evento = %s WHERE id_evento = %s"
        valores = (datos.get('titulo'), datos.get('descripcion'), datos.get('fecha_evento'), datos.get('lugar'), datos.get('foto_evento'), id_evento)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar(id_evento):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM eventos WHERE id_evento = %s", (id_evento,))
        conn.commit()
        cursor.close()
        conn.close()