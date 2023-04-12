def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('-------------')

def check_win(board):
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    current_player = players[0]
    while True:
        print_board(board)
        print("It's", current_player, "'s turn")
        row = int(input('Enter row number (1-3): ')) - 1
        col = int(input('Enter column number (1-3): ')) - 1
        if board[row][col] != ' ':
            print('That spot is already taken!')
            continue
        board[row][col] = current_player
        if check_win(board):
            print_board(board)
            print(current_player, 'wins!')
            break
        if all([board[i][j] != ' ' for i in range(3) for j in range(3)]):
            print_board(board)
            print('It is a tie!')
            break
        current_player = players[1] if current_player == players[0] else players[0]

tic_tac_toe()