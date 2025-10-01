from flask import Blueprint, request, jsonify
from backend.db import db
from backend.models.move import Move

moves_bp = Blueprint('moves', __name__)

@moves_bp.route('/games/<int:game_id>/moves', methods=['POST'])
def add_move(game_id):
    data = request.get_json()
    move_number = data.get('move_number')
    from_square = data.get('from_square')
    to_square = data.get('to_square')
    piece = data.get('piece')

    new_move = Move(game_id=game_id, move_number=move_number, from_square=from_square, to_square=to_square, piece=piece)
    db.session.add(new_move)
    db.session.commit()

    return jsonify({'id': new_move.id}), 201
