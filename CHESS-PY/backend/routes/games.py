from flask import Blueprint, request, jsonify
from backend.db import db
from backend.models.game import Game

games_bp = Blueprint('games', __name__)

@games_bp.route('/games', methods=['POST'])
def create_game():
    data = request.get_json()
    player1 = data.get('player1', 'Player 1')
    player2 = data.get('player2', 'Player 2')

    new_game = Game(status='ongoing', player1=player1, player2=player2, winner=None)
    db.session.add(new_game)
    db.session.commit()

    return jsonify({'id': new_game.id, 'status': new_game.status, 'player1': new_game.player1, 'player2': new_game.player2}), 201
