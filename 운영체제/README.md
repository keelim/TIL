# 운영체제

## 스케줄러

_프로세스를 스케줄링하기 위한 Queue 에는 세 가지 종류가 존재한다._

- Job Queue : 현재 시스템 내에 있는 모든 프로세스의 집합
- Ready Queue : 현재 메모리 내에 있으면서 CPU 를 잡아서 실행되기를 기다리는 프로세스의 집합
- Device Queue : Device I/O 작업을 대기하고 있는 프로세스의 집합

각각의 Queue 에 프로세스들을 넣고 빼주는 스케줄러에도 크게 **세 가지 종류가** 존재한다.

### 장기스케줄러(Long-term scheduler or job scheduler)

메모리는 한정되어 있는데 많은 프로세스들이 한꺼번에 메모리에 올라올 경우, 대용량 메모리(일반적으로 디스크)에 임시로 저장된다. 이 pool 에 저장되어 있는 프로세스 중 어떤 프로세스에 메모리를 할당하여 ready queue 로 보낼지 결정하는 역할을 한다.

- 메모리와 디스크 사이의 스케줄링을 담당.
- 프로세스에 memory(및 각종 리소스)를 할당(admit)
- degree of Multiprogramming 제어  
  (실행중인 프로세스의 수 제어)
- 프로세스의 상태  
  new -> ready(in memory)

_cf) 메모리에 프로그램이 너무 많이 올라가도, 너무 적게 올라가도 성능이 좋지 않은 것이다. 참고로 time sharing system 에서는 장기 스케줄러가 없다. 그냥 곧바로 메모리에 올라가 ready 상태가 된다._

### 단기스케줄러(Short-term scheduler or CPU scheduler)

- CPU 와 메모리 사이의 스케줄링을 담당.
- Ready Queue 에 존재하는 프로세스 중 어떤 프로세스를 running 시킬지 결정.
- 프로세스에 CPU 를 할당(scheduler dispatch)
- 프로세스의 상태  
  ready -> running -> waiting -> ready

### 중기스케줄러(Medium-term scheduler or Swapper)

- 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄 (swapping)
- 프로세스에게서 memory 를 deallocate
- degree of Multiprogramming 제어
- 현 시스템에서 메모리에 너무 많은 프로그램이 동시에 올라가는 것을 조절하는 스케줄러.
- 프로세스의 상태  
  ready -> suspended

#### Process state - suspended

Suspended(stopped) : 외부적인 이유로 프로세스의 수행이 정지된 상태로 메모리에서 내려간 상태를 의미한다. 프로세스 전부 디스크로 swap out 된다. blocked 상태는 다른 I/O 작업을 기다리는 상태이기 때문에 스스로 ready state 로 돌아갈 수 있지만 이 상태는 외부적인 이유로 suspending 되었기 때문에 스스로 돌아갈 수 없다.

