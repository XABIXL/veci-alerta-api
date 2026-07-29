from config import get_db_connection

class NotificacionService:
    @staticmethod
    def obtener_todas():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notificaciones ORDER BY fecha_notificacion DESC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO notificaciones (id_usuario, mensaje, leida) VALUES (%s, %s, %s)"
        valores = (datos.get('id_usuario'), datos.get('mensaje'), datos.get('leida', 0))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id