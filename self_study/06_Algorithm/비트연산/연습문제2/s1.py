'''
2
0F97A3
01D06079861D79F99F
'''

# T = int(input())
# for tc in range(1, T+1):
#     arr = input()
#     bit = ''
#     for i in range(len(arr)):


T = int(input())
for tc in range(1, T+1):
    arr = input()
    # print(arr)

    # 전체를 4bit 2진수로 바꾼 값들을 모아둘 문자열
    bit = ''
    # 입력 받은 16진수 하나하나 순회해서 변경해 나갈 것이다.
    for i in range(len(arr)):
        # 각 값을 10진수로 먼저 바꾸자
        tmp = int(arr[i], 16)
        print(tmp, end=' ')
        print('###')
        # 10진수를 다시 2진수로 바꾸자
        # 바뀐 tmp에 들어 있는 값 = 0
        # 내가 바꿔야 하는 2진수 0 = 0000
        tmp = bin(tmp).replace('0b', '')
        # print(f'{tmp:04b}')
        print(tmp)

        # 길이가 4인 2진수가 필요하다.
        while len(tmp) != 4:
            tmp = '0' + tmp
        # print(tmp)

        bit += tmp
    # print(bit)

    # 0부터 끝까지 7단계씩 떼오기
    for i in range(0, len(bit), 7):
        # [S:E:step] E에 들어가는 값이
        # 전체 길이를 벗어나더라도 IndexError 발생안함
        print(int(bit[i:i+7], base=2), end=' ')
    print()