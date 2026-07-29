from config import get_db_connection

class ReporteService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reportes ORDER BY fecha_creacion DESC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def obtener_por_id(id_reporte):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reportes WHERE id_reporte = %s", (id_reporte,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO reportes (id_usuario, id_categoria, id_estado, titulo, descripcion, ubicacion) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (datos.get('id_usuario'), datos.get('id_categoria'), datos.get('id_estado'), datos.get('titulo'), datos.get('descripcion'), datos.get('ubicacion'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id

    @staticmethod
    def actualizar(id_reporte, datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE reportes SET id_categoria = %s, id_estado = %s, titulo = %s, descripcion = %s, ubicacion = %s WHERE id_reporte = %s"
        valores = (datos.get('id_categoria'), datos.get('id_estado'), datos.get('titulo'), datos.get('descripcion'), datos.get('ubicacion'), id_reporte)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar(id_reporte):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reportes WHERE id_reporte = %s", (id_reporte,))
        conn.commit()
        cursor.close()
        conn.close()