from flask import Blueprint, jsonify, request
from services.servicio_local_service import ServicioLocalService

servicio_local_bp = Blueprint('servicio_local_bp', __name__)

@servicio_local_bp.route('/api/servicios', methods=['GET'])
def obtener_servicios():
    return jsonify(ServicioLocalService.obtener_todos()), 200

@servicio_local_bp.route('/api/servicios', methods=['POST'])
def crear_servicio():
    nuevo_id = ServicioLocalService.crear(request.json)
    return jsonify({'mensaje': 'Servicio local agregado', 'id_servicio': nuevo_id}), 201