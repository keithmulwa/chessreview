import psycopg2
import os
from dotenv import load_dotenv

class Model:
    def __init__(self):
        load_dotenv()
        self.conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        self.game_id = None
    
    def start_game(self, player1, player2):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO game (status, player1, player2, winner)
                VALUES (%s, %s, %s, %s) RETURNING id
            ''', ('ongoing', player1, player2, ''))
            self.game_id = cursor.fetchone()[0]
            self.conn.commit()
            return self.game_id
        except Exception as e:
            print(f"Error starting game: {e}")
            self.conn.rollback()
            return None
    
    def log_user_input(self, input_type, data):
        print(f"Logged {input_type}: {data}")
    
    def log_move(self, move_data, player_color):
        if not self.game_id:
            print("No active game to log move")
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO moves (game_id, player_color, piece, from_x, from_y, to_x, to_y)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (self.game_id, player_color, move_data['piece'], 
                  move_data['from'][0], move_data['from'][1],
                  move_data['to'][0], move_data['to'][1]))
            self.conn.commit()
        except Exception as e:
            print(f"Error logging move: {e}")
            self.conn.rollback()
    
    def end_game(self, winner):
        if self.game_id:
            try:
                cursor = self.conn.cursor()
                cursor.execute('''
                    UPDATE game SET status = %s, winner = %s, ended_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                ''', ('completed', winner, self.game_id))
                self.conn.commit()
            except Exception as e:
                print(f"Error ending game: {e}")
                self.conn.rollback()
    
    def close(self):
        self.conn.close()