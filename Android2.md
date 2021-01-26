# Android

- [Android](#android)
  - [CustomView](#customview)
  - [Activity](#activity)
    - [Activity Life Cycle](#activity-life-cycle)
  - [Fragment](#fragment)
  - [BroadcastReceiver](#broadcastreceiver)
  - [ContentProvider](#contentprovider)
  - [Service](#service)
  - [Intent](#intent)
  - [Lambda function / High order function](#lambda-function--high-order-function)
  - [RESTful API](#restful-api)
  - [List / RecyclerView](#list--recyclerview)
  - [로컬데이터베이스 (SQLite, Realm, Room)](#로컬데이터베이스-sqlite-realm-room)
  - [애니메이션](#애니메이션)
  - [하단 메뉴](#하단-메뉴)
  - [HTTP API (Retrofit / OKHttp3)](#http-api-retrofit--okhttp3)
  - [Image (Picasso / Glide)](#image-picasso--glide)
  - [HTTP API (Retrofit / OKHttp3)](#http-api-retrofit--okhttp3-1)
  - [Image (Picasso / Glide)](#image-picasso--glide-1)
  - [Cache](#cache)
  - [Thread / Handler / Looper](#thread--handler--looper)
  - [Handler](#handler)
  - [Looper](#looper)
  - [AsyncTask](#asynctask)
  - [Manifest 매니페스트](#manifest-매니페스트)
  - [반응형 프로그래밍 / RxJava](#반응형-프로그래밍--rxjava)
  - [Task](#task)
  - [안드로이드의 메모리 구조](#안드로이드의-메모리-구조)
  - [FCM](#fcm)
  - [쓰레드간 통신방법에 대해 설명해보세요.](#쓰레드간-통신방법에-대해-설명해보세요)
  - [액티비티간 통신 방법](#액티비티간-통신-방법)
  - [안드로이드에서 Garbage Collector](#안드로이드에서-garbage-collector)
  - [DI (Dagger2)](#di-dagger2)
  - [Jetpack (Feat. AAC)](#jetpack-feat-aac)
  - [JAVA](#java)
  - [Callback](#callback)
  - [Listener](#listener)
  - [Observer](#observer)
  - [Kotlin](#kotlin)
  - [others](#others)

## CustomView

기존에 있는 View (ImageView, TextView 등) 으로 표현할 수 없는 모양의 View를 구현해야 할때 필요하다. View를 상속받는 자손 클래스를 만들어서 구현한다.
구현 방법:
기존 View 상속
onDraw(), onMeasure(), onKeyDown()과 같이 시작하는 키워드가 ‘on’인 수퍼 클래스 메서드를 오버라이드
onDraw()

- 뷰를 실제로 그릴때 사용
- Canvas 객체를 매개변수로 받음
  Canvas 객체는 어떤 도형을 그릴지 설정
  Paint 객체는 도형의 색, 스타일, 글꼴 등을 설정
  protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec)
- 뷰의 크기 설정할때 사용
  예를 들어, 직사각형 모양에 코너가 둥근 이미지뷰를 만들고 싶다면, 먼저 ImageView를 상속받는 CustomImageView를 만들고, onMeasure에서 width의 길이를 잰뒤 height의 길이를 width의 길이와 똑같이 맞춘 뒤, onDraw에서 코너부분을 둥글게 자르는 식으로 구현한다. (Canvas.drawRoundRect)
  같은 형태의 뷰를 여러번 사용할때도 사용할수 있음 (재사용성)

## Activity

화면에 UI를 표시하는 기본요소. 대부분의 경우 액티비티는 꽉찬 화면을 구성하지만, 예외적으로 floating windows, multi-window mode 처럼 화면의 일부를 차지하게 할수 있다.

Acitivty 의 종류 중 하나로 FragmentActivity가 있는데, 이는 nested fragment, 즉 fragment 안에 다른 fragment가 있는 경우 고려할만 하다.

AppCompatActivity는 안드로이드 하위버전의 안드로이드를 지원하기 위해 사용된다. 참고로 AppCompatActivity는 FragmentActivity를 상속한다.

### Activity Life Cycle

액티비티의 상태는 크게 3가지로 나눌수 있다.

재개 (create, start, resume)
일시정지 (pause)
멈춤 (stop, destroy)
액티비티에는 각각의 상태에 따른 콜백 메소드들이 존재하는데 일반적으로 순서는

- onCreate (액티비티 생성 직전)
- onRestart (액티비티가 stop상태에서 재시작될 경우)
- onStart (액티비티가 화면에 보여지기 직전)
- onResumed (액티비티가 사용자와 상호작용하기 직전)
- onPause (액티비티가 부분적으로 가려짐)
- onStopped (액티비티가 더 이상 보이지 않을때)
- onDestroy (액티비티가 소멸되기 직전)

여기서 주목할 점은 사용자가 홈버튼을 누르거나 다른 액티비티가 화면을 차지했을 때 onPause -> onStop 상태가 되는데, 이때 액티비티의 상태는 메모리에 보관되게 되며, 기기의 RAM 메모리가 부족하게 되면 시스템의 판단에 따라 액티비티는 destory 된다.

또, 안드로이드에서는 액티비티의 configuration이 바뀌면 (화면 회전이나 멀티 윈도우 모드로 전환 같은 경우) 액티비티가 완전히 소멸 (detroy) 된후 재시작되게 되는데, 이때 액티비티의 상태를 보존하기 위해 사용되는게 onSaveInstanceState, onRestoreInstanceState, onCreate(bundle) 이다.

## Fragment

프래그먼트는 액티비티의 부분부분을 동적으로 동작시키기 위해 생긴 개념이다. 쉽게 비유를 들어 설명하자면, 앱하나를 서랍이라고 하고 액티비티를 서랍의 한칸이라고 하면, 프래그먼트는 서랍안의 부분부분을 나눠서 정리하는 정리함의 한 칸이라고 생각하면 된다.

프래그먼트를 사용하는 대표적인 예로 탭레이아웃이 있는데, 탭을 눌러서 다른화면으로 전환하는 앱의 경우이다. 이때 한 액티비티안에서 탭을 눌렀을대 보여지는 프래그먼트만 바꾸게 되는데, 프래그먼트는 액티비티와 달리 스택에 쌓이지 않기 때문에 백버튼을 누른다고 해서 이전 프래그먼트로 돌아가지 않는다. 만약 어떤 이유로 프래그먼트를 스택에 넣고 싶다면 개발자가 직접 backStack에 추가해주는 방법도 있다.

프래그먼트의 라이프사이클은 액티비티와 거의 동일한데, onAttach, onCreateView, onDestroyView, onDetach라는 콜백이 추가된다. onCreateView에서 프래그먼트에 맞는 UI Layout을 리턴한다.

## BroadcastReceiver

안드로이드의 구성요소 중 하나로 원하는 메시지를 보내거나 받을 수 있는 컴포넌트이다. 예를 들면, 충전기를 꼽았다던지, SMS문자메시지, 전화가온다거나 하는 일에 대한 메세지를 받을 수 있다. sendBroadCast() 라는 메소드를 통해 메세지를 보내면 리시버에서 메세지를 받을 수 있다.

BroadCastReceiver를 등록하는 방법은 크게 두가지가 있다. 첫번째로 정적으로 등록하는 방법인데, AndroidManifest 파일에 리시버라는 태그를 이용해서 추가하는 방법이다. 이 방법을 사용하면 앱이 실행중이지 않을때도 메세지를 받을 수 있다.

두번째 방법으로 동적 등록은 액티비티의 Context를 통해 등록한다. Context의 registerReceiver() 메소드를 통해 등록할 수 있는데, 이렇게 등록하게 되면 액티비티가 destroy되기 전까지만 메세지를 받을 수 있다. unRegisterReceiver()를 통해 리시버가 더 이상 필요하지 않을때 해제시킬 수 있다.

메세지를 보내는 방법
sendOrderBroadcast() 는 한번에 한 수신자에게만 메세지를 전달한다. BroadcastReceiver를 따라 전파됨에 따라 다음 수신자에게 계속 메세지를 전달할수도, 또는 차단할수도 있다.
sendBroadcast()는 모든 수신자에게 메세지를 전파한다.
LocalBroadcastManager.sendBroadcast() 의 경우 송신자 내부 프로세스에서만 메세지를 전달한다. 해당 Broadcast message 를 앱 내부에서만 사용한다면 해당 메서드를 사용하는것이 효율적이다. 프로세스간 통신이 불필요하며 속도 및 보안적으로도 훨씬 더 유리한 방법이다.

매개변수로 action이 추가된 Intent를 보내줘야함.
예) intent.setAction("com.example.test");
sendBroadcast(intent);
소스: https://medium.com/@eevee300/android-broadcast-receiver-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-84d3ce07db88

메시지 받는 방법
onRecieveMessage(Context, Intent) 를 사용한다. 메니페스트에 등록한 경우에는 BroadCastReceiver를 상속하는 클래스를 만들고, 액티비티 컨텍스트를 통해 등록한 경우에는 액티비티 내부에서 브로드캐스트리시버의 익명 클래스를 만들면 된다.

참고로 BroadcastReceiver은 추상클래스로 그 중 추상 메소드는 onReceive() 메소드 하나이다.

## ContentProvider

앱간의 데이터 교환을 위해 다른 앱에게 데이터를 제공하고 데이터를 가져올 수 있게 하는 구성요소이다. 실제로 앱의 데이터베이스는 해당 앱만 접근 가능하기 때문에 다른 앱의 데이터를 가져오기 위해서는 ContentProvider를 사용해야 한다.

추가: CalenderProvider ContactsProvider

## Service

백그라운드에서 오래 실행되는 작업을 할때 사용되는 구성요소이다. 다른 애플리케이션 구성요소가 서비스를 실행할 수 있고, 서비스는 다른 애플리케이션으로 전환되더라도 계속 실행된다.

서비스는 포그라운드, 백그라운드, 바인드 서비스가 있다.

포그라운드 서비스는 사용자에게 보이는 서비스를 제공하고 알림을 표시해야 한다.
백그라운드 서비스는 사용자에게 보이지 않는 작업을 수행한다. 예를 들어 앱이 저장소를 압축하는데 서비스를 사용하였다면, 이는 대개 백그라운드 서비스이다.
바인드 서비스는 다른 앱 구성요소가 bindService() 메소드를 호출하여 구성요소가 서비스에 바인딩되는 경우이다. 바인딩된 서비스는 해당 구성요소와 서로 상호작용할 수 있고, 하나의 서비스가 여러개의 구성요소와 바인딩되는 경우도 가능하다. 이때 모든 바인딩된 구성요소에서 바인딩이 해제되면 서비스는 소멸한다.
서비스와 쓰레드
서비스는 쓰레드가 아니라 단순히 백그라운드에서 실행 될수 있는 구성요소이고 기본적으로 메인쓰레드에서 실행된다. 만약 서비스가 집약적이거나 메인쓰레드와 별도로 작업을 수행해야 한다면, 서비스 안에서 새로운 쓰레드를 만들어서 작업해야 한다.

안드로이드8 이후의 서비스와 브로드캐스트리시버
안드로이드8 이후 사용자와의 상호작용과 별개로 백그라운드에서 수행되는 메니페스트로 등록된 브로드캐스트리시버와 서비스에 대한 제한이 강화 되었다.

브로드캐스트 리시버의 경우 예전에는 시스템으로 부터 충전기가 연결되었다던지 하는 메세지를 받게 되면 저장소 정리를 한다던지 하는 식으로 많이 이용됬었는데, 이런 식으로 백그라운드에 등록되는 앱이 많아지게 되면 시스템에 과부하가 걸릴 수 있어서, 안드로이드8 이후로 암시적 브로드캐스트에 대한 리시버의 등록을 제한시켰다. 암시적 브로드캐스트란 특정 앱을 대상으로 하지 않는 브로드캐스트이다.

백그라운드 서비스는 우선순위가 높은 메세지만 받을수 있게 되며, sms/mms와 같은 메세지는 받을 수 있다. 또한, 알림에서 PendingIntent를 수행하는 일 또한 가능하다.

구글에서는 이러한 제한 사항으로 못하게 된 작업들을 JobScheduler를 통해 수행하길 권장한다.

## Intent

인텐트는 구성요소를 실행시키고 구성 요소 간 데이터 전달을 하는데에 사용된다. 데이터는 putExtra()를 통해 담을 수 있고, 전달 받은 데이터를 getExtra() 를 통해 받을 수 있다.

PendingIntent
펜딩 인텐트는 이름에서 볼수 있듯이 보류된 인텐트로, 당장 해당 작업을 다른 컴포넌트에 요청하는게 아닌 특정시점에 자신이 아닌 컴포넌트가 다른 컴포넌트에게 펜딩 인텐트를 사용하여 작업을 요청한다는 특징이 있다.

대표적으로, 사용자가 Notification을 클릭했을 때 특정한 작업을 수행시키거나, 위젯을 통해 앱을 실행시키거나, 미래의 특정 시점에 실행되는 인텐트를 선언하는 경우에 펜딩 인텐트를 사용한다.

펜딩인텐트의 인스턴스를 생성하는 방법은 크게 네가지가 있다.

getActivity(Context, int, Intent, int)
매개변수에 포함된 Intent를 통해 한가지 액티비티를 실행시킬때 사용
getActivities(Context, int, Intent[], int)
매개변수에 포함된 Intent배열을 통해 여러개의 액티비티를 실행시킬때 사용. 이때 Context.startActivities와 똑같이 작동한다. startActivities는 거의 사용되지 않지만 액티비티들을 백스택에 넣고 싶을때 사용되기 때문에 실행된 액티비티에서 백버튼을 눌렀을때 다른 액티비티로 이동하고 싶다면 사용한다.
getBroadcast(Context, int, Intent, int)
context.sendBroadCast(intent)를 하고 싶을때 사용
getService(Context, int, Intent, int)
Intent를 통해 context.startService(intent)를 하고 싶을때 사용

## Lambda function / High order function

## RESTful API

## List / RecyclerView

## 로컬데이터베이스 (SQLite, Realm, Room)

## 애니메이션

## 하단 메뉴

## HTTP API (Retrofit / OKHttp3)

## Image (Picasso / Glide)

ㅣ## 하단 메뉴

## HTTP API (Retrofit / OKHttp3)

## Image (Picasso / Glide)

ㅣURL에서 이미지 다운로드 받아와서 ImageView에 적용하는 라이브러리

## Cache

## Thread / Handler / Looper

안드로이드는 기본적으로 하나의 메인 쓰레드로 작동한다. UI 조작은 메인 쓰레드만 할 수 있는데, 그 이유는 두개 이상의 쓰레드가 UI에 동시에 접근했을때 의도와 다르게 동작할 가능성이 크기 때문이다. 참고로 메인쓰레드에 너무 오래 걸리는 작업을 담당해서 긴 시간동안 응답할 수 없을때 안드로이드에서 ANR (애플리케이션 응답 없음) 오류를 트리거 시킨다.

이같이 멀티 쓰레드 환경에서 동기화 이슈를 차단하고 쓰레드간의 통신을 위해서 사용되는 것이 핸들러와 루퍼이다. 핸들러는 이름에서 알 수 있듯이 받은 메세지를 처리하고, 쓰레드 간의 메세지를 전달하는 작업을 수행한다.택 루퍼는 계속해서 같은 작업을 수행한다고 해서 루퍼(Looper)라고 부르는데, MessageQueue에서 차례대로 메세지나 Runnable 객체를 꺼내서 핸들러에게 전달한다.

## Handler

핸들러를 생성하면 기본적으로 핸들러를 생성한 쓰레드와 루퍼에 연결된다. 예를 들어, 메인 쓰레드에서 핸들러A를 생성한 뒤 쓰레드B에서 핸들러A.sendMessage(Message) 혹은 핸들러A.post(Runnable) 을 호출하면 메인쓰레드의 MessageQueue에 해당 메세지와 러너블을 추가하게 된다. 핸들러에는 postDelayed라던지 postAtFrontOfQueue와 같이 메세지의 순서나 보내는 시간을 조작하는 함수를 가지고 있어서 스케쥴링을 할 수 있다는 장점이 있다.

## Looper

루퍼는 run() 메소드 내부에 Looper.prepare()을 통해 MessageQueue를 생성하고 Looper.loop()을 통해 메세지 전달을 기다린다. Looper는 quit() 또는 quitSafely()를 통해 종료시킬 수 있는데, quitSafely()는 MessageQueue에 쌓여있는 작업을 모두 완료한 후에 종료된다.

HandlerThread는 기본적으로 내부에 루퍼를 가지고 있는 쓰레드이다.

## AsyncTask

AsyncTask는 백그라운드에서 작업을 수행한 뒤 그 결과를 UI Thread에서 갱신할때 주로 사용된다. 최대 몇초간의 짧은 작업에 사용하는게 가장 적절하다. AsynkTask는 순차적으로 실행되는데, 만약 병렬적으로 실행하고 싶다면 myTask.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR); 처럼 사용할 수 있다.

단점

1. 액티비티 종료시 따로 명시해주지 않으면 메모리에 계속 남아 있어 Memory leak이 발생할 수 있다.
2. 오직 한번만 실행되고 재사용이 불가능하다.
3. 기본적으로 처리작업의 수가 1개이다.
4. Configuration 변경이 일어났을때 크래시가 일어날 수 있다. (단점 1번 때문에..?)

이런 이유때문인지 Api R (Android 11)부터는 deprecated 된다. 구글에서는 대안으로 java.util.concurrent API나 Kotlin coroutine을 사용하길 권장하고 있으며 RXJava 또한 합리적인 대안이라고 한다.

## Manifest 매니페스트

애플리케이션에 관한 정보를 입력하는 파일로 xml형태로 저장된다. < Manifest >, < Application >, < Activity > 등의 태그를 포함할 수 있고, 패키지 이름, 앱 이름, 앱 설명, 아이콘, 앱이나 구성요소에서 필요한 권한, 앱에서 사용되는 액티비티, 서비스, 브로드캐스트에 대한 정보 등 전반적인 앱에 대한 정보를 저장한다.

## 반응형 프로그래밍 / RxJava

리액티브 프로그래밍은 데이터 흐름(data flows)과 변화 전파에 중점을 둔 프로그래밍 패러다임(programming paradigm)이다.
이것은 프로그래밍 언어로 정적 또는 동적인 데이터 흐름을 쉽게 표현할 수 있어야하며, 데이터 흐름을 통해 하부 실행 모델이 자동으로 변화를 전파할 수 있는 것을 의미한다.

쉽게 말해서 데이터 흐름의 변화를 하부 실행 모델이 감지하며 이를 전파하는 과정을 수행하는 프로그래밍 언어 혹은 기법을 반응형 프로그래밍이라고 한다.

반응형 프로그래밍은 크게 3가지 핵심포인트로 나뉜다.

Observable
Observable은 데이터 흐름을 얘기한다. 주기적으로 데이터를 처리하고 변화를 방출하며 데이터 흐름을 다른 구성요소에게 전달한다.

Observer
Observer은 Observable이 방출한 데이터를 받아서 데이터 흐름의 변화를 관찰한다. Observable이 방출한 데이터를 메인 쓰레드나 UI에 전달하는 역할을 주로 한다.

주요 메소드

onComplete()
Observable이 더 이상 방출할 데이터가 없을때 호출된다.

onError(Throwable e)
Error 발생시 호출된다.

onNext(Object o)
새로운 데이터가 방출될때 호출된다. 이때 방출된 데이터는 매개 변수에서 찾을 수 있다.

Schedulers
Rx의 핵심은 비동기 처리에 있다. Schedulers는 Observable과 Observer가 어떤 쓰레드에서 작업을 수행할지 지정해준다.

주요 메소드

subscribeOn(Thread)
Observable이 실행되야 하는 쓰레드를 지정한다.
observeOn(Thread)
Observer가 실행되야 하는 쓰레드를 지정한다.
RxJava와 RxJava는 몇몇 미리 정의된 Scheduler를 제공한다. 예를 들어, Schedulers.IO()는 IO Thread를, AndroidSchedulers.MainThread()는 메인 스레드를 리턴한다.

## Task

Collection of activities. Activities are stored in back stack, and when another task takes place, or if the user presses home button, then the task remains in the background and it keeps its backstack in it.

## 안드로이드의 메모리 구조

안드로이드의 메모리구조를 보면 램, 내장메모리, 외장메모리로 구분됩니다.

렘 : 프로그램이 실행될때 상주되는 공간입니다. 평상시에 하드에 저장되어있다가 런타임시에 차지되는 공간을 말합니다.

내장메모리 : 간단하게 하드디스크라고 생각해도 됩니다.

외장메모리 : 메모리가 더 필요할때 추가 할 수 있는 메모리입니다.

## FCM

본연의 서버의 기능을 수행하면서 또 하나의 복잡한 알림 기능까지 포함한다면 서버의 속도는 처리량이 많아 느려질 것이다. 따라서 이러한 해결책으로 알림의 기능은 다른 서버가 제공을 해주고 본 서버는 알림기능을 제공하는 서버에 알림이 있는지 요청을 해서 정보를 가져오는 구조이다.

FCM의 동작을 위해서 HTTP나 XMPP로 FCM과 통신하는 서버와 클라이언트 앱이 필요합니다.

동작 순서

디바이스에 앱이 설치된후 최초 실행되면서 고유 식별자인 디바이스 토큰이 발급된다. 이 토큰을 앱 서버에 등록한다.

앱 서버에서 FCM 연결 서버로 푸시 알림을 요청한다. 이때 준비물은 디바이스 토큰과 API 서버 키이다.

FCM 연결 서버는 토큰을 대상으로 알림 메시지를 푸시한다.

출처: https://jw910911.tistory.com/18

FirebaseMessagingService : FCM 관련 작업 수행을 돕는 base class. 해당 클래스를 상속하는 서비스 클래스를 만든 뒤 메니페스트 파일에 등록시켜야 한다.

onNewToken() : 앱 최초실행시 혹은 새 토큰이 생성 됐을때 실행된다. 이때 받은 토큰은 서버에 등록 시킨다.

onMessageReceived() : 메세지 받았을때 사용되는 콜백 메소드.

개인적으로 개발했을 때는 앱 특성상 한개의 계정으로 여러개의 디바이스에서 로그인을 가능하게 해주고 싶어서 User와 FCMDeviceToken간의 관계를 one to many 관계로 설정해줬었다.

## 쓰레드간 통신방법에 대해 설명해보세요.

Java IO에서 제공하는 파이프를 이용한 방법
쓰레드간의 공유메모리를 통한 접근
(인스턴스 맴버변수,클래스멤버변수)
synchronized를 이용한 시그널링
BlockingQueue를 이용한 방법
안드로이드 스레드 통신 메커니즘을 알기 위해서는 android.os 패키지 안의 다음 사항을 알아야 한다.

핸들러 - 루퍼 - 메시지 큐 - 메시지
android.os.Looper : UI 스레드에 하나가 존재하며 소비자 스레드와 연관된 메시지 발송자 (데이터를 읽는 역활)
(소비자 => 데이터를 읽는다)

android.os.Handler : 큐에 메시지를 삽입하는 생산자 스레드를 위한 인터페이스와 소비자 스레드 메시지 처리, 하나의 Looper 객체는 많은 핸들러를 갖지만 모두 같은 큐에 삽입
android.os.MessageQueue : 소비자 스레드에서 처리할 메시지들이 담긴 무제한의 연결 리스트. 모든 루퍼와 스레드는 최대 하나의 메시지 큐를 가진다.
android.os.Message : 소비자 스레드에서 실행하는 메시지

Intent Flag - FLAG_ACTIVITY_CLEAR_TOP, FLAG_ACTIVITY_SINGLE_TOP에 대해 설명

FLAG_ACTIVITY_SINGLE_TOP => 동일한 액티비티가 연속적으로 호출될경우 1개로 취급

FLAG_ACTIVITY_CLEAR_TOP => 동일한 액티비티가 쌓일경우 rootActivity만 남기고 제거

출처: https://jw910911.tistory.com/18

## 액티비티간 통신 방법

intent, broadcast receiver

## 안드로이드에서 Garbage Collector

CMS 알고리즘을 사용한다고 한다.

Register based VM vs Stack based VM
구글에서 JVM이 아닌 DVM을 선택한데에는 라이센스 문제와 더불어 안드로이드 특성상 컴퓨터보다 메모리 공간이 적다는 이유가 있다. 간단하게 아래 표로 비교.

Register Based VM Stack Based VM
예 DVM JVM
장점 1.빠르다 2.메모리가 적게든다 3. operand의 주소값을 사용하기 때문에 계산한 값을 저장해두었다가 재사용이 가능하다 스택에서 다음 operand를 pop하기만 하면 되기 때문에 operand의 주소값을 알 필요가 없다
단점 operand의 주소값을 포함해야 되기 때문에 instruction이 길다 스택을 pop/push 하는 과정에서 오버헤드가 생길 수 있다
안드로이드 가상머신
안드로이드는 JVM이 아닌 DVM(Dalvik Virtual Machine) 혹은 ART (Android Runtime)에서 실행된다. DVM은 안드로이드가 처음 나왔을때 구글에서 개발한 가상머신인데, Java byte code를 Dex byte code로 변환하는 과정을 추가로 거쳐서 실행된다.

Dalvik은 JIT 컴파일러를 사용하는데, 기존 Java 컴파일러가 바이트 코드로 컴파일한 내용을 런타임 시점에 기계어로 해석하면서 생기는 성능 저하를 개선하기 위해 나온 컴파일러이다. JIT은 런타임시에 특정횟수 이상 반복 호출되는 코드에 대해 추가로 기계어로 컴파일하여 캐싱하고, 이를 통해 불필요한 바이트 코드 해석을 배제하여 실행속도를 향상 시킨다.

하지만 안드로이드에서 바이트 코드 해석이 가장 빈번하게 일어나는 시점이 앱을 실행할때와 화면을 전환할때인데, 이런 동작은 굉장히 빈번하게 일어나기 때문에 배터리 소모량이 크고 캐싱으로 인한 RAM 점유율도 높은편이였다. 거기에 UI의 부드러움 또한 기대하기 어려웠다는 단점이 있다.

이에 대한 해결책으로 나온게 ART이다. ART는 AOT 컴파일러를 사용하는데 AOT는 설치시점에 모든 바이트 코드를 기계어로 해석한후 저장한다. 결국 런타임시점에는 네이티브 언어로 작성된 결과물과 같은 퍼포먼스를 기대할수 있고 바이트 코드의 장점인 플랫폼 종속성이 없다는 점 또한 유지할수 있었다. 단점으로는 설치시간이 길고 저장공간을 많이 차지한다는 단점이 있다.

## DI (Dagger2)

의존성 주입 (Depenedency Injection) 프로그램 내 객체간의 의존관계를 내부가 아닌 외부에서 정의하는 디자인 패턴이다.

DI의 장점

코드가 유연해짐, 클래스간의 결합도를 줄임.
리팩토링이 수월함
유닛테스트를 더 쉽게 수행 할 수 있음
코드의 재사용성 증대
보일러 플레이트 코드 감소
스코프를 이용한 객체 관리
반면 단점도 있는데, 의존성 주입을 위한 선행작업이 필요하고 코드를 추적하고 읽기가 어려워집니다.
Dagger2는 안드로이드 개발에서 의존성 주입을 위해 가장 많이 사용하는 라이브러리이다. Dagger2의 특징은 대부분의 DI 라이브러리가 Reflection을 이용해서 동적으로 동작하는데 반해 Compile 시점에서 의존성 관계 그래프를 적용해서 정적으로 동작한다는 점이다. 정적으로 구현되었기 때문에 실제로 런타임시에 다른 라이브러리에 비해 훨씬 빠르다고 한다.

@Module
의존성 주입에 필요한 객체를 @Provide가 붙은 메소드를 통해 관리한다.

@Inject
생성자, 변수, 메소드 앞에 붙혀서 컴포넌트로부터 객체를 주입받는다.

@Component
Interface 혹은 abstract class 앞에 붙히며, 내부에 선언된 Provision method와 Member-injection method를 통해 의존성 주입에 도움을 주는 컴포넌트 클래스를 Dagger2에서 작성할 수 있도록 돕는다.

Provision method
매개변수가 없고, 모듈이 제공하는 객체의 타입을 반환형으로 갖는다. 생성된 컴포넌트 클래스에서 이 메소드를 통해 객체를 얻는다.
예) Object makeObject();

Member-injection method
의존성을 제공할 객체를 매개변수 안의 타겟 클래스로 넘긴다. 멤버 인젝션 메소드 호출시, 타겟 클래스 내부에 @Inject로 선언된 멤버들에 의존성이 주입된다.
예) inject(Activity targetActivity)

@Component.Builder
컴포넌트를 생성하기 위한 Builder를 선언하는 어노테이션이다.

```java
@Component(modules = AModule.class)
public interface MyComponent {
@Component.Builder
interface Builder{
MyComponent build();
 Builder aModule(AModule module);
}
}
```

Builder는 반드시 Component를 반환하는 메소드와 Builder를 반환하면서 컴포넌트가 필요로 하는 모듈을 파라미터로 받는 메소드를 가지고 있어야합니다. 이 조건을 충족하지 못하면 컴파일 타임에 에러가 발생합니다.

출처: https://www.charlezz.com/?p=1259

## Jetpack (Feat. AAC)

- ViewModel (AAC)
- Room (AAC)
- LiveData (AAC)
- setValue() -> UI Thread에서 실행
- postValue() -> background thread에서 실행
- postValue()와 setValue()가 동시에 실행되는 경우 postValue()가 더 늦게 호출되어 postValue()의 값이 최신데이터로 반영될수 있음
- LifeCycle (AAC)
- Databinding (AAC)
- Paging (AAC)
- Navigation (AAC)
- WorkManager (AAC)
- CameraX
- Permissions
- Notifications
- Slices
- Animations & Transitions
- Viewpager2
- Webview

## JAVA

null
매번 null 체크하기 너무 불편하다..
기본 자료형은 null이 안됨
JAVA8 에서 Optional을 통해 이를 개선하려함
그래도 Kotlin한테는 안되지..
Kotlin의 nullable은 훨씬 간결하고 compile 시점에서 오류를 잡을 수 있는 반면, optional은 런타임 익셉션이 발생한다. 그리고 optional이라는 별도의 객체를 생성하기 때문에 런타임시 오버헤드가 발생한다.

@Nullable, @NotNull

## Callback

말 그대로 호출을 반대로 하는것
예를 들어, 화면 A에서 버튼 B를 누르면 화면 C를 보여주는 스마트폰 어플이 있다고 해보자. 원래대로라면 프로그램이 일방적으로 스마트폰에게 화면 A를 띄워달라고 하지만, 버튼 B를 눌렀을때 시스템에서 이를 인식하고 프로그램에게 화면 B를 띄워달라고 하는것이다. (적절한 비유인지는 모르겠지만...)
어쨌든, 특정 이벤트 발생시 자동으로 실행되는 함수를 Callback 함수라고 한다.

## Listener

여러 자료를 찾아봤는데, 원래 개념은 Listener는 n개의 이벤트를 처리할 수 있다는 점과 Callback은 동기로 Listener은 비동기로 처리된다는 점, 등의 차이점이 있는 다른 개념이지만, 안드로이드에서는 거의 차이가 없다.
이벤트 리스너 같은 경우는 콜백 메소드를 포함하고 있는 인터페이스를 말한다
이벤트 리스너는 이벤트가 발생하는걸 감지하는 반면 이벤트 핸들러는 발생한 이벤트에 대한 작업을 처리한다는 개념적인 차이가 있지만, 안드로이드에서는 보통 Listener에 있는 메소드에서 작업 처리를 하기 때문에 그냥 리스너 안에 있는 메소드를 핸들러라고 봐도 무방한듯 하다.

## Observer

데이터나 속성의 변경을 감지하여 구독자에게 변경사항을 전달한다.

## Kotlin

장점
자바에 비해 훨씬 간결해진 코드
객체지향이면서 함수형 프로그래밍 언어
자바와 상호운용 가능 (자바에서 코틀린으로 작성된 클래스를 부를수 있고 반대도 가능)

## others

- Null
- Android 고급
- 테스트 및 성능 관리
- Crashlytics
- Roboletics
- 메모리 관리 (설정)
- 화면 수직 / 수평 전환 테스트
- Espresso UI Test
- JUnit Test
- Gson
- Proguard
- 그 외
- 지도
- 동영상 / 음악
- Bluetooth / Beacon / NFC

---

- Activity 생명주기
- Activity Fragment 차이
- Activity 하위 호환성, 어떤 패키지에 있는지
- View 생명 주기
- onActivityResult
- linear/relative/constraint 차이
- Listview / recyclerview 차이
- Service/intentService. JobintentService
- Asynctask 설명, 반드시 구현해야 할 부분은장단점
- 음악 재생시 Asynctask 쓴다면?
- 스레드간 통신 방법
- 클린 아키텍처
- Gradle
- Build Variants
  안드로이드 면접 인터뷰 질문 정리 Binder 개념과 Binder에서 발생 가능한 문제

- Zygote

- 프로세스 우선순위

- LMK와 OOM Killer의 차이

- 프로세스 분리 이유 동작

- Http Call 방법(library?)

- ActivityThread

- ActivityThread와 ActivityManagerService간의 통신

- ANR

- Looper는 몇 개?

- Message object pool, Message.obtain 쓰는 이유.

- pool의 개수

- pool은 어디에 어떤 형태로?

- ViewParent, getParent

- ViewRootImpl의 용도는?

- AsyncTask 사용 시 문제점

- AsyncTask 취소

- mayInterruptIfRunning의 의미
- HandlerThread란?

- deep sleep 현상은 무엇이고 이에 대한 대책은?

- Context는 어떤 데 쓰이고 자식 클래스는 어떻게 되나?

- Activity에서 this, getBaseContext(), getApplicationContext() 차이

- ActivityA에서 ActivityB 호출한 경우 생명주기/ActivityA로 다시 돌아오는 경우 생명주기

- onSaveInstanceState() 실행 시점

- taskAffinity 동작

- singleTask, singleInstance 차이

- Fragment 쓰면 장점, 불편한 점

- Fragment 정적 생성 메서드를 쓰는 이유

- 서비스는 언제 사용?

- 시스템 서비스와 서비스 컴포넌트 차이점

- Service onStartCommand 리턴 값 구분

- Started & Bound Service 언제 쓰이나?

- BIND_AUTO_CREATE 옵션은 왜 쓰나

- aidl 스텁과 프락시

- 서비스와 Activity 통신 방법은 어떤 것들이?

- cp와 직접 db 접근 코드 선택 기준

- 브로드캐스트리시버에서 Toast를 띄우면?

- LocalBroadcastManager 역할

- Application의 용도

- SharedPreferences commit()과 apply() 차이

- google play service 연결은 어떻게 하는가? 내부 구조

- Parcelable/Serializable 차이

- 메모리릭 확인하는 방법

- targetSdkVersion 용도

- 싱글톤에 Context가 그대로 전달되면 어떤 문제가 생기는가? (코드로 만들기)

---

- Subject 문제점과 어느 때 사용하면 되는가?

- Scheduler와 Worker의 관계

- subscribeOn/observerOn 차이

---

- State 패턴과 Strategy 패턴 차이

- 마커 인터페이스

- 애너테이션 활용은?

- AOP 장단점?

- 스레드풀 AbortPolicy

- CountDownLatch 사용. 주의할 점

- enum은 어떤 때 쓰는가?

- for each 내부 구조는?

- 다이나믹 프록시는? ==> Java 다이나믹 프록시
