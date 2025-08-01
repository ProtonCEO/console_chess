import chess
import chess.engine
import random

board = chess.Board()

def print_board():
    print(board)
    print()

print("♟️  Welcome to Console Chess!")
print("You are playing as White. Enter moves in UCI format (e.g., e2e4).")
print("Type 'q' to quit.\n")

while not board.is_game_over():
    print_board()

    # Player move
    move = input("Your move: ").lower()
    if move == 'q':
        print("👋 Goodbye!")
        break

    try:
        player_move = chess.Move.from_uci(move)
        if player_move in board.legal_moves:
            board.push(player_move)
        else:
            print("❌ Illegal move. Try again.")
            continue
    except:
        print("❌ Invalid input. Use UCI notation like 'e2e4'.")
        continue

    if board.is_game_over():
        break

    # Computer move
    computer_move = random.choice(list(board.legal_moves))
    print(f"\n🤖 Computer plays: {computer_move}")
    board.push(computer_move)

# Game over
print_board()
if board.is_checkmate():
    print("♔ Checkmate!")
elif board.is_stalemate():
    print("½ Stalemate!")
elif board.is_insufficient_material():
    print("½ Draw — insufficient material!")
else:
    print("Game over.")
