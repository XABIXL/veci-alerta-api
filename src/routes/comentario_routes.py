from flask import Blueprint, jsonify, request
from services.comentario_service import ComentarioService

comentario_bp = Blueprint('comentario_bp', __name__)

@comentario_bp.route('/api/comentarios', methods=['GET'])
def obtener_comentarios():
    return jsonify(ComentarioService.obtener_todos()), 200

@comentario_bp.route('/api/comentarios', methods=['POST'])
def crear_comentario():
    nuevo_id = ComentarioService.crear(request.json)
    return jsonify({'mensaje': 'Comentario agregado', 'id_comentario': nuevo_id}), 201

@comentario_bp.route('/api/comentarios/<int:id_comentario>', methods=['DELETE'])
def eliminar_comentario(id_comentario):
    ComentarioService.eliminar(id_comentario)
    return jsonify({'mensaje': 'Comentario eliminado correctamente'}), 200