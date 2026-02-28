from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
game_over = False
winner = None

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    return all(cell != '' for row in board for cell in row)

@app.route('/api/move', methods=['POST'])
def move():
    global current_player, game_over, winner
    if game_over:
        return jsonify({"message": "Game over! Please reset."}), 400

    data = request.get_json()
    row = data['row']
    col = data['col']

    if board[row][col] == '':
        board[row][col] = current_player
        if check_win(board, current_player):
            winner = current_player
            game_over = True
        elif check_tie(board):
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
        return jsonify({"board": board, "current_player": current_player, "game_over": game_over, "winner": winner})
    else:
        return jsonify({"message": "Invalid move"}), 400

@app.route('/api/reset', methods=['POST'])
def reset():
    global board, current_player, game_over, winner
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    game_over = False
    winner = None
    return jsonify({"board": board, "current_player": current_player, "game_over": game_over, "winner": winner})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"board": board, "current_player": current_player, "game_over": game_over, "winner": winner})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
