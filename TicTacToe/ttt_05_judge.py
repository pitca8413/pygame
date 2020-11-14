# ttt_05_judge.py
#
# 틱택토 대각선 판정


# 보드 출력 함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("{}|{}|{}".format(tb[r][0], tb[r][1], tb[r][2]))
        print("-" * 5)


# 판정 함수 judge(y, x)
def judge(ty, tx):
    win = False
    if board[ty][0] == turn and board[ty][1] == turn and board[ty][2] == turn:
        win = True
    if board[0][tx] == turn and board[1][tx] == turn and board[2][tx] == turn:
        win = True
    if ty - tx == 0:
        if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
            win = True
    if ty - tx == 0 or abs(ty - tx) == 2:
        if board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:
            win = True
    return win


# 돌 변경
def change_stone(tt):
    if tt == 'X':
        return 'O'
    return 'X'


# 변수 초기화(board, turn)
turn = 'X'
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
msg = 'DRAW'

# 게임 루프
for cnt in range(9):
    # 좌표 입력 받기
    while True:
        y, x = map(int, input("y, x: ").split(","))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")

    # 돌 놓기
    board[y][x] = turn
    prn_board(board)

    # 판정 (행, 열, 대각선)
    if judge(y, x):
        msg = turn + "의 승리!!!"
        break

    # 돌 모양 변경
    turn = change_stone(turn)

# 결과 출력
print(msg)