[뒤로](https://github.com/JaeYeopHan/for_beginner)/[위로](#part-1-4-운영체제)

---

### CPU 스케줄러

_스케줄링 대상은 Ready Queue 에 있는 프로세스들이다._

### FCFS(First Come First Served)

- 특징

- 먼저 온 고객을 먼저 서비스해주는 방식, 즉 먼저 온 순서대로 처리.
- 비선점형(Non-Preemptive) 스케줄링  
  일단 CPU 를 잡으면 CPU burst 가 완료될 때까지 CPU 를 반환하지 않는다. 할당되었던 CPU 가 반환될 때만 스케줄링이 이루어진다.

- 문제점

- convoy effect 소요시간이 긴 프로세스가 먼저 도달하여 효율성을 낮추는 현상이 발생한다.

### SJF(Shortest - Job - First)

- 특징

- 다른 프로세스가 먼저 도착했어도 CPU burst time 이 짧은 프로세스에게 선 할당
- 비선점형(Non-Preemptive) 스케줄링

- 문제점

- starvation  
  효율성을 추구하는게 가장 중요하지만 특정 프로세스가 지나치게 차별받으면 안되는 것이다. 이 스케줄링은 극단적으로 CPU 사용이 짧은 job 을 선호한다. 그래서 사용 시간이 긴 프로세스는 거의 영원히 CPU 를 할당받을 수 없다.

### SRT(Shortest Remaining time First)

- 특징

- 새로운 프로세스가 도착할 때마다 새로운 스케줄링이 이루어진다.
- 선점형 (Preemptive) 스케줄링  
  현재 수행중인 프로세스의 남은 burst time 보다 더 짧은 CPU burst time 을 가지는 새로운 프로세스가 도착하면 CPU 를 뺏긴다.

- 문제점

- starvation
- 새로운 프로세스가 도달할 때마다 스케줄링을 다시하기 때문에 CPU burst time(CPU 사용시간)을 측정할 수가 없다.

### Priority Scheduling

- 특징

- 우선순위가 가장 높은 프로세스에게 CPU 를 할당하는 스케줄링이다. 우선순위란 정수로 표현하게 되고 작은 숫자가 우선순위가 높다.
- 선점형 스케줄링(Preemptive) 방식  
  더 높은 우선순위의 프로세스가 도착하면 실행중인 프로세스를 멈추고 CPU 를 선점한다.
- 비선점형 스케줄링(Non-Preemptive) 방식  
  더 높은 우선순위의 프로세스가 도착하면 Ready Queue 의 Head 에 넣는다.

- 문제점

- starvation
- 무기한 봉쇄(Indefinite blocking)  
  실행 준비는 되어있으나 CPU 를 사용못하는 프로세스를 CPU 가 무기한 대기하는 상태

#### 해결책

- aging 아무리 우선순위가 낮은 프로세스라도 오래 기다리면 우선순위를 높여주자.

### Round Robin

- 특징

- 현대적인 CPU 스케줄링
- 각 프로세스는 동일한 크기의 할당 시간(time quantum)을 갖게 된다.
- 할당 시간이 지나면 프로세스는 선점당하고 ready queue 의 제일 뒤에 가서 다시 줄을 선다.
- `RR`은 CPU 사용시간이 랜덤한 프로세스들이 섞여있을 경우에 효율적
- `RR`이 가능한 이유는 프로세스의 context 를 save 할 수 있기 때문이다.

#### 장점

- `Response time`이 빨라진다.  
  n 개의 프로세스가 ready queue 에 있고 할당시간이 q(time quantum)인 경우 각 프로세스는 q 단위로 CPU 시간의 1/n 을 얻는다. 즉, 어떤 프로세스도 (n-1)q time unit 이상 기다리지 않는다.
- 프로세스가 기다리는 시간이 CPU 를 사용할 만큼 증가한다.  
  공정한 스케줄링이라고 할 수 있다.

#### 주의할 점

설정한 `time quantum`이 너무 커지면 `FCFS`와 같아진다.
또 너무 작아지면 스케줄링 알고리즘의 목적에는 이상적이지만 잦은 context switch 로 overhead 가 발생한다.
그렇기 때문에 적당한 `time quantum`을 설정하는 것이 중요하다.

## 동기와 비동기의 차이

### Sync vs Async

일반적으로 동기와 비동기의 차이는 메소드를 실행시킴과 `동시에` 반환 값이 기대되는 경우를 **동기** 라고 표현하고 그렇지 않은 경우에 대해서 **비동기** 라고 표현한다. 동시에라는 말은 실행되었을 때 값이 반환되기 전까지는 `blocking`되어 있다는 것을 의미한다. 비동기의 경우, `blocking`되지 않고 이벤트 큐에 넣거나 백그라운드 스레드에게 해당 task 를 위임하고 바로 다음 코드를 실행하기 때문에 기대되는 값이 바로 반환되지 않는다.

### 프로세스 동기화

### Critical Section(임계영역)

멀티 스레딩에 문제점에서 나오듯, 동일한 자원을 동시에 접근하는 작업(e.g. 공유하는 변수 사용, 동일 파일을 사용하는 등)을 실행하는 코드 영역을 Critical Section 이라 칭한다.

### Critical Section Problem(임계영역 문제)

프로세스들이 Critical Section 을 함께 사용할 수 있는 프로토콜을 설계하는 것이다.

#### Requirements(해결을 위한 기본조건)

- Mutual Exclusion(상호 배제)  
  프로세스 P1 이 Critical Section 에서 실행중이라면, 다른 프로세스들은 그들이 가진 Critical Section 에서 실행될 수 없다.
- Progress(진행)  
  Critical Section 에서 실행중인 프로세스가 없고, 별도의 동작이 없는 프로세스들만 Critical Section 진입 후보로서 참여될 수 있다.
- Bounded Waiting(한정된 대기)  
  P1 가 Critical Section 에 진입 신청 후 부터 받아들여질 때가지, 다른 프로세스들이 Critical Section 에 진입하는 횟수는 제한이 있어야 한다.

### 해결책

### Lock

- 하드웨어 기반 해결책으로써, 동시에 공유 자원에 접근하는 것을 막기 위해 Critical Section 에 진입하는 프로세스는 Lock 을 획득하고 Critical Section 을 빠져나올 때, Lock 을 방출함으로써 동시에 접근이 되지 않도록 한다.

#### 한계

- 다중처리기 환경에서는 시간적인 효율성 측면에서 적용할 수 없다.

### Semaphores(세마포)

- 소프트웨어상에서 Critical Section 문제를 해결하기 위한 동기화 도구

#### 종류

OS 는 Counting/Binary 세마포를 구분한다

- 카운팅 세마포  
  **가용한 개수를 가진 자원** 에 대한 접근 제어용으로 사용되며, 세마포는 그 가용한 **자원의 개수** 로 초기화 된다.
  자원을 사용하면 세마포가 감소, 방출하면 세마포가 증가 한다.

- 이진 세마포  
  MUTEX 라고도 부르며, 상호배제의 (Mutual Exclusion)의 머릿글자를 따서 만들어졌다.
  이름 그대로 0 과 1 사이의 값만 가능하며, 다중 프로세스들 사이의 Critical Section 문제를 해결하기 위해 사용한다.

#### 단점

- Busy Waiting(바쁜 대기)  
  Spin lock이라고 불리는 Semaphore 초기 버전에서 Critical Section 에 진입해야하는 프로세스는 진입 코드를 계속 반복 실행해야 하며, CPU 시간을 낭비했었다. 이를 Busy Waiting이라고 부르며 특수한 상황이 아니면 비효율적이다.
  일반적으로는 Semaphore에서 Critical Section에 진입을 시도했지만 실패한 프로세스에 대해 Block시킨 뒤, Critical Section에 자리가 날 때 다시 깨우는 방식을 사용한다. 이 경우 Busy waiting으로 인한 시간낭비 문제가 해결된다.

#### Deadlock(교착상태)

- 세마포가 Ready Queue 를 가지고 있고, 둘 이상의 프로세스가 Critical Section 진입을 무한정 기다리고 있고, Critical Section 에서 실행되는 프로세스는 진입 대기 중인 프로세스가 실행되야만 빠져나올 수 있는 상황을 지칭한다.

### 모니터

- 고급 언어의 설계 구조물로서, 개발자의 코드를 상호배제 하게끔 만든 추상화된 데이터 형태이다.
- 공유자원에 접근하기 위한 키 획득과 자원 사용 후 해제를 모두 처리한다. (세마포어는 직접 키 해제와 공유자원 접근 처리가 필요하다. )

## 메모리 관리 전략

### 메모리 관리 배경

각각의 **프로세스** 는 독립된 메모리 공간을 갖고, 운영체제 혹은 다른 프로세스의 메모리 공간에 접근할 수 없는 제한이 걸려있다. 단지, **운영체제** 만이 운영체제 메모리 영역과 사용자 메모리 영역의 접근에 제약을 받지 않는다.

**Swapping** : 메모리의 관리를 위해 사용되는 기법. 표준 Swapping 방식으로는 round-robin 과 같은 스케줄링의 다중 프로그래밍 환경에서 CPU 할당 시간이 끝난 프로세스의 메모리를 보조 기억장치(e.g. 하드디스크)로 내보내고 다른 프로세스의 메모리를 불러 들일 수 있다.

> 이 과정을 **swap** (**스왑시킨다**) 이라 한다. 주 기억장치(RAM)으로 불러오는 과정을 **swap-in**, 보조 기억장치로 내보내는 과정을 **swap-out** 이라 한다. swap 에는 큰 디스크 전송시간이 필요하기 때문에 현재에는 메모리 공간이 부족할때 Swapping 이 시작된다.

**단편화** (**Fragmentation**) : 프로세스들이 메모리에 적재되고 제거되는 일이 반복되다보면, 프로세스들이 차지하는 메모리 틈 사이에 사용 하지 못할 만큼의 작은 자유공간들이 늘어나게 되는데, 이것이 **단편화** 이다. 단편화는 2 가지 종류로 나뉜다.

- 외부 단편화: 메모리 공간 중 사용하지 못하게 되는 일부분. 물리 메모리(RAM)에서 사이사이 남는 공간들을 모두 합치면 충분한 공간이 되는 부분들이 **분산되어 있을때 발생한다고 볼 수 있다.**
- 내부 단편화: 프로세스가 사용하는 메모리 공간 에 포함된 남는 부분. 예를들어 **메모리 분할 자유 공간이 10,000B 있고 Process A 가 9,998B 사용하게되면 2B 라는 차이** 가 존재하고, 이 현상을 내부 단편화라 칭한다.

압축 : 외부 단편화를 해소하기 위해 프로세스가 사용하는 공간들을 한쪽으로 몰아, 자유공간을 확보하는 방법론 이지만, 작업효율이 좋지 않다. (위의 메모리 현황이 압축을 통해 아래의 그림 처럼 바뀌는 효과를 가질 수 있다)

### Paging(페이징)

하나의 프로세스가 사용하는 메모리 공간이 연속적이어야 한다는 제약을 없애는 메모리 관리 방법이다.
외부 단편화와 압축 작업을 해소 하기 위해 생긴 방법론으로, 물리 메모리는 Frame 이라는 고정 크기로 분리되어 있고, 논리 메모리(프로세스가 점유하는)는 페이지라 불리는 고정 크기의 블록으로 분리된다.(페이지 교체 알고리즘에 들어가는 페이지)

페이징 기법을 사용함으로써 논리 메모리는 물리 메모리에 저장될 때, 연속되어 저장될 필요가 없고 물리 메모리의 남는 프레임에 적절히 배치됨으로 외부 단편화를 해결할 수 있는 큰 장점이 있다.

하나의 프로세스가 사용하는 공간은 여러개의 페이지로 나뉘어서 관리되고(논리 메모리에서), 개별 페이지는 **순서에 상관없이** 물리 메모리에 있는 프레임에 mapping 되어 저장된다고 볼 수 있다.

- 단점 : 내부 단편화 문제의 비중이 늘어나게 된다. 예를들어 페이지 크기가 1,024B 이고 **프로세스 A** 가 3,172B 의 메모리를 요구한다면 3 개의 페이지 프레임(1,024 \* 3 = 3,072) 하고도 100B 가 남기때문에 총 4 개의 페이지 프레임이 필요한 것이다. 결론적으로 4 번째 페이지 프레임에는 924B(1,024 - 100)의 여유 공간이 남게 되는 내부 단편화 문제가 발생하는 것이다.

### Segmentation(세그멘테이션)

페이징에서처럼 논리 메모리와 물리 메모리를 같은 크기의 블록이 아닌, 서로 다른 크기의 논리적 단위인 세그먼트(Segment)로 분할
사용자가 두 개의 주소로 지정(세그먼트 번호 + 변위)
세그먼트 테이블에는 각 세그먼트의 기준(세그먼트의 시작 물리 주소)과 한계(세그먼트의 길이)를 저장

- 단점 : 서로 다른 크기의 세그먼트들이 메모리에 적재되고 제거되는 일이 반복되다 보면, 자유 공간들이 많은 수의 작은 조각들로 나누어져 못 쓰게 될 수도 있다.(외부 단편화)

## 가상 메모리

다중 프로그래밍을 실현하기 위해서는 많은 프로세스들을 동시에 메모리에 올려두어야 한다. 가상메모리는 **프로세스 전체가 메모리 내에 올라오지 않더라도 실행이 가능하도록 하는 기법** 이며, 프로그램이 물리 메모리보다 커도 된다는 주요 장점이 있다.

### 가상 메모리 개발 배경

실행되는 **코드의 전부를 물리 메모리에 존재시켜야** 했고, **메모리 용량보다 큰 프로그램은 실행시킬 수 없었다.** 또한, 여러 프로그램을 동시에 메모리에 올리기에는 용량의 한계와, 페이지 교체등의 성능 이슈가 발생하게 된다.
또한, 가끔만 사용되는 코드가 차지하는 메모리들을 확인할 수 있다는 점에서, 불필요하게 전체의 프로그램 전체가 메모리에 올라와 있어야 하는게 아니라는 것을 알 수 있다.

#### 프로그램의 일부분만 메모리에 올릴 수 있다면

- 물리 메모리 크기에 제약받지 않게 된다.
- 더 많은 프로그램을 동시에 실행할 수 있게 된다. 이에 따라 `응답시간`은 유지되고, `CPU 이용률`과 `처리율`은 높아진다.
- [swap](#메모리-관리-배경)에 필요한 입출력이 줄어들기 때문에 프로그램들이 빠르게 실행된다.

### 가상 메모리가 하는 일

가상 메모리는 실제의 물리 메모리 개념과 사용자의 논리 메모리 개념을 분리한 것으로 정리할 수 있다. 이로써 작은 메모리를 가지고도 얼마든지 큰 `가상 주소 공간`을 프로그래머에게 제공할 수 있다.

#### 가상 주소 공간

- 한 프로세스가 메모리에 저장되는 논리적인 모습을 가상메모리에 구현한 공간이다.
  프로세스가 요구하는 메모리 공간을 가상메모리에서 제공함으로서 현재 직접적으로 필요치 않은 메모리 공간은 실제 물리 메모리에 올리지 않는 것으로 물리 메모리를 절약할 수 있다.
- 예를 들어, 한 프로그램이 실행되며 논리 메모리로 100KB 가 요구되었다고 하자.
  하지만 실행까지에 필요한 메모리 공간`(Heap영역, Stack 영역, 코드, 데이터)`의 합이 40KB 라면, 실제 물리 메모리에는 40KB 만 올라가 있고, 나머지 60KB 만큼은 필요시에 물리메모리에 요구한다고 이해할 수 있겠다.

| `Stack` | :free (60KB) | `Heap` | `Data` | `Code` : |
| ------- | ------------ | :----: | ------ | -------- |


#### 프로세스간의 페이지 공유

가상 메모리는...

- `시스템 라이브러리`가 여러 프로세스들 사이에 공유될 수 있도록 한다.
  각 프로세스들은 `공유 라이브러리`를 자신의 가상 주소 공간에 두고 사용하는 것처럼 인식하지만, 라이브러리가 올라가있는 `물리 메모리 페이지`들은 모든 프로세스에 공유되고 있다.
- 프로세스들이 메모리를 공유하는 것을 가능하게 하고, 프로세스들은 공유 메모리를 통해 통신할 수 있다.
  이 또한, 각 프로세스들은 각자 자신의 주소 공간처럼 인식하지만, 실제 물리 메모리는 공유되고 있다.
- `fork()`를 통한 프로세스 생성 과정에서 페이지들이 공유되는 것을 가능하게 한다.

### Demand Paging(요구 페이징)

프로그램 실행 시작 시에 프로그램 전체를 디스크에서 물리 메모리에 적재하는 대신, 초기에 필요한 것들만 적재하는 전략을 `요구 페이징`이라 하며, 가상 메모리 시스템에서 많이 사용된다. 그리고 가상 메모리는 대개 [페이지](#paging페이징)로 관리된다.
요구 페이징을 사용하는 가상 메모리에서는 실행과정에서 필요해질 때 페이지들이 적재된다. **한 번도 접근되지 않은 페이지는 물리 메모리에 적재되지 않는다.**

프로세스 내의 개별 페이지들은 `페이저(pager)`에 의해 관리된다. 페이저는 프로세스 실행에 실제 필요한 페이지들만 메모리로 읽어 옮으로서, **사용되지 않을 페이지를 가져오는 시간낭비와 메모리 낭비를 줄일 수 있다.**

#### Page fault trap(페이지 부재 트랩)

### 페이지 교체

`요구 페이징` 에서 언급된대로 프로그램 실행시에 모든 항목이 물리 메모리에 올라오지 않기 때문에, 프로세스의 동작에 필요한 페이지를 요청하는 과정에서 `page fault(페이지 부재)`가 발생하게 되면, 원하는 페이지를 보조저장장치에서 가져오게 된다. 하지만, 만약 물리 메모리가 모두 사용중인 상황이라면, 페이지 교체가 이뤄져야 한다.(또는, 운영체제가 프로세스를 강제 종료하는 방법이 있다.)

#### 기본적인 방법

물리 메모리가 모두 사용중인 상황에서의 메모리 교체 흐름이다.

1.  디스크에서 필요한 페이지의 위치를 찾는다
1.  빈 페이지 프레임을 찾는다.
    1.  `페이지 교체 알고리즘`을 통해 희생될(victim) 페이지를 고른다.
    1.  희생될 페이지를 디스크에 기록하고, 관련 페이지 테이블을 수정한다.
1.  새롭게 비워진 페이지 테이블 내 프레임에 새 페이지를 읽어오고, 프레임 테이블을 수정한다.
1.  사용자 프로세스 재시작

#### 페이지 교체 알고리즘

##### FIFO 페이지 교체

가장 간단한 페이지 교체 알고리즘으로 FIFO(first-in first-out)의 흐름을 가진다. 즉, 먼저 물리 메모리에 들어온 페이지 순서대로 페이지 교체 시점에 먼저 나가게 된다는 것이다.

- 장점

  - 이해하기도 쉽고, 프로그램하기도 쉽다.

- 단점
  - 오래된 페이지가 항상 불필요하지 않은 정보를 포함하지 않을 수 있다(초기 변수 등)
  - 처음부터 활발하게 사용되는 페이지를 교체해서 페이지 부재율을 높이는 부작용을 초래할 수 있다.
  - `Belady의 모순`: 페이지를 저장할 수 있는 페이지 프레임의 갯수를 늘려도 되려 페이지 부재가 더 많이 발생하는 모순이 존재한다.

##### 최적 페이지 교체(Optimal Page Replacement)

`Belady의 모순`을 확인한 이후 최적 교체 알고리즘에 대한 탐구가 진행되었고, 모든 알고리즘보다 낮은 페이지 부재율을 보이며 `Belady의 모순`이 발생하지 않는다. 이 알고리즘의 핵심은 `앞으로 가장 오랫동안 사용되지 않을 페이지를 찾아 교체`하는 것이다.
주로 비교 연구 목적을 위해 사용한다.

- 장점

  - 알고리즘 중 가장 낮은 페이지 부재율을 보장한다.

- 단점
  - 구현의 어려움이 있다. 모든 프로세스의 메모리 참조의 계획을 미리 파악할 방법이 없기 때문이다.

##### LRU 페이지 교체(LRU Page Replacement)

`LRU: Least-Recently-Used`  
최적 알고리즘의 근사 알고리즘으로, 가장 오랫동안 사용되지 않은 페이지를 선택하여 교체한다.

- 특징
  - 대체적으로 `FIFO 알고리즘`보다 우수하고, `OPT알고리즘`보다는 그렇지 못한 모습을 보인다.

##### LFU 페이지 교체(LFU Page Replacement)

`LFU: Least Frequently Used`  
참조 횟수가 가장 적은 페이지를 교체하는 방법이다. 활발하게 사용되는 페이지는 참조 횟수가 많아질 거라는 가정에서 만들어진 알고리즘이다.

- 특징
  - 어떤 프로세스가 특정 페이지를 집중적으로 사용하다, 다른 기능을 사용하게되면 더 이상 사용하지 않아도 계속 메모리에 머물게 되어 초기 가정에 어긋나는 시점이 발생할 수 있다
  - 최적(OPT) 페이지 교체를 제대로 근사하지 못하기 때문에, 잘 쓰이지 않는다.

##### MFU 페이지 교체(MFU Page Replacement)

`MFU: Most Frequently Used`  
참조 회수가 가장 작은 페이지가 최근에 메모리에 올라왔고, 앞으로 계속 사용될 것이라는 가정에 기반한다.

- 특징
  - 최적(OPT) 페이지 교체를 제대로 근사하지 못하기 때문에, 잘 쓰이지 않는다.

[뒤로](https://github.com/JaeYeopHan/for_beginner)/[위로](#part-1-4-운영체제)

---

## 캐시의 지역성

### 캐시의 지역성 원리

캐시 메모리는 속도가 빠른 장치와 느린 장치간의 속도차에 따른 병목 현상을 줄이기 위한 범용 메모리이다. 이러한 역할을 수행하기 위해서는 CPU 가 어떤 데이터를 원할 것인가를 어느 정도 예측할 수 있어야 한다. 캐시의 성능은 작은 용량의 캐시 메모리에 CPU 가 이후에 참조할, 쓸모 있는 정보가 어느 정도 들어있느냐에 따라 좌우되기 때문이다.

이 때 `적중율(Hit rate)`을 극대화 시키기 위해 데이터 `지역성(Locality)의 원리`를 사용한다. 지역성의 전제조건으로 프로그램은 모든 코드나 데이터를 균등하게 Access 하지 않는다는 특성을 기본으로 한다. 즉, `Locality`란 기억 장치 내의 정보를 균일하게 Access 하는 것이 아닌 어느 한 순간에 특정 부분을 집중적으로 참조하는 특성인 것이다.

이 데이터 지역성은 대표적으로 시간 지역성(Temporal Locality)과 공간 지역성(Spatial Locality)으로 나뉜다.

- 시간 지역성 : 최근에 참조된 주소의 내용은 곧 다음에 다시 참조되는 특성.
- 공간 지역성 : 대부분의 실제 프로그램이 참조된 주소와 인접한 주소의 내용이 다시 참조되는 특성

### Caching line

언급했듯이 캐시(cache)는 프로세서 가까이에 위치하면서 빈번하게 사용되는 데이터를 놔두는 장소이다. 하지만 캐시가 아무리 가까이 있더라도 찾고자 하는 데이터가 어느 곳에 저장되어 있는지 몰라 모든 데이터를 순회해야 한다면 시간이 오래 걸리게 된다. 즉, 캐시에 목적 데이터가 저장되어 있다면 바로 접근하여 출력할 수 있어야 캐시가 의미 있어진다는 것이다.

그렇기 때문에 캐시에 데이터를 저장할 때 특정 자료구조를 사용하여 `묶음`으로 저장하게 되는데 이를 **캐싱 라인** 이라고 한다. 다양한 주소에 있는 데이터를 사용하므로 빈번하게 사용하는 데이터의 주소는 흩어져 있다. 따라서 캐시에 저장하는 데이터에는 데이터의 메모리 주소 등을 기록해 둔 태그를 달아놓을 필요가 있다. 이러한 태그들의 묶음을 캐싱 라인이라고 하고 메모리로부터 가져올 때도 캐싱 라인을 기준으로 가져온다.
종류로는 대표적으로 세 가지 방식이 존재한다.

1. Full Associative
2. Set Associative
3. Direct Map

## 프로세스와 스레드의 차이

- 프로그램(Program) 이란
  - 사전적 의미: 어떤 작업을 위해 실행할 수 있는 파일
- 프로세스(Process) 란
  - 사전적 의미: 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램
    - 메모리에 올라와 **실행되고 있는 프로그램의 인스턴스(독립적인 개체)**
    - 운영체제로부터 시스템 자원을 할당받는 작업의 단위
    - 즉, 동적인 개념으로는 실행된 프로그램을 의미한다.
  - 할당받는 시스템 자원의 예
    - CPU 시간
    - 운영되기 위해 필요한 주소 공간
    - Code, Data, Stack, Heap의 구조로 되어 있는 독립된 메모리 영역
  - 특징
    - <img src="./images/process.png" width="40%" height="40%">
    - 프로세스는 각각 독립된 메모리 영역(Code, Data, Stack, Heap의 구조)을 할당받는다.
    - 기본적으로 프로세스당 최소 1개의 스레드(메인 스레드)를 가지고 있다.
    - 각 프로세스는 별도의 주소 공간에서 실행되며, 한 프로세스는 다른 프로세스의 변수나 자료구조에 접근할 수 없다.
    - 한 프로세스가 다른 프로세스의 자원에 접근하려면 프로세스 간의 통신(IPC, inter-process communication)을 사용해야 한다. (Ex. 파이프, 파일, 소켓 등을 이용한 통신 방법 이용)
- 스레드(Thread) 란
  - 사전적 의미: 프로세스 내에서 실행되는 여러 흐름의 단위
    - **프로세스의 특정한 수행 경로**
    - 프로세스가 할당받은 자원을 이용하는 실행의 단위
  - 특징
    - <img src="./images/thread.png" width="40%" height="40%">
    - 스레드는 프로세스 내에서 각각 Stack만 따로 할당받고 Code, Data, Heap 영역은 공유한다.
    - 스레드는 한 프로세스 내에서 동작되는 여러 실행의 흐름으로, 프로세스 내의 주소 공간이나 자원들(힙 공간 등)을 같은 프로세스 내에 스레드끼리 공유하면서 실행된다.
    - 같은 프로세스 안에 있는 여러 스레드들은 같은 힙 공간을 공유한다. 반면에 프로세스는 다른 프로세스의 메모리에 직접 접근할 수 없다.
    - 각각의 스레드는 별도의 레지스터와 스택을 갖고 있지만, 힙 메모리는 서로 읽고 쓸 수 있다.
    - 한 스레드가 프로세스 자원을 변경하면, 다른 이웃 스레드(sibling thread)도 그 변경 결과를 즉시 볼 수 있다.
- 자바 스레드(Java Thread) 란
  - 일반 스레드와 거의 차이가 없으며, JVM가 운영체제의 역할을 한다.
  - 자바에는 프로세스가 존재하지 않고 스레드만 존재하며, 자바 스레드는 JVM에 의해 스케줄되는 실행 단위 코드 블록이다.
  - 자바에서 스레드 스케줄링은 전적으로 JVM에 의해 이루어진다.
  - 아래와 같은 스레드와 관련된 많은 정보들도 JVM이 관리한다.
    - 스레드가 몇 개 존재하는지
    - 스레드로 실행되는 프로그램 코드의 메모리 위치는 어디인지
    - 스레드의 상태는 무엇인지
    - 스레드 우선순위는 얼마인지
  - 즉, 개발자는 자바 스레드로 작동할 스레드 코드를 작성하고, 스레드 코드가 생명을 가지고 실행을 시작하도록 JVM에 요청하는 일 뿐이다.

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - [https://gmlwjd9405.github.io/2018/09/14/process-vs-thread.html](https://gmlwjd9405.github.io/2018/09/14/process-vs-thread.html)
> - [https://brunch.co.kr/@kd4/3](https://brunch.co.kr/@kd4/3)
> - [https://magi82.github.io/process-thread/](https://magi82.github.io/process-thread/)
> - [https://jaybdev.net/2017/06/05/Java-3/](https://jaybdev.net/2017/06/05/Java-3/)
> - [http://includestdio.tistory.com/6](http://includestdio.tistory.com/6)
> - [https://lalwr.blogspot.com/2016/02/process-thread.html](https://lalwr.blogspot.com/2016/02/process-thread.html)

### 멀티 프로세스 대신 멀티 스레드를 사용하는 이유

- 쉽게 설명하면, 프로그램을 여러 개 키는 것보다 하나의 프로그램 안에서 여러 작업을 해결하는 것이다.
  - <img src="./images/multi-thread.png" width="50%" height="50%">

1. 자원의 효율성 증대
   - 멀티 프로세스로 실행되는 작업을 멀티 스레드로 실행할 경우, **프로세스를 생성하여 자원을 할당하는 시스템 콜이 줄어들어** 자원을 효율적으로 관리할 수 있다.
     - 프로세스 간의 문맥교환시 단순히 CPU 레지스터 교체 뿐만 아니라 RAM과 CPU 사이의 캐시 메모리에 대한 데이터까지 초기화되므로 오버헤드가 크기 때문
   - 스레드는 프로세스 내의 메모리를 공유하기 때문에 독립적인 프로세스와 달리 스레드 간 데이터를 주고 받는 것이 간단해지고 시스템 자원 소모가 줄어들게 된다.
2. 처리 비용 감소 및 응답 시간 단축
   - 또한 프로세스 간의 통신(IPC)보다 스레드 간의 통신의 비용이 적으므로 작업들 간의 통신의 부담이 줄어든다.
     - 스레드는 Stack 영역을 제외한 모든 메모리를 공유하기 때문
   - 프로세스 간의 전환 속도보다 스레드 간의 전환 속도가 빠르다.
     - 문맥교환시 스레드는 Stack 영역만 처리하기 때문

- **_주의할 점!_**
  - **동기화 문제**
  - 스레드 간의 자원 공유는 전역 변수(데이터 세그먼트)를 이용하므로 함께 상용할 때 충돌이 발생할 수 있다.

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - [http://you9010.tistory.com/136](http://you9010.tistory.com/136)

### Thread-safe

- **Thread-safe란?**
  - 직역하면 **스레드 안전**.
  - 멀티스레드 환경에서 <u>여러 스레드</u>가 동시에 <u>하나의 객체 및 변수(공유 자원)</u>에 접근할 때, 의도한 대로 동작하는 것을 말한다.
  - 이러한 상황을 "Thead-safe하다" 라고 표현한다.
- **Thread-safe하게 구현하기**
  - Thread-safe하기 위해서는 공유 자원에 접근하는 임계영역(critical section)을 동기화 기법으로 제어해줘야 한다.
    - 이를 '상호배제'라고 한다.
  - 동기화 기법으로는 Mutex나 Semaphore 등이 있다.
- **Reentrant** - Reentrant는 **재진입성**이라는 의미로, 어떤 함수가 Reentrant하다는 것은 여러 스레드가 동시에 접근해도 언제나 같은 실행 결과를 보장한다는 의미이다. - 이를 만족하기 위해서 해당 서브루틴에서는 공유자원을 사용하지 않으면 된다. - 예를들어 정적(전역) 변수를 사용하거나 반환하면 안 되고 호출 시 제공된 매개변수만으로 동작해야한다. - 따라서, Reentrant하다면 Thread-safe하지만 그 역은 성립하지 않는다.
  > :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

> - [위키백과 - 재진입성](https://ko.wikipedia.org/wiki/%EC%9E%AC%EC%A7%84%EC%9E%85%EC%84%B1)
> - [[OS] Thread Safe란? - 곰팡](gompangs.tistory.com/7)
> - [스레드-안전(Thread-safe)과 재진입가능(Reentrant)의 차이 - 커피한잔의 여유와 코딩](sjava.net/tag/thread-safe/)

### 동기화 객체의 종류

- 스레드 동기화 방법
  1. 실행 순서의 동기화
     - 스레드의 실행순서를 정의하고, 이 순서에 반드시 따르도록 하는 것
  2. 메모리 접근에 대한 동기화
     - 메모리 접근에 있어서 동시접근을 막는 것
     - 실행의 순서가 중요한 상황이 아니고, 한 순간에 하나의 스레드만 접근하면 되는 상황을 의미
- 동기화 기법의 종류
  1. 유저 모드 동기화
     - 커널의 힘을 빌리지 않는(커널 코드가 실행되지 않는) 동기화 기법
     - 성능상 이점, 기능상의 제한
     - **Ex) 크리티컬 섹션 기반의 동기화, 인터락 함수 기반의 동기화**
  2. 커널 모드 동기화
     - 커널에서 제공하는 동기화 기능을 활용하는 방법
     - 커널 모드로의 변경이 필요하고 이는 성능 저하로 이어짐, 다양한 기능 활용 가능
     - **Ex) 뮤텍스 기반의 동기화, 세마포어 기반의 동기화, 이름있는 뮤텍스 기반의 프로세스 동기화, 이벤트 기반의 동기화**

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - [http://christin2.tistory.com/entry/Chapter-13-%EC%93%B0%EB%A0%88%EB%93%9C-%EB%8F%99%EA%B8%B0%ED%99%94-%EA%B8%B0%EB%B2%95-1](http://christin2.tistory.com/entry/Chapter-13-%EC%93%B0%EB%A0%88%EB%93%9C-%EB%8F%99%EA%B8%B0%ED%99%94-%EA%B8%B0%EB%B2%95-1)
> - [https://m.blog.naver.com/PostView.nhn?blogId=smuoon4680&logNo=50127179815&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=smuoon4680&logNo=50127179815&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)

### 뮤텍스와 세마포어의 차이

- 뮤텍스(Mutex)
  - 공유된 자원의 데이터를 **여러 스레드가** 접근하는 것을 막는 것
  - 상호배제라고도 하며, Critical Section을 가진 스레드의 Running time이 서로 겹치지 않도록 각각 단독으로 실행하게 하는 기술이다.
  - 다중 프로세스들의 공유 리소스에 대한 접근을 조율하기 위해 synchronized 또는 lock을 사용한다.
    - 즉, 뮤텍스 객체를 두 스레드가 동시에 사용할 수 없다.
- 세마포어(Semaphore)
  - 공유된 자원의 데이터를 **여러 프로세스가** 접근하는 것을 막는 것
  - 리소스 상태를 나타내는 간단한 카운터로 생각할 수 있다.
    - 운영체제 또는 커널의 한 지정된 저장장치 내의 값이다.
    - 일반적으로 비교적 긴 시간을 확보하는 리소스에 대해 이용한다.
    - 유닉스 시스템 프로그래밍에서 세마포어는 운영체제의 리소스를 경쟁적으로 사용하는 다중 프로세스에서 행동을 조정하거나 또는 동기화 시키는 기술이다.
  - 공유 리소스에 접근할 수 있는 프로세스의 최대 허용치만큼 동시에 사용자가 접근하여 사용할 수 있다.
  - 각 프로세스는 세마포어 값은 확인하고 변경할 수 있다.
    - 1. 사용 중이지 않는 자원의 경우 그 프로세스가 즉시 자원을 사용할 수 있다.
    - 2. 이미 다른 프로세스에 의해 사용 중이라는 사실을 알게 되면 재시도하기 전에 일정 시간을 기다려야 한다.
    - 세마포어를 사용하는 프로세스는 그 값을 확인하고, 자원을 사용하는 동안에는 그 값을 변경함으로써 다른 세마포어 사용자들이 기다리도록 해야한다.
  - 세마포어는 이진수 (0 또는 1)를 사용하거나, 또는 추가적인 값을 가질 수도 있다.
- 차이
  1. 가장 큰 차이점은 관리하는 **동기화 대상의 개수**
     - Mutex는 동기화 대상이 오직 하나뿐일 때, Semaphore는 동기화 대상이 하나 이상일 때 사용한다.
  2. Semaphore는 Mutex가 될 수 있지만 Mutex는 Semaphore가 될 수 없다.
     - Mutex는 상태가 0, 1 두 개 뿐인 binary Semaphore
  3. Semaphore는 소유할 수 없는 반면, Mutex는 소유가 가능하며 소유주가 이에 대한 책임을 가진다.
     - Mutex 의 경우 상태가 두개 뿐인 lock 이므로 lock 을 가질 수 있다.
  4. Mutex의 경우 Mutex를 소유하고 있는 스레드가 이 Mutex를 해제할 수 있다. 하지만 Semaphore의 경우 이러한 Semaphore를 소유하지 않는 스레드가 Semaphore를 해제할 수 있다.
  5. Semaphore는 시스템 범위에 걸쳐있고 파일시스템상의 파일 형태로 존재하는 반면 Mutex는 프로세스 범위를 가지며 프로세스가 종료될 때 자동으로 Clean up 된다.

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - [http://jwprogramming.tistory.com/13](http://jwprogramming.tistory.com/13)

### 스케줄러

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 동기와 비동기

이 개념은 OS에서 뿐만 아니라 여러가지 분야에서도 쓰인다.

- **동기(Synchronous)란?**
  > '동기' 라고하면 다수의 개채들이 동일(일정)한 **무언가**를 가지는 것. 또는 **무언가**가 동일(일정)하게 되는 것.
  - 그 **무언가**는 `상태`가 될 수 있고 `행위`가 될 수 있고, `시간`,`속도`, `주기`, `출현` 등이 될 수 있다.
  - 여기서 말하는 '동기'는 두개의 프로세스가 데이터를 주고 받을 때, 주고 받는 `순서`(또는 `시간`)가 일정하다는 것을 뜻한다. (너 한번, 나 한번)
- **비동기(Asynchronous)란?**
  - '동기'가 아닌 것.
- **동기식, 동기적이다.**
  - 어떤 작업을 요청했을 때 그 작업이 종료될 때까지 기다린 후 다음 작업을 수행한다.
    - 데이터를 주고받는 '순서'가 중요할때 사용된다.
    - 요청한 작업만 처리하면 되기 때문에 전체적인 수행 속도는 빠를 수 있다. (일만 하면 된다)
    - 한 작업에 대한 시간이 길어질 경우, 전체 응답이 지연될 수 있다.
- **비동기식, 비동기적이다.**
  - 어떤 작업을 요청했을 때 그 작업이 종료될 때까지 기다리지 않고(작업을 위임하고), 다음 작업을 수행한다. 요청했던 작업이 끝나면 결과를 받고, 그에 따른 추가 작업이 있다면 수행한다.
    - 요청 순서에 상관없이, 동시에 다수의 작업을 처리할 수 있다.
    - 작업이 끝날 때 따로 이벤트를 감지하고 결과를 받아 그에 따른 추가 작업을 해줘야하기 때문에, 비교적 느릴 수 있다.
    - I/O 작업이 잦고, 빠른 응답속도를 요구하는 프로그램에 적합하다.

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - [동기(Sync) 와 비동기(Async) - 리충닷컴](http://leechoong.com/posts/2017/nodejs_syncasync/)
> - [Sync async-blocking-nonblocking-io - Choloh Bae](https://www.slideshare.net/unitimes/sync-asyncblockingnonblockingio)
> - [Synchronous(동기) Vs Asynchronous(비동기) - Nesoy Bolg](https://nesoy.github.io/articles/2017-01/Synchronized)

### 프로세스 동기화

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 메모리 관리 전략

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 가상 메모리

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 캐시의 지역성

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 교착상태의 개념과 조건

- 교착상태(데드락, Deadlock) 란
  - 첫 번째 스레드는 두 번째 스레드가 들고 있는 객체의 락이 풀리기를 기다리고 있고, 두 번째 스레드 역시 첫 번째 스레드가 들고 있는 객체의 락이 풀리기를 기다리는 상황을 일컷는다.
  - 모든 스레드가 락이 풀리기를 기다리고 있기 때문에, 무한 대기 상태에 빠지게 된다. 이런 스레드를 교착상태에 빠졌다고 한다.
- 교착상태의 4가지 조건
  1. 상호 배제(mutual exclusion)
     - 한 번에 한 프로세스만 공유 자원을 사용할 수 있다.
     - 좀 더 정확하게는, 공유 자원에 대한 접근 권한이 제한된다. 자원의 양이 제한되어 있더라도 교착상태는 발생할 수 있다.
  2. 들고 기다리기(hold and wait) = **점유대기**
     - 공유 자원에 대한 접근 권한을 갖고 있는 프로세스가, 그 접근 권한을 양보하지 않은 상태에서 다른 자원에 대한 접근 권한을 요구할 수 있다.
  3. 선취(preemption) 불가능 = **비선점**
     - 한 프로세스가 다른 프로세스의 자원 접근 권한을 강제로 취소할 수 없다.
  4. 대기 상태의 사이클(circular wait) = **순환대기**
     - 두 개 이상의 프로세스가 자원 접근을 기다리는데, 그 관계에 사이클이 존재한다.
- 교착상태 방지
  - 4가지 조건들 가운데 하나를 제거하면 된다.
  - 공유 자원 중 많은 경우가 한 번에 한 프로세스만 사용할 수 있기 때문에(예를 들어, 프린트) 1번 조건은 제거하기 어렵다.
  - 대부분의 교착상태 방지 알고리즘은 4번 조건, 즉 대기 상태의 사이클이 발생하는 일을 막는 데 초점이 맞춰져 있다.

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - [코딩 인터뷰 완전 분석, 프로그래밍인사이트](https://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788966263080&OV_REFFER=http://click.linkprice.com/click.php?m=kbbook&a=A100532541&l=9999&l_cd1=0&u_id=jm0gctc7ca029ofs02yqe&l_cd2=0&tu=https%3A%2F%2Fwww.kyobobook.co.kr%2Fproduct%2FdetailViewKor.laf%3FmallGb%3DKOR%26ejkGb%3DKOR%26barcode%3D9788966263080)

### 사용자 수준 스레드와 커널 수준 스레드

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 외부 단편화와 내부 단편화

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
>
> - []()

### 문맥교환

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

- 문맥교환이란?
  - 현재 진행하고 있는 Task(Process, Thread)의 상태를 저장하고 다음 진행할 Task의 상태 값을 읽어 적용하는 과정을 말한다.
- 문맥교환 과정
  1. Task의 대부분 정보는 Register에 저장되고 PCB(Process Control Block)로 관리된다.
  2. 현재 실행하고 있는 Task의 PCB 정보를 저장한다. (Process Stack, Ready Queue)
  3. 다음 실행할 Task의 PCB 정보를 읽어 Register에 적재하고 CPU가 이전에 진행했던 과정을 연속적으로 수행할 수 있다.
- 문맥교환 Cost (Process vs Thread)
  - Process 문맥교환 비용 > Thread 문맥교환 비용
  - Thread는 Stack 영역을 제외한 모든 메모리를 공유하므로 문맥교환 수행 시 Stack 영역만 변경하면 되기 때문에 비용이 적게 든다.

> - [문맥교환이란?](https://nesoy.github.io/articles/2018-11/Context-Switching)

### Swapping

> :arrow_double_up:[Top](#3-operating-system) :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#3-operating-system) :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
