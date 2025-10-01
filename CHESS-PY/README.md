# Chess Python Project

A chess game with a Flask backend and separate chess engine.

## Structure

- `chess/`: Chess engine logic
- `backend/`: Flask backend with models, routes, and database
- `migrations/`: Database migrations
- `app.py`: Backend entrypoint

## Setup

1. Install dependencies: `pipenv install`
2. Activate virtualenv: `pipenv shell`
3. Initialize migrations: `flask db init`
4. Create migration: `flask db migrate -m "create games and moves tables"`
5. Apply migration: `flask db upgrade`
6. Run the app: `flask run`

## API

- `POST /games`: Create a new game
- `POST /games/<id>/moves`: Add a move to a game
