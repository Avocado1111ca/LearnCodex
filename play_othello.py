from othello import Othello


def print_board(game: Othello) -> None:
    """Display the current board and the active player."""
    print(game)
    print(f"Current player: {game.current}\n")


def main() -> None:
    game = Othello()
    while not game.is_game_over():
        moves = game.valid_moves(game.current)
        if not moves:
            print(f"{game.current} has no valid moves and must pass.\n")
            game.current = game.opponent(game.current)
            continue

        print_board(game)
        move_input = input("Enter move as 'row col': ")
        try:
            r, c = map(int, move_input.split())
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by a space.\n")
            continue

        if not game.make_move(r, c):
            print("Illegal move, try again.\n")

    print_board(game)
    scores = game.score()
    print(
        f"Game over. Black: {scores[Othello.BLACK]}, "
        f"White: {scores[Othello.WHITE]}"
    )
    if scores[Othello.BLACK] > scores[Othello.WHITE]:
        print("Black wins!")
    elif scores[Othello.BLACK] < scores[Othello.WHITE]:
        print("White wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
