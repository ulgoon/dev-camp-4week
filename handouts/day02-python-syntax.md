---
marp: true
---

# Fastcampus Sprint - Programming

## Day 2. 파이썬 핵심문법 이해하기

---
<!--
paginate: true
theme: default
class: invert
size: 16:9
footer : fastcampus 4주만에 프로그래머되기, Wooyoung Choi, 2019
-->

## Index

- 정리한 요소 저장하기(xlsx, json)
- Python 핵심문법
	- 연산과 연산자
	- 변수
	- 자료형
	- 문자열
	- 리스트
	- 조건문
	- 반복문

---

## Python

---

### 특징

- 인터프리터
- 객체지향
- 동적타이핑
- 엄격한 문법

---

### C vs Python

```c
int main(){
int num;
for(i=0;i<=10;i++){
if (i % 2 == 0){
printf(i);
}
}
}
```

```python
for i in range(1,10+1):
    if i % 2 == 0:
        print(i)
```

---

## Numbers & Math

`<object> <operator> <object>`

```python
print(3 + 7)
print(10 - 3)
print(15 / 7)
print(34 * 100)
```

---

## Numbers & Math

```python
print(15 / 7)
print(15 / 5)
type(15 / 5)

print(15 // 5)
type(15 // 5)

print(7 % 3)

print(15 ** 3)

print(34 * 100)
print(3 * 2.5)
type(3 * 2.5)
```

---

## Boolean

```python
print(3 < 7)
print(10 < 3)
print(15 > 7)
print(3 >= 3)
print(3 <= 10)
print(34 == 100)
print(34 != 100)

```

---

## Variable

```python
print("hello python!")
hello = "hello"
python = "python!"
print(hello, python)
```

```python
num1 = 14
num2 = 5

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
```

---

## Let's Code PYTHONIC

### Variables

- `_variable`: 내부적으로 사용되는 변수
- `print_` : 파이썬 키워드와 충돌 방지
- 클래스 이름은 `CamelCase`
- 함수, 변수, 메소드 이름은 `snake_case`

---

### Data type

- int
- float
- long(0b, 0o, 0x)
- string
- boolean
- list, tuple, range
- set
- dictionary

---

### type casting

float(3) --> int to float
int(3.6) --> float to int
str(1) --> int to string
int("12") --> string to int

---

## input

```python
name = input("What is your name? ")
print("Hi, ", name)
```

## input with evaluation

```python
input("How old are you? ")
eval(input("How old are you? "))
```

---

## Small Project Again!

`사용자의 입력을 받아` 반지름(`r`)을 선언한 뒤, 이를 이용하여 원의 지름, 둘레, 넓이, 구의 겉넓이, 부피를 각각 출력하는 파이썬 파일을 만들어보세요.(`pi=3.1415`)

---

## type casting with input

```python
int(input("How old are you? "))
```

---

## String Functions

```python
func = "python is easy programming language"
func.count('p')

func.find('p')

comma = ","
func = comma.join('python')

func.split(',')

python_is_easy = "python is easy"
python_is_easy.split()

python_is_easy.replace("python", "golang")
```

---

## String Functions

```python
some_string = "   computer     "
some_string.strip()
```

```python
some_string = ",,,Fastcampus..."
some_string.strip(",")
some_string.strip(".")
```

---

## String Formatting

```python
print("I have a {}, I have an {}.".format("pen", "apple"))
```

```python
print("I have a {0}, I have an {1}.".format("pen", "apple"))
```

```python
print("I have a {0}, I have an {0}.".format("pen", "apple"))
```

---

## padding and align

- `{:10}`
- `{:>10}`
- `{:^10}`
- `{:_^10}`

---

## List

List

```
animals = ['','','']
```

---

### List

### 빈 list를 선언합니다. 선언과 동시에 값을 채워넣을 수 있습니다.

`lang = ["python", "c", "java", "golang"]`
lang = []

### list에 요소를 추가합니다.

lang.append("python")
lang.append("java")
lang.append("golang")
print(lang)

---

### 혹은 특정한 위치에 원하는 값을 추가할 수 있습니다.

lang.insert(1, "c")
print(lang)

### 특정 요소를 삭제할 수도 있습니다.

lang.remove("golang")
print(lang)

### 혹은 리스트에 있던 값을 빼낼 수도 있습니다.

java = lang.pop(2)
print(lang)
print(java)

---

### 리스트를 정렬하는 법을 알아봅니다.

numbers = [2, 1, 4, 3]
print(numbers)

numbers.sort()
print(numbers)

### 리스트를 역순으로 출력하고 싶을땐 이렇게 한답니다.

numbers = [2, 1, 4, 3]
numbers.reverse()
print(numbers)

---

### 리스트를 내림차순으로 정렬하려면??

---

#### 1. sort -> reverse

```python
numbers.sort()
numbers.reverse()
```

#### [2. sort(reverse=True)](https://docs.python.org/3/library/stdtypes.html?highlight=sort#list.sort)

```python
numbers.sort(reverse=True)
```

---

### 특정 값의 위치를 출력할땐 이렇게 합니다.

index_of_two = numbers.index(2)
print(index_of_two)

### 리스트끼리 더할 땐 extend를 활용합니다.

numbers += [5, 6]
print(numbers)
numbers.extend([7, 8])
print(numbers)

---

## 조건문

### Conditional Statements

---

`배가 고프다!!!`

- case 1: 집이라면
	- 밥이 있다면
	- 밥이 없다면

- case 2: 밖이라면
	- 현금이 10만원 초과라면
	- 현금이 5만원 초과라면
	- 현금이 없다면

---

