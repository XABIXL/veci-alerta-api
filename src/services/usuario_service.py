from config import get_db_connection

class UsuarioService:
    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_usuario, id_rol, nombre, apellido, correo, telefono, calle_lote, foto_perfil FROM usuarios")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def obtener_por_id(id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def registrar(datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (id_rol, nombre, apellido, telefono, correo, contrasena, calle_lote, foto_perfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        
        # Resuelve el valor de la contraseña sin importar si viene como 'contrasena' o 'password'
        contrasena_usuario = datos.get('contrasena') or datos.get('password')
        
        valores = (
            datos.get('id_rol'), 
            datos.get('nombre'), 
            datos.get('apellido'), 
            datos.get('telefono'), 
            datos.get('correo'), 
            contrasena_usuario, 
            datos.get('calle_lote'), 
            datos.get('foto_perfil')
        )
        
        cursor.execute(query, valores)
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return nuevo_id

    @staticmethod
    def crear_usuario(datos):
        return UsuarioService.registrar(datos)

    @staticmethod
    def actualizar(id_usuario, datos):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET id_rol = %s, nombre = %s, apellido = %s, telefono = %s, correo = %s, calle_lote = %s, foto_perfil = %s WHERE id_usuario = %s"
        valores = (datos.get('id_rol'), datos.get('nombre'), datos.get('apellido'), datos.get('telefono'), datos.get('correo'), datos.get('calle_lote'), datos.get('foto_perfil'), id_usuario)
        cursor.execute(query, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar(id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        conn.commit()
        cursor.close()
        conn.close()