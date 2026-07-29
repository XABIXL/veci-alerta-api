from config import get_db_connection

class EmergenciaService:
    @staticmethod
    def obtener_todas():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM emergencias_sos ORDER BY fecha_alerta DESC")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO emergencias_sos (id_usuario, latitud, longitud, estado_emergencia) VALUES (%s, %s, %s, %s)"
        valores = (datos.get('id_usuario'), datos.get('latitud'), datos.get('longitud'), datos.get('estado_emergencia', 'Activa'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id