from flask import Blueprint, jsonify, request
from services.emergencia_service import EmergenciaService

emergencia_bp = Blueprint('emergencia_bp', __name__)

@emergencia_bp.route('/api/emergencias', methods=['GET'])
def obtener_emergencias():
    return jsonify(EmergenciaService.obtener_todas()), 200

@emergencia_bp.route('/api/emergencias', methods=['POST'])
def crear_emergencia():
    nuevo_id = EmergenciaService.crear(request.json)
    return jsonify({'mensaje': 'Emergencia SOS registrada', 'id_emergencia': nuevo_id}), 201