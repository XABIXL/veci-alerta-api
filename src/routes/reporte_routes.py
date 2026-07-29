from flask import Blueprint, jsonify, request
from services.reporte_service import ReporteService

reporte_bp = Blueprint('reporte_bp', __name__)

@reporte_bp.route('/api/reportes', methods=['GET'])
def obtener_reportes():
    return jsonify(ReporteService.obtener_todos()), 200

@reporte_bp.route('/api/reportes/<int:id_reporte>', methods=['GET'])
def obtener_reporte_por_id(id_reporte):
    reporte = ReporteService.obtener_por_id(id_reporte)
    if reporte:
        return jsonify(reporte), 200
    return jsonify({"error": "Reporte no encontrado"}), 404

@reporte_bp.route('/api/reportes', methods=['POST'])
def crear_reporte():
    nuevo_id = ReporteService.crear(request.json)
    return jsonify({'mensaje': 'Reporte creado con éxito', 'id_reporte': nuevo_id}), 201

@reporte_bp.route('/api/reportes/<int:id_reporte>', methods=['PUT'])
def actualizar_reporte(id_reporte):
    ReporteService.actualizar(id_reporte, request.json)
    return jsonify({'mensaje': 'Reporte actualizado correctamente'}), 200

@reporte_bp.route('/api/reportes/<int:id_reporte>', methods=['DELETE'])
def eliminar_reporte(id_reporte):
    ReporteService.eliminar(id_reporte)
    return jsonify({'mensaje': 'Reporte eliminado correctamente'}), 200