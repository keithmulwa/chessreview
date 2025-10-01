from backend.db import db

class Game(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(150), nullable=False)
    player1 = db.Column(db.String(150), nullable=True)
    player2 = db.Column(db.String(150), nullable=True)
    winner = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    ended_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    moves = db.relationship('Move', backref='game', lazy=True)

    def __repr__(self):
        return f'<Game {self.id} - Status: {self.status}>'
