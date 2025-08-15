from typing import List, Tuple


class Othello:
    SIZE = 8
    EMPTY = '.'
    BLACK = 'B'
    WHITE = 'W'

    DIRECTIONS = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    def __init__(self) -> None:
        self.board = [[self.EMPTY for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        mid = self.SIZE // 2
        self.board[mid - 1][mid - 1] = self.WHITE
        self.board[mid][mid] = self.WHITE
        self.board[mid - 1][mid] = self.BLACK
        self.board[mid][mid - 1] = self.BLACK
        self.current = self.BLACK

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.SIZE and 0 <= c < self.SIZE

    def opponent(self, player: str) -> str:
        return self.BLACK if player == self.WHITE else self.WHITE

    def _captures_in_direction(self, r: int, c: int, dr: int, dc: int, player: str):
        r += dr
        c += dc
        pieces = []
        while self.in_bounds(r, c) and self.board[r][c] == self.opponent(player):
            pieces.append((r, c))
            r += dr
            c += dc
        if self.in_bounds(r, c) and self.board[r][c] == player and pieces:
            return pieces
        return []

    def valid_moves(self, player: str):
        moves = []
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.board[r][c] != self.EMPTY:
                    continue
                for dr, dc in self.DIRECTIONS:
                    if self._captures_in_direction(r, c, dr, dc, player):
                        moves.append((r, c))
                        break
        return moves

    def make_move(self, r: int, c: int) -> bool:
        player = self.current
        if (r, c) not in self.valid_moves(player):
            return False
        to_flip = []
        for dr, dc in self.DIRECTIONS:
            to_flip.extend(self._captures_in_direction(r, c, dr, dc, player))
        self.board[r][c] = player
        for fr, fc in to_flip:
            self.board[fr][fc] = player
        self.current = self.opponent(player)
        return True

    def is_game_over(self) -> bool:
        return not self.valid_moves(self.current) and not self.valid_moves(self.opponent(self.current))

    def score(self):
        black = sum(row.count(self.BLACK) for row in self.board)
        white = sum(row.count(self.WHITE) for row in self.board)
        return {self.BLACK: black, self.WHITE: white}

    def board_str(self) -> str:
        header = "  " + " ".join(str(i) for i in range(self.SIZE))
        rows = [header]
        for idx, row in enumerate(self.board):
            rows.append(f"{idx} " + " ".join(row))
        return "\n".join(rows)

    def __str__(self) -> str:
        return self.board_str()
