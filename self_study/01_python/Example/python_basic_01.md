### 1. Python 예약어

**문제 1) **python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하시오.



code

```python
# 식별자(예약어) 조건
# 1.a~z, A-Z, 0~9, _ 를 사용할 수 있다.
# 2.숫자는 맨 처음에 사용할 수 없다. (0shape -> x, shape1 -> o)
# 3.키워드는 이미 정해졌기에 사용할 수 없다.
# 4. 특수문자(‘.’, ‘!’, ‘@’, ‘#’, ‘$’, ‘%’)는 사용할 수 없다.
# 5.파이썬 도큐먼트에서는 식별자 길이제한이 없다고 하지만 이 것은 반만 맞는 이야기다. 79글자 많이 쓰면 PEP-8 기준에 의해 설정된 규칙을 어기게 된다. 즉, 79자 보다 많이 쓰지 말자.

1total, len, cnt! 등등

```



---



### 2. 실수 비교

**문제 2) ** python은 부동소수점 방식을 이용하여 실수(float)를 표현하는 과정에서, 나타내고자 하는 값과의 오차가 발생하여 원하는 대로 연산 또는 비교가 되지 않을 때가 있다. 이를 참고하 여, 아래와 같은 두 실수 값을 올바르게 비교하기 위한 코드를 작성하시오.

```
num1 = 0.1 * 3
num2 = 0.3
```

code

```python
num1 = 0.1 * 3
num2 = 0.3 



print(num1 - num2) 		# 5.551115123125783e-17 출력
print(num1 == num2) 	# 따라서 False가 출력
print(abs(num1 - num2)<= (1e-10))	# 하지만 num1-num2의 절대값이 (1e-10)보다 작거나 같으면 a와 										b는 같다고 볼 수 있다.
```



---



### 3. 이스케이프 시퀀스

**문제 3) **(1) 줄 바꿈, (2) 탭, (3) 백슬래시를 의미하는 이스케이프 시퀀스를 작성하시오.

code

``` python
(1) \n 
(2) \t
(3) \\

# 이 밖에도 밑의 표를 참고하면 된다.
```

| 예약문자 | 내용(의미)        |
| -------- | ----------------- |
| \n       | 줄 바꿈           |
| \t       | 탭                |
| \r       | 캐리지리턴        |
| \0       | 널(Null)          |
| \\       | `\`               |
| \'       | 단일인용부호(`'`) |
| \"       | 이중인용부호(`"`) |



---



### 4. String Interpolation

**문제 4) **‘안녕, 철수야’를 string interpolation을 사용하여 출력하시오.

code

```python
name = input()

print('안녕, %d야', % name)	# %-formatting : (`%s`는 문자열, `$d`는 정수, `%f`는 실수)
print('안녕, {}야', .format(name))	# str.format
print(f'안녕, {name}야')	# f-strings : 파이썬 3.6 이후 버전에서 지원
```



---



### 5. 형 변환

**문제 5) **다음 중, 실행 시 오류가 발생하는 코드를 고르시오.

```
str(1)	# (1)
int('30')	# (2)
int(5)	# (3)
bool('50')	# (4)
int('3.5')	# (5)
```

code

```python
# 값을 다 출력해보았다.

print(str(1))	# (1)
print(int('30'))	# (2)
print(int(5))	# (3)
print(bool('50'))	# (4)
print(int('3.5'))	# (5)

1
30
5
True
# Traceback (most recent call last):
#   File "c:\Users\kjmk1\Desktop\python_code\python 보충학습 연습장\python_practice_01.py", # line 81, in <module>
#     print(int('3.5'))   # (5)
# ValueError: invalid literal for int() with base 10: '3.5'


# 잘 나오다가 5번에서 이런 오류가 났는데 그대로 해석해보면 '기본 10인 int()에 대한 잘못된 리터럴'이라고 한다. str을 int로 바꿨지만 소수이기 때문에 오류가 난 것 같다.
```



---



### 6. 네모 출력

**문제 6)** 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문은 사용할 수 없다.

```
n = 5
m = 9
```

code

```python
n = 5
m = 9

print(n*'*')
print((m*'*   *\n'))
print(n*'*')
```

```python
n = 5
m = 9

print(n*'*')  # `*`에 가로의 길이를 곱해준다.
print(m * ('*' + (n-2) * ' ' + '*\n'))  # 우선, 내가 만들고 싶은 한 줄을 먼저 코딩하고 거기에 맞는                                           세로줄의 값을 곱해준다.
print(n*'*')    # '*'에 가로의 길이를 곱해준다.
```



```python
# 정답
print((('*' * n) + '\\n') * m)	# '*'을 n번만큼 나타내고 그 뒤에 '\n'을 붙힌다. 그리고 m번만큼 출력한다.
```



---



### 7. 이스케이프 시퀀스 응용

**문제 7) **print() 함수를 한 번만 사용하여 다음 문장을 출력하시오.

```
"파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다."
나는 생각했다. 'cd를 써서 gir bash로 들어가 봐야지.'
```

code

```python
# 작은 따옴표는 큰 따옴표로 묶고 큰 따옴표는 작은 따옴표로 묶어서 출력시킨다.
# `\`(역슬래쉬)를 출력시키기 위해 앞에 `\`를 한 번더 입력해준다.

print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."''\n나는 생각했다.' " 'cd를 써서 gir bash로 들어가 봐야지.'")
```



---



### 8. 근의 공식

**문제 8)**다음은 이차 방정식의 근을 찾는 수식이다. 이를 파이썬 코드로 작성하시오.

code

```python
# +-를 어떻게 표현할 지 몰라서 이렇게 만들었는데 너무 이상했다.
# 그리고 곱하기와 괄호를 제대로 사용하지 못했다.

(-b +- (((b**2)-4ac)**1/2)) / 2a	# 처음 만든 답

(-b + (((b**2)-4*a*c)**(1/2))) / (2*a)	# 수정한 답이다.

# 답을 보니 두 개의 식으로 표현하였다.

(-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
(-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
```



---
