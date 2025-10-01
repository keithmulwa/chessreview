from flask import Flask
from flask_migrate import Migrate
from backend.db import db
from backend.routes.games import games_bp
from backend.routes.moves import moves_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/chess.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(games_bp)
    app.register_blueprint(moves_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
