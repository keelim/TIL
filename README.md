# Kotlin
 
## start date: 2019 06 23
## name: StartKotlin
- - - 
### daily 1 lecture 

- - - 
## 2019 06 23

1. 함수 정의
- fun 으로 함수 정의
- return 생략 가능 기능이 있다.
- package 는 자바와 유사하다.
- 코틀린은 리턴 할 값이 없는 경우  Unit 으로 리턴

2. 변수 정의
- val --> 일기 전용 변수
- var --> mutable 변수
- 컴파일러 타입 추론
- val 은 값을 할당을 할 수 가 없다.

3. comment 거의 유사
- 중첩 허용

4. 문자열 보간법
- String 안에서 다 할 수 있다.

5. nullable
- null 인 경우를 명시를 해야 한다.
- null check 를 할 수 가 있게 된다.
- nullable 를 지원을 하는 것이 안정적으로 코딩할 수 있다.

6. 자동 타입 변환
7. while loop 는 같다.
8. when expression 
    - switch 보다 더 강력하게 사용 가능
9. range
10. Collections 

## 2019 06 24
1. 모든 것은  객체
    - Number Class 로 접근
2. 리터럴
    - 10, long, double, float, 2진수 16진수 8진수 x
3. Underscore 수치를 표현 가능
4. Representation 
    - Nullable, Generic
5. 문자 char 는 숫자로 취급되지 않음
    - java 에서는 가능하지만 직접적인 비교는 되지 않는다.
6.  배열또한 클래스로 표현 된다.
7. get, set, size
8. 배열 생성 
    - arrayOf --> 라이브러리 생성 

## 2019 06 27
### Control flow
1. if else
    - java 유사
    -<code> val max = if(a>b) a else b </code> 식으로 작용할 수 있다.
    - 

## 2019 06 29
1. 코트린에는 삼항 연산자가 없다. 
    - 대신 if를 사용을 한다.
    
2. when --> switch 와 유사하다고 생각
    - 순차적으로 인자를 비교
    - branch 가 실행
    - 식으로의 사용이 가능 (else가 필수이다.)
    - boolean 은 else 는 없어도 가능
    - , 로 표현이 가능
    - 조건문 함수나 식이 가능
    - in을 통하여 범위안에 있는지를 확인이 가능
    - range
    - type 검사 가능 --> 스마트 캐스트 또한 적용 가능
    - when 으로 인자 입력 없을 시 사용 가능
    
3. for loop
    <code> for(item in collection)
        print(item)</code>
    - body block 가능
    - iterator 를 반환이 가능 경우 for loop 작동 가능
    - 상속의 구현을 받지 않음
    - indicies 통하여 index 접근 가능
    - withindex()
    - while java 와 유사

## 2019 07 03
> package 

    - 패키지를 명세하지 않으면 default package 포함
    - 이름이 없는 패키지는 그냥 호출을 하면 된다.
    - 기본적으로 import가 되는 패키지가 있다. 
    - jvm --> java.lang, kotlin.jvm
    - js --> kotlin.js
    - import bar.Bar as bBar --> 로컬 리네임 가능
        - 파이썬관 유사

> Return and Jumps

    - return, break, continue 자바와 똑같다.
    - Label로 break and Continue
    - <code>
        loop@ for(i in 10){
            println("--i: $i ---")
            for(j in 1..10){
                println("j: $j")
                if( j+1>12)
                    break @loop
            }
        }
    </code>
    - 함수를 입력으로 가능 --> 입력 함수
    - 함수 중첩에서 return --> 한개의 함수가 return 
    - lambda는 함수가 아니기 떄문에 return을 하면 포함 함수가 종료
    - label를 사용을 하면 lambda 적용이 가능
    - 
    <code>
        fun foo3(){
            var ints = listOf(0, 1, 2, 3)
            ints.forEach label@ ({
                if(it == 1) return @label
                print(it)
            })
            print("End")
        }
    </code>
    - 암시적 레이블을 사용을 할 수 있다. 
        - 람다에서만 레이블을 사용하기 어렵다.
        - 
        <code>
        fun foo3(){
            var ints = listOf(0, 1, 2, 3)
            ints.forEach ({
                if(it == 1) return @forEach
                print(it)
            })
            print("End")
        }
    </code>
     