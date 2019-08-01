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
   
``` val max = if(a>b) a else b ``` 식 사용
    

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

``` 
for(item in collection)
        print(item)     
```
        
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
```
        loop@ for(i in 10){
            println("--i: $i ---")
            for(j in 1..10){
                println("j: $j")
                if( j+1>12)
                    break @loop
            }
        }
```

    - 함수를 입력으로 가능 --> 입력 함수
    - 함수 중첩에서 return --> 한개의 함수가 return 
    - lambda는 함수가 아니기 떄문에 return을 하면 포함 함수가 종료
    - label를 사용을 하면 lambda 적용이 가능

```
        fun foo3(){
            var ints = listOf(0, 1, 2, 3)
            ints.forEach label@ ({
                if(it == 1) return @label
                print(it)
            })
            print("End")
        }
```

    - 암시적 레이블을 사용을 할 수 있다. 
        - 람다에서만 레이블을 사용하기 어렵다.
```
        fun foo3(){
            var ints = listOf(0, 1, 2, 3)
            ints.forEach ({
                if(it == 1) return @forEach
                print(it)
            })
            print("End")
        }
```
    
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

``` class Person constructor(firstName:String)
       class Person(firstName: String)
```
    
    - 기본 생성자는 코드를 가질 수 없음
    - 바디안에서는 클래스 코드
    - init {} 생성자 코드 작성
```
fun main(args :Array<String>){
    val obj = Customer("kotlin)
    println(obj)
}


class Customer(name: String){
    init{
        println("이름: $name")
    }
}

fun main(args:Array<String>){
    val obj = Customer()
    obj.fulname = "코틀린"
    println(obj).fullname
}

class Customer(){
    var fullname: String = ""
        get() {return field}
        set(value) {feild = value}
 
}

class Customer pubic @inject constructor(name: String)

```

    - property
    - 기본생성자의 파라미터 프로퍼티 초기화 선언에도 사용 가능
    - 프로퍼티 선언 및 초기화는 기본 생성자에서 간결한 구문으로 사용 가능    

> 보조 생성자

    - 기본 생성자는 클래스 헤더에서 선언
    - 클래스 바디에 선언

```java
class Person(val name: String){ 
    constructor(name: String, parent: Person) : this(name){
     //this 기본 생성자에 접근   
    }

    constructor() : this("홍길동", Person()){

    }
}
```

> 생성된 기본 생성자 (generated primarty constructor)

    - 생성자를 따로 선언하지 않으면 생성자 형서
    - 가시성이 public 으로 선언된

> 인스턴스 생성
    
    - 코틀린은 new 키워드가 없다.
```kotlin
val invoice = invoice()
```

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



    - 클론뒤에 생성자를 넣는다.
    - Any, equals, hashCode, toString

```kotlin
class Example1 
class Example2 : Any();

fun main(args :Array<String>){

}
open class AA(x: Int){

}
class BB(x:Int) : AA(x){

}
```
    - 파생클래스에 기본생성자가 없으면
    - super를 통하여 초기화

```kotlin
class MyView : View{
    constructor() :super(1)

    constructor(ctx:Int) : this()

    constructor(ctx: Int, attrs: Int) : super(ctx, attrs)
}
```
    - 코틀린은 전부 final
    - open annotation을 사용해야 한다.
    - final 의 반대
    - Effective Java

> 메소드 오버라이딩

```kotlin
open class Base{
    open fun v(){}
    fun nv() {}
}

class Derived() : Base(){
    override fun v(){}
}
```

    - 명시적으로 'override' 키워드 사용
    - open 키워드와  override 키워드 사용

```kotlin
open class Foo{ 
    open val x:Int get{}
}

class Bar1 :Foo(){
    ovverride val x : Int
}
```

    - 코틀린은 단일 상속만 가능
    - 코틀린은 인터페이스에서도 함수를 구현 가능
    - 자바는 아님
```kotlin
open class A{
    open fun f() {print("A")}
    fun a(){print("a")}
}

interface B{
    fun f() {print("B")}
    fun b( {print("b")})
}

class C :A(), B{
    override fun f(){
        super<A>.f()
        super<B>.f()
    }
}
```

> 추상 클래스
    
    - abstract 멤버는 구현 없음
    - abstract 클래스나 멤버는 open 필요 없음

```kotlin
abstract class AbsClass{ 
    abstract fun f()
}

class MyClass : AbsClass(){
    override fun f()
}
```

# 2019 07 11
> property

    - class 는 프로퍼티를 가질수 있음
    - var mutable val read only
```kotlin
class Address {
    var name: String = "Kotlin"
    val city: String = "Seoul"
}

fun copyAddress(address:Address): Address{
    val result = Address()
    result.name = address.name

    return result
}
```

    - filed 사용하듯이 사용하면 안된다.
    - option(생략 가능)
        - PropertyType  
            - property_initializer에서 타입을 추론 가능 생략 가능
            - property_initializer
            - getter
            - setter