## If

```python
if 조건:
	실행문

if 조건1 and 조건2:
	실행문

if 조건1 or 조건2:
	실행문
if not 조건:
	실행문
```

### Comparison Operators

```
x == n
x != n

x < n
x > n
x <= n
x >= n
```

---

## if

```python
if 현금 > 100000:
	레스토랑으로 간다
```

```python
cash = 120000
if cash > 100000:
	print("go to restaurant")
```

---

## else

```python
if 조건:
	실행문1
else:
	실행문2
```

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
else:
    print("go to cvs")
```

---

## else if

```python
if 조건1:
	실행문1
else:
	if 조건2:
		실행문2
	else:
		실행문3
```

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
else:
        if cash > 50000:
            print("go to bobjib")
        else:
            print("go to cvs")
```

---

## if in else in if in else in ..

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
else:
    if cash > 50000:
        print("go to bobjib")
    else:
        if cash > 30000:
            print("go to buffet")
        else:
            if cash > 20000:
                print("go to ramen store")
            else:
                if cash > 10000:
                    print("go to chinese restaurant")
                else:
                    print("go to cvs")
```

---

## elif

```python
if 조건1:
	실행문1
elif 조건2:
	실행문2
elif 조건3:
	실행문3
...
else:
	실행문n
```

---

### elif

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
elif cash > 50000:
    print("go to bobjib")
elif cash > 30000:
    print("go to buffet")
elif cash > 20000:
    print("go to ramen store")
elif cash > 10000:
    print("go to chinese restaurant")
else:
    print("go to cvs")
```

---

### If with Web scraper

---

```python
box_office_list = []
for tr in tr_list:
    a_list = tr.find_all("a")
    score = int(a_list[0].find("span", attrs={"class":"tMeterScore"}).text[:-1])
    url = base_uri + a_list[0]["href"]
    movie_name = a_list[1].text
    revenue = a_list[2].text[1:]

    # convert scale to zeros
    if revenue[-1] == 'M':
        digits = 6
    elif revenue[-1] == 'B':
        digits = 9
    elif revenue[-1] == 'K':
        digits = 3

    if revenue.find('.') == -1:
        revenue = int(revenue[:-1] + '0'*digits)
    elif revenue[0] == '0':
        revenue = int(revenue[1:-1].replace(".","") + '0'*(digits-1))
    else:
        revenue = int(revenue[:-1].replace(".","") + '0'*(digits-1))

    box_office_list.append((executed_time, url, score, movie_name, revenue))
box_office_list
```

---

## Do it your self!

### Numguess

- 1부터 100까지 정수 중 하나를 `answer`라는 변수에 할당
- 사용자로 부터 임의의 값 하나를 받아 `guess`라는 변수에 할당
- `answer`와 `guess`를 비교하여 정답여부를 출력

---

## numguess

```python
import random


answer = random.randint(1,100)
print(answer)
```

---

## numguess

```python
username = input("Hi there, What's your name?? ")
guess = eval(input("Hi, "+ username + "guess the number: "))

if guess == answer:
	print("Correct! The answer was ", str(answer))
else:
	print("That's not what I wanted!! The answer was ", str(answer))
```

---

## Iteration

---

## For, while

```python
for 변수 in (리스트 or 문자열):
	실행문1
    ...
```

```python
for i in ["python", "java", "golang"]:
	print(i)
```

---

## For, while

```python
sum = 0
for i in range(1,11):
	sum += i
    sum = sum + i
	print(sum)
```

---

## For, while

```python
while 조건:
	실행문1
	...
```

```python
while name != "foo bar":
	name = input("What's your name? ")
	print("Hi, " + name + "So, where is foo bar?")
```

```python
while 1:
	print("Hello world!")
```

---

## Iterations with Conditional Statements

---

## Fizzbuzz

1부터 100까지 **반복하면서,**

3의 배수 = "Fizz"
5의 배수 = "Buzz"
15의 배수 = "FizzBuzz"
나머지 = 그 숫자

---

## Fizzbuzz

```python
num = eval(input("type the number: "))

for i in range(1, num + 1):
	if i % 15 == 0:
		print("fizzbuzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
		print(i)
```

---

## Refactoring numguess

```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")

while True:
	guess = eval(input("Hi "+ username + ", guess the number: "))

	if guess == answer:
		print("Correct! The answer was ", str(answer))
		break
	else:
		print("That's not what I wanted!! Try again!!")
```

---

## give a hint!!

```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")

while True:
    guess = eval(input("Hi, "+ username + "guess the number: "))

    if guess == answer:
        print("Correct! The answer was ", str(answer))
        break
    elif guess > answer:
        print("Too high!! Try again!!")
    elif guess < answer:
        print("Too Low!! Try again!!")
```

---

## limit trial

```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")
trial = 5
while trial:
    guess = eval(input("Hi, "+ username + ". guess the number: "))

    if guess == answer:
        print("Correct! The answer was ", str(answer))
        break
    elif guess > answer:
        trial -= 1
        print("Too high!! Try again!!(%d times left)" % (trial))
    elif guess < answer:
        trial -= 1
        print("Too Low!! Try again!!(%d times left)" % (trial))
    if trial == 0:
        print("You are Wrong! The answer was ", str(answer))
```

<link href="https://fonts.googleapis.com/css?family=Nanum+Gothic:400,800" rel="stylesheet">
<link rel='stylesheet' href='//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css'>

<style>
h1,h2,h3,h4,h5,h6,
p,li, dd, table > * > * {
font-family: 'Nanum Gothic', Gothic;
}
span, pre {
font-family: Hack, monospace;
}
</style>