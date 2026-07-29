from flask import Blueprint, jsonify, request
from services.rol_service import RolService

rol_bp = Blueprint('rol_bp', __name__)

@rol_bp.route('/api/roles', methods=['GET'])
def obtener_roles():
    return jsonify(RolService.obtener_todos()), 200

@rol_bp.route('/api/roles', methods=['POST'])
def crear_rol():
    nuevo_id = RolService.crear(request.json)
    return jsonify({'mensaje': 'Rol creado con éxito', 'id_rol': nuevo_id}), 201