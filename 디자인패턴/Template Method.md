## [디자인 패턴] Template Method Pattern

> 로직을 단계 별로 나눠야 하는 상황에서 적용한다.
>
> 단계별로 나눈 로직들이 앞으로 수정될 가능성이 있을 경우 더 효율적이다.



#### 조건

- 클래스는 추상(abstract)로 만든다.
- 단계를 진행하는 메소드는 수정이 불가능하도록 final 키워드를 추가한다.
- 각 단계들은 외부는 막고, 자식들만 활용할 수 있도록 protected로 선언한다.



예를 들어보자. 피자를 만들 때는 크게 `반죽 → 토핑 → 굽기` 로 3단계로 이루어져있다.

이 단계는 항상 유지되며, 순서가 바뀔 일은 없다. 물론 실제로는 도우에 따라 반죽이 달라질 수 있겠지만, 일단 모든 피자의 반죽과 굽기는 동일하다고 가정하자. 그러면 피자 종류에 따라 토핑만 바꾸면 된다.

```java
abstract class Pizza {
    
    protected void 반죽() { System.out.println("반죽!"); }
    abstract void 토핑() {}
    protected void 굽기() { System.out.println("굽기!"); }
    
    final void makePizza() { // 상속 받은 클래스에서 수정 불가
        this.반죽();
        this.토핑();
        this.굽기();
    }
    
}
```

```java
class PotatoPizza extends Pizza {
    
    @Override
    void 토핑() {
        System.out.println("고구마 넣기!");
    }
    
}

class TomatoPizza extends Pizza {
    
    @Override
    void 토핑() {
        System.out.println("토마토 넣기!");
    }
    
}
```

abstract 키워드를 통해 자식 클래스에서는 선택적으로 메소드를 오버라이드 할 수 있게 된다.





#### abstract와 Interface의 차이는?

- abstract : 부모의 기능을 자식에서 확장시켜나가고 싶을 때
- interface : 해당 클래스가 가진 함수의 기능을 활용하고 싶을 때

> abstract는 다중 상속이 안된다. 상황에 맞게 활용하자!



#### 디자인 패턴 _ Template Method Pattern

---

[디자인 패턴 예]

1. 템플릿 메서드 패턴

   특정 환경 or 상황에 맞게 확장, 변경할 때 유용한 패턴

   **<u>추상 클래스, 구현 클래스</u>** 둘로 구분. 

   추상클래스 (Abstract Class) : 메인이 되는 로직 부분은 일반 메소드로 선언해 둠.

   구현클래스 (Concrete Class) : 메소드를 선언 후 호출하는 방식.

   - 장점
     - 구현 클래스에서는 추상 클래스에 선언된 메소드만 사용하므로, **<u>핵심 로직 관리가 용이</u>**
     - 객체 추가 및 확장 가능
   - 단점
     - 추상 메소드가 많아지면, 클래스 관리가 복잡함.

   * 설명

     1) HouseTemplate.java

     > Template 추상 클래스를 하나 생성. (예, HouseTemplate)
     >
     > 이 HouseTemplate을 사용할 때는,
     >
     > "HouseTemplate houseType = new WoodenHouse()" 이런 식으로 넣음.
     >
     > HouseTemplate 내부에 **<u>buildHouse</u>**라는 변해서는 안되는 핵심 로직을 만들어 놓음. (장점 1)
     >
     > Template 클래스 내부의 **<u>핵심 로직 내부의 함수</u>**를 상속하는 클래스가 직접 구현하도록, abstract를 지정해 둠.

     ```java
     public abstract class HouseTemplate {
         
         // 이런 식으로 buildHouse라는 함수 (핵심 로직)을 선언해 둠.
         public final void buildHouse() {
             buildFoundation();	// (1)
             buildPillars();		// (2)
             buildWalls();		// (3)
             buildWindows();		// (4)
             System.out.println("House is built.");
         }
         
         // buildFoundation(); 정의 부분 (1)
         // buildWalls(); 정의 부분		(2)
         
         // 위의 두 함수와는 다르게 이 클래스를 상속받는 클래스가 별도로 구현했으면 하는 메소드들은 abstract로 선언하여, 정의하도록 함
         public abstract void buildWalls();	// (3)
         public abstract void buildPillars();// (4)
         
     }
     
     ```

     

     2) WoodenHouse.java (GlassHouse.java도 가능)

     > HouseTemplate을 상속받는 클래스.
     >
     > Wooden이나, Glass에 따라서 buildHouse 내부의 핵심 로직이 바뀔 수 있으므로,
     >
     > 이 부분을 반드시 선언하도록 지정해둠.

     ```java
     public class WoodenHouse extends HouseTemplate {
         @Override
         public void buildWalls() {
             System.out.println("Building Wooden Walls");
         }
         @Override
         public void buildPillars() {
             System.out.println("Building Pillars with Wood coating");
         }
     }
     ```

     