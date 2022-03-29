player = True
taken_input = list()

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]


def print_board():
    print(f'\n{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}\n')


# -------------------- Input --------------------

def isnum(inp):
    if not inp.isnumeric():
        print(f'{inp} is not a valid number')
        return True
    else:
        return False


def num_check(inp):
    inp = int(inp)
    if inp < 1 or inp > 9:
        print('Number should be between 1 and 9')
        return False
    else:
        return True


def istaken(inp):
    if inp in taken_input:
        print('This position is taken, please try again')
        return True
    else:
        return False


def correct_inp(inp):
    if isnum(inp):
        return True
    if num_check(inp):
        return True
    else:
        return False


def current_user(player):
    if player:
        return 'X'
    else:
        return 'O'
    




# -------------------- Checking Win --------------------

def won_game(user, board):
    if check_row(user, board) or check_column(user, board) or check_diag(user, board):
        return True


def check_row(user, board):
    complete_row = True
    if (board[0] == user and board[1] == user and board[2] == user) or (board[3] == user and board[4] == user and board[5] == user) or (board[6] == user and board[7] == user and board[8] == user):
        complete_row = True
    else:
        complete_row = False

    if complete_row:
        return True
    return False


def check_column(user, board):
    complete_col = True
    if (board[0] == user and board[3] == user and board[6] == user) or (board[1] == user and board[4] == user and board[7] == user) or (board[2] == user and board[5] == user and board[8] == user):
        complete_col = True
    else:
        complete_col = False

    if complete_col:
        return True
    return False

def check_diag(user, board):
    complete_diag = True
    if (board[0] == user and board[4] == user and board[8] == user) or (board[2] == user and board[4] == user and board[6] == user) :
        complete_diag = True
    else:
        complete_diag = False

    if complete_diag:
        return True
    return False



# -------------------- Main Loop -------------------- #
while True:
    active_user = current_user(player)
    print_board()
    first = input('Enter a position from 1 - 9: ')

    if not correct_inp(first):
        print('Please try again')
        continue
    try:
        first = int(first) - 1
    except ValueError:
        continue

    if istaken(first):
        continue
    taken_input.append(first)

    board[first] = active_user
    player = not player
    if won_game(active_user, board):
        print(f'{active_user} won!')
        print_board()
        quit()
