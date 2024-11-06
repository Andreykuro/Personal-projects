class Board:
    def __init__(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]

    def display(self):
        for row in self.board:
            print(" ".join(row))

    def check_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1
        piece = self.board[y1][x1]

        if piece == " ":
            return False

        if piece.isupper():
            direction = 1
        else:
            direction = -1

        if x1 + dx * direction < 0 or x1 + dx * direction > 7 or y1 + dy * direction < 0 or y1 + dy * direction > 7:
            return False

        return True

    def make_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = " "

def get_input():
    while True:
        move = input("Enter your move (e.g., a2a3): ")
        if len(move) == 4:
            start = (ord(move[0]) - ord("a"), int(move[1]) - 1)
            end = (ord(move[2]) - ord("a"), int(move[3]) - 1)
            if board.check_move(start, end):
                return start, end
        print("Invalid move. Please try again.")

def minimax(board, depth, maximizing_player):
    if depth == 0 or board.check_game_over():
        return board.evaluate()

    if maximizing_player:
        max_eval = float("-inf")
        for move in board.get_legal_moves():
            board.make_move(*move)
            eval = minimax(board, depth - 1, False)
            board.undo_move(*move)
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float("inf")
        for move in board.get_legal_moves():
            board.make_move(*move)
            eval = minimax(board, depth - 1, True)
            board.undo_move(*move)
            min_eval = min(min_eval, eval)
        return min_eval

def play_game():
    while not board.check_game_over():
        print("\n".join([""] * 100))
        print("White to move:")
        board.display()
        start, end = get_input()
        board.make_move(start, end)

        if not board.check_game_over():
            print("\n".join([""] * 100))
            print("Black to move:")
            board.display()
            start, end = get_best_move()
            board.make_move(start, end)

def get_best_move():
    best_move = None
    best_eval = float("inf")
    for move in board.get_legal_moves():
        board.make_move(*move)
        eval = minimax