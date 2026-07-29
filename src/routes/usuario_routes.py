from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

from config import get_db_connection

# Definición exacta del Blueprint
usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/api/usuarios')

@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = UsuarioService.obtener_todos()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@usuario_bp.route('/', methods=['POST'])
def registrar_usuario():
    try:
        data = request.get_json()
        campos_requeridos = ['id_rol', 'nombre', 'correo', 'password']
        for campo in campos_requeridos:
            if not data or campo not in data:
                return jsonify({"error": f"El campo '{campo}' es obligatorio"}), 400

        resultado = UsuarioService.crear_usuario(data)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500