from flask import Blueprint, jsonify, request
from services.estado_reporte_service import EstadoReporteService

estado_reporte_bp = Blueprint('estado_reporte_bp', __name__)

@estado_reporte_bp.route('/api/estados-reporte', methods=['GET'])
def obtener_estados_reporte():
    return jsonify(EstadoReporteService.obtener_todos()), 200

@estado_reporte_bp.route('/api/estados-reporte', methods=['POST'])
def crear_estado_reporte():
    nuevo_id = EstadoReporteService.crear(request.json)
    return jsonify({'mensaje': 'Estado de reporte creado', 'id_estado': nuevo_id}), 201