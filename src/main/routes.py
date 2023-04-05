from flask import Blueprint, request, jsonify

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.pokemon_create_composer import pokemon_create_composer
from src.errors.error_handler import ErrorHandler
routes_bp = Blueprint("api_routes", __name__)


@routes_bp.route("/", methods=["POST"])
def pokemon_create():
    try:
        http_response = request_adapter(request, pokemon_create_composer())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        response = ErrorHandler(exception).response
        return jsonify(response.body), response.status_code

# @routes_bp.route("/", methods=["GET"])
# def person_list():
#     http_response = request_adapter(request, person_list_composer())
#     return jsonify(http_response.body), http_response.status_code

# @routes_bp.route("/", methods=["DELETE"])
# def person_delete():
#     http_response = request_adapter(request, person_delete_composer())
#     return jsonify(http_response.body), http_response.status_code
