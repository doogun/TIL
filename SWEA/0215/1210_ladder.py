# 1210_ladder 풀이
# 2022-02-15


import sys
sys.stdin = open('input.txt', 'r')


# 문제에서 주어진 테이스트케이스가 10개
T = 10

for tc in range(1, T+1):

    # 따로 숫자를 받아준다.
    N = int(input())

    # 100 X 100 개 리스트를 만들어준다.
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 2에서부터 출발하기 위하여 행의 마지막 값인 99를 r에 넣어준다.(밑에서부터 탐색)
    r = 99

    # 마지막 행에서 하나씩 값을 전부 탐색
    for c in range(100):

        # 그러다 값이 2인 곳이 있다면 사다리 출발!
        if arr[r][c] == 2:

            # 우선 바로 왼, 오른쪽으로 가는 일은 없기 때문에 r에 빼기 1을 해준다.
            # 그리고 지나간 자리에는 숫자를 3으로 바꿔준다.(다시 지나가지 않게 하기 위해)
            while True:
                r -= 1
                arr[r][c] = 3

                # 이 후로 왼쪽반복문을 작동
                # c를 -1(왼쪽으로 한 칸 옮김)한 값이 0과 100(미만)사이에 들어가며 arr좌표의 값이 1이라면 왼쪽으로 계속 이동
                # 0이나 다른 수를 만나게 되면 더 이상 왼쪽을 가지 않고 왼쪽반복문을 나온다.
                while True:

                    if c-1 >= 0 and c-1 < 100 and arr[r][c-1] == 1:
                        c -= 1
                        arr[r][c] = 3
                    else:
                        break

                # 이 후로 오른쪽반복문을 작동
                # c를 -1(왼쪽으로 한 칸 옮김)한 값이 0과 100(미만)사이에 들어가며 arr좌표의 값이 1이라면 오른쪽으로 계속 이동
                # 0이나 다른 수를 만나게 되면 더 이상 왼쪽을 가지 않고 왼쪽반복문을 나온다.
                while True:

                    if c+1 >= 0 and c+1 < 100 and arr[r][c+1] == 1:
                        c += 1
                        arr[r][c] = 3
                    else:
                        break

                # r == 0(제일 꼭대기)에 도착했을 때 열의 위치를 출력한다.
                if r == 0:
                    print('#{} {}'.format(tc, c))
                    break
