from flask import Blueprint, jsonify, request
from services.foro_service import ForoService

foro_bp = Blueprint('foro_bp', __name__)

@foro_bp.route('/api/foros', methods=['GET'])
def obtener_foros():
    return jsonify(ForoService.obtener_todos()), 200

@foro_bp.route('/api/foros/<int:id_foro>', methods=['GET'])
def obtener_foro_por_id(id_foro):
    foro = ForoService.obtener_por_id(id_foro)
    if foro:
        return jsonify(foro), 200
    return jsonify({"error": "Foro no encontrado"}), 404

@foro_bp.route('/api/foros', methods=['POST'])
def crear_foro():
    nuevo_id = ForoService.crear(request.json)
    return jsonify({'mensaje': 'Tema de foro creado', 'id_foro': nuevo_id}), 201

@foro_bp.route('/api/foros/<int:id_foro>', methods=['PUT'])
def actualizar_foro(id_foro):
    ForoService.actualizar(id_foro, request.json)
    return jsonify({'mensaje': 'Foro actualizado correctamente'}), 200

@foro_bp.route('/api/foros/<int:id_foro>', methods=['DELETE'])
def eliminar_foro(id_foro):
    ForoService.eliminar(id_foro)
    return jsonify({'mensaje': 'Foro eliminado correctamente'}), 200