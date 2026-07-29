from flask import Blueprint, jsonify, request
from services.categoria_service import CategoriaService

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/api/categorias', methods=['GET'])
def obtener_categorias():
    return jsonify(CategoriaService.obtener_todas()), 200

@categoria_bp.route('/api/categorias', methods=['POST'])
def crear_categoria():
    nuevo_id = CategoriaService.crear(request.json)
    return jsonify({'mensaje': 'Categoría creada', 'id_categoria': nuevo_id}), 201