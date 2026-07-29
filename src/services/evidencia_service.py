from config import get_db_connection

class EvidenciaService:
    @staticmethod
    def obtener_todas():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM evidencias_reportes")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO evidencias_reportes (id_reporte, url_imagen) VALUES (%s, %s)"
        cursor.execute(query, (datos.get('id_reporte'), datos.get('url_imagen')))
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id