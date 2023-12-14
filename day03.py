"""
name = input('이름을 입력하세요')
age =input('나이를 입력하세요>>')
print("입력된 이름은{0} 나이는 {1}".format(name,age))
문제 1
5만원짜리 물건을 할부로 구입한 뒤 매달 내는 돈을 계산해서 보여주는 프로그램을 만들어보자
price = 50000
print("물건의 가격은{0}".format(price))
n = int(input('할부개월 입력'))
print("매달 내는 돈은{}원입니다.".format(price/n))
문제 2: 사용자로부터 1에서 12사이에 월을 입력받아 해달월이 며칠까지 있는지 있는지 출력하는 프로그램을 만들자
(리스트 : 배열을 활용한 문제)

days=[31,28,31,30,31,30,31,31,30,31,30,31]
month= int(input("1~12사이의 월을 입력하세요>>"))
day = days[month-1]
print("{0}월은 {1}일 까지 있습니다.".format(month,day))



문제 3: 영어사전을 구현하고자 한다. 딕셔너리를 하나 생성하고 예시와 같이 동작하자
(딕셔너리: {'name':'sbs':age':'20}


english_dict = {'flower':'꽃','fly':'날다','floor':'바닥'}
word = input("영어단어를 입력하세요>>")
print("{0}: {1}".format(word,english_dict[word]))

a = 7
b = 2
print("{0} + {1} ={2}".format(a,b,a+b))
print("{0} - {1} ={2}".format(a,b,a-b))
print("{0} * {1} ={2}".format(a,b,a*b))
print("{0} ** {1} ={2}".format(a,b,a**b))
print("{0} / {1} ={2}".format(a,b,a/b))
print("{0} %  {1} ={2}".format(a,b,a%b))
print("{0} //  {1} ={2}".format(a,b,a//b))
@ 복합 대입 연산자

piggy_bank = 0
money = 10000
piggy_bank += money
print("저금통에 용돈{}을 넣었습니다.".fortmat(money))
print("지금 저금통에는 {}원이 있습니다.".format(piggy_bank))

a=10
b= 0

print("{0}>0 and {1}>0 :{2}".format(a,b,a>0 and b>0))
print("{0}>0 or {1}>0 :{2}".format(a,b,a>0 or b>0))

@비트연산자
a=00001010
b = 01000110

a= 10

b =70


piggy_bank = 0
money = 10000
piggy_bank =+ money
print("저금통에 용돈{}을 넣었습니다.".format(money))
print("지금 저금통에는 {}원이 있습니다.".format(piggy_bank))

@조건연산자(삼항)
(a==b)?true:false >> 파이썬은 ?물음표가  if로 사용 : 는 else 로 사용

a = 10
b = 20
result = (a-b)if(a>=b)else(b-a)
print("{0}과 {1}의 차이는 {2}입니다.".format(a,b,result))

85p 3번문제
emp_no = int(input("4자리 사원번호를 입력하세요:"))
emp_last_no = emp_no % 10
print(emp_last_no)
is_am = emp_last_no>=5
print("근무시간은{}입니다.".format('오전'if is_am else'오후'))
86p 5번 문제

kor = int(input("국어점수를 입력하세요 :"))
eng = int(input("영어점수를 입력하세요 :"))
mat = int(input("수학점수를 입력하세요 :"))
avg= int((kor+eng+mat) / 3)
result = '합격'if avg >=80 else '불합격'
print(" 평균은{0}점이고, 결과는 {1}입니다.".format(avg,result))
@ if 문 심화 : input을 이용한 if 문을 만들자
몇살입니까? >>20
성인
몇살입니까?>>10
미성년
1. 현재 나이를 물어보는 입력값을 만든다.
2. 입력값에 따라서 조건을 만든다 (성인(age >=20) : 미성년자)


age = int(input("몇살입니까?"))
if age>=20:
    print("성인")
else:
    print("미성년자")
@if elif else 문 :input을 이용한   if-elif 문을 만들다
몇살입니까 >>5
미취학
몇살입니까 >>10
초등학생
몇살입니까 >>15
중학생
몇살입니까 >>18
고등학생

age = int(input("몇살입니까?"))
if age<=7:
    print("미취학")
elif  age<=13 :
    print("초등학생")
elif age <=16 :
    print("중학생")
elif age <= 19:
    print("고등학생")

else:
    print("성인")
@if문을 논리연산자( and / or)
조건문으로 관리자를 구별하는 프로그램만들자
사이트의 관리자 id는 = admin이고 레벨이 1이다.

 아이디를 입력하세요 >>  admin
 회원의 레벨을 입력하세요  : >>1
 일반회원입니다.
 아이디를 입력하세요 >>  jiwon
 회원의 레벨을 입력하세요  : >>1
 관리자입니다.

1. 비밀번호를 만든다.
2. 비밀번호를 입력한다.
3. 조건문에 비밀번호를 추가해서 비밀번호가 맞다면 관리자이다.


password = '1234'

id = input("아이디를 입력하세요")
level = int(input("회원의 레벨을 입력하세요"))
pwd = int(input("비밀번호를 입력하세요"))

if id == 'admin' and level == 1 and pwd == password:

    print("관리자입니다.")

else:
    print("일반회원입니다.")


문제 : 조건문으로 계절을 판단하는 프로그램을 만들어보자
월을 입력하세요 >>

1. 입력하는 월이 3과 같거나 크면서 5보다 같거나 작으면 봄이다.
2. 입력하는 월이 6과 같거나 크면서 8보다 같거나 작으면 여름이다.
3. 입력하는 월이 9와 같거나 크면서 11보다 같거나 작으면 가을이다.
4. 입력하는 월이 12와 같거나 크면서 2보다 같거나 작으면 겨울이다.

월을 입력하세요 >>7
7월은 여름입니다.
월을 입력하세요 >>12
12월은 겨울입니다.


month = int(input("월을 입력하세요"))

if month >=3 and month<=5 :
    print("{0}월은 봄이다.".format(month))
elif month >= 6 and month <= 8:
     print("{0}월은 여름이다.".format(month))
elif month >=9 and month<=11 :
    print("{0}월은 가을이다.".format(month))
elif month >=12 and month<=2 :
    print("{0}월은 겨울이다.".format(month))


@조건문으로 좌석의 종류를 구별하기
좌석의 종류를 입력하세요 1. 일반실 2. 특실
일반실입니다.
좌석의 종류를 입력하세요 1. 일반실 2. 특실
특실입니다.
sit = int(input("좌석의 종류를 입력하세요(1:일반실 2:특실)"))

if sit==1 :
     print("일반실입니다.")
else :
    print("특실입니다.")


num1 = int(input("정수1 입력 :"))
num2 = int(input("정수2 입력 :"))
num3 = int(input("정수3 입력 :"))

if num1 >=num2 and num1 >=num3 :
    print("가장큰수는 {}입니다.".format(num1))
elif num2 >= num1 and num2 >= num3 :
    print("가장큰수는 {}입니다.".format(num2))
else :
    print("가장큰수는 {}입니다.".format(num3))
    """
