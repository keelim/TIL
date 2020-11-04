### 어댑터 패턴

---

> - 용도 : 클래스를 바로 사용할 수 없는 경우가 있음 (다른 곳에서 개발했다거나, 수정할 수 없을 때)
>   중간에서 변환 역할을 해주는 클래스가 필요 → 어댑터 패턴
>
> - 사용 방법 : 상속
> - 호환되지 않은 인터페이스를 사용하는 클라이언트 그대로 활용 가능
>
> - 향후 인터페이스가 바뀌더라도, 변경 내역은 어댑터에 캡슐화 되므로 클라이언트 바뀔 필요X

##### 클래스 다이어그램

![img](https://t1.daumcdn.net/cfile/tistory/99D2F0445C6A152229)

아이폰의 이어폰을 생각해보자

가장 흔한 이어폰 잭을 아이폰에 사용하려면, 잭 자체가 맞지 않는다.

따라서 우리는 어댑터를 따로 구매해서 연결해야 이런 이어폰들을 사용할 수 있다

이처럼 **어댑터는 필요로 하는 인터페이스로 바꿔주는 역할**을 한다

![img](https://t1.daumcdn.net/cfile/tistory/99F3134C5C6A152D31)

이처럼 업체에서 제공한 클래스가 기존 시스템에 맞지 않으면?

> 기존 시스템을 수정할 것이 아니라, 어댑터를 활용해 유연하게 해결하자

##### 코드로 어댑터 패턴 이해하기

> 오리와 칠면조 인터페이스 생성
>
> 만약 오리 객체가 부족해서 칠면조 객체를 대신 사용해야 한다면?
>
> 두 객체는 인터페이스가 다르므로, 바로 칠면조 객체를 사용하는 것은 불가능함
>
> 따라서 칠면조 어댑터를 생성해서 활용해야 한다

- Duck.java

```java
package AdapterPattern;

public interface Duck {
	public void quack();
	public void fly();
}
```

- Turkey.java

```java
package AdapterPattern;

public interface Turkey {
	public void gobble();
	public void fly();
}
```

- WildTurkey.java

```java
package AdapterPattern;

public class WildTurkey implements Turkey {

	@Override
	public void gobble() {
		System.out.println("Gobble gobble");
	}

	@Override
	public void fly() {
		System.out.println("I'm flying a short distance");
	}
}
```

- TurkeyAdapter.java

```java
package AdapterPattern;

public class TurkeyAdapter implements Duck {

	Turkey turkey;

	public TurkeyAdapter(Turkey turkey) {
		this.turkey = turkey;
	}

	@Override
	public void quack() {
		turkey.gobble();
	}

	@Override
	public void fly() {
		turkey.fly();
	}

}
```

- DuckTest.java

```java
package AdapterPattern;

public class DuckTest {

	public static void main(String[] args) {

		MallardDuck duck = new MallardDuck();
		WildTurkey turkey = new WildTurkey();
		Duck turkeyAdapter = new TurkeyAdapter(turkey);

		System.out.println("The turkey says...");
		turkey.gobble();
		turkey.fly();

		System.out.println("The Duck says...");
		testDuck(duck);

		System.out.println("The TurkeyAdapter says...");
		testDuck(turkeyAdapter);

	}

	public static void testDuck(Duck duck) {

		duck.quack();
		duck.fly();

	}
}
```

아까 확인한 클래스 다이어그램에서 Target은 오리에 해당하며, Adapter는 칠면조라고 생각하면 된다.

#### Design Pattern - Adapter Pattern

---

[어댑터 패턴]

국가별 사용하는 전압이 달라서 220v를 110v형으로 바꿔서 끼우는 경우를 생각해보기.

- 실행 부분 (Main.java)

  ```java
  public class Main {
      public static void main (String[] args) {
          MediaPlayer player = new MP3();
          player.play("file.mp3");
          
          // MediaPlayer로 실행 못하는 MP4가 있음.
          // 이것을 mp3처럼 실행시키기 위해서,
          // Adapter를 생성하기.
          player = new FormatAdapter(new MP4());
          player.play("file.mp4");
      }
  }
  ```

- 변환 장치 부분 (FormatAdapter.java)

  ```java
  // MediaPlayer의 기능을 활용하기 위해 FormatAdapter라는 새로운 클래스를 생성
  // 그리고 그 클래스 내부에 (MP4, MKV와 같은) 클래스를 정리하려고 함.
  public class FormatAdapter implements MediaPlayer {
      private MediaPackage media;
      public FormatAdapter(MediaPackage m) {
          media = m;
      }
      // 그리고 반드시 사용해야하는 클래스의 함수를 선언해 둠
      @Override
      public void play(String filename) {
          System.out.print("Using Adapter");
          media.playFile(filename);
      }
  }
  ```

