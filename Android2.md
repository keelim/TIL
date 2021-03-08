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
  - [PendingIntent](#pendingintent)
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
  - [안드로이드의 4대 컴포넌트](#안드로이드의-4대-컴포넌트)
  - [액티비티의 수명주기](#액티비티의-수명주기)
  - [프래그먼트의 생명주기](#프래그먼트의-생명주기)
  - [메니페스트](#메니페스트)
  - [안드로이드에서 인플레이션](#안드로이드에서-인플레이션)
  - [WebView란?](#webview란)
  - [RxJava란 무엇인가?](#rxjava란-무엇인가)
  - [반응형 프로그래밍의 특징](#반응형-프로그래밍의-특징)
  - [코틀린의 장점](#코틀린의-장점)
  - [안드로이드의 테스크란?](#안드로이드의-테스크란)
  - [Realm이란? (SQLite와의 비교) [렐름]](#realm이란-sqlite와의-비교-렐름)
  - [Restful API란? \*Representation State Transfer의 약자](#restful-api란-representation-state-transfer의-약자)
  - [FCM의 구동 원리? (Firebase Cloud Messaging의 약자)](#fcm의-구동-원리-firebase-cloud-messaging의-약자)
  - [하이브리드 앱이란?](#하이브리드-앱이란)
  - [Looper란 무엇인지 설명해보세요.](#looper란-무엇인지-설명해보세요)
  - [안드로이드에서 메모리 관리](#안드로이드에서-메모리-관리)
  - [안드로이드 HTTP 라이브러리의 역사](#안드로이드-http-라이브러리의-역사)
  - [쓰레드 간 통신 방법, Looper와 Handler](#쓰레드-간-통신-방법-looper와-handler)
  - [Handler](#handler-1)
  - [Looper와 Message Queue](#looper와-message-queue)
  - [Message와 Runnable](#message와-runnable)
  - [HandlerThread](#handlerthread)
  - [Async Task](#async-task)
  - [안드로이드 애플리케이션 프로젝트 구조](#안드로이드-애플리케이션-프로젝트-구조)
  - [안드로이드에서 이용할 수 있는 데이터 저장 옵션들](#안드로이드에서-이용할-수-있는-데이터-저장-옵션들)
  - [SharedPreference 저장 옵션에 대한 설명](#sharedpreference-저장-옵션에-대한-설명)
  - [Android Architecture의 핵심 component](#android-architecture의-핵심-component)
  - [Intent Filter가 하는 일](#intent-filter가-하는-일)
  - [AIDL](#aidl)
  - [Service Lifecycle에서 요구되는 단계들](#service-lifecycle에서-요구되는-단계들)
  - [안드로이드를 위한 서비스에 사용되는 작업의 다른 모드](#안드로이드를-위한-서비스에-사용되는-작업의-다른-모드)
  - [Activity Life Cycle - onStop()에서 db 업데이트들을 모두 저장할 수 있는가?](#activity-life-cycle---onstop에서-db-업데이트들을-모두-저장할-수-있는가)
  - [this와 getApplicationContext의 차이점](#this와-getapplicationcontext의-차이점)
  - [UI 반응 제한 시간](#ui-반응-제한-시간)
  - [ANR(Android Not Responding) 이란 무엇인가?](#anrandroid-not-responding-이란-무엇인가)
  - [Bundle과 Parcel의 차이점](#bundle과-parcel의-차이점)
  - [Activity와 Fragment 차이점](#activity와-fragment-차이점)
  - [스레드와 서비스의 차이점](#스레드와-서비스의-차이점)
  - [안드로이드의 실행환경](#안드로이드의-실행환경)
  - [안드로이드는 다른 플랫폼에 비해 어떤 장점이 있는가?](#안드로이드는-다른-플랫폼에-비해-어떤-장점이-있는가)
  - [안드로이드 프로젝트 구성요소에 대해서 설명하시오.](#안드로이드-프로젝트-구성요소에-대해서-설명하시오)
  - [안드로이드에서 다국어 지원을 위해 해야할 작업](#안드로이드에서-다국어-지원을-위해-해야할-작업)
  - [안드로이드 매니페스트(android manifest)](#안드로이드-매니페스트android-manifest)
  - [디스플레이(display), 윈도우(window), 서피스(surface), 뷰(view), 뷰 그룹(view group), 뷰 컨테이너(view container), 레이아웃(layout)에 대해서 설명](#디스플레이display-윈도우window-서피스surface-뷰view-뷰-그룹view-group-뷰-컨테이너view-container-레이아웃layout에-대해서-설명)
  - [인플레이션(inflation)](#인플레이션inflation)
  - [안드로이드에서 색상을 지정하는 다양한 방식은 어떤 것들이 있는가?](#안드로이드에서-색상을-지정하는-다양한-방식은-어떤-것들이-있는가)
  - [안드로이드의 크기를 표현하는 다양한 표현방법에 대해서 설명하시오.](#안드로이드의-크기를-표현하는-다양한-표현방법에-대해서-설명하시오)
  - [안드로이드 MVC 모델은 어떻게 구성되어있는가?](#안드로이드-mvc-모델은-어떻게-구성되어있는가)
  - [액티비티(activity)가 무엇인지와 액티비티 생명주기에 대해서 설명하시오.](#액티비티activity가-무엇인지와-액티비티-생명주기에-대해서-설명하시오)
  - [액티비티간 데이터 전달에서 임의의 클래스 객체를 바로 전달하지 못하는 이유는 무엇이고 전달하기 위해서는 어떤 처리가 필요한가?](#액티비티간-데이터-전달에서-임의의-클래스-객체를-바로-전달하지-못하는-이유는-무엇이고-전달하기-위해서는-어떤-처리가-필요한가)
  - [부모 액티비티에서 자식 액티비티의 결과 값을 받아오기 위해 어떻게 해야하는가?](#부모-액티비티에서-자식-액티비티의-결과-값을-받아오기-위해-어떻게-해야하는가)
  - [서비스(service)가 무엇인지와 서비스 생명주기](#서비스service가-무엇인지와-서비스-생명주기)
  - [어플리케이션(application)과 컨텍스트(context)에 대해서 설명하시오.](#어플리케이션application과-컨텍스트context에-대해서-설명하시오)
  - [노티피케이션(notification)은 무엇인가?](#노티피케이션notification은-무엇인가)
  - [안드로이드에서 로그(log)를 출력하는 방법과 종류를 설명하시오.](#안드로이드에서-로그log를-출력하는-방법과-종류를-설명하시오)
  - [스타일(style), 테마(theme)에 대해서 설명하시오.](#스타일style-테마theme에-대해서-설명하시오)
  - [프레그먼트(fragment)가 와 프레그먼트 생명주기에 설명하시오.](#프레그먼트fragment가-와-프레그먼트-생명주기에-설명하시오)
  - [뷰 홀더 패턴(view holder pattern)에 대해서 설명하시오.](#뷰-홀더-패턴view-holder-pattern에-대해서-설명하시오)
  - [나인패치(9patch)란 무엇인가?](#나인패치9patch란-무엇인가)
  - [태스크(task)란 무엇인가?](#태스크task란-무엇인가)
  - [안드로이드의 메모리 관리 방식에 대해서 설명하시오.](#안드로이드의-메모리-관리-방식에-대해서-설명하시오)
  - [안드로이드의 쓰레드(thread)와 쓰레드 핸들러(thread handler)에 대해서 설명하시오.](#안드로이드의-쓰레드thread와-쓰레드-핸들러thread-handler에-대해서-설명하시오)
  - [NDK에 대해서 설명하라.](#ndk에-대해서-설명하라)
  - [NDK에서 로그캣(logcat)에 로그를 출력하기 위해 어떻게 해야하는가?](#ndk에서-로그캣logcat에-로그를-출력하기-위해-어떻게-해야하는가)
  - [naver](#naver)
  - [서비스 / 브로드캐스트 리시버 / 콘텐트 프로바이더를 사용해본 적이 있나요? 언제 사용해봤나요?](#서비스--브로드캐스트-리시버--콘텐트-프로바이더를-사용해본-적이-있나요-언제-사용해봤나요)
  - [액티비티의 생명 주기에 호출되는 콜백 함수는 어떤 것들이 있나요?](#액티비티의-생명-주기에-호출되는-콜백-함수는-어떤-것들이-있나요)
  - [액티비티에서 뒤로 가기 버튼을 눌렀을 때는 어떤 콜백이 호출될까요?](#액티비티에서-뒤로-가기-버튼을-눌렀을-때는-어떤-콜백이-호출될까요)
  - [그렇다면 액티비티에서 홈 버튼을 눌렀을 때는 어떤 콜백이 호출될까요?](#그렇다면-액티비티에서-홈-버튼을-눌렀을-때는-어떤-콜백이-호출될까요)
  - [코틀린으로 개발을 했던데 왜 코틀린을 선택했나요?](#코틀린으로-개발을-했던데-왜-코틀린을-선택했나요)
  - [코틀린을 사용해본 감상?](#코틀린을-사용해본-감상)
  - [서피스, 윈도우 개념](#서피스-윈도우-개념)
  - [액티비티가 다이얼로그 가려졌을 때 어떤 콜백이 호출될까?](#액티비티가-다이얼로그-가려졌을-때-어떤-콜백이-호출될까)
  - [그렇다면 액티비티가 또 다른 투명 액티비티에 의해 가려졌다면?](#그렇다면-액티비티가-또-다른-투명-액티비티에-의해-가려졌다면)
  - [그렇다면 화면을 꽉 채우는 다이얼로그에 의해 가려졌다면?](#그렇다면-화면을-꽉-채우는-다이얼로그에-의해-가려졌다면)
  - [스트링을 파라미터로 받아서, 그것을 역순으로 리턴하는 함수를 코딩해보세요.](#스트링을-파라미터로-받아서-그것을-역순으로-리턴하는-함수를-코딩해보세요)
  - [가장 인상 깊은, 자랑스러운 성취?](#가장-인상-깊은-자랑스러운-성취)
  - [현재 스타트업 재직 중인데 대기업 문화에 잘 적응할 수 있는지?](#현재-스타트업-재직-중인데-대기업-문화에-잘-적응할-수-있는지)
  - [GC 메커니즘에 대해 아는 대로 설명해보면?](#gc-메커니즘에-대해-아는-대로-설명해보면)
  - [어떤 파일을 다운로드 받고 있을 때 진행 상황을 표시하려면 어떻게 해야할까?](#어떤-파일을-다운로드-받고-있을-때-진행-상황을-표시하려면-어떻게-해야할까)
  - [특정 시간에 데이터를 받아 갱신하고 싶다면 어떻게 코드를 짜겠어요?](#특정-시간에-데이터를-받아-갱신하고-싶다면-어떻게-코드를-짜겠어요)
  - [왜 메인스레드에서 돌리면 안되는지 커널 관점에서 설명해보세요.](#왜-메인스레드에서-돌리면-안되는지-커널-관점에서-설명해보세요)
  - [Git 잘 쓰시나요?](#git-잘-쓰시나요)
  - [해쉬테이블 탐색에 걸리는 시간?](#해쉬테이블-탐색에-걸리는-시간)
  - [Google IO 발표된 기술 중 아는 것?](#google-io-발표된-기술-중-아는-것)
  - [제일 편한 언어? 자바는 잘 쓸 수 있는지?](#제일-편한-언어-자바는-잘-쓸-수-있는지)
  - [개발했던 앱에서 "안드로이드적"인 요소?](#개발했던-앱에서-안드로이드적인-요소)
  - [액티비티가 갑자기 종료됐을 때를 대비한 콜백이 있는데 아는지?](#액티비티가-갑자기-종료됐을-때를-대비한-콜백이-있는데-아는지)
  - [그 콜백이 언제 불릴지?](#그-콜백이-언제-불릴지)
  - [Stack 2개를 이용해서 Queue 처럼 거동하는 클래스를 정의해보세요.](#stack-2개를-이용해서-queue-처럼-거동하는-클래스를-정의해보세요)
  - [액티비티 스택: A, B, C 가 있는 상황에서 B를 런칭하고 여기서 백버튼 눌렀을 때 A가 뜨게 하고 싶다면? 스택 개념과 액티비티 생명주기 연결해서 설명해보세요.](#액티비티-스택-a-b-c-가-있는-상황에서-b를-런칭하고-여기서-백버튼-눌렀을-때-a가-뜨게-하고-싶다면-스택-개념과-액티비티-생명주기-연결해서-설명해보세요)
  - [액티비티 스택2: A, B, C, D, E가 있는 상황에서 차례대로 액티비티를 전환할 때 각 액티비티의 스샷을 따고 싶다. 어떤 콜백을 이용해야 할까?](#액티비티-스택2-a-b-c-d-e가-있는-상황에서-차례대로-액티비티를-전환할-때-각-액티비티의-스샷을-따고-싶다-어떤-콜백을-이용해야-할까)
  - [1440\*2880 비트맵을 만들면 용량이 어느정도 나올까?](#14402880-비트맵을-만들면-용량이-어느정도-나올까)
  - [이미지 다뤄본 적?](#이미지-다뤄본-적)
  - [이번 구글IO 에서 기억에 남는 발표?(2번 면접관님도 비슷한 거 물어보셨는데 화장실 갔을 때 검색이라도 해볼걸... 그런데 어디 대답 제대로 못한 게 한두 개여야지)](#이번-구글io-에서-기억에-남는-발표2번-면접관님도-비슷한-거-물어보셨는데-화장실-갔을-때-검색이라도-해볼걸-그런데-어디-대답-제대로-못한-게-한두-개여야지)
  - [웹뷰API 중 기억에 나는 것?](#웹뷰api-중-기억에-나는-것)
  - [여기도 결국 회사일 뿐이다. 위에서 시키는 대로 해야하고 멍청한 결정도 많이 내려오곤 하는데 잘 적응할 수 있을지?](#여기도-결국-회사일-뿐이다-위에서-시키는-대로-해야하고-멍청한-결정도-많이-내려오곤-하는데-잘-적응할-수-있을지)
  - [Thread간 통신방법에 대해 설명](#thread간-통신방법에-대해-설명)
  - [Looper에 대해 설명](#looper에-대해-설명)
  - [백그라운드에서 UI 업데이트 하는 방법](#백그라운드에서-ui-업데이트-하는-방법)
  - [앱을 사용하는 도중에 카카오톡 메세지가 온다면 사용하던 앱의 TopActivity의 생명주기는 어떤 상태가 되나요?](#앱을-사용하는-도중에-카카오톡-메세지가-온다면-사용하던-앱의-topactivity의-생명주기는-어떤-상태가-되나요)
  - [데이터 불러오는 작업은 어디서 해야할까?](#데이터-불러오는-작업은-어디서-해야할까)
  - [다른 액티비티가 상단에 올라오면 어떤 상태?](#다른-액티비티가-상단에-올라오면-어떤-상태)
  - [onRestart는 언제 호출이 되나요?](#onrestart는-언제-호출이-되나요)
  - [Fragment의 생명주기에 대해 얘기하고 각 항목에 대해 설명](#fragment의-생명주기에-대해-얘기하고-각-항목에-대해-설명)
  - [ANR(Application Not Responding)](#anrapplication-not-responding)
  - [Content Provider와 Content Resolver 차이](#content-provider와-content-resolver-차이)
  - [XML 기반 레이아웃은 왜 중요?](#xml-기반-레이아웃은-왜-중요)
  - [Vector , 비트맵 이미지 차이점](#vector--비트맵-이미지-차이점)
  - [ConstraintLayout 왜 사용?](#constraintlayout-왜-사용)
  - [네트워크](#네트워크)
  - [Process Vs. Thread](#process-vs-thread)
  - [Http vs. Https](#http-vs-https)
  - [OkHttp와 Retrofit 차이점, 장단점](#okhttp와-retrofit-차이점-장단점)
  - [DataBinding 장점 왜사용?](#databinding-장점-왜사용)
  - [Rx 적용했을 때 좋은 점](#rx-적용했을-때-좋은-점)

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

Extent Intent(명시적 인텐트)와 Implicit Intent(암시적 인텐트)가 있다. Intent는 action과 data 쌍으로 동작한다. action은 수정, 보기와 같은 수행할 작업을 정의하고 data는 Uri 객체처럼 지정된다. 명시적 인텐트는 호출대상이 명확하게 지정되어 있는 경우고, 암시적 인텐트는 호출되는 대상이 명확하게 정의되어 있찌 않은 경우이다. (Action, Data, Type, Category, Flags)

## PendingIntent

Intent를 직접 보내지 않고 다른 클래스에서 Intent를 위임해주기 위한 클래스이다.

보통 NotificationBar와 상호작용 하는 어플리케이션을 작성할때 사용된다.

즉 알림바, 알람, 다른앱에서 startActivity,sendBroadCast,StartService가 실행되게 하고 싶을때 Intent를 PendingIntent에 담아서 호출한다.

펜딩 인텐트는 이름에서 볼수 있듯이 보류된 인텐트로, 당장 해당 작업을 다른 컴포넌트에 요청하는게 아닌 특정시점에 자신이 아닌 컴포넌트가 다른 컴포넌트에게 펜딩 인텐트를 사용하여 작업을 요청한다는 특징이 있다.

대표적으로, 사용자가 Notification을 클릭했을 때 특정한 작업을 수행시키거나, 위젯을 통해 앱을 실행시키거나, 미래의 특정 시점에 실행되는 인텐트를 선언하는 경우에 펜딩 인텐트를 사용한다.

펜딩인텐트의 인스턴스를 생성하는 방법은 크게 네가지가 있다.

- getActivity(Context, int, Intent, int)
  매개변수에 포함된 Intent를 통해 한가지 액티비티를 실행시킬때 사용
- getActivities(Context, int, Intent[], int)
  매개변수에 포함된 Intent배열을 통해 여러개의 액티비티를 실행시킬때 사용. 이때 Context.startActivities와 똑같이 작동한다. startActivities는 거의 사용되지 않지만 액티비티들을 백스택에 넣고 싶을때 사용되기 때문에 실행된 액티비티에서 백버튼을 눌렀을때 다른 액티비티로 이동하고 싶다면 사용한다.
- getBroadcast(Context, int, Intent, int)
  context.sendBroadCast(intent)를 하고 싶을때 사용
- getService(Context, int, Intent, int)
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

## 안드로이드의 4대 컴포넌트

`액티비티`는 안드로이드에서 화면을 관리하고 사용자의 다양한 이벤트를 처리하는데 사용됩니다.

`서비스`는 화면에서 보이지 않지만 특정한 기능을 백그라운드에서 처리하는데 사용됩니다.

`브로드캐스트리시버`는 안드로이드에서 발생하는 특정 브로트캐스트 메세지를 처리하기 위한 컴포넌트입니다.

`콘텐트 프로바이더`는 앱 사이의 데이터의 공유를 위한 인터페이스를 제공하는 컴포넌트입니다.

## 액티비티의 수명주기

안도르이드에서 화면을 관리하며 사용자가 발생시키는 다양한 이벤트를 처리하는 컴포넌트입니다
부모 액티비티에서 새로운 자식 액티비티를 실행하고자 한다면 먼저 매니페스트 파일에 해당 자식 액티비티를 추가 해줘야합니다. 다음으로 부모 액티비티에서 startActivity 메소드에 인텐트를 파라미터로 넘겨 실행하거나 startActivities 메소드를 이용하여 여러개의 액티비티를 한꺼번에 실행할 수 있습니다. 액티비티의 실행과정은 첫 번째로 부모 액티비티에서 자식 액티비티를 생성 및 호출합니다. 두 번째로 액티비티 매니저 서비스가 해당 앱 프로세스에서 인텐트를 복사해온 후 매니페스트 파일에서 해당 인텐트에 명시되어있는 액티비티를 찾고 어떻게 실행시켜야할지 결정합니다. 세 번째로 찾아낸 액티비티를 실행하고 다시 해당 앱 프로세스에 인텐트를 복사하여 넘겨줍니다. 그 외 자식 액티비티 내의 onCreate 메소드에서 setContentView 메소드에 레이아웃의 아이디를 파라미터로 넘겨 해당 액티비티의 화면을 구성하게됩니다.
액티비티는 크게 3가지 상태가 존재합니다. 먼저 실행(running) 상태는 액티비티 스택의 최상위에 있으며 포커스를 가지고 있어 사용자에게 보이는 상태입니다. 다음으로 일시 중지(paused) 상태는 사용자에게 보이기는 하지만 다른 액티비티가 위에 있어 포커스를 받지 못하는 상태를 말합니다. 예를들어 대화상자가 위에 있어 일부가 가려져 있는 경우를 말합니다. 마지막으로 중지 (stopped) 상태는 다른 액티비티에 의해 완전히 가려져 보이지 않는 상태를 말합니다.
액티비티가 처음 만들어지면 onCreate 메소드가 호출되어 레이아웃을 구성합니다. 이후 onStart 메소드가 화면에 보이기 직전에 호출됩니다. 다음으로 onResume 메소드가 사용자 상호작용(화면이 포커스를 얻었을 때)하기 바로 전에 호출됩니다. 이 3가지 메소드가 호출되어 액티비티는 실행 상태를 갖게됩니다. 이후 포커스를 잃었을 때 onPause 메소드가 호출되고 일시 중지 상태가 됩니다. 일시 중지 상태에서 다시 포커스를 획득하면 onResume 메소드가 호출되거나 다른 액티비티에 의해서 완전히 화면이 가려졌는지 여부를 확인하여 가려져 보이지 않는 경우 onStop 메소드가 호출되어 중지 상태가됩니다. 정지 상태에서 다시 화면이 보이기 직전에 onRestart 메소드가 호출되고 onStart 메소드가 차례로 호출됩니다. 그 외 finish 메소드가 실행되어 해당 액티비티가 종료되기 직전에 onDestroy 메소드가 실행됩니다.
가끔은 일시 중지나 중지 상태에서 시스템이 메모리가 부족하다고 판단될 경우 onCreate 메소드부터 다시 해당 액티비티를 구동합니다. 이 경우 onStop, onResume 메소드 호출이 생략됩니다. 따라서 onSaveInstanceState, onRestoreInstanceState 메소드를 이용하여 액티비티가 갑자기 죽을 것을 대비해서 상태를 저장하고 복원하기 위한 작업을 정의해줄 수 있습니다.

## 프래그먼트의 생명주기

onAttach함수가 OnCreate이전에 호출됩니다. 그 이후 OnCreate함수가 호출되고 OncreateView에서 LayoutInflater로 UI관련 잡업을 할 수 있습니다. 그리고 화면이 포커스를 잃었을때는 onPause OnStop onDestroyView가 호출되고
종료시에 onDestory onDetach()가 호출됩니다.

## 메니페스트

매니페스트 파일은 앱의 이름, 버전, 구성요소, 권한등 앱의 실행에서 꼭 필요한 정보가 저장되어 있는 파일입니다.
xml파일로 프로젝트의 최상위에 존재합니다.

태그 구성으로 가장 위는 manifest태그가 존재하고 패키지명, 버전 등이 기제됩니다.

application태그에는 앱 아이콘, 앱 이름등의 정보가 저장됩니다.

activity태그에는 액티비티 클래스명과 액티비티 이름을 정의합니다.
activity하위에는 intent-filter태그를 이용하여 엑티비티에 대한 인텐트 작업시 필요한 action과 category를 정의합니다.

service,receiver,provider 태그에는 서비스,리시버,프로바이더에 대한 내용이 정의되어 있습니다.

permission태그에는 앱에서 필요한 권한을 정의합니다.

그밖에 sdk버전을 지칭하는 uses-sdk와 다른 패키지를 등록할 수 있는 uses-library등이 존재합니다.

## 안드로이드에서 인플레이션

## WebView란?

안드로이드 프레임워크에 내장된 컴포넌트로 View의 형태로 임베딩 할 수 있는 형태이다.

웹페이지를 보거나 안드로이드 앱 안에서 HTML을 호출하여 앱을 구현하는 하이브리드 형태의 앱을 개발하는데에도 많이 사용된다.

## RxJava란 무엇인가?

일단 RxJava는 Reactive Programming을 기반으로 한 언어입니다.
즉 Reactive Extension의 JVM버전입니다.
비동기 데이터처리를 효율적으로 할 수 있는 장점이 있습니다.

![](https://t1.daumcdn.net/cfile/tistory/99C54A4E5B4603D10F)

RxJava는 반응형 프로그래밍으로 명령형 프로그래밍과 다른 개념입니다

## 반응형 프로그래밍의 특징

for if while같은 것이 아니라 sql 쿼리 같은 선언형으로 구성됩니다.

또 함수를 단지 호출하는 대상이 아니라 변수로도, 혹은 인자로도 넘길 수 있습니다.
이러한 함수형언어의 도구들을 자유롭게 활용해야 합니다(ex) java8의 람다표현식)

## 코틀린의 장점

기존의 자바 코드의 보일러 플레이트 구문을 최소화 시킬 수 있습니다.

기존의 자바에서도 람다표현식을 이용하여 코드의 간소화를 위해 노력했습니다.
java8에서는 Retrolambda라이브러리를 사용하지 않고 람다표현식이 가능합니다.

그렇지만 안드로이드 스튜디오 2.4버전 이상부터 JDK 1.8로 빌드가 가능하고 minsdk도 24부터이기때문에 실질적으로 사용하지 못합니다. 즉 JDK 1.6기반의 API와 문법적으로 조금 추가된 형태로 빌드 할 수 있다고 봅니다.

안드로이드의 대표적인 보일러 플레이트 구문은 레이아웃에 정의한 뷰 레퍼런스를 가지고 오는 부분이나 SQLite트랜젝션을 처리하는 부분 등이 있습니다.

또 자바 8의 스트림 API를 사용할 수도 없습니다.

스트림에 대한 대비로는 streamsupport, Lightweight-Strem-API가 있습니다.

RxJAVA또한 자바 8 스트림의 훌륭한 대안이고 안드로이드 커뮤니티에서 많이 쓰이고 있습니다.

하지만 위의 라이브러리들의 의존성문제와 기존 라이브러리에 대한 학습등이 부담으로 다가온다는 사실이 있습니다.

코틀린의 좋은점으로는 NullPointerException다루기, 보일러 플레이트 개선하기, Collections에 filter,map,foreach같은 고차함수를 적용할 수 있고, 변경가능한 컬렉션과 불가능한 컬렉션을 엄격히 구분합니다. 서버에서 수신받은 데이터를 컬렉션으로 다룰 일이 많기때문에 코드를 보다 간결하고, 안전하게 만드는 데 도움이 됩니다. 또 확장함수(이미 존재하는 클래스에 새로운 함수를 추가)라는 강력한 기능도 있습니다.

또 자바와 호완성이 무척 좋고 기존의 라이브러리를 제약없이 사용 할 수 있습니다.

하지만 새로운 언어를 배워야 한다는 점에대한 부담감과 기술적 이슈가 발생했을때 대응기간이 상대적으로 길어 질 수 있다는 단점도 분명 존재합니다.

## 안드로이드의 테스크란?

Task는 어플리케이션에서 실행되는 Activity를 관리하는 스택입니다. 선입 후출의 형태로 나중에 적제된 액티비티가 가장 먼저 사용됩니다. 최초적재된 엑티비티는 Root Activity라고 하고 마지막에 적재된 Activity는 Top Activity라고 합니다.

Flag를 이용하여 엑티비티의 흐름을 제어 할 수 있습니다.

## Realm이란? (SQLite와의 비교) [렐름]

sqlite,realm은 안드로이드 단말에서 사용하는 관계형 데이터베이스입니다.

sqlite는 오픈소스 데이터베이스로 OS와 상호작용하기위해 SQLiteOpenHelper인터페이스를 이용합니다. SQLite는 C언어로 되어있고 경량데이터베이스이며 하나의 디스크 파일에 모든 데이터를 저장 할 수 있습니다.

Realm은 크로스 플랫폼 기반의 모바일 데이터베이스입니다. IOS와 Android에서 모두 사용이 가능하며 성능 및 효율성이 우수합니다. 설치도 간편하며 쿼리 응답속도도 기타 ORMLite나 SQLite보다 더 좋습니다. 크로스 플랫폼이기 때문에 협업에서 유용합니다.

특징으로는 zero-copy모델을 사용하기 때문에 데이터 객체 자체에서 그대로 작업이 가능합니다.
크로스 플랫폼이기 때문에 특정 OS를 가리지 않고 동기화 될 수 있습니다.
ACID를 준수합니다.

Realm은 데이터베이스 컨테이너의 인스턴스입니다.
SQLite 기반의 ORM 프레임워크 입니다.

## Restful API란? \*Representation State Transfer의 약자

웹상에 존재하는 모든 자원에 URI를 부여하여 사용하는 방법이다. (비연결성, URI로 자원에 접근)
HTTP 웹 표준을 이용하며 http의 캐싱을 활용 할 수 있다는 장점이 있다. 그리고 구조가 명확하여
클라이언트와 서버에서 개발해야할 부분이 명확해지고 Uri만 봐도 어떤 요청인지 파악될 수 있게
직관적이다라는 특징이 있습니다.

## FCM의 구동 원리? (Firebase Cloud Messaging의 약자)

본연의 서버의 기능을 수행하면서 또 하나의 복잡한 알림 기능까지 포함한다면 서버의 속도는 처리량이 많아 느려질 것이다. 따라서 이러한 해결책으로 알림의 기능은 다른 서버가 제공을 해주고 본 서버는 알림기능을 제공하는 서버에 알림이 있는지 요청을 해서 정보를 가져오는 구조이다.

FCM의 동작을 위해서 HTTP나 XMPP로 FCM과 통신하는 서버와 클라이언트 앱이 필요합니다.

동작 순서

디바이스에 앱이 설치된후 최초 실행되면서 고유 식별자인 디바이스 토큰이 발급된다. 이 토큰을 앱 서버에 등록한다.

앱 서버에서 FCM 연결 서버로 푸시 알림을 요청한다. 이때 준비물은 디바이스 토큰과 API 서버 키이다.

FCM 연결 서버는 토큰을 대상으로 알림 메시지를 푸시한다.

## 하이브리드 앱이란?

네이티브 앱처럼 하드웨어의 기능들을 사용할 수 있으며 마켓에 등록이 가능하며 배포 후에도 웹만 연결되어 있다면 수정/보완을 할 수 있습니다. 또한 하나의 소스로 아이폰과 안드로이드에 맞게 포장이 가능하며 핵심 부분은 웹 앱 기술로 빠르게 제작이 가능하여 개발 비용이 적어질 수 있습니다.

실제 핵심기능은 코드로 구현하고 지속적으로 업데이트 할 부분은 웹에서 관리하는 기능입니다.

ex)멜론차트

## Looper란 무엇인지 설명해보세요.

Looper는 스레드간의 신호이므로 handler에 보낸다고 해서 곧바로 처리되는 것이 아닙니다. 동시다발적으로 메세지가 발생할 수 있기 때문에 메세지 큐(Message Queue)에 쌓았다가 처리합니다. 큐(Queue)에 들어있는 내용을 하나하나 꺼내 처리하는 놈이 바로 루퍼입니다. 메인 쓰레드가 looper를 가지고 있으며 무한 루프를 돌며 큐의 내용을 처리합니다.

## 안드로이드에서 메모리 관리

안드로이드에서 메모리 관리는 GC를 이용해서 진행되게 됩니다.

주기적으로 GC루트에서 모든 객체 참조에 대해 활성객체를 표시하고 활성되지 않은 객체는 메모리에서 지워집니다.

String References와 WeakReference로 나눌 수 있습니다.

## 안드로이드 HTTP 라이브러리의 역사

2007년 => 안드로이드 발표 , HttpClient, 아파치의 DefaultHttpClient등이 사용
(HttpClient의 여러 버그들 문제가 있음)

2011년 => Goolge의 Developer 블로그에서 HttpUrlConnetction 사용 권장

이후... => Volley나 Square의 Okhttp가 등장하여 쉽게 Http 통신을 사용할 수 있게 됨.

2014년 => 롤리팝 이후 HttpClient 가 Deprecated되며 이를 베이스로 하는 Volley
도 Deprecated됨

이후.... => Okhttp와 그 래퍼인 Retrofit이 인기를 가짐.
Retrofit은 클라이언트 부분과 콜백 형식등을 플러그로 변경할수 있다는점에서 인기를 가짐.

## 쓰레드 간 통신 방법, Looper와 Handler

안드로이드의 애플리케이션을 실행하면 시스템은 메인 액티비티를 메인 메모리로 올려 프로세스로 만들며, 이 때 메인 스레드가 자동으로 생성된다. 메인 스레드는 안드로이드의 주요 컴포넌트를 실행하는 곳이자 UI를 그리거나 갱신하는 일을 담당할 수 있는 유일한 스레드이므로 UI스레드라고도 불린다.

안드로이드 화면을 구성하는 뷰나 뷰 그룹을 하나의 스레드에서만 담당하는 원칙을 싱글 스레드 모델이라고 한다. 싱글 스레드 모델의 규칙은

1. 메인 스레드(UI 스레드)를 블럭하지 말 것

2. 안드로이드 UI 툴 킷은 오직 UI 스레드에서만 접근할 수 있도록 할 것

으로 2가지이다. 이런 싱글 스레드 모델의 영향을 고려하지 않으면 애플리케이션의 성능이 저하될 수 있다. 긴 시간이 걸리는 작업을 메인 스레드에서 담당한다면 애플리케이션의 반응성이 낮아질 수 있고, 급기야 사용자의 불편함을 방지하고자 시스템이 애플리케이션을 ANR 상태로 전환시킬 수 있다. 따라서 시간이 걸리는 작업을 하는 코드는 여분의 스레드를 사용하여 메인 스레드에서 분리해야 하고, 자연스럽게 메인 스레드와 다른 스레드가 통신하는 방법이 필요하게 된다. 다른 스레드에서 메인 스레드로 접근하기 위해 Looper와 Handler를 사용할 수 있으며, 안드로이드는 자바의 스레드를 좀 더 쉽게 사용할 수 있도록 래핑한 Handler 스레드, 더 나아가 스레드나 메시지 Loop 등의 작동 원리를 크게 고려하지 않고도 사용이 가능한 AsyncTask 등의 클래스를 제공한다.

Looper와 Handler의 사용 목적

왜 안드로이드는 메인 스레드에서만 UI 작업이 가능하도록 제한할까? 메인 스레드가 아닌 스레드가 병렬적으로 실행되고 있을 때, 메인 스레드와 다른 스레드, 두 개 이상의 스레드가 동시에 같은 텍스트 뷰에 setText()를 시도하는 경우를 생각하면 간단하다. 두 개 이상의 스레드를 사용할 때의 동기화 이슈를 차단하기 위해서 Looper와 Handler를 사용하게 된다.

Looper와 Handler의 작동 원리

먼저 스레드와 Looper, Handler가 어떻게 작동할까? 메인 스레드는 내부적으로 Looper를 가지며 그 안에는 Message Queue가 포함된다. Message Queue는 스레드가 다른 스레드나 혹은 자기 자신으로부터 전달받은 Message를 기본적으로 선입선출 형식으로 보관하는 Queue다. Looper는 Message Queue에서 Message나 Runnable 객체를 차례로 꺼내 Handler가 처리하도록 전달한다. Handler는 Looper로부터 받은 Message를 실행, 처리하거나 다른 스레드로부터 메시지를 받아서 Message Queue에 넣는 역할을 하는 스레드 간의 통신 장치이다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile4.uf.tistory.com%2Fimage%2F999EB5445AD7A3C5011972)

## Handler

Handler는 스레드의 Message Queue와 연계하여 Message나 Runnable 객체를 받거나 처리하여 스레드 간의 통신을 할 수 있도록 한다. Handler 객체는 하나의 스레드와 해당 스레드의 Message Queue에 종속된다. 새로 Handler 객체를 만든 경우 이를 만든 스레드와 해당 스레드의 Message Queue에 바인드된다. 다른 스레드가 특정 스레드에게 메시지를 전달하려면 특정 스레드에 속한 Handler의 post나 sendMessage 등의 메서드를 호출하면 된다. 앞서 Message Queue는 전달받은 Message를 선입선출 형식으로 보관한다고 설명했지만, 전달 시점에 다른 메서드를 사용하여 Queue의 맨 위로 보내거나, 원하는 만큼 Message나 Runnable 객체의 전송을 지연시킬 수도 있다.

외부 혹은 자기 스레드로부터 받은 메시지를 어떤 식으로 처리할 지는 handlerMessage() 메서드를 구현하여 정한다. sendMessage()나 post()로 특정 Handler에게 메시지를 전달할 수 있고, 재귀적인 호출도 가능하므로 딜레이를 이용한 타이머나 스케줄링 역할도 할 수 있어 편리하다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F9992FA4E5AD7A51B339F93)

## Looper와 Message Queue

Looper는 무한히 루프를 돌며 자신이 속한 스레드의 Message Queue에 들어온 Message나 Runnable 객체를 차례로 꺼내서 이를 처리할 Handler에 전달하는 역할을 한다. 메인 스레드는 Looper가 기본적으로 생성되어 있지만, 새로 생성한 스레드는 기본적으로 Looper를 가지고 있지 않고, 단지 run 메서드만 실행한 후 종료하기 때문에 메시지를 받을 수 없다. 따라서 기본 스레드에서 메시지를 전달받으려면 prepare() 메서드를 통해 Looper를 생성하고, loop() 메서드를 통해 Looper가 무한히 루프를 돌며 Message Queue에 쌓인 Message나 Runnable 객체를 꺼내 Handler에 전달하도록 한다. 이렇게 활성화된 Looper는 quit()이나 quitSafely() 메서드로 중단할 수 있다. quit() 메서드가 호출되면 Looper는 즉시 종료되고, quitSafely() 메서드가 호출되면 현재 Message Queue에 쌓인 메시지들을 처리한 후 종료된다.

## Message와 Runnable

Message란 스레드 간 통신할 내용을 담는 객체이자 Queue에 들어갈 단위로 Handler를 통해 보낼 수 있다. 일반적으로 Message가 필요할 때 새 Message 객체를 생성하면 성능 이슈가 생길 수 있으므로 안드로이드가 시스템에 만들어 둔 Message Pool의 객체를 재사용한다. obtain() 메서드는 빈 Message 객체를, obtain(Handler h, int what ...)은 목적 handler와 다른 인자들을 담은 Message 객체를 리턴한다.

새 스레드는 Thread() 생성자로 만들어서 내부적으로 run()을 구현하던지, Thread(Runnable runnable) 생성자로 만들어서 Runnable 인터페이스를 구현한 객체를 생성하여 전달하던지 둘 중 하나의 방법으로 생성하게 된다. 후자에서 사용하는 것이 Runnable로 스레드의 run() 메서드를 분리한 것이다. 따라서, Runnable 인터페이스는 run() 추상 메서드를 가지고 있으므로 상속받은 클래스는 run() 코드를 반드시 구현해야 한다.

## HandlerThread

Looper에서 언급했듯이 안드로이드의 스레드는 자바의 스레드를 사용하기 때문에 안드로이드에서 도입한 Looper를 기본으로 가지지 않는다는 불편함이 있다. 이런 불편함을 개선하기 위해 생성할 때, Looper를 자동으로 보유한 클래스를 제공하는데, 이것이 바로 HandlerThread이다. Handler Thread는 일반적인 스레드를 확장한 클래스로 내부에 반복해서 루프를 도는 Looper를 가진다. 자동으로 Looper 내부의 Message Queue도 생성되므로 이를 통해 스레드로 Message나 Runnable을 전달받을 수 있다.

## Async Task

AsyncTask는 스레드나 메시지 루프 등의 작동 원리를 몰라도 하나의 클래스에서 UI 작업과 background 작업을 쉽게 할 수 있도록 안드로이드에서 제공하는 클래스이다. 캡슐화가 잘 되어 있기 때문에 사용시 코드 가독성이 증대되는 장점이 있으며, 태스크 스케쥴을 관리할 수 있는 콜백 메서드를 제공하고, 필요할 때 쉽게 UI 갱신도 가능하며 작업 취소도 쉽다. 따라서, 리스트에 보여주기 위한 데이터 다운로드 등 UI와 관련된 독립된 작업을 실행할 경우 AsyncTask로 간단하게 구현할 수 있다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile1.uf.tistory.com%2Fimage%2F9993BC3C5AD7A7FE3C016B)

그러나 AsyncTask를 사용해서 스케줄링할 수 있는 작업 수의 제한이 있고, 몇 초 정도의 짧은 작업에서만 이상적으로 동작한다는 한계가 있다. 또한, 안드로이드의 버전 별로 병렬 처리 동작이 다르므로 허니콤 이후 버전에서 멀티스레드로 병렬적인 동작을 원한다면 AsyncTask를 실행할 때, AsyncTask.Thread_POOL_EXECUTOR 스케줄러를 지정해야 한다.

## 안드로이드 애플리케이션 프로젝트 구조

- src : .java 소스 파일들을 포함하고 있고 코드를 여기에 작성한다. 이 파일은 프로젝트의 패키지 이름으로 사용할 수 있다.

- gen : R.java 소스 파일들을 포함하고 있고 프로젝트에 있는 모든 자원을 참조하는 컴파일러가 생성한 파일이다.

- assets : 이 폴더는 모든 HTML, test file, database와 같은 정보들을 가지고 있다.

- bin : 빌드 과정에서 ADT에 의해 생성된 .apk 파일이 있다. apk 파일은 애플리케이션 바이너리 파일이고 실행하기 위한 모든 것을 담고 있다.

- res : drawable, menu, layout, value와 같은 안드로이드 애플리케이션에 쓰이는 모든 resource 파일들을 가지고 있다.

## 안드로이드에서 이용할 수 있는 데이터 저장 옵션들

- SharedPreferences

- Property

- SQlite

- ContentProvider

- File Storage

- Cloud Storage

## SharedPreference 저장 옵션에 대한 설명

- SharedPreference는 안드로이드에서 데이터를 저장하는 가장 간단한 mechanism이다. 별도의 파일 생성이 필요없이 key와 value 쌍형태의 XML 파일로 데이터를 저장한다. SharedPreference class는 key-value 쌍을 primitive 데이터 형태(boolean, float, int, long, string)로만 저장하여 쓸 수 있도록 허용한다. 이 XML 파일은 data/data/shared-prefs 폴더 안에 있다.

## Android Architecture의 핵심 component

- 리눅스 커널

- 라이브러리 : 안드로이드 애플리케이션 API를 위한 라이브러리

- 안드로이드 프레임워크 : 안드로이드 애플리케이션을 위한 API (WindowManager)
- 안드로이드 애플리케이션

## Intent Filter가 하는 일

이용하고자 하는 service와 activity에 따라 하나 이상의 intent들이 있을 수 있다. 각 component는 응답하려는 intent들을 말할 필요가 있다. Intent Filter는 이러한 component에 대응하고자 하는 intent를 필터링할 수 있다.

## AIDL

- AIDL은 Android Interface Definition Language의 약어이다.

- IPC를 통한 동일한 레벨로 통신하는 클라이언트와 서비스 간 인터페이스 요구사항들을 처리한다.

- IPC 통신을 위해 Parcel을 이용해 data들을 primitive type으로 주고받는다는 내용

## Service Lifecycle에서 요구되는 단계들

- service는 Context.startSevice() 함수를 통해 시작되고 시스템에서 onCreate() 메서드를 사용하여 서비스를 검색한다. service를 시작하기 위해 onStartCommand(Intent, int, int) 메서드를 적절한 arguments들과 함께 호출해야 한다.

- 만약 service를 멈추려면 Context.stopService() 또는 stopSelf() 메서드를 실행시켜야 한다.

- Context.startSevice() 메서드의 복수 호출로 인해 프로그램 중첩이나 서비스 정지를 하지 않는다.

- service는 stopSelf(int) 메서드를 이용해 스스로 정지할 수 있다. 모든 프로세스가 처리될 때까지 서비스가 중지되지 않는다.

## 안드로이드를 위한 서비스에 사용되는 작업의 다른 모드

- START_STICKY : service가 강제 종료되었을 경우, 시스템이 다시 service를 재시작시켜주지만, intent 값을 null로 초기화시켜 재시작한다.

- service 실행 시, startService(Intent service) 메서드를 호출하는데 onStartCommand(Intent intent, int flags, int startId) 메서드에 intent로 value를 넘겨줄 수 있다. 기존에 intent에 value값이 설정이 되어 있다고 하더라도 service 재시작 시 intent 값이 null로 초기화되서 재시작된다.

- START_NOT_STICKY : 이 flag를 리턴하면 강제로 종료된 service가 재시작하지 않는다.

- START_REDELIVER_INTENT : START_STICKY와 마찬가지로 service가 종료되었을 경우, 시스템이 다시 service를 재시작시켜 주지만, intent 값을 그대로 유지시켜 준다. startService() 메서드 호출 시 Intent value 값을 사용한 경우라면 해당 flag를 사용해서 리턴 값을 설정해준다.

## Activity Life Cycle - onStop()에서 db 업데이트들을 모두 저장할 수 있는가?

메모리 부족이나 화면 회전(configuration change)인 경우, onStop()에 도달하기 전에 안드로이드가 강제로 애플리케이션을 종료할 수 있다. onPause()는 프로그램을 종료되기 전에 반드시 호출되는 유일한 메서드이기 때문에 DB 테이블같은 모든 영구적인 데이터들을 onPause()에 저장해야 한다.

## this와 getApplicationContext의 차이점

- this는 항상 현재 클래스 객체를 가리키고, app context는 전체 프로세스를 가리킨다. 오직 하나의 App context만이 존재하므로, 만약 Application Life Time 동안 컨트롤하려면 App Context를 사용하고 아니면 this를 이용해야한다.

## UI 반응 제한 시간

- 유저가 Activity를 터치함에도 불구하고 프로그램이 `5초` 동안 반응이 없다면 안드로이드는 이를 용납하지 않고 강제로 애플리케이션을 종료할 것이다. 이 에러를 ANR이라 부른다.

- 터치를 통한 사용자 입력이 5초 내에 처리되지 않았을 때

- 브로드캐스트가 10초 내에 처리되지 않았을 때

## ANR(Android Not Responding) 이란 무엇인가?

- ANR은 하나의 메인 스레드를 통해 무거운 작업을 수행하는 경우 발생한다. 만약 2개의 heavy한 작업들을 하나의 스레드에서 수행하면, action에 대한 반응이 늦춰짐에 따라 유저들을 자극하고, 결국 프로세스를 멈추게 한다.

## Bundle과 Parcel의 차이점

- Bundle은 액티비티 간 주고받는 데이터를 보유한 데이터 Holder이다. 액티비티 강제 종료 시에, 나중에 액티비티의 상태를 복원하기 위해 UI 상태나 일시적인 상태들을 모두 저장한다. 이 저장된 상태들은 Bundle을 통해 onCreate() 함수에 전달되어 종료된 액티비티를 다시 복원한다. 메모리 부족이나 회전 시에 발생한다.

- onSaveInstanceState() : onPause() 이전 또는 이후에 호출된다.

- onRestoreInstanceState() : onStart() 이후에 호출된다.

- Parcel는 범용 직렬화 메커니즘이 아니다. 이 클래스는 고성능 IPC 전송으로 설계되었고 IBinder에 많이 사용된다. 보통 직렬화 시, Serializables를 이용하고 직렬화가 무겁거나 오랜 시간이 걸리면 임베디드 디바이스에서의 IPC 통신을 위해 Parcel을 이용한다.

## Activity와 Fragment 차이점

- 프래그먼트는 액티비티에 종속되어 있다.

- 프래그먼트는 더 넓은 스크린 장치 내의 공간을 효율적으로 이용하기 위해 사용된다.

- 하나의 액티비티는 스크린 사이즈에 따라 0개 또는 여러 개의 프래그먼트들을 포함하고 있다. 프래그먼트는 여러 개의 액티비티에서 재사용할 수 있기때문에 재사용 가능한 component처럼 동작할 수 있다.

- 프래그먼트는 독립적으로 존재할 수 없다. 반드시 액티비티의 한 부분으로 있어야 한다. 그러나 액티비티는 독립적으로 존재할 수 있다.

## 스레드와 서비스의 차이점

- 서비스는 UI 없이 백그라운드에서 오랫동안 작업을 수행하기 위한 안드로이드 component 중 하나이다.

- 스레드는 백그라운드에서 몇몇 작업을 수행하기 위한 O.S 레벨에서의 기능이다.

## 안드로이드의 실행환경

안드로이드는 크게 4가지 실행환경으로 구성되어있습니다. 가장 하단부터 리눅스 커널, 라이브러리, 어플리케이션 프레임워크, 어플리케이션 순서입니다. 리눅스 커널은 OS로 안드로이드 스마트폰의 다양한 하드웨어(화면, 카메라, 블루투스, GPS, 메모리 등)를 관리합니다.

라이브러리는 안드로이드에 있는 다양한 기능(UI 처리, 미디어 프레임워크, 데이터베이스, 그래픽 처리, 웹 킷 등)을 소프트웨어적으로 구현해 놓은 환경 뿐만 아니라 안드로이드 앱을 구동해주는 dalvik 가상머신과 코어 라이브러리까지 포함하는 영역입니다.

어플리케이션 프레임워크는 사용자의 입력(액티비티, 윈도우, 컨텐츠, 뷰, 노티피케이션 등) 또는 특정한 이벤트에 따라 출력을 담당하는 환경을 말합니다. 마지막으로 실제로 동작하는 앱이 설치되는 환경인 어플리케이션이 있습니다.

## 안드로이드는 다른 플랫폼에 비해 어떤 장점이 있는가?

첫째로 안드로이드를 구성하는 모든 소스가 오픈소스로 무료로 개방되어있어 비용적인 부담이 없습니다. 또한 전 세계의 수많은 개발자로부터 피드백을 받아 수정되기 때문에 안정성과 버그 수정이 빠릅니다. 그 밖에도 원한다면 소스를 다운 받아 수정해서 쓰기 편리합니다. 둘째로 자바를 주 언어로 사용하고 있기 때문에 많은 세계적으로 점유율이 높은 자바 개발자들이 쉽게 개발할 수 있습니다. 셋째로 리눅스 커널을 OS로 채택했기 때문에 다양한 하드웨어에 대한 드라이버 소스가 풍부합니다. 마지막으로 구글의 다양한 앱과 연동이 매우 편리하며 다른 플랫폼에 비해 앱간 연동에 너그러운편입니다.

## 안드로이드 프로젝트 구성요소에 대해서 설명하시오.

libs : 프로젝트에서 사용하는 다양한 라이브러리 소스가 저장되는 공간입니다.

androidTest : 앱의 일부 코드를 테스트하기 위한 소스를 저장하는 공간입니다.

java : 자바 코드를 저장하는 공간입니다. 표준 자바와 동일하게 패키지를 이용한 하위 디렉토리 생성 방식을 사용합니다.

res : 리소스(이미지, xml 레이아웃, 메뉴, 값)를 저장하는 공간입니다.

AndroidManifest.xml : 앱에 대한 전체적인 정보를 담고있는 파일입니다. 앱의 구성요소와 실행 권한 정보가 정의되어있습니다.

project > build.gradle : 프로그래머가 직접 작성한 그래들 빌드 스크립트 파일입니다.

gradle > build.gradle : 앱에 대한 컴파일 버전정보, 의존성 프로젝트에 대한 정의가 되어있는 파일입니다.

## 안드로이드에서 다국어 지원을 위해 해야할 작업

다국어 지원을 위해서는 value resource file을 따로 생성해주는 방식으로 사용합니다.

'values > 마우스 오른쪽 버튼 클릭 > value resource file > 리소스 파일 이름을 strings로 입력 > available qualifiers 탭에서 locale 선택 > language 탭에서 언어 선택 > specific region only에서 세부 국가 선택'

파일을 생성하면 디렉토리의 이름은 values-국가코드(예를 들어 values-kr) 형식으로 생성되며 내부에 strings.xml 파일이 생성됩니다. 해당 파일에 string의 name 값은 동일하게 유지한 후 해당 국가의 언어로 번역하여 추가하면됩니다.

## 안드로이드 매니페스트(android manifest)

안드로이드 매니페스트는 앱의 이름, 버전, 구성요소, 권한 등 앱의 실행에 있어서 필요한 각종 정보가 저장되어있는 파일입니다. 반드시 존재해야하는 xml 형식의 파일로 안드로이드 프로젝트의 최상위에 위치하고 있습니다.

가장 최상위는 manifest 태그가 위치하고 있습니다. manifest 태그에는 패키지명, 앱 버전 코드, 앱 버전 이름을 정의합니다.

application 태그에는 앱 아이콘, 앱 이름을 정의합니다.

activity 태그에는 액티비티의 클래스명과 액티비티 이름을 정의합니다. 하위에는 intent-filter 태그를 이용하여 액티비티에 대한 인텐트 작업시 필요한 action과 category를 정의합니다.

service, receiver, provider 태그에는 각각 서비스, 리시버, 프로바이더에 대한 내용을 정의합니다.

permission 태그에는 앱에서 필요한 권한에 내용을 정의합니다.

그 밖에 최소 안드로이드 SDK 버전을 지정하는 uses-sdk와 다른 패키지를 등록할 수 있는 uses-library 태그 등이 존재합니다.

## 디스플레이(display), 윈도우(window), 서피스(surface), 뷰(view), 뷰 그룹(view group), 뷰 컨테이너(view container), 레이아웃(layout)에 대해서 설명

디스플레이 : 안드로이드 단말기가 가지고 있는 하드웨어 화면을 의미합니다.

윈도우 : 안드로이드에서 실행되는 앱이 그림(뷰)을 그릴 수 있는 영역을 의미합니다. 사용자로부터 입력(터치, 키) 이벤트를 받아 앱에 전달합니다.

서피스 : 윈도우에 그림(뷰)을 그릴 때 그림이 저장되는 메모리 버퍼를 의미합니다.

뷰 : 사용자 인터페이스를 구성하는 최상위 클래스를 말합니다. 윈도우의 서피스를 이용하여 화면에 어떤 모양으로 그림을 그릴지와 발생하는 이벤트를 어떻게 처리할 것인지에 대한 기능을 구현하고 있습니다. 뷰 중에서 일반적인 제어 역할을 하고 있는 것들을 위젯이라고 합니다.

뷰 그룹 : 여러개의 뷰를 포함하고 있는 뷰를 의미합니다.

뷰 컨테이너 : 다른 뷰를 포함할 수 있는 뷰를 의미합니다. 대표적으로 리스트 뷰(list view), 스크롤 뷰(scroll view), 그리드 뷰(grid view) 등이 있습니다.

레이아웃 : 뷰 그룹 중에서 내부에 뷰를 포함하고 있으면서 해당 뷰를 어떻게 윈도우에 배치할지 정의하는 관리자 역할을 하는 클래스 말합니다.

## 인플레이션(inflation)

xml 레이아웃 파일로 정의한 정보를 런타임에 setContentView 메소드가 호출됨에 따라 메모리 상에 객체로 만들어주는 과정을 말합니다. 이 과정에서 xml 레이아웃 파일에서 뷰에 id를 설정하고 해당 id가 R.java 파일에 주소 값으로 환원되며 findViewById 메소드와 id를 이용하여 코드 상으로 뷰 객체를 가져와 제어할 수 있습니다.

## 안드로이드에서 색상을 지정하는 다양한 방식은 어떤 것들이 있는가?

#RGB, #ARGB, #RRGGBB, #AARRGGBB 총 4가지 방식이 있습니다. R은 붉은색, G는 초록색, B는 파란색의 정도를 나타내며 A는 알파 값 즉 투명도를 나타내는 수치입니다. 각각의 요소는 16진수(0부터 F까지)로 표현합니다.

## 안드로이드의 크기를 표현하는 다양한 표현방법에 대해서 설명하시오.

픽셀(px) : 화면의 픽셀을 의미합니다.

밀도 독립적 픽셀(dp, dip) : 160dpi(160인치에 들어가있는 픽셀 수) 화면을 기준으로 한 픽셀을 의미합니다.

축척 독립적 픽셀(sp, sip) : 가변 글꼴을 기준으로 한 픽셀을 의미합니다. 글꼴의 설정에 따라 차이가 있습니다.

텍스트 크기(em) : 글꼴과 상관없이 동일한 텍스트 크기를 표시하기 위한 단위입니다.

그 외 인치(in), 밀리미터(mm)가 있습니다.

## 안드로이드 MVC 모델은 어떻게 구성되어있는가?

- 안드로이드에서 뷰는 화면에 실제로 보이는 구성을 만드는 영역으로 View 클래스를 상속하는 클래스를 이용하여 구성할 수 있습니다.
- 컨트롤러는 뷰와 모델을 서로 연결하며 제어하는 영역으로 액티비티, 서비스, 브로드캐스트 리시버, 프래그먼트로 구성됩니다.
- 모델은 앱의 다양한 데이터를 저장하는 역할로 SQLite를 이용한 DB, SharedPreference를 이용한 파일 시스템, 콘텐트 프로바이더가 있습니다.

## 액티비티(activity)가 무엇인지와 액티비티 생명주기에 대해서 설명하시오.

안도르이드에서 화면을 관리하며 사용자가 발생시키는 다양한 이벤트를 처리하는 컴포넌트입니다.

부모 액티비티에서 새로운 자식 액티비티를 실행하고자 한다면 먼저 매니페스트 파일에 해당 자식 액티비티를 추가 해줘야합니다. 다음으로 부모 액티비티에서 startActivity 메소드에 인텐트를 파라미터로 넘겨 실행하거나 startActivities 메소드를 이용하여 여러개의 액티비티를 한꺼번에 실행할 수 있습니다.

액티비티의 실행과정은 첫 번째로 부모 액티비티에서 자식 액티비티를 생성 및 호출합니다. 두 번째로 액티비티 매니저 서비스가 해당 앱 프로세스에서 인텐트를 복사해온 후 매니페스트 파일에서 해당 인텐트에 명시되어있는 액티비티를 찾고 어떻게 실행시켜야할지 결정합니다. 세 번째로 찾아낸 액티비티를 실행하고 다시 해당 앱 프로세스에 인텐트를 복사하여 넘겨줍니다. 그 외 자식 액티비티 내의 onCreate 메소드에서 setContentView 메소드에 레이아웃의 아이디를 파라미터로 넘겨 해당 액티비티의 화면을 구성하게됩니다.

액티비티는 크게 3가지 상태가 존재합니다. 먼저 실행(running) 상태는 액티비티 스택의 최상위에 있으며 포커스를 가지고 있어 사용자에게 보이는 상태입니다. 다음으로 일시 중지(paused) 상태는 사용자에게 보이기는 하지만 다른 액티비티가 위에 있어 포커스를 받지 못하는 상태를 말합니다. 예를들어 대화상자가 위에 있어 일부가 가려져 있는 경우를 말합니다. 마지막으로 중지 (stopped) 상태는 다른 액티비티에 의해 완전히 가려져 보이지 않는 상태를 말합니다.

액티비티가 처음 만들어지면 onCreate 메소드가 호출되어 레이아웃을 구성합니다. 이후 onStart 메소드가 화면에 보이기 직전에 호출됩니다. 다음으로 onResume 메소드가 사용자 상호작용(화면이 포커스를 얻었을 때)하기 바로 전에 호출됩니다. 이 3가지 메소드가 호출되어 액티비티는 실행 상태를 갖게됩니다. 이후 포커스를 잃었을 때 onPause 메소드가 호출되고 일시 중지 상태가 됩니다. 일시 중지 상태에서 다시 포커스를 획득하면 onResume 메소드가 호출되거나 다른 액티비티에 의해서 완전히 화면이 가려졌는지 여부를 확인하여 가려져 보이지 않는 경우 onStop 메소드가 호출되어 중지 상태가됩니다. 정지 상태에서 다시 화면이 보이기 직전에 onRestart 메소드가 호출되고 onStart 메소드가 차례로 호출됩니다. 그 외 finish 메소드가 실행되어 해당 액티비티가 종료되기 직전에 onDestroy 메소드가 실행됩니다.

가끔은 일시 중지나 중지 상태에서 시스템이 메모리가 부족하다고 판단될 경우 onCreate 메소드부터 다시 해당 액티비티를 구동합니다. 이 경우 onStop, onResume 메소드 호출이 생략됩니다. 따라서 onSaveInstanceState, onRestoreInstanceState 메소드를 이용하여 액티비티가 갑자기 죽을 것을 대비해서 상태를 저장하고 복원하기 위한 작업을 정의해줄 수 있습니다.

## 액티비티간 데이터 전달에서 임의의 클래스 객체를 바로 전달하지 못하는 이유는 무엇이고 전달하기 위해서는 어떤 처리가 필요한가?

액티비티간 전달할 수 있는 데이터의 type은 보통 기본형으로 정해져있습니다. 그 이유는 인텐트를 이용하여 액티비티의 데이터를 전달하는 과정에서 현재 실행중인 앱 프로세스가 시스템 프로세스로 실행중인 액티비티 매니저 서비스 프로세스에게 인텐트를 전달합니다. 이 경우 프로세스간 통신이기 때문에 인텐트에 있는 값들을 복사하여 넘기는 방식으로 처리되기 때문에 객체 주소를 바로 넘기지 못하는 문제가 발생합니다. 따라서 이 문제를 해결하기 위해 자신이 임의로 만든 클래스 객체를 전달하기 위해서는 Serilizable이나 Parcelable 인터페이스를 상속받아 객체를 직렬화하여 넘기는 방식을 사용해야합니다.

## 부모 액티비티에서 자식 액티비티의 결과 값을 받아오기 위해 어떻게 해야하는가?

먼저 부모 액티비티에서 startActivityForResult 메소드를 이용하여 인텐트와 리퀘스트 코드를 파라미터로 넘깁니다. 이후 자식 액티비티에서 setResult 메소드에 결과 코드와 데이터를 파라미터로 넘깁니다. 다시 부모 액티비티에서 onActivityResult 메소드를 오버라이딩하여 자식 액티비티에서 보낸 결과 코드와 데이터를 받아 처리하는 코드를 작성할 수 있습니다. 이후 실행과정에서 자식 액티비티의 finish 메소드가 호출되면 부모 액티비티가 다시 화면에 나타나면서 onResume 메소드가 실행됩니다. 이때 onActivityResult 메소드가 작동하게 됩니다.

## 서비스(service)가 무엇인지와 서비스 생명주기

서비스는 백그라운드에서 실행되는 구성 요소입니다. 서비스는 사용자에게 보이는 화면이 존재하지 않으며, 정해지지 않은 시간 동안 운영됩니다. 각각의 서비스는 매니페스트 파일에 서비스 태그를 이용하여 선언해야합니다. 서비스는 Service 클래스를 상속받아 onStartCommand 또는 onBind 메소드를 재정의하여 구현할 수 있습니다.

서비스는 다른 구성 요소들처럼 메인 쓰레드에서 동작합니다. 따라서 CPU를 많이 사용하거나 대기 상태를 필요로 하는 경우 새로운 쓰레드를 이용하여 생성해야합니다. 또한 서비스의 객체는 단말에서 오직 1개만 생성되어 관리합니다.

먼저 서비스가 startService 메소드로 실행되는 경우 서비스가 생성될 때 onCreate 메소드가 실행됩니다. 이후 서비스가 실행을 시작할 때 onStartCommand 메소드가 호출되며 서비스의 상태가 실행중으로 변경됩니다. 이후 stopService 메소드가 실행되면 서비스가 종료되며 onDestroy 메소드를 호출하며 서비스의 상태가 종료로 변경됩니다.

다음으로 서비스가 bindService 메소드로 실행되는 경우 서비스가 생성될 때 onBind 메소드가 호출됩니다. 다음으로 unbindService 메소드가 호출되어 바인딩이 해제되면 onUnbind 메소드가 호출됩니다. 이후 완전히 종료될 때 onDestroy 메소드가 호출됩니다.

## 어플리케이션(application)과 컨텍스트(context)에 대해서 설명하시오.

어플리케이션 앱 프로세스가 실행되면 가장 먼저 생성되는 객체로 하나의 어플리케이션 객체는 하나의 앱 프로세스와 대응됩니다. 앱이 백그라운드로 내려가도 앱 프로세스는 계속 살아있기 때문에 어플리케이션 객체도 살아있다고 할 수 있습니다.

컨텍스트는 안드로이드의 컴포넌트들이 동작하기 위해 필요한 정보를 담고 있는 객체를 말합니다. 각각의 컴포넌트들(액티비티, 서비스, 브로드캐스트 리시버 등)은 자신만의 컨텍스트를 가지고 있습니다. 컨텍스트 내에는 어플리케이션의 정보(패키지명 등), 컨텍스트가 실행되는데 필요한 정보(테마 등)를 얻거나 시스템 서비스(윈도우 매니저, 레이아웃 인플레이터 등)를 구동하는데 사용됩니다.

## 노티피케이션(notification)은 무엇인가?

## 안드로이드에서 로그(log)를 출력하는 방법과 종류를 설명하시오.

## 스타일(style), 테마(theme)에 대해서 설명하시오.

## 프레그먼트(fragment)가 와 프레그먼트 생명주기에 설명하시오.

프레그먼트는 액티비티의 일부분에만 배치되는 화면 및 동작을 조작하기 위한 객체입니다. 안드로이드 3.0(허니콤)에서 화면이 비교적 큰 태블릿의 등장으로 작은 단위의 화면의 생명주기 관리할 필요가 있어 추가되었습니다. 프레그먼트 매니저를 통해서 여러개의 프레그먼트를 조작할 수 있습니다. 레이아웃 xml 파일에서 다른 뷰들과 함께 배치될 수 있습니다.

액티비티가 생성되면 프레그먼트 매니저는 초기화(initializing) 상태가 됩니다. 프레그먼트가 매니저에 의해 추가되면 onAttach, onAttachFragment, onCreate 메소드가 차례로 실행됩니다. 다음으로 액티비티의 onCreate 메소드 호출 이후 매니저는 생성(created) 상태로 변경됩니다. 이때 onCreateView, onViewCreated, onActivityCreated 메소드가 차례로 호출됩니다. 다음으로 액티비티의 onStart 메소드가 호출되면 매니저는 시작(started) 상태로 onStart 메소드를 호출합니다. 이후 액티비티의 onResume 메소드가 호출되면 매니저 역시 재시작(resume) 상태로 변하며 onResume 메소드를 호출합니다. 그 외 액티비티가 화면에서 보이지 않을경우 호출되는 onStop 메소드 호출 이후 매니저는 중지(stop) 상태가 되며 액티비티의 onDestroy 메소드 호출 이후 매니저는 onDestroyView 메소드를 호출합니다.

## 뷰 홀더 패턴(view holder pattern)에 대해서 설명하시오.

## 나인패치(9patch)란 무엇인가?

## 태스크(task)란 무엇인가?

예를들어 어떤 앱에서 앨범 앱을 실행하는 기능이 있다면 이 앱은 두개의 앱을 실행하는 형태가 되지만 사용자 입장에서는 하나의 앱에서 화면이 전환된다고 판단합니다. 이와 같은 사용자 입장에서 논리적인 화면 구성의 단위를 태스크라고 말합니다.

## 안드로이드의 메모리 관리 방식에 대해서 설명하시오.

안드로이드는 액티비티, 서비스, 리시버, 프로바이더를 실행하기 위해 앱이 실행되는 과정에서 프로세스를 생성합니다. 실행중인 모든 앱은 컴포넌트가 모두 종료되어도 다음에 이 앱을 다시 실행할 가능성이 높기 때문에 프로세스를 바로 제거하지 않습니다. 바로 종료하지 않는 이유는 앱을 실행하기 위해 프로세스를 생성하는 과정에서 딜레이가 발생하는데 이 딜레이를 줄이기 위함입니다. 따라서 사용자에 의해 다시 앱이 실행되면 남아있던 프로세스가 존재하는 경우 바로 실행됩니다. 이 과정에서 쌓여있던 많은 프로세스로 인해 메모리가 부족해지는 경우 프로세스의 우선순위(사용빈도)에 따라 프로세스를 종료하여 메모리를 확보합니다.

## 안드로이드의 쓰레드(thread)와 쓰레드 핸들러(thread handler)에 대해서 설명하시오.

## NDK에 대해서 설명하라.

## NDK에서 로그캣(logcat)에 로그를 출력하기 위해 어떻게 해야하는가?

android/log.h 헤더를 임포트 한 후 \_\_android_log_print 메소드를 호출하여 NDK 환경에서 로그캣에 로그를 출력할 수 있습니다.

```cpp
#include <android/log.h>
...중략...
\_\_android_log_print(ANDROID_LOG_VERBOSE, "com.example", "hello world!", 1);
```

---

## naver

## 서비스 / 브로드캐스트 리시버 / 콘텐트 프로바이더를 사용해본 적이 있나요? 언제 사용해봤나요?

## 액티비티의 생명 주기에 호출되는 콜백 함수는 어떤 것들이 있나요?

## 액티비티에서 뒤로 가기 버튼을 눌렀을 때는 어떤 콜백이 호출될까요?

## 그렇다면 액티비티에서 홈 버튼을 눌렀을 때는 어떤 콜백이 호출될까요?

## 코틀린으로 개발을 했던데 왜 코틀린을 선택했나요?

## 코틀린을 사용해본 감상?

## 서피스, 윈도우 개념

## 액티비티가 다이얼로그 가려졌을 때 어떤 콜백이 호출될까?

## 그렇다면 액티비티가 또 다른 투명 액티비티에 의해 가려졌다면?

## 그렇다면 화면을 꽉 채우는 다이얼로그에 의해 가려졌다면?

## 스트링을 파라미터로 받아서, 그것을 역순으로 리턴하는 함수를 코딩해보세요.

## 가장 인상 깊은, 자랑스러운 성취?

## 현재 스타트업 재직 중인데 대기업 문화에 잘 적응할 수 있는지?

## GC 메커니즘에 대해 아는 대로 설명해보면?

## 어떤 파일을 다운로드 받고 있을 때 진행 상황을 표시하려면 어떻게 해야할까?

## 특정 시간에 데이터를 받아 갱신하고 싶다면 어떻게 코드를 짜겠어요?

## 왜 메인스레드에서 돌리면 안되는지 커널 관점에서 설명해보세요.

## Git 잘 쓰시나요?

## 해쉬테이블 탐색에 걸리는 시간?

## Google IO 발표된 기술 중 아는 것?

## 제일 편한 언어? 자바는 잘 쓸 수 있는지?

## 개발했던 앱에서 "안드로이드적"인 요소?

## 액티비티가 갑자기 종료됐을 때를 대비한 콜백이 있는데 아는지?

## 그 콜백이 언제 불릴지?

## Stack 2개를 이용해서 Queue 처럼 거동하는 클래스를 정의해보세요.

## 액티비티 스택: A, B, C 가 있는 상황에서 B를 런칭하고 여기서 백버튼 눌렀을 때 A가 뜨게 하고 싶다면? 스택 개념과 액티비티 생명주기 연결해서 설명해보세요.

## 액티비티 스택2: A, B, C, D, E가 있는 상황에서 차례대로 액티비티를 전환할 때 각 액티비티의 스샷을 따고 싶다. 어떤 콜백을 이용해야 할까?

## 1440\*2880 비트맵을 만들면 용량이 어느정도 나올까?

## 이미지 다뤄본 적?

## 이번 구글IO 에서 기억에 남는 발표?(2번 면접관님도 비슷한 거 물어보셨는데 화장실 갔을 때 검색이라도 해볼걸... 그런데 어디 대답 제대로 못한 게 한두 개여야지)

## 웹뷰API 중 기억에 나는 것?

## 여기도 결국 회사일 뿐이다. 위에서 시키는 대로 해야하고 멍청한 결정도 많이 내려오곤 하는데 잘 적응할 수 있을지?

1. What is Application?
   The Application class in Android is the base class within an Android app that contains all other components such as activities and services. The Application class, or any subclass of the Application class, is instantiated before any other class when the process for your application/package is created.
2. What is Context?
   A Context is a handle to the system; it provides services like resolving resources, obtaining access to databases and preferences, and so on. An Android app has activities. Context is like a handle to the environment your application is currently running in.
   Application Context: This context is tied to the lifecycle of an application. The application context can be used where you need a context whose lifecycle is separate from the current context or when you are passing a context beyond the scope of an activity.
   Activity Context: This context is available in an activity. This context is tied to the lifecycle of an activity. The activity context should be used when you are passing the context in the scope of an activity or you need the context whose lifecycle is attached to the current context.
3. What is Armv7?
   There are 3 CPU architectures in Android. ARMv7 is the most common as it is optimised for battery consumption. ARM64 is an evolved version of that that supports 64-bit processing for more powerful computing. ARMx86, is the least used for these three, since it is not battery friendly. It is more powerful than the other two.
4. Why bytecode cannot be run in Android?
   Android uses DVM (Dalvik Virtual Machine ) rather using JVM(Java Virtual Machine).
5. What is a BuildType in Gradle? And what can you use it for?
   Build types define properties that Gradle uses when building and packaging your Android app.
   A build type defines how a module is built, for example whether ProGuard is run.
   A product flavour defines what is built, such as which resources are included in the build.
   Gradle creates a build variant for every possible combination of your project’s product flavours and build types.
6. Explain the build process in Android:
   First step involves compiling the resources folder (/res) using the aapt (android asset packaging tool) tool. These are compiled to a single class file called R.java. This is a class that just contains constants.
   Second step involves the java source code being compiled to .class files by javac, and then the class files are converted to Dalvik bytecode by the “dx” tool, which is included in the sdk ‘tools’. The output is classes.dex.
   The final step involves the android apkbuilder which takes all the input and builds the apk (android packaging key) file.
7. What is the Android Application Architecture?
   Android application architecture has the following components:
   Services − It will perform background functionalities
   Intent − It will perform the inter connection between activities and the data passing mechanism
   Resource Externalization − strings and graphics
   Notification − light, sound, icon, notification, dialog box and toast
   Content Providers − It will share the data between applications
8. Describe activities
   Activities are basically containers or windows to the user interface.
9. Lifecycle of an Activity
   OnCreate(): This is when the view is first created. This is normally where we create views, get data from bundles etc.
   OnStart(): Called when the activity is becoming visible to the user. Followed by onResume() if the activity comes to the foreground, or onStop() if it becomes hidden.
   OnResume(): Called when the activity will start interacting with the user. At this point your activity is at the top of the activity stack, with user input going to it.
   OnPause(): Called as part of the activity lifecycle when an activity is going into the background, but has not (yet) been killed.
   OnStop(): Called when you are no longer visible to the user.
   OnDestroy(): Called when the activity is finishing
   OnRestart(): Called after your activity has been stopped, prior to it being started again
10. What’s the difference between onCreate() and onStart()?
    The onCreate() method is called once during the Activity lifecycle, either when the application starts, or when the Activity has been destroyed and then recreated, for example during a configuration change.
    The onStart() method is called whenever the Activity becomes visible to the user, typically after onCreate() or onRestart().
11. Scenario in which only onDestroy is called for an activity without onPause() and onStop()?
    If finish() is called in the OnCreate method of an activity, the system will invoke onDestroy() method directly.
12. Why would you do the setContentView() in onCreate() of Activity class?
    As onCreate() of an Activity is called only once, this is the point where most initialisation should go. It is inefficient to set the content in onResume() or onStart() (which are called multiple times) as the setContentView() is a heavy operation.
13. onSavedInstanceState() and onRestoreInstanceState() in activity?
    OnRestoreInstanceState() - When activity is recreated after it was previously destroyed, we can recover the saved state from the Bundle that the system passes to the activity. Both the onCreate() and onRestoreInstanceState() callback methods receive the same Bundle that contains the instance state information. But because the onCreate() method is called whether the system is creating a new instance of your activity or recreating a previous one, you must check whether the state Bundle is null before you attempt to read it. If it is null, then the system is creating a new instance of the activity, instead of restoring a previous one that was destroyed.
    onSaveInstanceState() - is a method used to store data before pausing the activity.
14. Launch modes in Android?
    Standard: It creates a new instance of an activity in the task from which it was started. Multiple instances of the activity can be created and multiple instances can be added to the same or different tasks.
    Eg: Suppose there is an activity stack of A -> B -> C.
    Now if we launch B again with the launch mode as “standard”, the new stack will be A -> B -> C -> B.
    SingleTop: It is the same as the standard, except if there is a previous instance of the activity that exists in the top of the stack, then it will not create a new instance but rather send the intent to the existing instance of the activity.
    Eg: Suppose there is an activity stack of A -> B.
    Now if we launch C with the launch mode as “singleTop”, the new stack will be A -> B -> C as usual.
    Now if there is an activity stack of A -> B -> C.
    If we launch C again with the launch mode as “singleTop”, the new stack will still be A -> B -> C.
    SingleTask: A new task will always be created and a new instance will be pushed to the task as the root one. So if the activity is already in the task, the intent will be redirected to onNewIntent() else a new instance will be created. At a time only one instance of activity will exist.
    Eg: Suppose there is an activity stack of A -> B -> C -> D.
    Now if we launch D with the launch mode as “singleTask”, the new stack will be A -> B -> C -> D as usual.
    Now if there is an activity stack of A -> B -> C -> D.
    If we launch activity B again with the launch mode as “singleTask”, the new activity stack will be A -> B. Activities C and D will be destroyed.
    SingleInstance: Same as single task but the system does not launch any activities in the same task as this activity. If new activities are launched, they are done so in a separate task.
    Eg: Suppose there is an activity stack of A -> B -> C -> D. If we launch activity B again with the launch mode as “singleInstance”, the new activity stack will be:
    Task1 — A -> B -> C
    Task2 — D
15. How does the activity respond when the user rotates the screen?
    When the screen is rotated, the current instance of activity is destroyed a new instance of the Activity is created in the new orientation. The onRestart() method is invoked first when a screen is rotated. The other lifecycle methods get invoked in the similar flow as they were when the activity was first created.
16. How to prevent the data from reloading and resetting when the screen is rotated?
    The most basic approach would be to use a combination of ViewModels and onSaveInstanceState() . So how we do we that?
    Basics of ViewModel: A ViewModel is LifeCycle-Aware. In other words, a ViewModel will not be destroyed if its owner is destroyed for a configuration change (e.g. rotation). The new instance of the owner will just re-connected to the existing ViewModel. So if you rotate an Activity three times, you have just created three different Activity instances, but you only have one ViewModel.
    So the common practice is to store data in the ViewModel class (since it persists data during configuration changes) and use OnSaveInstanceState to store small amounts of UI data.
    For instance, let’s say we have a search screen and the user has entered a query in the Edittext. This results in a list of items being displayed in the RecyclerView. Now if the screen is rotated, the ideal way to prevent resetting of data would be to store the list of search items in the ViewModel and the query text user has entered in the OnSaveInstanceState method of the activity.
17. Mention two ways to clear the back stack of Activities when a new Activity is called using intent
    The first approach is to use a FLAG_ACTIVITY_CLEAR_TOP flag. The second way is by using FLAG_ACTIVITY_CLEAR_TASK and FLAG_ACTIVITY_NEW_TASK in conjunction.
18. What’s the difference between FLAG*ACTIVITY_CLEAR_TASK and FLAG_ACTIVITY_CLEAR_TOP?
    FLAG_ACTIVITY_CLEAR_TASK is used to clear all the activities from the task including any existing instances of the class invoked. The Activity launched by intent becomes the new root of the otherwise empty task list. This flag has to be used in conjunction with FLAG* ACTIVITY_NEW_TASK.
    FLAG_ACTIVITY_CLEAR_TOP on the other hand, if set and if an old instance of this Activity exists in the task list then barring that all the other activities are removed and that old activity becomes the root of the task list. Else if there’s no instance of that activity then a new instance of it is made the root of the task list. Using FLAG_ACTIVITY_NEW_TASK in conjunction is a good practice, though not necessary.
19. Describe content providers
    A ContentProvider provides data from one application to another, when requested. It manages access to a structured set of data. It provides mechanisms for defining data security. ContentProvider is the standard interface that connects data in one process with code running in another process.
    When you want to access data in a ContentProvider, you must instead use the ContentResolver object in your application’s Context to communicate with the provider as a client. The provider object receives data requests from clients, performs the requested action, and returns the results.
20. Access data using Content Provider:
    Start by making sure your Android application has the necessary read access permissions. Then, get access to the ContentResolver object by calling getContentResolver() on the Context object, and retrieving the data by constructing a query using ContentResolver.query().
    The ContentResolver.query() method returns a Cursor, so you can retrieve data from each column using Cursor methods.
21. Describe services
    A Service is an application component that can perform long-running operations in the background, and it doesn't provide a user interface. It can run in the background, even when the user is not interacting with your application. These are the three different types of services:
    Foreground Service: A foreground service performs some operation that is noticeable to the user. For example, we can use a foreground service to play an audio track. A Notification must be displayed to the user.
    Background Service: A background service performs an operation that isn’t directly noticed by the user. In Android API level 26 and above, there are restrictions to using background services and it is recommended to use WorkManager in these cases.
    Bound Service: A service is bound when an application component binds to it by calling bindService(). A bound service offers a client-server interface that allows components to interact with the service, send requests, receive results. A bound service runs only as long as another application component is bound to it.
22. Difference between Service & Intent Service
    Service is the base class for Android services that can be extended to create any service. A class that directly extends Service runs on the main thread so it will block the UI (if there is one) and should therefore either be used only for short tasks or should make use of other threads for longer tasks.
    IntentService is a subclass of Service that handles asynchronous requests (expressed as “Intents”) on demand. Clients send requests through startService(Intent) calls. The service is started as needed, handles each Intent in turn using a worker thread, and stops itself when it runs out of work.
23. Difference between AsyncTasks & Threads?
    Thread should be used to separate long running operations from main thread so that performance is improved. But it can’t be cancelled elegantly and it can’t handle configuration changes of Android. You can’t update UI from Thread.
    AsyncTask can be used to handle work items shorter than 5ms in duration. With AsyncTask, you can update UI unlike java Thread. But many long running tasks will choke the performance.
24. Difference between Service, Intent Service, AsyncTask & Threads
    Android service is a component that is used to perform operations on the background such as playing music. It doesn’t has any UI (user interface). The service runs in the background indefinitely even if application is destroyed.
    AsyncTask allows you to perform asynchronous work on your user interface. It performs the blocking operations in a worker thread and then publishes the results on the UI thread, without requiring you to handle threads and/or handlers yourself.
    IntentService is a base class for Services that handle asynchronous requests (expressed as Intents) on demand. Clients send requests through startService(Intent) calls; the service is started as needed, handles each Intent in turn using a worker thread, and stops itself when it runs out of work.
    A thread is a single sequential flow of control within a program. Threads can be thought of as mini-processes running within a main process.
25. What are Handlers?
    Handlers are objects for managing threads. It receives messages and writes code on how to handle the message. They run outside of the activity’s lifecycle, so they need to be cleaned up properly or else you will have thread leaks.
    Handlers allow communicating between the background thread and the main thread.
    A Handler class is preferred when we need to perform a background task repeatedly after every x seconds/minutes.
26. What is a Job Scheduling?
    Job Scheduling api, as the name suggests, allows to schedule jobs while letting the system optimize based on memory, power, and connectivity conditions. The JobScheduler supports batch scheduling of jobs. The Android system can combine jobs so that battery consumption is reduced. JobManager makes handling uploads easier as it handles automatically the unreliability of the network. It also survives application restarts. Some scenarios:
    Tasks that should be done once the device is connect to a power supply
    Tasks that require network access or a Wi-Fi connection.
    Task that are not critical or user facing
    Tasks that should be running on a regular basis as batch where the timing is not critical
    You can click on this link to learn more about Job Schedulers.
27. What is the relationship between the life cycle of an AsyncTask and an Activity? What problems can this result in? How can these problems be avoided?
    An AsyncTask is not tied to the life cycle of the Activity that contains it. So, for example, if you start an AsyncTask inside an Activity and the user rotates the device, the Activity will be destroyed (and a new Activity instance will be created) but the AsyncTask will not die but instead goes on living until it completes.
    Then, when the AsyncTask does complete, rather than updating the UI of the new Activity, it updates the former instance of the Activity (i.e., the one in which it was created but that is not displayed anymore!). This can lead to an Exception (of the type java.lang.IllegalArgumentException: View not attached to window manager if you use, for instance, findViewById to retrieve a view inside the Activity).
    There’s also the potential for this to result in a memory leak since the AsyncTask maintains a reference to the Activity, which prevents the Activity from being garbage collected as long as the AsyncTask remains alive.
    For these reasons, using AsyncTasks for long-running background tasks is generally a bad idea . Rather, for long-running background tasks, a different mechanism (such as a service) should be employed.
    Note: AsyncTasks by default run on a single thread using a serial executor, meaning it has only 1 thread and each task runs one after the other.
28. What is the onTrimMemory() method?
    onTrimMemory(): Called when the operating system has determined that it is a good time for a process to trim unneeded memory from its process. This will happen for example when it goes in the background and there is not enough memory to keep as many background processes running as desired.
    Android can reclaim memory for from your app in several ways or kill your app entirely if necessary to free up memory for critical tasks. To help balance the system memory and avoid the system’s need to kill your app process, you can implement the ComponentCallbacks2 interface in your Activity classes. The provided onTrimMemory() callback method allows your app to listen for memory related events when your app is in either the foreground or the background, and then release objects in response to app lifecycle or system events that indicate the system needs to reclaim memory. Reference
29. Android Bound Service
    A bound service is a service that allows other android components (like activity) to bind to it and send and receive data. A bound service is a service that can be used not only by components running in the same process as local service, but activities and services, running in different processes, can bind to it and send and receive data.
    When implementing a bound service we have to extend Service class but we have to override onBind method too. This method returns an object that implements IBinder, that can be used to interact with the service.
    Implementing Android bound service with Android Messenger
    Service based on Messenger can communicate with other components in different processes, known as Inter Process Communication (IPC), without using AIDL.
    A service handler: this component handles incoming requests from clients that interact with the service itself.
    A Messenger: this class is used to create an object implementing IBinder interface so that a client can interact with the service.
    Example Implementation: Link
30. AIDL vs Messenger Queue
    As Ariq Ahmad mentioned in the response, Messenger Queue builds us a queue and the data/messages are passed between 2 or more processes sequential. But in case of AIDL the messages are passed in parallel.
    AIDL is for the purpose when you’ve to go application level communication for data and control sharing, a scenario depicting it can be : An app requires list of all contacts from Contacts app (content part lies here) plus it also wants to show the call’s duration and you can also disconnect it from that app (control part lies here).
    In Messenger queues you’re more IN the application and working on threads and processes to manage the queue having messages so no Outside services interference here.
    Messenger is needed if you want to bind a remote service (e.g. running in another process).
31. What is a ThreadPool? And is it more effective than using several separate Threads?
    Creating and destroying threads has a high CPU usage, so when we need to perform lots of small, simple tasks concurrently, the overhead of creating our own threads can take up a significant portion of the CPU cycles and severely affect the final response time. ThreadPool consists of a task queue and a group of worker threads, which allows it to run multiple parallel instances of a task.
32. Difference between Serializable and Parcelable?
    Serialization is the process of converting an object into a stream of bytes in order to store an object into memory, so that it can be recreated at a later time, while still keeping the object’s original state and data.
    How to disallow serialization? We can declare the variable as transient.
    Serializable is a standard Java interface. Parcelable is an Android specific interface where you implement the serialization yourself. It was created to be far more efficient than Serializable (The problem with this approach is that reflection is used and it is a slow process. This mechanism also tends to create a lot of temporary objects and cause quite a bit of garbage collection.).
33. Difference between Activity & Service
    Activities are basically containers or windows to the user interface. Services is a component that is used to perform operations on the background. It does not have an UI.
34. How would you update the UI of an activity from a background service?
    We need to register a LocalBroadcastReceiver in the activity. And send a broadcast with the data using intents from the background service. As long as the activity is in the foreground, the UI will be updated from the background. Ensure to unregister the broadcast receiver in the onStop() method of the activity to avoid memory leaks. We can also register a Handler and pass data using Handlers. You can find more details on how to implement here.
35. What is an intent?
    Intents are messages that can be used to pass information to the various components of android. For instance, launch an activity, open a webview etc. Two types of intents-
    Implicit: Implicit intent is when you call system default intent like send email, send SMS, dial number.
    Explicit: Explicit intent is when you call an application activity from another activity of the same application.
36. What is a Sticky Intent?
    Sticky Intents allows communication between a function and a service. sendStickyBroadcast() performs a sendBroadcast(Intent) known as sticky, i.e. the Intent you are sending stays around after the broadcast is complete, so that others can quickly retrieve that data through the return value of registerReceiver(BroadcastReceiver, IntentFilter). For example, if you take an intent for ACTION_BATTERY_CHANGED to get battery change events: When you call registerReceiver() for that action — even with a null BroadcastReceiver — you get the Intent that was last Broadcast for that action. Hence, you can use this to find the state of the battery without necessarily registering for all future state changes in the battery.
37. What is a Pending Intent?
    If you want someone to perform any Intent operation at future point of time on behalf of you, then we will use Pending Intent.
38. What is an Action?
    Description of the intent. For instance, ACTION_CALL — used to perform calls
39. What are intent Filters?
    Specifies the type of intent that the activity/service can respond to.
40. Describe fragments:
    Fragment is a UI entity attached to Activity. Fragments can be reused by attaching in different activities. Activity can have multiple fragments attached to it. Fragment must be attached to an activity and its lifecycle will depend on its host activity.
41. Describe fragment lifecycle
    onAttach() : The fragment instance is associated with an activity instance.The fragment and the activity is not fully initialized. Typically you get in this method a reference to the activity which uses the fragment for further initialization work.
    onCreate() : The system calls this method when creating the fragment. You should initialize essential components of the fragment that you want to retain when the fragment is paused or stopped, then resumed.
    onCreateView() : The system calls this callback when it’s time for the fragment to draw its user interface for the first time. To draw a UI for your fragment, you must return a View component from this method that is the root of your fragment’s layout. You can return null if the fragment does not provide a UI.
    onActivityCreated() : The onActivityCreated() is called after the onCreateView() method when the host activity is created. Activity and fragment instance have been created as well as the view hierarchy of the activity. At this point, view can be accessed with the findViewById() method. example. In this method you can instantiate objects which require a Context object
    onStart() : The onStart() method is called once the fragment gets visible.
    onResume() : Fragment becomes active.
    onPause() : The system calls this method as the first indication that the user is leaving the fragment. This is usually where you should commit any changes that should be persisted beyond the current user session.
    onStop() : Fragment going to be stopped by calling onStop()
    onDestroyView() : Fragment view will destroy after call this method
    onDestroy() :called to do final clean up of the fragment’s state but Not guaranteed to be called by the Android platform.
42. What is the difference between fragments & activities. Explain the relationship between the two.
    An Activity is an application component that provides a screen, with which users can interact in order to do something whereas a Fragment represents a behavior or a portion of user interface in an Activity (with its own lifecycle and input events, and which can be added or removed at will).
43. When should you use a fragment rather than an activity?
    When there are ui components that are going to be used across multiple activities.
    When there are multiple views that can be displayed side by side (viewPager tabs)
    When you have data that needs to be persisted across Activity restarts (such as retained fragments)
44. Difference between adding/replacing fragment in backstack?
    replace removes the existing fragment and adds a new fragment. This means when you press back button the fragment that got replaced will be created with its onCreateView being invoked.
    add retains the existing fragments and adds a new fragment that means existing fragment will be active and they wont be in ‘paused’ state hence when a back button is pressed onCreateView is not called for the existing fragment(the fragment which was there before new fragment was added).
    In terms of fragment’s life cycle events onPause, onResume, onCreateView and other life cycle events will be invoked in case of replace but they wont be invoked in case of add.
45. Why is it recommended to use only the default constructor to create a Fragment?
    The reason why you should be passing parameters through bundle is because when the system restores a fragment (e.g on config change), it will automatically restore your bundle. This way you are guaranteed to restore the state of the fragment correctly to the same state the fragment was initialised with.
46. You’re replacing one Fragment with another — how do you ensure that the user can return to the previous Fragment, by pressing the Back button?
    We need to save each Fragment transaction to the backstack, by calling addToBackStack() before you commit() that transaction
47. Callbacks invoked during addition of a fragment to back stack and while popping back from back stack:
    addOnBackStackChangedListener is called when fragment is added or removed from the backstack. Checkout this link for reference.
48. What are retained fragments?
    By default, Fragments are destroyed and recreated along with their parent Activity’s when a configuration change occurs. Calling setRetainInstance(true) allows us to bypass this destroy-and-recreate cycle, signaling the system to retain the current instance of the fragment when the activity is recreated.
49. Difference between FragmentPagerAdapter vs FragmentStatePagerAdapter?
    FragmentPagerAdapter: the fragment of each page the user visits will be stored in memory, although the view will be destroyed. So when the page is visible again, the view will be recreated but the fragment instance is not recreated. This can result in a significant amount of memory being used. FragmentPagerAdapter should be used when we need to store the whole fragment in memory. FragmentPagerAdapter calls detach(Fragment) on the transaction instead of remove(Fragment).
    FragmentStatePagerAdapter: the fragment instance is destroyed when it is not visible to the User, except the saved state of the fragment. This results in using only a small amount of Memory and can be useful for handling larger data sets. Should be used when we have to use dynamic fragments, like fragments with widgets, as their data could be stored in the savedInstanceState.Also it won’t affect the performance even if there are large number of fragments.
50. What is Toast in Android?
    Android Toast can be used to display information for the short period of time. A toast contains message to be displayed quickly and disappears after sometime.
51. What are Loaders in Android?
    Loader API was introduced in API level 11 and is used to load data from a data source to display in an activity or fragment. Loaders persist and cache results across configuration changes to prevent duplicate queries.
    Checkout the Sample Implementation.
52. What is the difference between Dialog & DialogFragment?
    A fragment that displays a dialog window, floating on top of its activity’s window. This fragment contains a Dialog object, which it displays as appropriate based on the fragment’s state. Dialogs are entirely dependent on Activities. If the screen is rotated, the dialog is dismissed. Dialog fragments take care of orientation, configuration changes as well.
53. Difference between margin & padding?
    Padding will be space added inside the container, for instance, if it is a button, padding will be added inside the button. Margin will be space added outside the container.
54. What is View Group? How are they different from Views?
    View: View objects are the basic building blocks of User Interface(UI) elements in Android. View is a simple rectangle box which responds to the user’s actions. Examples are EditText, Button, CheckBox etc. View refers to the android.view.View class, which is the base class of all UI classes.
    ViewGroup: ViewGroup is the invisible container. It holds View and ViewGroup. For example, LinearLayout is the ViewGroup that contains Button(View), and other Layouts also. ViewGroup is the base class for Layouts.
55. What is the difference between a regular .png and a nine-patch image?
    It is one of a resizable bitmap resource which is being used as backgrounds or other images on the device. The NinePatch class allows drawing a bitmap in nine sections. The four corners are unscaled; the middle of the image is scaled in both axes, the four edges are scaled into one axis.
56. Difference between RelativeLayout and LinearLayout?
    Linear Layout — Arranges elements either vertically or horizontally. i.e. in a row or column.
    Relative Layout — Arranges elements relative to parent or other elements.
57. What is ConstraintLayout?
    It allows you to create large and complex layouts with a flat view hierarchy (no nested view groups). It’s similar to RelativeLayout in that all views are laid out according to relationships between sibling views and the parent layout, but it’s more flexible than RelativeLayout and easier to use with Android Studio’s Layout Editor.
    Checkout the Sample Implementation and you can read more about how to implement a simple app with ConstraintLayout here, by yours truly :)
58. When might you use a FrameLayout?
    Frame Layouts are designed to contain a single item, making them an efficient choice when you need to display a single View.
    If you add multiple Views to a FrameLayout then it’ll stack them one above the other, so FrameLayouts are also useful if you need overlapping Views, for example if you’re implementing an overlay or a HUD element.
59. What is Adapters?
    An adapter responsible for converting each data entry into a View that can then be added to the AdapterView (ListView/RecyclerView).
60. How to support different screen sizes?
    Create a flexible layout — The best way to create a responsive layout for different screen sizes is to use ConstraintLayout as the base layout in your UI. ConstraintLayout allows you to specify the position and size for each view according to spatial relationships with other views in the layout. This way, all the views can move and stretch together as the screen size changes.
    Create stretchable nine-patch bitmaps
    Avoid hard-coded layout sizes — Use wrap_content or match_parent. Create alternative layouts — The app should provide alternative layouts to optimise the UI design for certain screen sizes. For eg: different UI for tablets
    Use the smallest width qualifier — For example, you can create a layout named main_activity that’s optimised for handsets and tablets by creating different versions of the file in directories as follows:
    res/layout/main_activity.xml — For handsets (smaller than 600dp available width)
    res/layout-sw600dp/main_activity.xml — For 7” tablets (600dp wide and bigger).
    The smallest width qualifier specifies the smallest of the screen’s two sides, regardless of the device’s current orientation, so it’s a simple way to specify the overall screen size available for your layout.
61. Outline the process of creating custom Views:
    Create a class that Subclass a view
    Create a res/values/attrs.xml file and declare the attributes you want to use with your custom View.
    In your View class, add a constructor method, instantiate the Paint object, and retrieve your custom attributes.
    Override either onSizeChanged() or onMeasure().
    Draw your View by overriding onDraw().
    Checkout the Sample Implementation
62. Briefly describe some ways that you can optimize View usage
    Checking for excessive overdraw: install your app on an Android device, and then enable the “Debug GPU Overview” option.
    Flattening your view hierarchy: inspect your view hierarchy using Android Studio’s ‘Hierarchy Viewer’ tool.
    Measuring how long it takes each View to complete the measure, layout, and draw phases. You can also use Hierarchy Viewer to identify any parts of the rendering pipeline that you need to optimise.
63. Bitmap pooling in android?
    Bitmap pooling is a simple technique, that aims to reuse bitmaps instead of creating new ones every time. When you need a bitmap, you check a bitmap stack to see if there are any bitmaps available. If there are not bitmaps available you create a new bitmap otherwise you pop a bitmap from the stack and reuse it. Then when you are done with the bitmap, you can put it on a stack.
    Find more info here
64. How to load bitmap to memory?
    Checkout this article on it. I couldn’t have explained it better myself.
65. What are the permission protection levels in Android?
    Normal — A lower-risk permission that gives requesting applications access to isolated application-level features, with minimal risk to other applications, the system, or the user. The system automatically grants this type of permission to a requesting application at installation, without asking for the user’s explicit approval.
    Dangerous — A higher-risk permission. Any dangerous permissions requested by an application may be displayed to the user and require confirmation before proceeding, or some other approach may be taken to avoid the user automatically allowing the use of such facilities.
    Signature — A permission that the system grants only if the requesting application is signed with the same certificate as the application that declared the permission. If the certificates match, the system automatically grants the permission without notifying the user or asking for the user’s explicit approval.
    SignatureOrSystem — A permission that the system grants only to applications that are in the Android system image or that are signed with the same certificate as the application that declared the permission.
66. What is an Application Not Responding (ANR) error, and how can you prevent them from occurring in an app?
    An ANR dialog appears when your UI has been unresponsive for more than 5 seconds, usually because you’ve blocked the main thread. To avoid encountering ANR errors, you should move as much work off the main thread as possible.
67. What is a singleton class in Android?
    A singleton class is a class which can create only an object that can be shared all other classes.

I took references from this article to implement the below code. 68. What’s the difference between commit() and apply() in SharedPreferences?
commit() writes the data synchronously and returns a boolean value of success or failure depending on the result immediately.
apply() is asynchronous and it won’t return any boolean response. Also if there is an apply() outstanding and we perform another commit(). The commit() will be blocked until the apply() is not completed. 69. How does RecyclerView work?
RecyclerView is designed to display long lists (or grids) of items. Say we want to display 100 row of items. A simple approach would be to just create 100 views, one for each row and lay all of them out. But that would be wasteful because at any point of time, only 10 or so items could fit on screen and the remaining items would be off screen. So RecyclerView instead creates only the 10 or so views that are on screen. This way you get 10x better speed and memory usage.
But what happens when you start scrolling and need to start showing next views? Again a simple approach would be to create a new view for each new row that you need to show. But this way by the time you reach the end of the list you will have created 100 views and your memory usage would be the same as in the first approach. And creating views takes time, so your scrolling most probably wouldn’t be smooth. This is why RecyclerView takes advantage of the fact that as you scroll, new rows come on screen also old rows disappear off screen. Instead of creating new view for each new row, an old view is recycled and reused by binding new data to it.
This happens inside the onBindViewHolder() method. Initially you will get new unused view holders and you have to fill them with data you want to display. But as you scroll you will start getting view holders that were used for rows that went off screen and you have to replace old data that they held with new data. 70. How does RecyclerView differ from ListView?
ViewHolder Pattern: Recyclerview implements the ViewHolders pattern whereas it is not mandatory in a ListView. A RecyclerView recycles and reuses cells when scrolling.
What is a ViewHolder Pattern? — A ViewHolder object stores each of the component views inside the tag field of the Layout, so you can immediately access them without the need to look them up repeatedly. In ListView, the code might call findViewById() frequently during the scrolling of ListView, which can slow down performance. Even when the Adapter returns an inflated view for recycling, you still need to look up the elements and update them. A way around repeated use of findViewById() is to use the "view holder" design pattern.
LayoutManager: In a ListView, the only type of view available is the vertical ListView. A RecyclerView decouples list from its container so we can put list items easily at run time in the different containers (linearLayout, gridLayout) by setting LayoutManager.
Item Animator: ListViews are lacking in support of good animations, but the RecyclerView brings a whole new dimension to it. 71. How would you implement swipe animation in Android

```xml
<set xmlns:android="http://schemas.android.com/apk/res/android" android:shareInterpolator=”false”>
<translate android:fromXDelta=”-100%”
           android:toXDelta=”0%”
           android:fromYDelta=”0%”
           android:toYDelta=”0%”
           android:duration=”700"/>
</set>
```

72. Arraymap/SparseArray vs HashMap in Android?
    Article 1 on the subject
    Article 2 on the subject
73. How to plug memory Leak in Android?
    Checkout this awesome article by yours truly :)
74. How to reduce apk size in Android?
    Checkout this awesome article.
    The summary the article states:
    Enable proguard in your project by adding following lines to your release build type.
    Enable shrinkResources .
    Strip down all the unused locale resources by adding required resources name in “resConfigs”.
    Convert all the images to the webp or vector drawables.
75. How to reduce build time of an android application?
    Checkout this awesome article.
    What I got from the article was: A few commands we can add to the gradle.properties file:
    org.gradle.configureondemand=true - This command will tell gradle to only build the projects that it really needs to build.
    Use Daemon — org.gradle.daemon=true - Daemon keeps the instance of the gradle up and running in the background even after your build finishes. This will remove the time required to initialize the gradle and decrease your build timing significantly.
    org.gradle.parallel=true - Allow gradle to build your project in parallel. If you have multiple modules in you project, then by enabling this, gradle can run build operations for independent modules parallelly.
    Increase Heap Size — org.gradle.jvmargs=-Xmx3072m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8 - Since android studio 2.0, gradle uses dex in the process to decrease the build timings for the project. Generally, while building the applications, multiple dx processes runs on different VM instances. But starting from the Android Studio 2.0, all these dx processes runs in the single VM and that VM is also shared with the gradle. This decreases the build time significantly as all the dex process runs on the same VM instances. But this requires larger memory to accommodate all the dex processes and gradle. That means you need to increase the heap size required by the gradle daemon. By default, the heap size for the daemon is about 1GB.
    Ensure that dynamic dependency is not used. i.e. do not use
    implementation 'com.android.support:appcompat-v7:27.0.+'.
    This command means gradle will go online and check for the latest version every time it builds the app.
    Instead use fixed versions i.e. 'com.android.support:appcompat-v7:27.0.2'
    I followed the steps in there and reduced by build time from 167 seconds to 65 seconds ~ 38%.
76. Android Architecture Components?
    A collection of libraries that help you design robust, testable, and maintainable apps.
    Checkout the Official documentation.

77. Difference between MVC & MVP & MVVM?
    MVC is the Model-View-Controller architecture where model refers to the data model classes. The view refers to the xml files and the controller handles the business logic. The issue with this architecture is unit testing. The model can be easily tested since it is not tied to anything. The controller is tightly coupled with the android apis making it difficult to unit test. Modularity & flexibility is a problem since the view and the controller are tightly coupled. If we change the view, the controller logic should also be changed. Maintenance is also an issues.
    MVP architecture: Model-View-Presenter architecture. The View includes the xml and the activity/fragment classes. So the activity would ideally implement a view interface making it easier for unit testing (since this will work without a view).
    Sample Implementation
    MVVM: Model-View-ViewModel Architecture. The Model comprises data, tools for data processing, business logic. The View Model is responsible for wrapping the model data and preparing the data for the view. IT also provides a hook to pass events from the view to the model.
    Sample Implementation
78. S.O.L.I.D principles in software development?
    The Single Responsibility Principle (SRP)
    The Open-Closed Principle (OCP)
    The Liskov Substitution Principle (LSP)
    The Interface Segregation Principle (ISP)
    The Dependency Inversion Principle (DIP)
    You can checkout the whole article on what this means from here.

Why is Java said to be platform independent?
The execution of the code does not depend upon the OS

1. Difference between ‘throw’ and ‘throws’ in Java Exception Handling?
   throw keyword is used to throw Exception from any method or static block whereas throws is used to indicate that which Exception can possibly be thrown by this method.
2. Is there ever a scenario where we can skip the finally block in a try catch?
   By Calling System.exit(0) in try or catch block, we can skip the finally block. System.exit(int) method can throw a SecurityException. If System.exit(0) exits the JVM without throwing that exception then finally block will not execute. But, if System.exit(0) does throw security exception then finally block will be executed.
3. What are anonymous classes?
   An anonymous class is just what its name implies — it has no name. It combines the class declaration and the creation of an instance of the class in one step. Since anonymous classes have no name, objects can not be instantiated from outside the class in which the anonymous class is defined. In fact, an anonymous object can only be instantiated from within the same scope in which it is defined.
   Rules:
   An anonymous class must always extend a super class or implement an interface but it cannot have an explicit extends or implements clause.
   An anonymous class must implement all the abstract methods in the super class or the interface.
   An anonymous class always uses the default constructor from the super class to create an instance.
   Example:
   MyButton.setOnClickListener(new Button.OnClickListener {
   @override
   public void onClick(View view){
   //some code
   }
   });
4. Why is the main method static in java?
   The method is static because otherwise there would be ambiguity on which method to be called. If static is removed from the main method, Program compiles successfully . But at runtime throws an error “NoSuchMethodError”.
   We can overload the main method in Java. But the program doesn’t execute the overloaded main method when we run your program, we need to call the overloaded main method from the actual main method only. To run a method without calling this main method, we would need to execute a static block.
   In order to avoid NoSuchMethodError, we can call System.exit(0) after the static method.
   Note: Any method declared static will be executed even before the main class is executed.
   Example:
   public class Hello {
   static {
   System.out.println("Hello, World!");
   }
   }
5. What is garbage collector? How does it work?
   All objects are allocated on the heap area managed by the JVM. As long as an object is being referenced, the JVM considers it alive. Once an object is no longer referenced and therefore is not reachable by the application code, the garbage collector removes it and reclaims the unused memory.
6. Difference between stack memory & heap memory?
   Stack is used for static memory allocation and Heap for dynamic memory allocation, both stored in the computer’s RAM .
   Variables allocated on the stack are stored directly to the memory and access to this memory is very fast, and it’s allocation is dealt with when the program is compiled. When a function or a method calls another function which in turns calls another function etc., the execution of all those functions remains suspended until the very last function returns its value. The stack is always reserved in a LIFO order, the most recently reserved block is always the next block to be freed. This makes it really simple to keep track of the stack, freeing a block from the stack is nothing more than adjusting one pointer.
   Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, but the heap size is only limited by the size of virtual memory . Element of the heap have no dependencies with each other and can always be accessed randomly at any time. You can allocate a block at any time and free it at any time. This makes it much more complex to keep track of which parts of the heap are allocated or free at any given time.
   You can use the stack if you know exactly how much data you need to allocate before compile time and it is not too big. You can use heap if you don’t know exactly how much data you will need at runtime or if you need to allocate a lot of data.
   In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap. Stack is thread specific and Heap is application specific. The stack is important to consider in exception handling and thread executions.
   Heap memory is used by all the parts of the application whereas stack memory is used only by one thread of execution.
   Whenever an object is created, it’s always stored in the Heap space and stack memory contains the reference to it. Stack memory only contains local primitive variables and reference variables to objects in heap space.
   Objects stored in the heap are globally accessible whereas stack memory can’t be accessed by other threads.
   Memory management in stack is done in LIFO manner whereas it’s more complex in Heap memory because it’s used globally. Heap memory is divided into Young-Generation, Old-Generation etc, more details at Java Garbage Collection.
   Stack memory is short-lived whereas heap memory lives from the start till the end of application execution.
   When stack memory is full, Java runtime throws java.lang.StackOverFlowError whereas if heap memory is full, it throws java.lang.OutOfMemoryError: Java Heap Space error.
   Stack memory size is very less when compared to Heap memory. Because of simplicity in memory allocation (LIFO), stack memory is very fast when compared to heap memory.
7. Explain OOPs concept
   Object Oriented Programming is a programming style that involves concepts such as Classes, objects,Abstraction, Encapsulation, Inheritance, Polymorphism.
8. What is Inheritance?
   Inheritance is the process by which objects of one class acquire the properties & objects of another class. The two most common reasons to use inheritance are:
   a) To promote code reuse. b) To use polymorphism.
9. Does Java support multiple inheritance?
   Java supports multiple inheritance by interface only since it can implement multiple interfaces but can extend only one class.
10. What is Encapsulation?
    Encapsulation involves binding code and data together as a single unit.
    Encapsulation is a technique used for hiding the properties and behaviours of an object and allowing outside access only as appropriate. It prevents other objects from directly altering or accessing the properties or methods of the encapsulated object.
    For instance, a class can be an encapsulated class if all the variables in it are defined as Private and by providing getter and setter methods.
11. What is Abstract class?
    Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation.
    If even a single method is abstract, the whole class must be declared abstract.
    Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.
    You can’t mark a class as both abstract and final.
    Non-abstract methods can access a method that you declare as abstract.
12. What are Interfaces?
    Interfaces are only declared methods that an implementing class would need.
    Interfaces cannot be marked as final. Interface variables must be static or final.
    Interfaces cannot be instantiated directly.
    Marker Interfaces: Marker interfaces are those which do not declare any required Methods. The java.io.Serializable interface is a typical marker interfaces. These do not contain any methods, but classes must implement this interface in order to be serialized and de-serialized.
13. Difference between Abstract and Interfaces?
    Abstract classes can have non abstract methods. It can have instance variables. We have provide default implementation to abstract class method. A class can extend only one abstract class.A class can implement multiple interfaces.
    Image for post
14. What is Polymorphism?
    Polymorphism is when an object takes on multiple forms. For instance, String is a subclass of Object class.
    Polymorphism manifests itself in Java in the form of multiple methods having the same name. In some cases, multiple methods have the same name, but different formal argument lists (overloaded methods). In other cases, multiple methods have the same name, same return type, and same formal argument list (overridden methods).
    Polymorphism is a characteristic of being able to assign a different meaning or usage to something in different contexts — specifically, to allow an entity such as a variable, a function, or an object to have more than one form.
    2 forms of polymorphism:
    Compile time polymorphism: The flow of control is decided during the compile time itself. By overloading.
    Run time polymorphism: is done using inheritance and interface. The flow of control is decided during the runtime. Overriding: Overriding will have the same method name with the same parameters. One will be the parent class method and the other will be the child class method. Overloading occurs when the same method name is declared but with different parameters.
15. What is Method overloading?
    Method Overloading means to have two or more methods with same name in the same class with different arguments.
    Note:
    Overloaded methods MUST change the argument list
    Overloaded methods CAN change the return type
    Overloaded methods CAN change the access modifier
    Overloaded methods CAN declare new or broader checked exceptions
    A method can be overloaded in the same class or in a subclass
16. What is Method overriding?
    Method overriding occurs when sub class declares a method that has the same type arguments as a method declared by one of its superclass
    You can’t override a method marked public and make it protected
    You cannot override a method marked final
    You cannot override a method marked static
    Note: Static methods cannot be overridden. Overloaded methods can still be overridden.
17. Why would you not call abstract method in constructor?
    The problem is that the class is not yet fully initialised, and when the method is called in a subclass, it may cause trouble.
18. Composition over inheritance?
    Composition is typically “has a” or “uses a” relationship. In the below example, the Employee class has a Person. It does not inherit from Person but instead gets the Person object passed to it, which is why it is a “has a” Person.
    class Person {
    String Title;
    String Name;
    Int Age;
    public Person(String title, String name, String age) {
    this.Title = title;
    this.Name = name;
    this.Age = age;
    }
    }
    class Employee {
    Int Salary;
    private Person person;
    public Employee(Person p, Int salary) {
    this.person = p;
    this.Salary = salary;
    }
    }
19. Difference between Encapsulation & Abstraction?
    Abstraction focuses on the outside view of an object (i.e. the interface)
    Encapsulation (information hiding) prevents clients from seeing it’s inside view.
    Abstraction solves the problem in the design side while Encapsulation is the Implementation.
20. Constructors vs Methods?
    Constructors must have the name as the class name and does not have a return type. It can be used to instantiate any objects in the class whereas methods have no such rule and is another member of the class. Constructors cannot be inherited but a derived class can call the super constructor of parent class.
    this(): Constructors use this to refer to another constructor in the same class with a different parameter list.
    super(): Constructors use super to invoke the superclass's constructor.
    Methods: Instance methods on the other hand require an instance of the class to exist before they can be called, so an instance of a class needs to be created by using the new keyword. Class methods are methods which are declared as static. The method can be called without creating an instance of the class.
21. What is the difference between instantiation and initialisation of an object?
    Initialisation is the process of the memory allocation, when a new variable is created. Variables should be explicitly given a value, otherwise they may contain a random value that remained from the previous variable that was using the same memory space. To avoid this problem, Java language assigns default values to data types.
    Instantiation is the process of explicitly assigning definitive value to a declared variable.
22. Do objects get passed by reference or value in Java? Elaborate on that.
    Java is always pass-by-value. When we pass the value of an object, we are passing the reference to it.
    Java creates a copy of the variable being passed in the method and then does the manipulations. Hence the change is not reflected in the main method.
    But when you pass an object reference into a method, a copy of this reference is made, so it still points to the same object. This means, that any changes that you make to the insides of this object are retained, when the method exits.
    Java copies and passes the reference by value, not the object. Thus, method manipulation will alter the objects, since the references point to the original objects. But since the references are copies, swaps will fail.
23. Primitives in Java?
    Image for post
24. Difference between == and .equals() method in Java?
    We can use == operators for reference comparison (address comparison) and .equals() method for content comparison.

- In simple words, == checks if both objects point to the same memory location whereas .equals() evaluates to the comparison of values in the objects.

26. Why strings are Immutable?
    Once a value is assigned to a string it cannot be changed. And if changed, it creates a new object of the String. This is not the case with StringBuffer.
27. What is String.intern()? When and why should it be used?
    String.intern() method can be used to to deal with String duplication problem in Java. By carefully using the intern() method you can save a lot of memories consumed by duplicate String instances. A string is duplicate if it contains the same content as another string but occupied different memory location.
    By calling the intern() method on a string object, for instance “abc”, you can instruct JVM to put this String in the pool and whenever someone else creates “abc”, this object will be returned instead of creating a new object. This way, you can save a lot of memory in Java, depending upon how many Strings are duplicated in your program.
    When the intern method is invoked, if the String pool already contains that String object such that equals() return true, it will return the String object from the pool, otherwise it will add that object to the pool of unique String.
28. String pool in Java:
    String Pool in java is a pool of Strings stored in Java Heap Memory. When we use double quotes to create a String, it first looks for String with same value in the String pool, if found it just returns the reference else it creates a new String in the pool and then returns the reference. However using new operator, we force String class to create a new String object in heap space. We can use intern() method to put it into the pool or refer to other String object from string pool having same value.
    For example, how many strings are getting created in below statement;
    String str = new String("Cat");
    In above statement, either 1 or 2 string will be created. If there is already a string literal “Cat” in the pool, then only one string “str” will be created in the pool. If there is no string literal “Cat” in the pool, then it will be first created in the pool and then in the heap space, so total 2 string objects will be created.
29. Final modifier?
    Final modifiers — once declared cannot be modified. A blank final variable in Java is a final variable that is not initialised during declaration.
    final Classes- A final class cannot have subclasses.
    final Variables- A final variable cannot be changed once it is initialised.
    final Methods- A final method cannot be overridden by subclasses.
30. Finalize keyword?
    Finalize is a method used to perform clean up processing just before object is garbage collected.
31. Finally keyword?
    finally is a code block and is used to place important code, it will be executed whether exception is handled or not.
32. Static variables?
    Variables that have only one copy per class are known as static variables. They are not attached to a particular instance of a class but rather belong to a class as a whole. A static variable is associated with the class as a whole rather than with specific instances of a class. Non-static variables take on unique values with each object instance.
33. What is reflection?
    Java Reflection makes it possible to inspect classes, interfaces, fields and methods at runtime, without knowing the names of the classes, methods etc. at compile time. It is also possible to instantiate new objects, invoke methods and get/set field values using reflection.
34. Multi threading?
    Multiple tasks are running concurrently in a program.
35. Fail-fast & Fail-Safe?
    Fail-fast Iterators throws ConcurrentModificationException when one Thread is iterating over collection object and other thread structurally modify Collection either by adding, removing or modifying objects on underlying collection. They are called fail-fast because they try to immediately throw Exception when they encounter failure.
    On the other hand fail-safe Iterators works on copy of collection instead of original collection.
36. What does the keyword synchronized mean?
    When you have two threads that are reading and writing to the same ‘resource’, say a variable named ‘test’, you need to ensure that these threads access the variable in an atomic way. Without the synchronized keyword, your thread 1 may not see the change thread 2 made to test.
    synchronized variables blocks the next thread’s call to method as long as the previous thread’s execution is not finished. Threads can access this method one at a time.
37. What does the keyword volatile mean?
    Suppose two threads are working on a method. If two threads run on different processors each thread may have its own local copy of variable. If one thread modifies its value the change might not reflect in the original one in the main memory instantly.
    Now the other thread is not aware of the modified value which leads to data inconsistency.Essentially, volatile is used to indicate that a variable’s value will be modified by different threads. ‘volatile’ tells the compiler that the value of a variable must never be cached as its value may change outside of the scope of the program itself.
    The value of this variable will never be cached thread-locally: all reads and writes will go straight to ‘main memory’
    An access to a volatile variable never has the potential to block: we’re only ever doing a simple read or write, so unlike a synchronized block we will never hold on to any lock.
38. What is Autoboxing and Unboxing?
    Autoboxing is the automatic conversion that the Java compiler makes between the primitive types and their corresponding object wrapper classes. For example, converting an int to an Integer, a double to a Double, and so on. If the conversion goes the other way, this is called unboxing.
39. Optionals in Java?
    Optional is a container object which is used to contain not-null objects. Optional object is used to represent null with absent value. This class has various utility methods to facilitate code to handle values as ‘available’ or ‘not available’ instead of checking null values.
40. What is externalization?
    In serialization, the JVM is responsible for the process of writing and reading objects. This is useful in most cases, as the programmers do not have to care about the underlying details of the serialization process.
    However, the default serialization does not protect sensitive information such as passwords and credentials.
    Thus externalization comes to give the programmers full control in reading and writing objects during serialization.
    Implement the java.io.Externalizable interface — then you implement your own code to write object’s states in the writeExternal() method and read object’s states in the readExternal() method.
41. What are Data Structures?
    Intentional arrangement of a collection of data. There are 5 fundamental behaviours of a data structure: access, insert, delete, find & sort.
42. Explain Big O Notation?
    The notation Ο(n) is the formal way to express the upper bound of an algorithm’s running time. It measures the worst case time complexity or the longest amount of time an algorithm can possibly take to complete.
    Note: O(1) means that it takes a constant time, like three minutes no matter the amount of data in the set. O(n)means it takes an amount of time linear with the size of the set.
43. Explain Big Omega Notation
    The Big Omega Notation is used to describe the best case running time for a given algorithm.
44. Arrays in Java?
    Arrays is an ordered collection. It will have a fixed length which needs to be defined at the initialisation time whereas lists have a variable length. Arrays are easier to store elements of the same data type. Used internally in stack and queue. It is a convenient way of representing a 2D array.
    Arrays cannot hold generic data types whereas lists can.
    Arrays can store all data types whereas lists cannot store primitive data types, only objects.
    Image for post
    Complexity of Arrays
45. Linked Lists in Java?
    A LinkedList contains both a head and a tail. The “Head” is the first item in the LinkedList, while the “Tail” is the last item. It is not a circular data structure, therefore the tail does not have its’ pointer pointing at the Head — the pointer is just null.
    No indices but each node has a pointer pointing to the next element.
    They are dynamic in nature which means they allocate memory only when needed.
    Insertion, deletion, updation is easy
    A linked list is a group of nodes which represent a sequence. Each node consists of a data and a link or reference to the next node in the sequence.
    Singly Linked List: has a node and a pointer to the next node in the sequence.
    Doubly Linked List: has a node and 2 pointers — one to the next node and one to the previous node in the sequence. This is very convenient if you need to be able to traverse stored elements in both directions.
    Image for post
    Complexity of LinkedList
46. Binary Trees
    A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
    The left subtree of a node contains only values less than the parent node’s value.
    The right subtree of a node contains only values greater than or equal to the node’s value.
    Only if the above 2 criteria are matched, then the tree is said to be balanced.
    Advantages of Binary tree over Linked List: In a linked list, the items are linked together through a single next pointer. In a binary tree, as long as the tree is balanced, the search path to each item is a lot shorter than that in a linked list.
    Their disadvantage is that in the worst case they can degenerate into a linked list in terms of efficiency.
47. Stacks:
    Stacks are an abstract collection that follow LIFO mechanism. Main functionalities include:
    Push: a new entity added to the top of the stack.
    Pop: an entity is removed from the top of the stack.
    The process of accessing data stored in a serial access memory is similar to manipulating data on a stack.
    A stack may be defined to have a bounded capacity i.e. if the stack is full and a new entity cannot be added, then it is considered to be in an overflow state.
    If the stack is empty and an entity cannot be popped, it is considered to be in an underflow state.
    Efficiency of stacks: The time is not dependent of the no of items in the stack so it is very efficient. O(1).
48. Queues:
    Queues are an abstract collection that follow FIFO mechanism. The entities in the queue are kept in an order. Main functionalities include:
    enqueue: Add an item to the end of the queue. Dequeue: remove an item from the start of the queue.
    Front: retrieves the first item from the queue.
    A queue may be defined to have a bounded capacity i.e. if the queue is full and a new entity cannot be added, then it is considered to be in an overflow state.
    If the queue is empty and an entity cannot be popped, it is considered to be in an underflow state.
    Efficiency of queues: The time is not dependent of the no of items in the queue so it is very efficient. O(1).
    A double ended queue (deque): is an abstract collection which differs from queue in a way that an item can be added/removed from either side of the queue.
    An input-restricted deque: is when deletion takes place at either end but insertion takes place at only one end.
    An output-restricted deque: is when insertion takes place at either end but deletion takes place only at one end. A common occurrence of deque is doubly linked list.
    Priority queue: same as queue but has a priority associated with it. Items are retrieved based on their priority.
49. Blocking Queues:
    A blocking queue is a queue that blocks when you try to dequeue from it and the queue is empty, or if you try to enqueue items to it and the queue is already full. A thread trying to dequeue from an empty queue is blocked until some other thread inserts an item into the queue. A thread trying to enqueue an item in a full queue is blocked until some other thread makes space in the queue.
    Example on implementing a blocking queue
50. Difference between stacks & queues?
    Image for post
51. What is a deadlock in Java
    A deadlock occurs when a thread enters a waiting state because a requested system resource is held by another waiting process, which in turn is waiting for another resource held by another waiting process.
    Example on how deadlock occurs
    Example on how to prevent deadlock
52. What is the List interface & Set interface?
    List interface supports for ordered collection of objects and it may contain duplicates. The Set interface provides methods for accessing the elements of a finite mathematical set. Sets do not allow duplicate elements
53. Difference between ArrayList & Vectors?
    Vectors are thread safe (synchronized) whereas arraylists are not. So performance of arraylists are better than vectors. \*In ArrayList, you have to start searching for a particular element from the beginning of an Arraylist. But in the Vector, you can start searching for a particular element from a particular position in a vector. This makes the search operation in Vector faster than in ArrayList. Vectors have a default size of 10 whereas arraylists size can be dynamic.
54. Insertion and deletion in ArrayList is slow compared to LinkedList?
    ArrayList internally uses an array to store the elements, when that array gets filled by inserting elements a new array of roughly 1.5 times the size of the original array is created and all the data of old array is copied to new array.
    During deletion, all elements present in the array after the deleted elements have to be moved one step back to fill the space created by deletion. In linked list data is stored in nodes that have reference to the previous node and the next node so adding element is simple as creating the node and updating the next pointer on the last node and the previous pointer on the new node. Deletion in linked list is fast because it involves only updating the next pointer in the node before the deleted node and updating the previous pointer in the node after the deleted node.
55. Implementations of Map?
    TreeMap: sorted based on ascending order of keys. For inserting, deleting, and locating elements in a Map, the HashMap offers the best alternative. If, however, you need to traverse the keys in a sorted order, then TreeMap is your better alternative.
    HashTable: Does not allow null values. It is not fail-safe and it is synchronized whereas HashMap allows null values and it is fail-safe and it is not synchronized.
    LinkedHashMap: This is a subclass of Hashmap. The order of insertion is preserved since it has a linkedList.
56. Difference between Enumeration and Iterators?
    Enumeration does not include remove() method whereas iterators do. Enumerators act as read only interface as it provides methods to read and traverse through a collection.
    ListIterator: is just like an iterator except it allows access to the collection in either the forward or backward direction
57. How Hashmap works in Java?
    HashMap in Java works on hashing principle. It is a data structure which allows us to store object and retrieve it in constant time O(1) provided we know the key. When we call put method, hashcode() method of the key object is called so that hash function of the map can find a bucket location to store Entry object.
    If two different objects have the same hashcode: in this case, a linked list is formed at that bucket location and a new entry is stored as next node. After finding bucket location, we will call keys.equals() method to identify a correct node in LinkedList and return associated value object for that key in Java HashMap
58. Generics in Java
    Before generics, we can store any type of objects in collection i.e. non-generic. Now generics, forces the java programmer to store specific type of objects.
    Type-safety: We can hold only a single type of objects in generics. It doesn’t allow to store other objects.
    Type casting is not required: There is no need to typecast the object.
    Compile-Time Checking: It is checked at compile time so problem will not occur at runtime. The good programming strategy says it is far better to handle the problem at compile time than runtime.
    Example:
    Before Generics, we need to type cast.
    List list = new ArrayList();  
    list.add("hello");  
    String s = (String) list.get(0); //typecasting
    After Generics, we don’t need to typecast the object.
    List<String> list = new ArrayList<String>();  
    list.add("hello");  
    String s = list.get(0);
    A class that can refer to any type is known as generic class. Here, we are using T type parameter to create the generic class of specific type. The T type indicates that it can refer to any type (like String, Integer, Employee etc.).The type you specify for the class, will be used to store and retrieve the data.
    The ? (question mark) symbol represents wildcard element. It means any type. If we write <? extends Number>, it means any child class of Number e.g. Integer, Float, double etc.

---

## Thread간 통신방법에 대해 설명

Handler를 이용

두 개 이상의 스레드를 사용할 때의 동기화 이슈를 차단하기 위해 Looper와 Handler를 사용

1. Handler 설명
   Handler는 Looper로부터 받은 Message를 실행, 처리하거나 다른 스레드로부터 메시지를 받아서 Message Queue에 넣는 역할을 하는 스레드 간의 통신 장치이다.

일반적으로 UI갱신을 위해 사용. (뷰나 뷰그룹에서 제공하는 메소드는 단일 스레드 모델(Thread-Unsafe))

핸들러는 두 종류의 객체를 메시지 큐(Message Queue)를 통해 특정 스레드로 전달한다.

문자와 필드로 구성된 메시지 객체 & Runnable 객체

## Looper에 대해 설명

Looper는 무한히 루프를 돌며 자신히 속한 스레드의 Message Queue에서 Message나 Runnable 객체를 차례로 꺼내 Handler가 처리하도록 전달한다.

메인 스레드에는 Looper가 기본적으로 생성되어 있지만, 새로 생성한 스레드는 Looper를 가지고 있지 않기 때문에 메시지를 받을 수 없다. 사용할 수 있는 메시지 큐가 없기 때문이다. 서브 스레드에서 메시지를 전달받기 위해서는 Looper를 생성해주어야 함 (but, Looper 자동 보유클래스-> HandlerThread)

## 백그라운드에서 UI 업데이트 하는 방법

Handler.post, Looper Handler, mainThread 안에 Handler 만들어 놓고 다른쓰레드에서 메시지 넣어주기, runOnUIThread, AsyncTask

## 앱을 사용하는 도중에 카카오톡 메세지가 온다면 사용하던 앱의 TopActivity의 생명주기는 어떤 상태가 되나요?

onPause 상태가 됩니다.

## 데이터 불러오는 작업은 어디서 해야할까?

- Activity가 중지 상태에서 다시 화면에 표시되기 직전에 호출됩니다. onRestart -> onStart -> onResume -> ActivityRunning..

## 다른 액티비티가 상단에 올라오면 어떤 상태?

- Activity가 중지 상태에서 다시 화면에 표시되기 직전에 호출됩니다. onRestart->onStart->onResume-> ActivityRunning..

## onRestart는 언제 호출이 되나요?

- Activity가 중지 상태에서 다시 화면에 표시되기 직전에 호출됩니다. onRestart->onStart->onResume-> ActivityRunning..

## Fragment의 생명주기에 대해 얘기하고 각 항목에 대해 설명

최초 생성 LifeCycle

onAttatch() : Fragment가 Activity에 붙을 때 호출

onCreate() : Activity에서의 oncreate()와 비슷, ui관련 작업X

onCreateView() : Layout을 inflater하여 View 작업

onActivityCreated() : Activity에서 Fragment를 모두 생성하고 난 다음 호출, 액티비티의 onCreate()에서 setContentView()한 다음이라고 생각 하면 쉽게 이해 될것 같다. 여기서 부터는 ui변경작업이 가능하다.

onStart() Fragment가 화면에 표시될때 호출된다. 사용자의 Action과 상호 작용 할 수 없다.

onResume()

Fragment가 화면에 완전히 그렸으며, 사용자의 Action과 상호 작용이 가능하다.

다른 Fragment가 add

**onPause() :** Fragment가 사용자의 Action과 상호 작용을 중지

**onStop() :** Fragment가 화면에서 더이상 보여지지 않게 되며, Fragment기능이 중지 되었을때 호출

**onDestoryView() :** View 리소스를 해제 할수 있도록 호출, backstack을 사용 했다면 Fragment를 다시 돌아 갈때 onCreateView()가 호출

Replace or backward로 removed되는 경우

**onDestory() :** Fragment상태를 완전히 종료 할 수 있도록 호출 한다.

**onDetach() :** Fragment가 Activity와 연결이 완전히 끊기기 직전에 호출 된다.

## ANR(Application Not Responding)

원인 : 메인스레드(UI 스레드)가 일정 시간 어떤 Task에 잡혀 있으면 발생한다.

input 이벤트에 5초안에 반응하지 않을 때

BroadcastReceiver가 10초내로 실행을 하지 않을 때 (UI가 없는 브로드캐스트 리시버, 서비스도 실행 주체가 메인스레드 이므로 긴 시간을 소모하는 작업인 경우 ANR발생)

- ANR 예방하려면?
  시간 소모가 많은 작업은 스레드를 통해 처리 사용자에게 프로그레스바 등을 이용해 작업의 진행과정을 알려 기다리도록 한다.

## Content Provider와 Content Resolver 차이

Content Provider : 어플리케이션 내에서 사용할 수 있는 데이터를 ‘공유’하기 위한 컴포넌트

Ex) 연락처,이미지 등 (카카오톡)

Content Resolver : 앱이 ContentProvider를 접근할 때에는, Content Resolver를 통해 접근하게 됨.

기본적으로 CRUD 함수들 제공 -> 다른 앱의 데이터베이스를 조작할 수 있음.

Ex) contentResolver.query()

## XML 기반 레이아웃은 왜 중요?

동작을 제어하는 코드로부터 따로 표시하기가 더 좋음, UI의 구조를 시각화하기 더 쉬하지만 제트펙 라이브러리에서는 선언적인 UI 를 구성을 하기 위한 COMPOSE 를 제공을 하고 있음. 개인적인 생각으로는 앞으로는 Swift 에서 사용하는 것처럼

자바로 레이아웃을 작성했다면, 레이아웃을 변경할 때마다 소스를 재컴파일 해야함.

## Vector , 비트맵 이미지 차이점

Vector : 리사이징이 되어도 전혀 깨지지 않음. 모든 해상도에서 자유자재로 활용할 수 있기 때문에 특정 해상도에 제한되어 있지 않다는 것이 핵심. Ex) SVG

비트맵 : 픽셀로 구성되어 있다. 자유자재로 바꿀 수가 없고 움직일 수도 없다. Ex) PNG, JPEG

## ConstraintLayout 왜 사용?

## 네트워크

## Process Vs. Thread

- Process : 실행 중인 하나의 애플리케이션, 사용자가 애플리케이션을 실행하면 운영체제로부터 실행에 필요한 메모리를 할당받아 애플리케이션의 코드를 실행, 하나의 애플리케이션은 다중 프로세스를 만들기도 한다. (크롬 브라우저 두 개 실행 -> 두 개의 크롬 Process 생성)

- Thread : 하나의 프로세스 내에서 할당 받은 자원을 공유하며 실행되는 독립적인 작업 단위이다. 즉, 스레드는 각자의 스택 메모리영역을 가지고 있으며 동일한 프로세스 내의 다른 스레드들과 전역 메모리를 공유한다. 따라서 CPU로부터 새로운 자원을 할당받지 않아도 되기 때문에 프로세스보다 실행 속도가 빠르다는 장점을 가지고 있다.

멀티 프로레스들은 운영체제에서 할당받은 자신의 메모리를 가지고 실행하기 때문에 서로 독립적.

따라서 하나의 프로세스에서 오류가 발생해도 다른 프로레스에게 영향을 미치지 않는다.

하지만 Thread는 하나의 프로세스 내부에 생성되기 때문에 하나의 스레드가 예외를 발생시키면 프로세스 자체가 종료될 수 있어 다른 스레드에게 영향을 미치게 된다.

## Http vs. Https

- **Http **: Hypertext transfer protocol, 웹 서버와 사용자의 인터넷 브라우저 사이에 문서를 전송하기 위한 통신규약. 인터넷에서 하이퍼텍스트를 교환하기 위해 사용되는 통신규약.

http에는 사용할 수 있는 메소드가 여러 가지 있다. HEAD, GET, POST, DELETE, OPTION등

Https : http하고 거의 같지만 모든 통신 내용을 암호화. s가 secure socket, 안전한 통신망을 뜻함.

패킷이 암호화 되어 있기 때문에 패킷캡쳐 프로그램으로 캡쳐를 해도 암호화된 내용만 보임.

암호화는 TLS라고 하여 Transport계층에서 이루어짐. L4의 전송계층에서 암호화가 이루어짐.

근데 왜 http써?

https암호화를 하려면 웹 서버에 부하가 생김(암호화 과정 때문에 https가 더 느림), 비용이 비쌈.

http는 비연결형으로 웹 페이지를 보는 중 인터넷 연결이 끊겼다가 다시 연결되어도 페이지를 계속 볼 수 있지만 https는 소켓(데이터를 주고받는 경로) 자체에서 인증을하기 때문에 인터넷 연결이 끊기면 소켓도 끊어져서 다시 https 인증을 해야한다. 그래서 시간이 또 걸린다.

그래서 아무나 봐도 상관없는 페이지는 http로, 남에게 보이면 안되는 금융 정보나 메일 등 중요한 것은 https로 하는 것이다. GMail은 https를 지원한다.

1. POST vs. GET
   GET : URL 마지막단에 ‘?’ 문자를 기준으로 모든 파라미터를 전달, 주소창에 값이 노출되기에 PW와 같은 민감한 정보를 전송하면 안됨,

POST : 전달하려는 정보가 HTTP body 에 포함되어 전달 -> 사용자에게 직접적으로 파라미터 노출 X

길이에 제한 없음, 서버 혹은 DB의 값이나 상태를 바꿀 때 사용

## OkHttp와 Retrofit 차이점, 장단점

## DataBinding 장점 왜사용?

## Rx 적용했을 때 좋은 점