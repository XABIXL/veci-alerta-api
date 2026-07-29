from flask import Blueprint, jsonify, request
from services.evidencia_service import EvidenciaService

evidencia_bp = Blueprint('evidencia_bp', __name__)

@evidencia_bp.route('/api/evidencias-reportes', methods=['GET'])
def obtener_evidencias():
    return jsonify(EvidenciaService.obtener_todas()), 200

@evidencia_bp.route('/api/evidencias-reportes', methods=['POST'])
def crear_evidencia():
    nuevo_id = EvidenciaService.crear(request.json)
    return jsonify({'mensaje': 'Evidencia agregada', 'id_evidencia': nuevo_id}), 201