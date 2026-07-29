from flask import Blueprint, jsonify, request
from services.grupo_service import GrupoService

grupo_bp = Blueprint('grupo_bp', __name__)

@grupo_bp.route('/api/grupos', methods=['GET'])
def obtener_grupos():
    return jsonify(GrupoService.obtener_todos()), 200

@grupo_bp.route('/api/grupos', methods=['POST'])
def crear_grupo():
    nuevo_id = GrupoService.crear(request.json)
    return jsonify({'mensaje': 'Grupo creado', 'id_grupo': nuevo_id}), 201