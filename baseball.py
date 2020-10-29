# baseball.py

import random

# 문제 생성
num_source = list(range(1, 10))
quiz = []
for _ in range(4):
    # list index는 0부터 n-1까지
    one = num_source.pop(random.randint(0, len(num_source)-1))
    quiz.append(str(one))

print(quiz, "".join(quiz)) # ''.join(quiz): 문자 원소 리스트를 ''로 연결하여 반환

running = True
while running:
    strike = 0
    ball = 0
    num = input('수? ')
    if (num == ''.join(quiz)):
        print("HOME RUN!")
        running = False
    for idx in range(3):
        if quiz[idx] == num[idx]:
            strike += 1
        elif quiz[idx] in num:
            ball += 1

