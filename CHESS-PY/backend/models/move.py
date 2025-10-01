from backend.db import db

class Move(db.Model):
    __tablename__ = 'moves'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    move_number = db.Column(db.Integer, nullable=True)
    from_square = db.Column(db.String(10), nullable=False)
    to_square = db.Column(db.String(10), nullable=False)
    piece = db.Column(db.String(10), nullable=False)
    move_timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Move {self.id} - Game {self.game_id} - {self.piece} from {self.from_square} to {self.to_square}>'
