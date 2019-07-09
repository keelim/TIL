# Kotlin
 
## start date: 2019 06 23
## name: StartKotlin
- - - 
### daily 1 lecture 
- - - 

## 2019 06 23

> 함수 정의
    
    - fun 으로 함수 정의
    - return 생략 가능 기능이 있다.
    - package 는 자바와 유사하다.
    - 코틀린은 리턴 할 값이 없는 경우  Unit 으로 리턴

> 변수 정의

    - val --> 일기 전용 변수
    - var --> mutable 변수
    - 컴파일러 타입 추론
    - val 은 값을 할당을 할 수 가 없다.

> comment 거의 유사

    - 중첩 허용

> 문자열 보간법

    - String 안에서 다 할 수 있다.

> nullable

    - null 인 경우를 명시를 해야 한다.
    - null check 를 할 수 가 있게 된다.
    - nullable 를 지원을 하는 것이 안정적으로 코딩할 수 있다.

> 자동 타입 변환

> while loop 는 같다.

> when expression
 
    - switch 보다 더 강력하게 사용 가능
> range
10. Collections

## 2019 06 24
> 모든 것은  객체

    - Number Class 로 접근
    
> 리터럴

    - 10, long, double, float, 2진수 16진수 8진수 x
> Underscore 수치를 표현 가능

> Representation
 
    - Nullable, Generic
> 문자 char 는 숫자로 취급되지 않음

    - java 에서는 가능하지만 직접적인 비교는 되지 않는다.
    
>  배열또한 클래스로 표현 된다.

> get, set, size

> 배열 생성
 
    - arrayOf --> 라이브러리 생성 

## 2019 06 27
> Control flow

    -  if else
    - java 유사
   
<code> val max = if(a>b) a else b </code> 식 사용
    

## 2019 06 29
> 코트린에는 삼항 연산자가 없다.
 
    - 대신 if를 사용을 한다.
    
> when --> switch 와 유사하다고 생각

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
    
> for loop

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
<code>
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
    
## 2019 07 06
> class and inheritance
    
    - class
    - inheritance
    
> android framework

    - android (kotlin)
    - 

## 2019 07 09
> class and ingeritance

> class

    - class Empty
    - 클래스 헤더의 일부

> 기본 생성자

    - 클래스 별로 1개
    - 클래스 헤더의 일부
    - 클래스 이름 뒤에 작성

<code> class Person constructor(firstName:String)<br>
       class Person(firstName: String)</code>
    
    - 기본 생성자는 코드를 가질 수 없음
    - 바디안에서는 클래스 코드
    - init {} 생성자 코드 작성
<code>
fun main(args :Array<String>){<br>
    val obj = Customer("kotlin)<br>
    println(obj)<br>
}<br>

class Customer(name: String){<br>
    init{<br>
        println("이름: $name")<br>
    }<br>
}<br>

fun main(args:Array<String>){<br>
    val obj = Customer()<br>
    obj.fulname = "코틀린"<br>
    println(obj).fullname<br>
}<br>
<br>
class Customer(){<br>
    var fullname: String = ""<br>
        get() {return field}<br>
        set(value) {feild = value}<br>
    <br><br>
}<br><br>
<br><br>
class Customer pubic @inject constructor(name: String)

</code>

    - property
    - 기본생성자의 파라미터 프로퍼티 초기화 선언에도 사용 가능
    - 프로퍼티 선언 및 초기화는 기본 생성자에서 간결한 구문으로 사용 가능    

> 보조 생성자

    - 기본 생성자는 클래스 헤더에서 선언
    - 클래스 바디에 선언

<code>
class Person(val name: String){ <br>
    constructor(name: String, parent: Person) : this(name){<br>
     //this 기본 생성자에 접근   <br>
    }<br>
<br>
    constructor() : this("홍길동", Person()){<br>
<br>
    }<br>
}
</code>

> 생성된 기본 생성자 (generated primarty constructor)

    - 생성자를 따로 선언하지 않으면 생성자 형서
    - 가시성이 public 으로 선언된

> 인스턴스 생성
    
    - 코틀린은 new 키워드가 없다.
<code>
val invoice = invoice()
</code>

> 클래스 멤버

    - constructor init
    - function
    - property
    - nested and inner class
    - object Declararation

## 2019 07 10

> inheritance

    - 코트린의 최상위 클래스는 Any
    - Java - object
<code>
    class Example1 <br>
    class Example2 : Any();
</code>
    - 클론뒤에 생성자를 넣는다.
    - Any, equals, hashCode, toString
<code>
fun main(args :Array<String>){<br>
<br>
}
open class AA(x: Int){<br>
<br>
}
class BB(x:Int) : AA(x){<br>
<br>
}
</code>
    - 파생클래스에 기본생성자가 없으면
    - super를 통하여 초기화
<code>
class MyView : View{<br>
    constructor() :super(1)<br>

    constructor(ctx:Int) : this()<br>

    constructor(ctx: Int, attrs: Int) : super(ctx, attrs)<br>
}
</code>
    - 코틀린은 전부 final
    - open annotation을 사용해야 한다.
    - final 의 반대
    - Effective Java

> 메소드 오버라이딩

<code>
open class Base{<br>
    open fun v(){}<br>
    fun nv() {}<br>
}<br>

class Derived() : Base(){<br>
    override fun v(){}<br>
}<br>
</code>

    - 명시적으로 'override' 키워드 사용
    - open 키워드와  override 키워드 사용

<code>
open class Foo{ <br>
    open val x:Int get{}<br>
}<br>

class Bar1 :Foo(){<br>
    ovverride val x : Int<br>
}<br>
</code>

    - 코틀린은 단일 상속만 가능
    - 코틀린은 인터페이스에서도 함수를 구현 가능
    - 자바는 아님
<code>
open class A{<br>
    open fun f() {print("A")}<br>
    fun a(){print("a")}<br>
}<br>

interface B{<br>
    fun f() {print("B")}<br>
    fun b( {print("b")})<br>
}<br>

class C :A(), B{<br>
    override fun f(){<br>
        super<A>.f()<br>
        super<B>.f()<br>
    }
}
</code>

> 추상 클래스
    
    - abstract 멤버는 구현 없음
    - abstract 클래스나 멤버는 open 필요 없음

<code>
abstract class AbsClass{ <br>
    abstract fun f()<br>
}<br>

class MyClass : AbsClass(){<br>
    override fun f()<br>
}<br>
</code>