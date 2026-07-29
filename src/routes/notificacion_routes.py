from flask import Blueprint, jsonify, request
from services.notificacion_service import NotificacionService

notificacion_bp = Blueprint('notificacion_bp', __name__)

@notificacion_bp.route('/api/notificaciones', methods=['GET'])
def obtener_notificaciones():
    return jsonify(NotificacionService.obtener_todas()), 200

@notificacion_bp.route('/api/notificaciones', methods=['POST'])
def crear_notificacion():
    nuevo_id = NotificacionService.crear(request.json)
    return jsonify({'mensaje': 'Notificación creada', 'id_notificacion': nuevo_id}), 201