```kotlin
    var <propertyName>[:<PropertyType>] [=<property_initializer>] [<getter>] [<setter>]

fun main(args:Array<String>){
    var obj = Address()
    println(obj.name)
}

class Address{
    var name:String = "Kotlin"
        get(){
            return field+"!!!"
            }
        set(value) {field = value}
}

class Address{
    var name = "Kotlin"
}

class Address2{
    var name:String = "Kotlin"
        get(){
            return field
        }
        set(value){
            field = value
        }

    val initialized = 1
}
Custom getter/setter
val isEmpty:Boolean 
    get() = this.size =0

var stringRepresentation: String
    get() = this.toString()
    set(value){ 
        setDataFromString(value)
    }

var setterVsibility: String = "abc"
    private set
    @inject set
    private set(value){
        field = value
    }
var counter = 0
    set(value){
        if(value >= 0) field = value
    }

```

    - 하나의 변수 필드처럼 보이게 된다.
    - 함수적인 요소와 필드 요소를 언어레벨에서 중간 역할을 하는 것
    - 프로퍼티 가시성을 변경이 필요한 경우
    - field 를 통하여 automatic backing field 를 제공가능
    - property accessor 만 사용 가능

```kotlin
fun main(args:Arrays<String>){
    var obj = Address()
    println(obj.name)
}

class Address{
    val isEmpty: Boolean = false
        get() {return field}
}

// backing property
private var _table = Map<String, Int>? = null --> backing property
public val table: Map<String, Int>
    get(){
        if(_table == null){
            _table = HashMap()
        }
        return _table ?:throuw AssertionError("null")
    }
```
     
> Compile-Time Constants
    
    - 컴파일 타임 상수를 만들 수 있음
```kotlin
const val SUBSYSTEM_DEPRECATED String = "This SubSystem is deprecated"
```

    - top level, object

>lat initialized property

    - non-null
    - dependency injection
    - Butter knife
    - unit test

```kotlin
    public class Mytest{
        lateinit var subject TestSubject

        @SetUp fun setup(){
            subject = testSubject()
        }

        @Test fun test(){

        }
    }
```

## 2019 07 12
> Data class Nested class

    - Data class 
    - 아무런 작동을 하지 않고 데이터만 보관을 할 때
```kotlin
fun main(args:Array<String>){
    val obj = User()
    println(obj.toString())
}   
data clss User(var name: String = "Kotlin", var age:Int = 123)
```

    - equals, hashCode, copy, toString
    - compiler 가 자동으로 생성
    - 기본 생성자에서 정의한 프로퍼티들만
    - 1개 이상의 파라미터
    - 기본 생성자의 파라미터가 var, val
    - abstract, open , sealed, inner
    - Data class interface , Sealed class
    - jvm 파라미터 없는 생성자가 필요한 경우
    - 모든 프로퍼티에 기본 값을 설정해 주면 됨
    - 코틀린이 간결한 이유

> 복사

    - 기존 값을 유지하고 일부만 고치는것
    - copy를 통하여 쉽게 사용 가능
    - 값만 고쳐서 새로운 객체를 만드는 것
```kotlin
fun copy(name:String = this.name, age:Int = this.age)

val jack = User(name= "Jack", age =1)
val orderjack = jack.copy(age =2)
```

> Destructing Declarations

    - data class Destructureing Declarations
    - compiler componentN 함수를 생성

```kotlin
    val Jane = User("jane", 35)
    val(name, age) = jane// --> 이러한 표현이 가능
    println("$name, $age years of age")
```

    - 값을 2개, 2개 설정을 할 수 있다. 
    - componentN 함수를 만든다.

>Standara data class

    - Pair, Triple
```kotlin
    val jane = User("Jane", 35)
    val pair = Pair("Jane", 35)
```

    - 임시적으로 사용 할 수 있는 클래스

> Nested Class 

    - inner keyword를 사용하여도 좋다.

## 2019 07 13
> Object Expression and Declaration

    - object 어떤 클래스에서 약간의 변경 없이 객체를 생성 하는 것
    - 명시적 선언이 아니라 바로 사용 함
    - Object expression --> 익명 객체
    - Object Declarations --> single tone
    - Companion Object --> single tone + class method (static)
    - 코틀린은 static method 가 없음
    - unpackage level function     

```kotlin
btn.setOnclickListener(new OnclickListener(){

})    
```

    - 슈퍼타입의 생성자가 있는 경우 반드시 값을 전달을 해주어야 함
    - 슈터타입이 여러개인 경우 콜론 뒤에 콤마로 구분해서 명시
    - public으로 객체를 접근을 하는 경우 안될 수 가 있다.
    - enclosing scope 변수를 접근 할 수 있음
    - final variables 제약 조건이 없음
    
> Object declarations

    - 그냥 객체가 선언이 되는 것이다. 
    - single tone pattern
    - 하나의 메소드만 가져야 하는 경우
    - object 뒤에 반드시 이름이 있어야 한다.
    - object declaration != object expression
    - 슈퍼타입을 가질 수 있음
    - static과 비슷하게 사용
    - 우측에서이 사용이 제한이 된다.

> Companion Object
    
    - 내부 클래스에서 companion 을 사용
    - companion 내부 클래스를 바로 사용 가능
    - 다른 언어에서의 static으로 접근이 가능하다.
    - top level로 접근이 될 수 있음을 아라야 한다.
    - 실제 객체의 멤버
  
    
> Singleton Pattern 
    
    - 어플리켕션 시작이 될때 어떤 클래스가 한 번 할당이 되고 지속적으로 사용
    - 실제 생성 객체는 하나
    - 하나의 인스턴스를 생성해서 사용을 하는 디자인 패턴
    - 새롭게 new를 쓰는 것을 막는다.
    - DataBase를 사용을 할 때 많이 사용된다
    - 안드로이드에 경우 싱클톤을 만드는 것이 편리하다.
    - 인스턴스가 하나인것을 보증해야 한다.
    - 객체 로딩시간이 현저히 준다.
    
    
## 2019 07 13
> annotation
    - anotation을 처리를 하는 것이 자바에서 코틀린을 변경을 한다.