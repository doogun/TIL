

### 1. 이름 공간(Namespace)

**문제 1) **Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.

code

```python
LEGB
- Local scope : 함수
- Enclosed scope : 특정 함수의 상위 함수
- Global scope : 함수 밖의 변수, Import 모듈
- Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
    
 	-즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
```



---

### 2. 매개변수와 인자, 그리고 반환

**문제 2) **아래의 보기 (1) ~ (4) 중에서, 옳지 않은 것을 고르시오.

```
(1) 함수는 오직 하나의 객체만 반환할 수 있으므로 'return a, b'와
같이 쓸 수 없다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 매개변수(parameter)는 함수를 선언할 때 설정한 값이며,
전달 인자(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 함수 선언 시 매개변수 앞에 * 을 붙이고,
이 때는 함수내에서 tuple로 처리 된다.
```

code

```python
답은 1.

return a, b 는 튜플로 반환된다.
```



---

### 3. 재귀 함수

**문제 3) **재귀 함수를 사용했을 때 얻을 수 있는 장점과 단점을 반복문과 비교하여 작성하시오.

code

```python
- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
- 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생
```



---







