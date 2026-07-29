from config import get_db_connection

class EstadoReporteService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estados_reporte")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estados_reporte (nombre_estado) VALUES (%s)", (datos.get('nombre_estado'),))
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id