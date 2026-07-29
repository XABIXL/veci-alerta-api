from config import get_db_connection

class ServicioLocalService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM servicios_locales")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def crear(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO servicios_locales (nombre_servicio, categoria, telefono, direccion, descripcion) VALUES (%s, %s, %s, %s, %s)"
        valores = (datos.get('nombre_servicio'), datos.get('categoria'), datos.get('telefono'), datos.get('direccion'), datos.get('descripcion'))
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id