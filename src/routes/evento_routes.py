from flask import Blueprint, jsonify, request
from services.evento_service import EventoService

evento_bp = Blueprint('evento_bp', __name__)

@evento_bp.route('/api/eventos', methods=['GET'])
def obtener_eventos():
    return jsonify(EventoService.obtener_todos()), 200

@evento_bp.route('/api/eventos/<int:id_evento>', methods=['GET'])
def obtener_evento_por_id(id_evento):
    evento = EventoService.obtener_por_id(id_evento)
    if evento:
        return jsonify(evento), 200
    return jsonify({"error": "Evento no encontrado"}), 404

@evento_bp.route('/api/eventos', methods=['POST'])
def crear_evento():
    nuevo_id = EventoService.crear(request.json)
    return jsonify({'mensaje': 'Evento creado con éxito', 'id_evento': nuevo_id}), 201

@evento_bp.route('/api/eventos/<int:id_evento>', methods=['PUT'])
def actualizar_evento(id_evento):
    EventoService.actualizar(id_evento, request.json)
    return jsonify({'mensaje': 'Evento actualizado correctamente'}), 200

@evento_bp.route('/api/eventos/<int:id_evento>', methods=['DELETE'])
def eliminar_evento(id_evento):
    EventoService.eliminar(id_evento)
    return jsonify({'mensaje': 'Evento eliminado correctamente'}), 200