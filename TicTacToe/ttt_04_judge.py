# ttt_04_judge.py
#
# 틱택토 판정


# 보드 출력함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("{}|{}|{}".format(tb[r][0], tb[r][1], tb[r][2]))
        print("-" * 5)


# 변수 초기화(board, turn)
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
turn = 'X'

# 게임 루프(9회 반복)
for cnt in range(9):
    while True:
        # 좌표 입력 받기
        y, x = map(int, input("y, x: ").split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")

    # 빈 칸이면 돌 놓은 후 보드 출력
    board[y][x] = turn
    prn_board(board)

    # 승리 판정 (행, 열, 대각선)
    if board[y][0] == turn and board[y][1] == turn and board[y][2] == turn:
        break
    if board[0][x] == turn and board[1][x] == turn and board[2][x] == turn:
        break

    # 턴(돌) 변경하기
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print("{} WIN!".format(turn))
