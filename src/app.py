import os
from flask import Flask, jsonify
from flask_cors import CORS

# Importar la conexión desde config.py
from config import get_db_connection

# Importar todos los Blueprints de rutas
from routes.rol_routes import rol_bp
from routes.usuario_routes import usuario_bp
from routes.categoria_routes import categoria_bp
from routes.estado_reporte_routes import estado_reporte_bp
from routes.reporte_routes import reporte_bp
from routes.evidencia_routes import evidencia_bp
from routes.emergencia_routes import emergencia_bp
from routes.foro_routes import foro_bp
from routes.comentario_routes import comentario_bp
from routes.evento_routes import evento_bp
from routes.servicio_local_routes import servicio_local_bp
from routes.notificacion_routes import notificacion_bp
from routes.grupo_routes import grupo_bp

app = Flask(__name__)
CORS(app)

# Registrar Blueprints
app.register_blueprint(rol_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(estado_reporte_bp)
app.register_blueprint(reporte_bp)
app.register_blueprint(evidencia_bp)
app.register_blueprint(emergencia_bp)
app.register_blueprint(foro_bp)
app.register_blueprint(comentario_bp)
app.register_blueprint(evento_bp)
app.register_blueprint(servicio_local_bp)
app.register_blueprint(notificacion_bp)
app.register_blueprint(grupo_bp)

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({"mensaje": "¡API modularizada de VeciAlerta funcionando al 100%! 🚀🏡"})

# Ruta de prueba para verificar la conexión a la base de datos
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT DATABASE() as db;")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return jsonify({
            "estado": "Conexión exitosa",
            "base_de_datos": result['db']
        })
    except Exception as ex:
        return jsonify({
            "estado": "Error de conexión",
            "detalles": str(ex)
        }), 500

if __name__ == '__main__':
    with app.app_context():
        print("--- RUTAS REGISTRADAS EN LA API ---")
        for regla in app.url_map.iter_rules():
            print(f"Ruta: {regla.rule} --> Métodos permitidos: {list(regla.methods)}")

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)