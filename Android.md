# 안드로이드 면접

- [안드로이드 면접](#안드로이드-면접)
  - [[activity] 왜 액티비티 클래스 의 onCreate() () 안에서 setContentView() 를 사용해야 할까](#activity-왜-액티비티-클래스-의-oncreate--안에서-setcontentview-를-사용해야-할까)
  - [[activity] onSaveInstanceState() 실행 시점](#activity-onsaveinstancestate-실행-시점)
  - [[activity] 액티비티 클래스의 onSavedInstanceState(), onRestoreInstanceState()의 역할은 무엇인가](#activity-액티비티-클래스의-onsavedinstancestate-onrestoreinstancestate의-역할은-무엇인가)
  - [[activity] 안드로이드의 테스크](#activity-안드로이드의-테스크)
  - [[activity] Activity에서 this, getBaseContext(), getApplicationContext() 차이](#activity-activity에서-this-getbasecontext-getapplicationcontext-차이)
  - [[activity] ActivityA에서 ActivityB 호출한 경우 생명주기/ActivityA로 다시 돌아오는 경우 생명주기](#activity-activitya에서-activityb-호출한-경우-생명주기activitya로-다시-돌아오는-경우-생명주기)
  - [[activity] 안드로이드 런치모드](#activity-안드로이드-런치모드)
  - [[activity] 화면 회전이 되었을 때, 데이터가 초기화 되는 것을 어떻게 막을 수 있나요](#activity-화면-회전이-되었을-때-데이터가-초기화-되는-것을-어떻게-막을-수-있나요)
  - [[activity] 액티비티 생명주기](#activity-액티비티-생명주기)
  - [[activity] onCreate() 와 onStart() 차이점?](#activity-oncreate-와-onstart-차이점)
  - [[activity] 액티비티에서 onPause() 나 onStop() 이 호출되지 않고 onDestroy() 가 호출되는 경우는 언제](#activity-액티비티에서-onpause-나-onstop-이-호출되지-않고-ondestroy-가-호출되는-경우는-언제)
  - [[activity] Activity와 AsyncTask 의 라이프 사이클이 어떤 관계이 있나요 어떤 문제가 결과적으로 발생할 수 있나요 그리고 어떻게 문제를 회피할 수 있을 까요](#activity-activity와-asynctask-의-라이프-사이클이-어떤-관계이-있나요-어떤-문제가-결과적으로-발생할-수-있나요-그리고-어떻게-문제를-회피할-수-있을-까요)
  - [[activity] 액티비티간 데이터 전달에서 임의의 클래스 객체를 바로 전달하지 못하는 이유는 무엇이고 전달하기 위해서는 어떤 처리가 필요한가](#activity-액티비티간-데이터-전달에서-임의의-클래스-객체를-바로-전달하지-못하는-이유는-무엇이고-전달하기-위해서는-어떤-처리가-필요한가)
  - [[activity] 부모 액티비티에서 자식 액티비티의 결과 값을 받아오기 위해 어떻게 해야하는가](#activity-부모-액티비티에서-자식-액티비티의-결과-값을-받아오기-위해-어떻게-해야하는가)
  - [[fragment] FragmentPagerAdapter 와 FragmentStatePagerAdapter 의 차이점은 무엇인가요](#fragment-fragmentpageradapter-와-fragmentstatepageradapter-의-차이점은-무엇인가요)
  - [[fragment] 프레그먼와 생명주기에 설명](#fragment-프레그먼와-생명주기에-설명)
  - [[async] 안드로이드 HTTP 라이브러리의 역사](#async-안드로이드-http-라이브러리의-역사)
  - [[aysnc] Thread 와 AsyncTask 차이점?](#aysnc-thread-와-asynctask-차이점)
  - [[memory] 안드로이드의 메모리 관리 방식에 대해서 설명](#memory-안드로이드의-메모리-관리-방식에-대해서-설명)
  - [[memory] Looper란?](#memory-looper란)
  - [[memory] 안드로이드의 메모리 구조](#memory-안드로이드의-메모리-구조)
  - [[memory] 핸들러](#memory-핸들러)
  - [[content provider] 콘텐트 프로바이더(Content providers)에 대해서 설명해주세요](#content-provider-콘텐트-프로바이더content-providers에-대해서-설명해주세요)
  - [[content provider] 콘텐트 프로바이더를 사용하여 데이터에 접근하는 방식을 간략하게 말해보세요](#content-provider-콘텐트-프로바이더를-사용하여-데이터에-접근하는-방식을-간략하게-말해보세요)
  - [[service] 서비스(service)가 무엇인지와 서비스 생명주기에 대해서 설명하시오](#service-서비스service가-무엇인지와-서비스-생명주기에-대해서-설명하시오)
  - [[service] 서비스와 인텐트 서비스의 다른점은 무엇](#service-서비스와-인텐트-서비스의-다른점은-무엇)
  - [[view] Linear/Relative/Constraint/Frame 차이점?](#view-linearrelativeconstraintframe-차이점)
  - [[view] 뷰 그룹과 뷰는 차이점?](#view-뷰-그룹과-뷰는-차이점)
  - [[view] RecyclerView 와 ListView 차이점?](#view-recyclerview-와-listview-차이점)
  - [[view] RecyclerView 를 어떻게 사용하나요](#view-recyclerview-를-어떻게-사용하나요)
  - [[error] ANR 이 무엇이고 언제 일어나며, 어떻게 예방할 수 있나요](#error-anr-이-무엇이고-언제-일어나며-어떻게-예방할-수-있나요)
  - [[error] LMK?](#error-lmk)
    - [[error] OOM(Out of memory) Killer와 LMK](#error-oomout-of-memory-killer와-lmk)
  - [[broadcast receiver] 브로드 캐스트 리시버에서 Toast를 띄우면](#broadcast-receiver-브로드-캐스트-리시버에서-toast를-띄우면)
  - [[basic] Dagger, Hilt (DI)](#basic-dagger-hilt-di)
  - [[basic] 어플리케이션(application)과 컨텍스트(context)에 대해서 설명](#basic-어플리케이션application과-컨텍스트context에-대해서-설명)
  - [[basic] 노티피케이션(notification)은 무엇인가 (FCM, pending intent)](#basic-노티피케이션notification은-무엇인가-fcm-pending-intent)
  - [[basic] 안드로이드 매니페스트(android manifest)](#basic-안드로이드-매니페스트android-manifest)
  - [[basic] 디스플레이(display), 윈도우(window), 서피스(surface), 뷰(view), 뷰 그룹(view group), 뷰 컨테이너(view container), 레이아웃(layout)](#basic-디스플레이display-윈도우window-서피스surface-뷰view-뷰-그룹view-group-뷰-컨테이너view-container-레이아웃layout)
  - [[basic] 인플레이션(inflation)이란 무엇인가](#basic-인플레이션inflation이란-무엇인가)
  - [[basic] 안드로이드 MVC, MVP, MVVM](#basic-안드로이드-mvc-mvp-mvvm)
  - [[basic] ARM64-v8a(64), ARMv7, ARMx86 등 ABI(Application binary interface)가 무엇인가요](#basic-arm64-v8a64-armv7-armx86-등-abiapplication-binary-interface가-무엇인가요)
  - [[basic] 바이트 코드를 안드로이드에서 바로 실행할 수 있나요?](#basic-바이트-코드를-안드로이드에서-바로-실행할-수-있나요)
  - [[basic] SharedPreferences 에서 commit() 과 apply() 의 다른점에 대해 말해주세요](#basic-sharedpreferences-에서-commit-과-apply-의-다른점에-대해-말해주세요)
  - [[basic] 빌드타입이 무엇인가요](#basic-빌드타입이-무엇인가요)
  - [[basic] 안드로이드 빌드 프로세스에 대해 간략하게 설명](#basic-안드로이드-빌드-프로세스에-대해-간략하게-설명)
  - [[basic] minsdk, compilesdk, targetsdk](#basic-minsdk-compilesdk-targetsdk)
  - [[basic] 안드로이드의 4대 컴포넌트](#basic-안드로이드의-4대-컴포넌트)
    - [[basic] 쓰레드간 통신방법에 대해 설명](#basic-쓰레드간-통신방법에-대해-설명)
  - [[db] Realm이란 (SQLite와의 비교) [렐름] Jetpack Room](#db-realm이란-sqlite와의-비교-렐름-jetpack-room)
  - [[intent] PendingIntent에 대해서 설명 (pending:보류)](#intent-pendingintent에-대해서-설명-pending보류)
  - [[intent] FLAG_ACTIVITY_CLEAR_TASK 와 FLAG_ACTIVITY_CLEAR_TOP 의 차이점은 무엇](#intent-flag_activity_clear_task-와-flag_activity_clear_top-의-차이점은-무엇)
  - [[intent] 인텐트란 무엇인가요(암시적/묵시적)](#intent-인텐트란-무엇인가요암시적묵시적)
  - [[intent] Intent 구성요소](#intent-intent-구성요소)
  - [[intent] 인텐트 필터(intent filter)에 대해서 설명하시오](#intent-인텐트-필터intent-filter에-대해서-설명하시오)
    - [AAPT?](#aapt)
    - [NDK?](#ndk)
    - [ANR?](#anr)
    - [ADB](#adb)
    - [안드로이드 4대 컴포넌트](#안드로이드-4대-컴포넌트)
    - [Android Application의 구조?](#android-application의-구조)
    - [컨텍스트란?](#컨텍스트란)
    - [안드로이드 HTTP 라이브러리의 역사](#안드로이드-http-라이브러리의-역사)
  - [액티비티](#액티비티)
    - [프레그먼트](#프레그먼트)
  - [서비스](#서비스)
  - [브로드캐스트 리시버](#브로드캐스트-리시버)
  - [콘텐트 프로바이더](#콘텐트-프로바이더)
  - [뷰, 커스텀 뷰](#뷰-커스텀-뷰)
  - [기타](#기타)

## [activity] 왜 액티비티 클래스 의 onCreate() () 안에서 setContentView() 를 사용해야 할까

액티비티의 onCretate()는 액티비티 불릴 때 한번만 호출이 되기 때문에, 초기화에 자주 사용된다 onResume() 또는 onStart() 같이 여러번 호출 될 수 있는 곳에서 호출하는 것은 매우 비효율적인 코드이다

## [activity] onSaveInstanceState() 실행 시점

activity가 running 에서 pause 로 넘어갈때 onPause() 보다 먼저 실행된다. 활동이 정지되기 시작하면 인스턴스 상태 번들에 상태 정보를 저장할 수 있도록 시스템이 onSaveInstanceState() 메서드를 호출합니다

## [activity] 액티비티 클래스의 onSavedInstanceState(), onRestoreInstanceState()의 역할은 무엇인가

onSaveInstanceState() - 액티비티가 pause 되기 전에 데이터를 저장하는데 사용합니다

onRestoreInstanceState() - 액티비티가 파괴되고, 다시 재생성될 때, 액티비티가 가지고 있는 번들로부터 데이터를 회복할수 있다 또한 onCreate() 와 onRestoreInstanceState() 콜백 메서드는 같은 번들 객체를 전달 받는다 그래서 보통은 데이터를 회복하는 코드를 onRestoreInstanceState() 에 많이 작성하는 편이며, onCreate 에서 savedInstance를 받아 처리하는 경우에는 처음 실행이 되는지, 재생성되는 것인지 판단하기 위해서, 데이터의 null check 가 필요하다 null 이라면 처음 생성되는 것이고, 아니라면 재생성이다

## [activity] 안드로이드의 테스크

ex) 어떤 앱에서 앨범 앱을 실행하는 기능이 있다면 이 앱은 두개의 앱을 실행하는 형태가 되지만 사용자 입장에서는 하나의 앱에서 화면이 전환된다고 판단합니다 이와 같은 사용자 입장에서 논리적인 화면 구성의 단위를 태스크라고 말합니다

Task는 어플리케이션에서 실행되는 Activity를 관리하는 스택입니다 후입 선출의 형태로 나중에 적제된 액티비티가 가장 먼저 사용됩니다 최초적재된 엑티비티는 Root Activity라고 하고 마지막에 적재된 Activity는 Top Activity라고 합니다

Flag를 이용하여 엑티비티의 흐름을 제어 할 수 있습니다

## [activity] Activity에서 this, getBaseContext(), getApplicationContext() 차이

- View.getContext() == this
  현재 실행되고 있는 View의 context를 return 하는데 보통은 현재 활성화된 activity의 context가 된다.

- Activity.getApplicationContext()
  어플리케이션의 Context가 return된다. 현재 activiy의 context 뿐만 아니라 application의 lifeCycle에 해당하는 Context가 사용된다.

- ContextWrapper.getBaseContext()
  자신의 Context가 아닌 다른 Context를 access하려 할 때 사용한다. ContextWrapper는 getBaseContext()를 경유해서 Context를 참조할 수 있다.

## [activity] ActivityA에서 ActivityB 호출한 경우 생명주기/ActivityA로 다시 돌아오는 경우 생명주기

1. 시작할 때 : onCreate -> onStart -> onResume

2. 화면 회전할 때 : onPause -> onStop -> onDestroy -> onCreate -> onStart -> onResume

3. 다른 액티비티가 위에 뜰 때/전원 키로 화면 OFF할 때/홈 키 : onPause -> onStop

4. 백 키로 액티비티 종료 : onPause -> onStop -> onDestory

5. 백 키로 기존 액티비티에 돌아올 때/홈 키로 나갔다가 돌아올 때 : onRestart -> onStart -> onResume

6. 다이얼로그 액티비티나 투명 액티비티가 위에 뜰 때 : onPause

- 액티비티 라이프타임

- 전체 라이프타임 : onCreate() ~ onDestroy()

- 가시(visible) 라이프타임 : onStart() < < onStop()

- 포그라운드 라이프타임 : onResume() < < onPause()

액티비티는 onPuase 이전까지 포그라운드이고 onPause()까지 실행된다면 백그라운드 상태가 된다. 또한 onPause()까지 화면 일부가 가시되고 onStop()까지 실행되면 더 이상 액티비티가 보이지 않는다. onCreate()에서 setContentView()를 호출하지만 onCreate()에서 onResume()까지는 하나의 메시지로 처리된다. 따라서 onResume() 이후에 액티비티가 가시된다.

- 다른 액티비티 호출하는 순서 m onPause(), d onCreate(), d onStart(), d onResume(), m onStop()
- 다시 돌아가는 순서 detail onPause(), m onRestart(), m onStart(), m onResume(), d onStop(), d onDestory()
- 액티비티에서 뒤로 가기 버튼을 눌렀을 때는 어떤 콜백이 호출될까요? onBackPressed()
- 갑자기 종료됐을 때를 대비한 콜백이 있는데 아는지? onDestroyed()

## [activity] 안드로이드 런치모드

런치모드(Launch Mode) 란 액티비티가 어떤 방식으로 실행되야하는지에 대한 방식들이다

- Standard : 시스템이 액티비티가 시작된 작업(Task)에서 액티비티의 새 인스턴스를 만들고 인텐트의 경로를 이것으로 지정한다 액티비티는 여러 번 인스턴스화될 수 있고, 각 인스턴스는 서로 다른 작업에 속할 수 있으며 한 작업에 여러 개의 인스턴스가 있을 수 있다

Eg : 현재 A -> B -> C 로 쌓여있는 액티비티 스택이 있다고 가정해보자, 현재 B를 다시 실행하고 싶은 상태이고, 이를 standard 로 액티비티 B를 실행할 경우 A -> B -> C -> B 이 된다

- SingleTop : 액티비티의 인스턴스가 이미 현재 작업의 맨 위에 존재하는 경우, 시스템은 새 액티비티 인스턴스를 만드는 대신 onNewIntent() 메서드를 호출하여 인텐트를 해당 인스턴스로 라우팅한다 액티비티는 여러 번 인스턴스화될 수 있고, 각 인스턴스는 서로 다른 작업에 속할 수 있으며 한 작업에 여러 개의 인스턴스가 있을 수 있다(다만 백 스택의 맨 위에 있는 액티비티가 액티비티의 기존 인스턴스가 아닌 경우에만 이것이 적용된다)

SingleTop 런치모드와 비슷하지만, 실행하는 액티비티가 액티비티 스택의 Top 일 때 새로운 인스턴트를 만드는 것이 아니라 현재 인스턴스스의 onNewIntent()를 호출한다

Eg : 현재 A -> B 로 이루어진 액티비티 스택이 있다고 가정해보자 만약 C 액티비티를 SingleTop 으로 실행하면 A -> B -> C로 정상적으로 쌓일 것이다 그리고 현재 A -> B -> C 로 이루어진 액티비티 스택에서 C를 SingleTop 으로 다시 실행하면 A -> B -> C -> C가 되는 것이 아니고 여전히 A -> B -> C 이다

- SingleTask : 시스템이 새 작업을 만들고 새 작업의 루트에 있는 액티비티를 인스턴스화한다 하지만, 액티비티의 인스턴스가 이미 별개의 작업에 존재하는 경우, 시스템은 인텐트의 경로를 기존 인스턴스로 지정한다 이때 새 인스턴스를 만들지 않고, 해당 인스턴스의 onNewIntent() 메서드를 호출하는 방법을 사용한다 한 번에 액티비티 인스턴스 한 개씩만 존재할 수 있습니다

Eg : A -> B -> C -> D 로 이루어진 액티비티 스택이 있다고 가정하자 현재 액티비티 D를 SingleTask 모드로 실행하면, A -> B -> C -> D이고 D의 onNewIntent() 가 불리운다 그리고 액티비티 B를 SingleTask 로 실행하면, 액티비티 스택은 A -> B 로 바뀌고, 액티비티 C, D 는 파괴된다

- SingleInstance : "singleTask"와 동일하다 단, 인스턴스가 있는 작업에 대해 시스템이 어떤 액티비티도 시작하지 않은 경우는 예외이다 액티비티는 언제나 자신의 작업의 유일무이한 멤버이고, 이것으로 시작한 액티비티는 모두 별개의 작업에서 열린다

Eg : A -> B -> C -> D로 이루어진 액티비티 스택이 있다 만약 액티비티 D를 singleInstance 모드로 실행할 경우, 아래와 같이 작업이 분리된다

Task 1 - A -> B -> C

Task 2 - D

## [activity] 화면 회전이 되었을 때, 데이터가 초기화 되는 것을 어떻게 막을 수 있나요

어떻게 동작하는가? --> 화면 회전을 했을 때, 현재 만들어진 액티비티 인스턴스는 파괴되고 새로운 Orientation 을 가진 액티비티 인스턴트가 만들어진다 그렇기 때문에 데이터를 백업해두지 않으면, 메모리에서 해제되기 때문에 이를 유의하여 개발해야한다 기본적인 문제 해결 접근으로는 ViewModel, onSavedInstanceState() 두 방법을 사용하는 방식

그렇다면 이들을 어떤식으로 사용해야할까요

ViewModel : 뷰모델은 라이프 사이클에 Aware 하다고 한다 알고 있다 or 알고 있기 때문에 좀더 유연해진다 정도로 받아드리면 될 것 같다 그리고 뷰모델은 앱의 Configuration (rotatin 등) 이 바뀌어 액티비티가 파괴되어도, 파괴되지 않고, 액티비티가 재생성되었을 때 다시 연결된다 만약에 화면 회전을 3번하면 액티비티 인스턴스는 부서지고 만들어져 3번 다 다른 인스턴스이지만, 뷰모델 인스턴스는 하나이다

그렇기 때문에 뷰모델 클래스에 데이터를 저장하면 자연스럽게 해결할 수 있다 또는 onSaveInstanceState() ()를 사용하는 방법이다

## [activity] 액티비티 생명주기

부모 액티비티에서 새로운 자식 액티비티를 실행하고자 한다면 먼저 매니페스트 파일에 해당 자식 액티비티를 추가 해줘야합니다 다음으로 부모 액티비티에서 startActivity ()에 인텐트를 파라미터로 넘겨 실행하거나 startActivities ()를 이용하여 여러개의 액티비티를 한꺼번에 실행할 수 있습니다
액티비티의 실행과정은 첫 번째로 부모 액티비티에서 자식 액티비티를 생성 및 호출합니다 두 번째로 액티비티 매니저 서비스가 해당 앱 프로세스에서 인텐트를 복사해온 후 매니페스트 파일에서 해당 인텐트에 명시되어있는 액티비티를 찾고 어떻게 실행시켜야할지 결정합니다 세 번째로 찾아낸 액티비티를 실행하고 다시 해당 앱 프로세스에 인텐트를 복사하여 넘겨줍니다 그 외 자식 액티비티 내의 onCreate ()에서 setContentView ()에 레이아웃의 아이디를 파라미터로 넘겨 해당 액티비티의 화면을 구성하게됩니다

액티비티는 크게 3가지 상태가 존재합니다 먼저 실행(running) 상태는 액티비티 스택의 최상위에 있으며 포커스를 가지고 있어 사용자에게 보이는 상태입니다 다음으로 일시 중지(paused) 상태는 사용자에게 보이기는 하지만 다른 액티비티가 위에 있어 포커스를 받지 못하는 상태를 말합니다 ex) 대화상자가 위에 있어 일부가 가려져 있는 경우를 말합니다 마지막으로 중지 (stopped) 상태는 다른 액티비티에 의해 완전히 가려져 보이지 않는 상태를 말합니다

액티비티가 처음 만들어지면 onCreate()가 호출되어 레이아웃을 구성합니다 이후
onStart()가 화면에 보이기 직전에 호출됩니다 다음으로
onResume ()가 사용자 상호작용(화면이 포커스를 얻었을 때)하기 바로 전에 호출됩니다

이 3가지 ()가 호출되어 액티비티는 실행 상태를 갖게됩니다 이후 포커스를 잃었을 때
onPause ()가 호출되고 일시 중지 상태가 됩니다 일시 중지 상태에서 다시 포커스를 획득하면
onResume ()가 호출되거나 다른 액티비티에 의해서 완전히 화면이 가려졌는지 여부를 확인하여 가려져 보이지 않는 경우
onStop ()가 호출되어 중지 상태가됩니다

정지 상태에서 다시 화면이 보이기 직전에 onRestart ()가 호출되고 onStart ()가 차례로 호출됩니다 그 외 finish ()가 실행되어 해당 액티비티가 종료되기 직전에 onDestroy ()가 실행됩니다

가끔은 일시 중지나 중지 상태에서 시스템이 메모리가 부족하다고 판단될 경우 onCreate ()부터 다시 해당 액티비티를 구동합니다 이 경우 onStop, onResume () 호출이 생략됩니다 따라서 onSaveInstanceState, onRestoreInstanceState ()를 이용하여 액티비티가 갑자기 죽을 것을 대비해서 상태를 저장하고 복원하기 위한 작업을 정의해줄 수 있습니다

- onCreate() : 뷰가 처음 만들어 질 때 호출된다 보통 뷰를 만들고, 초기화 하거나 번들로부터 데이터를 받아오는 코드를 많이 작성한다
- onStart() : 액티비티가 유저에게 가시적일 때 호출된다 더 나아가 액티비티가 포그라운드로 오면, onResume 이 호출되고, 내려가면 onStop 이 호출된다
- onRestart() : onStop() 이 호출되었던 액티비티가 포 그라운드로 돌아오면 호출되는 메서드 이후 onStart() 를 호출한다
- onResume() : 액티비티가 유저와 상호작용하고 있을 때 호출된다 액티비티 스택에서 가장 위에 있는 액티비티는 유저의 입력을 받을 수 있다
- onPause() : 액티비티가 백그라운드로 가기전 상황으로 부분적으로 가려질 때 호출된다 아직 Killed 되지 않은 상황이다
- onStop() : 액티비티가 보여지지 않게 되었을 때 (백그라운드로 갔을 때) 호출된다 더 나아가 액티비티가 종료되면 OnDestroy 가 호출되고, 포 그라운드로 돌아오면 onRestart() 가 호출된다
- onDestroy() 액티비티가 종료될 때 호출된다

## [activity] onCreate() 와 onStart() 차이점?

- onCreate() ()는 애플리케이션이 시작되거나, 액티비티가 삭제된후 재생성될 때, 액티비티 사이클에서 한번만 호출된다 (앱의 구성요소 (언어, Orientation, 등) 가 변경되어 액티비티가 부서지고 다시 생성될 때 등)
- onStart() ()는 언제든지 액티비티가 유저에게 보여줄 준비가 되었을 때(가시적일때) 호출될 수 있다 전형적으로 onCreate() 이후나, onRestart() 이후에 호출된다

## [activity] 액티비티에서 onPause() 나 onStop() 이 호출되지 않고 onDestroy() 가 호출되는 경우는 언제

onCreate() 함수 안에서, finish() 를 호출할 경우 시스템은 직접 onDestroy() 를 호출한다

## [activity] Activity와 AsyncTask 의 라이프 사이클이 어떤 관계이 있나요 어떤 문제가 결과적으로 발생할 수 있나요 그리고 어떻게 문제를 회피할 수 있을 까요

AsyncTask를 생성했던 Activity가 먼저 destroy되는 경우 메모리 릭이 발생할 수 있습니다. 왜냐면 Activity가 destory된다고 해서 AsyncTask도 같이 destory되지 않기 때문입니다. doInBackground() ()가 완료될때까지 AsyncTask는 실행 중 상태를 유지하게 됩니다. 완료 후, cancel () 호출된 적이 있다면 onCancelled()가 실행되고 그렇지 않으면 onPostExecute ()가 호출됩니다.

이미 자신을 실행시켰던 Activity가 존재하지 않는데 AsyncTask가 UI처리같은 걸을 요구하면 메모리상에 존재하지 않는 것을 참조하게 되어 메모리릭이 발생합니다. 따라서 반드시 Activity 종료 전 AsyncTask를 cancel해주어 백그라운드 스레드에서 처리하던 작업이 종료되도록 해야 합니다.

문제 2. 디바이스의 화면 회전(orientation)

Activity에서 AsyncTask를 실행하고나서 사용자가 디바이스의 화면을 회전시키면 Activity를 destroy를 시키고 (onDestroy) 새로운 Activity 인스턴스가 생성됩니다.(onCreate). 이때 Activity의 모든 멤버변수의 인스턴스가 새로 생성됩니다.

Activity의 상태가 변할 때, AsyncTask에 대한 처리를 자동으로 해주지 않기 때문에, AsyncTask는 백그라운드 스레드에서 작업을 하고 있는 상태로 남아있게 됩니다. 작업이 완료될 때까지 AsyncTask는 종료되지 않습니다.

문제는 AsyncTask가 작업을 완료하고 Activity의 UI를 업데이트 하려 할때, 새로 생성된 Activity 인스턴스가 아닌 이미 destroy된 Activity 인스턴스에 접근하기 때문입니다. 따라서 디바이스 화면의 UI를 업데이트 할 수 없으며, 예외(IllegalArgumentException)가 발생합니다. 또한 기존 destroy된 Activity를 계속 참조하고 있기 때문에 garbage collector가 destory된 Activity를 수집할 수 없어 메모리릭이 발생할 수 있습니다.

## [activity] 액티비티간 데이터 전달에서 임의의 클래스 객체를 바로 전달하지 못하는 이유는 무엇이고 전달하기 위해서는 어떤 처리가 필요한가

액티비티간 전달할 수 있는 데이터의 type은 보통 기본형으로 정해져있습니다 그 이유는 인텐트를 이용하여 액티비티의 데이터를 전달하는 과정에서 현재 실행중인 앱 프로세스가 시스템 프로세스로 실행중인 액티비티 매니저 서비스 프로세스에게 인텐트를 전달합니다 이 경우 프로세스간 통신이기 때문에 인텐트에 있는 값들을 복사하여 넘기는 방식으로 처리되기 때문에 객체 주소를 바로 넘기지 못하는 문제가 발생합니다 따라서 이 문제를 해결하기 위해 자신이 임의로 만든 클래스 객체를 전달하기 위해서는 Serilizable이나 Parcelable 인터페이스를 상속받아 객체를 직렬화하여 넘기는 방식을 사용해야합니다

Serializable 마크 인터페이스인 달리 직렬화 처리 방법을 사용자가 명시적으로 작성하기 때문에 자동으로 처리하기 위한 Reflection 이 필요 없습니다. 따라서 Serializable 보다 빠르게 안드로이드에서 사용을 할 수 있습니다.

## [activity] 부모 액티비티에서 자식 액티비티의 결과 값을 받아오기 위해 어떻게 해야하는가

먼저 부모 액티비티에서 startActivityForResult ()를 이용하여 인텐트와 리퀘스트 코드를 파라미터로 넘깁니다 이후 자식 액티비티에서 setResult ()에 결과 코드와 데이터를 파라미터로 넘깁니다 다시 부모 액티비티에서 onActivityResult ()를 오버라이딩하여 자식 액티비티에서 보낸 결과 코드와 데이터를 받아 처리하는 코드를 작성할 수 있습니다

이후 실행과정에서 자식 액티비티의 finish ()가 호출되면 부모 액티비티가 다시 화면에 나타나면서 onResume ()가 실행됩니다 이때 onActivityResult ()가 작동하게 됩니다

## [fragment] FragmentPagerAdapter 와 FragmentStatePagerAdapter 의 차이점은 무엇인가요

- FragmentPagerAdapter 에서는 프래그먼트 개 수가 정해진 화면에 사용하면 좋다.

프래그먼트 매니저에서 한 번 생성된 프래그먼트의 인스턴스를 제거하지 않고 연결된 View 만 제거합니다.

- FragmentStatePagerAdapter 에서는 프래그먼트 개 수가 변하는 화면에 사용하면 좋다.

프래그먼트 매니저에서 한 번 생성된 프래그먼트의 인스턴스를 완전히 제거하여 메모리 누수 문제에 적합하게 대응할 수 있습니다.

## [fragment] 프레그먼와 생명주기에 설명

프레그먼트는 액티비티의 일부분에만 배치되는 화면 및 동작을 조작하기 위한 객체입니다 안드로이드 30(허니콤)에서 화면이 비교적 큰 태블릿의 등장으로 작은 단위의 화면의 생명주기 관리할 필요가 있어 추가되었습니다 프레그먼트 매니저를 통해서 여러개의 프레그먼트를 조작할 수 있습니다 레이아웃 xml 파일에서 다른 뷰들과 함께 배치될 수 있습니다. 액티비티가 생성되면 프레그먼트 매니저는 초기화(initializing) 상태가 됩니다 프레그먼트가 매니저에 의해 추가되면 onAttach, onAttachFragment, onCreate ()가 차례로 실행됩니다 다음으로 액티비티의 onCreate () 호출 이후 매니저는 생성(created) 상태로 변경됩니다 이때 onCreateView, onViewCreated, onActivityCreated ()가 차례로 호출됩니다 다음으로 액티비티의 onStart ()가 호출되면 매니저는 시작(started) 상태로 onStart ()를 호출합니다 이후 액티비티의 onResume ()가 호출되면 매니저 역시 재시작(resume) 상태로 변하며 onResume ()를 호출합니다 그 외 액티비티가 화면에서 보이지 않을경우 호출되는 onStop () 호출 이후 매니저는 중지(stop) 상태가 되며 액티비티의 onDestroy () 호출 이후 매니저는 onDestroyView ()를 호출합니다

onAttach함수가 OnCreate이전에 호출됩니다 그 이후 OnCreate함수가 호출되고 OncreateView에서 LayoutInflater로 UI관련 잡업을 할 수 있습니다 그리고 화면이 포커스를 잃었을때는 onPause OnStop onDestroyView가 호출되고 종료시에 onDestory onDetach()가 호출됩니다

## [async] 안드로이드 HTTP 라이브러리의 역사

2007년 => 안드로이드 발표 , HttpClient, 아파치의 DefaultHttpClient등이 사용
(HttpClient의 여러 버그들 문제가 있음)

2011년 => Goolge의 Developer 블로그에서 HttpUrlConnetction 사용 권장

이후 => Volley나 Square의 Okhttp가 등장하여 쉽게 Http 통신을 사용할 수 있게 됨

2014년 => 롤리팝 이후 HttpClient 가 Deprecated되며 이를 베이스로 하는 Volley
도 Deprecated됨

이후 => Okhttp와 그 래퍼인 Retrofit이 인기를 가짐
Retrofit은 클라이언트 부분과 콜백 형식등을 플러그로 변경할수 있다는점에서 인기를 가짐

## [aysnc] Thread 와 AsyncTask 차이점?

스레드가 수행되기 위해서는, 메인 스레드에서 분리하여 실행된다 그러나 스레드를 취소하는 것은 우아하게(elegantly) 되지 않는 경우가 많고, 안드로이드 설정이 변경되는 것을 처리할 수 없다 또한 스레드에서는 UI를 변경할 수 없다 자바의 ()이다. AsyncTask 는 5ms 보다도 짧은 작업을 처리 할 수 있다 또한 스레드와는 다르게 UI를 업데이트 할 수 있는 부분이 있다 하지만 무겁고 다양한 작업들을 수행한다면 퍼포먼스는 저하된다 안드로이드 라이브러리에 있는 ()이다

## [memory] 안드로이드의 메모리 관리 방식에 대해서 설명

안드로이드는 액티비티, 서비스, 리시버, 프로바이더를 실행하기 위해 앱이 실행되는 과정에서 프로세스를 생성합니다 실행중인 모든 앱은 컴포넌트가 모두 종료되어도 다음에 이 앱을 다시 실행할 가능성이 높기 때문에 프로세스를 바로 제거하지 않습니다 바로 종료하지 않는 이유는 앱을 실행하기 위해 프로세스를 생성하는 과정에서 딜레이가 발생하는데 이 딜레이를 줄이기 위함입니다 따라서 사용자에 의해 다시 앱이 실행되면 남아있던 프로세스가 존재하는 경우 바로 실행됩니다 이 과정에서 쌓여있던 많은 프로세스로 인해 메모리가 부족해지는 경우 프로세스의 우선순위(사용빈도)에 따라 프로세스를 종료하여 메모리를 확보합니다

## [memory] Looper란?

Looper는 스레드간의 신호이므로 handler에 보낸다고 해서 곧바로 처리되는 것이 아닙니다 동시다발적으로 메세지가 발생할 수 있기 때문에 메세지 큐(Message Queue)에 쌓았다가 처리합니다 큐(Queue)에 들어있는 내용을 하나하나 꺼내 처리하는 놈이 바로 루퍼입니다 메인 쓰레드가 looper를 가지고 있으며 무한 루프를 돌며 큐의 내용을 처리합니다

## [memory] 안드로이드의 메모리 구조

안드로이드의 메모리구조를 보면 램, 내장메모리, 외장메모리로 구분됩니다

- 렘 : 프로그램이 실행될때 상주되는 공간입니다 평상시에 하드에 저장되어있다가 런타임시에 차지되는 공간을 말합니다
- 내장메모리 : 간단하게 하드디스크라고 생각해도 됩니다
- 외장메모리 : 메모리가 더 필요할때 추가 할 수 있는 메모리입니다

안드로이드에서 메모리 관리는 GC를 이용해서 진행되게 됩니다 주기적으로 GC루트에서 모든 객체 참조에 대해 활성객체를 표시하고 활성되지 않은 객체는 메모리에서 지워집니다

String References와 WeakReference로 나눌 수 있습니다

## [memory] 핸들러

핸들러는 스레드를 관리하기 위한 객체이다 핸들러는 메세지를 받거나 처리하는 방법을 정의할 수 있다 그들을 액티비티 라이프사이클 외에서 사용할 때에는 사용한 뒤 적절히 해제(Cleaned up) 시켜줘야 한다 그렇지 않으면 메모리 누수(thread leaks)가 발생할 것 이다

핸들러는 메인스레드와 백그라운드 스레드 혹은 백그라운드 스레드 사이의 커뮤니케이션을 가능하게 한다 핸들러는 몇초나 몇분 단위로 정기적으로 해야하는 백그라운드 작업을 수행하는데 선호된다

## [content provider] 콘텐트 프로바이더(Content providers)에 대해서 설명해주세요

컨텐츠 프로바이더는 하나의 어플리케이션에서 요청시에 다른 어플리케이션으로 데이터를 제공한다 어플리케이션의 데이터 보안으로 인해 구조화된 데이터 구조를 가지고 있도록 정의되어 있다 컨텐츠 프로바이더는 기본적으로 다른 프로세스에서 다른 프로세스로 데이터를 제공할 수있는 인터페이스를 가지고 있다 만약 컨텐츠 프로바이더를 이용하여 데이터 접근을 원한다면, Application Context 안에 있는 ContentResolver 오브젝트를 사용하여 클라이언트(요청하는 쪽)로서 커뮤니케이션한다 (요청 받는 쪽이 서버)

## [content provider] 콘텐트 프로바이더를 사용하여 데이터에 접근하는 방식을 간략하게 말해보세요

먼저 Access permissions 를 획득했는데 확인해야한다 그리고 컨텍스트 객체 안에 있는 ContentResolver 객체를 가져온다. ContentResolver 의 query() 함수를 통해 데이터를 끌어온다(Retrieving) query() 함수는 Cursor 를 리턴하기 때문에, 커서를 사용하여 각각의 칼럼을 가져와서 데이터를 사용한다

## [service] 서비스(service)가 무엇인지와 서비스 생명주기에 대해서 설명하시오

서비스는 보통 백그라운드에서 오랜시간 동안 수행될 때 적합한 어플리케이션 컴포넌트 이다 그리고 유저 인터페이스를 제공하지 않는다 심지어 유저가 해당 어플리케이션과 상호작용하고 있지 않을 때도 말이다 서비스는 3가지 타입이 있다

- 포그라운드
  포그라운드 서비스는 사용자에게 잘 보이는 몇몇 작업을 수행합니다. ex) 오디오 앱이라면 오디오 트랙을 재생할 때 포그라운드 서비스를 사용합니다. 포그라운드 서비스는 알림을 표시해야 합니다. 포그라운드 서비스는 사용자가 앱과 상호작용하지 않을 때도 계속 실행됩니다.

- 백그라운드
  백그라운드 서비스는 사용자에게 직접 보이지 않는 작업을 수행합니다. 예컨대 어느 앱이 저장소를 압축하는 데 서비스를 사용했다면 이것은 대개 백그라운드 서비스입니다.

- 바인드
  애플리케이션 구성 요소가 bindService()를 호출하여 해당 서비스에 바인딩되면 서비스가 바인딩됩니다. 바인딩된 서비스는 클라이언트-서버 인터페이스를 제공하여 구성 요소가 서비스와 상호작용하게 하며, 결과를 받을 수도 있고 심지어 이와 같은 작업을 여러 프로세스에 걸쳐 프로세스 간 통신(IPC)으로 수행할 수도 있습니다. 바인딩된 서비스는 또 다른 애플리케이션 구성 요소가 이에 바인딩되어 있는 경우에만 실행됩니다. 여러 개의 구성 요소가 서비스에 한꺼번에 바인딩될 수 있지만, 이 모든 것에서 바인딩이 해제되면 해당 서비스는 소멸됩니다.

서비스는 백그라운드에서 실행되는 구성 요소입니다 서비스는 사용자에게 보이는 화면이 존재하지 않으며, 정해지지 않은 시간 동안 운영됩니다 각각의 서비스는 매니페스트 파일에 서비스 태그를 이용하여 선언해야합니다 서비스는 Service 클래스를 상속받아 onStartCommand 또는 onBind ()를 재정의하여 구현할 수 있습니다. 서비스는 다른 구성 요소들처럼 메인 쓰레드에서 동작합니다 따라서 CPU를 많이 사용하거나 대기 상태를 필요로 하는 경우 새로운 쓰레드를 이용하여 생성해야합니다 또한 서비스의 객체는 단말에서 오직 1개만 생성되어 관리합니다

먼저 서비스가 startService ()로 실행되는 경우 서비스가 생성될 때 onCreate ()가 실행됩니다 이후 서비스가 실행을 시작할 때 onStartCommand ()가 호출되며 서비스의 상태가 실행중으로 변경됩니다 이후 stopService ()가 실행되면 서비스가 종료되며 onDestroy ()를 호출하며 서비스의 상태가 종료로 변경됩니다

다음으로 서비스가 bindService ()로 실행되는 경우 서비스가 생성될 때 onBind ()가 호출됩니다 다음으로 unbindService ()가 호출되어 바인딩이 해제되면 onUnbind ()가 호출됩니다 이후 완전히 종료될 때 onDestroy ()가 호출됩니다

- Service
  이것은 모든 서비스의 기본 클래스입니다. 이 클래스를 확장할 때는 서비스가 모든 작업을 완료할 수 있는 새 스레드를 생성하는 것이 중요합니다. 서비스는 기본적으로 애플리케이션의 기본 스레드를 사용하기 때문에 애플리케이션이 실행 중인 액티비티의 성능을 저하시킬 수 있습니다.

- IntentService
  이것은 Service의 하위 클래스로, 작업자 스레드를 사용하여 모든 시작 요청을 처리하되 한 번에 하나씩 처리합니다. 서비스가 여러 개의 요청을 동시에 처리하지 않아도 되는 경우에는 최선의 옵션입니다. onHandleIntent()를 구현합니다. 이는 각 시작 요청에 대해 인텐트를 수신해서 백그라운드 작업을 완료하도록 합니다.

## [service] 서비스와 인텐트 서비스의 다른점은 무엇

- 서비스는 안드로이드 서비스를 위한 기초(Base) 클래스이다 그래서 어떤한 서비스로도 확장되거나, 만들어질 수 있다 서비스를 직접적으로 상속받은 클래스는 기본적으로 메인 스레드에서 실행되기 때문에 UI를 Block 할 수 있다 그래서 비교적 간단한 태스크를 수행하거나, 무거운 작업을 하게 될 경우에는 다른 스레드를 만들어 사용해야한다

- 인텐트 서비스는 서비스의 하위 클래스 이다 "인텐트" 라고 불리는 비동기 요청을 처리하는 서비스이다 클라이언트는 startService() ()를 통해 요청을 보낸다 인텐트 서비스는 필요에 따라 실행되며, 워커 스레드를 사용하여 각각의 인텐트가 처리된다 작업을 모두 수행하면, 종료한다

## [view] Linear/Relative/Constraint/Frame 차이점?

- ConstraintLayout은 RelativeLayout의 상대적 위치 관계에 따른 배치 특성에 LinearLayout의 가중치가 가진 장점을 가지고 있으며 체인을 사용하여 다른 레이아웃없이 요소들을 그룹화 할 수 있다.

## [view] 뷰 그룹과 뷰는 차이점?

뷰는 최상위 클래스 Object를 상속받는데, 뷰를 상속받아 사용하는 클래스들을 위젯(Widget)이라고 합니다.
여기서 화면에 텍스트를 보여주기 위한 TextView, 이미지를 보여주는 ImageView, 사용자가 키보드로 입력되는 정보를 보여주는 EditText, 사용자로부터 액션을 받거나 정보를 받는 데 사용되는 Button, CheckBox, RadioButton은 가장 자주 사용되는 뷰들입니다.

다음은 뷰 그룹에 대한 상속관계입니다.
뷰 그룹은 뷰를 상속받은 것으로 뷰 그룹을 상속받은 클래스들을 레이아웃(Layout)이라고도 합니다.
레이아웃에는 FrameLayout, AbsoluteLayout, RelativeLayout, LinearLayout, AdapterView가 있으며, 각 항목별로 상속받은 클래스들로 이루어져 있습니다.

이 상속도를 보면 뷰 그룹도 뷰를 상속받기 때문에 뷰의 일종이라는 것을 알 수 있습니다.
그 말은 즉, 하나의 뷰 그룹이 다른 뷰 그룹에 뷰로서 포함될 수 있다는 것을 뜻합니다.

## [view] RecyclerView 와 ListView 차이점?

ListView와는 다르게 RecyclerView는 이름에서 알 수 있듯이 재활용이 가능한 뷰이다. 무엇을 재활용 할까? 파란색 라인 한 개가 채팅방 리스트 한 개라고 가정하자. 전체 채팅방 리스트는 100개가 훌쩍 넘을 수가 있다. 그러나 정작 화면에 보여지는 채팅방 목록은 한 번에 10개 조차 되지 않는다. 매번 사용자가 아래로 스크롤 할 때 마다 맨 위에 위치한 뷰 객체가 새로 삭제되고, 아랫 부분에서 새로 나타날 채팅방 뷰 객체를 새로 생성하면 결국 100개의 뷰 객체가 삭제되고 생성되는 것일 뿐만 아니라, 스크롤을 위아래로 왔다 갔다 하면 수 백개의 뷰 객체가 새로 생성되고 삭제됨을 반복한다.

리사이클러 뷰는 사용자가 아래로 스크롤 한다고 가정했을 때, 맨 위에 존재해서 이제 곧 사라질 뷰 객체를 삭제 하지않고 아랫쪽에서 새로 나타나날 파란색 뷰 위치로 객체를 이동시킨다. 즉 뷰 객체 자체를 재사용 하는 것인데, **중요한 점은 뷰 객체를 재사용 할 뿐이지 뷰 객체가 담고 있는 데이터(채팅방 이름)는 새로 갱신된다는 것이다. 어쨋거나 뷰 객체를 새로 생성하지는 않으므로 효율적인 것이다.**

## [view] RecyclerView 를 어떻게 사용하나요

`ViewHolder`
위에서 설명 햇듯이, 스크롤을 밑으로 내릴 때, 맨 위에 존재해서 이제 곧 사라질 파란색 뷰 객체는 맨 아래로 이동하여 재활용된다. 즉, 10개의 뷰 객체만 계속해서 위에서 아래로 이동하면서 재사용 되는 것이며, 우리는 딱 10개 정도의 뷰 객체만을 만들어서 가지고 있으면 된다. 10개의 뷰 객체들은 언제든 text라던지 이미지가 바뀔 수 있다(뷰 객체를 재사용 할 뿐이지 재사용 될 때의 데이터는 계속 바껴야 하기 때문이다). 따라서 맨 처음 10개의 뷰객체를 기억하고 있을(홀딩) 객체가 필요한데 이 것이 ViewHolder이다. 나중에 전체 코드를 보겠지만, ViewHolder 코드 부분만 보자면 아래와 같다.

Adpater와 LayoutManager 는 리싸이클러뷰에서 필수적이다. Adapter는 100개의 채팅방 제목 이름이 담긴 리스트를 리사이클러 뷰에 바인딩 시켜주기 위한 사전 작업이 이루어 지는 객체이다. 직접 작성해서 리사이클러뷰에 적용시키면 된다. LayoutManager는 많은 역할을 하지만 간단하게 스크롤을 위아래로 할지, 좌우로 할지를 결정하는 것이라고 생각하자. 실제로는 더 많은 역할을 하지만 자세한건 구글링…ㅎ

```java
// MainActivity
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_recycler_view)

    val datas = Array(100) {
        "chat $it"
    }

    recycler_view.adapter = MyApdater(datas)
    recycler_view.layoutManager = LinearLayoutManager(this)
}
```

```java
class MyApdater(private var datas: Array<String>) : RecyclerView.Adapter<MyViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item, parent, false)
        Log.d("tag1" , "onCreateViewHolder")
        return MyViewHolder(view)
    }

    override fun getItemCount(): Int {
        return datas.size
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        Log.d("tag1" , "onBind")
        holder.textField.text = datas[position]
    }
}

class MyViewHolder(view: View): RecyclerView.ViewHolder(view) {
    var textField = view.chat_title
}

onCreateViewHolder
getItemCount다음으로 호출되는 함수는 onCreateViewHolder함수이다. 이름에서 알 수 있듯이 ViewHolder가 생성되는 함수다. 여기서 ViewHolder객체를 만들어 주면 된다.

위에서 언급했듯이 맨 처음 화면에 보이는 전체 리스트 목록이 딱 10개라면, 위아래 버퍼를 생각해서 13~15개 정도의 뷰 객체가 생성된다. 정확하게 말하자면 뷰 객체를 담고 있는 ViewHolder가 생성되는 것이다. 그래서 onCreateViewHolder함수는 딱 13~15번 정도만 호출되고 더 이상 호출되지 않는다.

return되는 곳에서 MyViewHolder의 생성자에 view 객체를 넘겨주는데, 이 view객체는 아까 사진에서 본 한개의 채팅방 목록이 디자인 되어있는 레이아웃이다. 즉 viewHolder는 그 레이아웃을 인자로 받아서 기억하고 있는 것이다. 이제는 계속해서 재사용되는 뷰 홀더(레이아웃)들에 데이터를 바인딩 해주는 작업만 남았다.

onBindViewHolder
onBindViewHolder함수는 생성된 뷰홀더에 데이터를 바인딩 해주는 함수이다. 이름이 참 직관적이여서 좋다.

ex) 데이터가 스크롤 되어서 맨 위에있던 뷰 홀더(레이아웃) 객체가 맨 아래로 이동한다면, 그 레이아웃은 재사용 하되 데이터는 새롭게 바뀔 것이다. 고맙게도 아래에서 새롭게 보여질 데이터의 인덱스 값이 position이라는 이름으로 사용가능하다. 즉 아래에서 새롭게 올라오는 데이터가 리스트의 20번째 데이터라면 position으로 20이 들어오는 것이다.

onCreateViewHolder는 ViewHolder를 만들기 위해 13~15번 정도밖에 호출되지 않지만, onBindViewHolder는 스크롤을 해서 데이터 바인딩이 새롭게 필요할 때 마다 호출된다. 스크롤을 무한정 돌린다면, onBindViewHolder도 무한정 호출된다. 무한정 호출된다 하더라도 우리는 딱 13~15개의 뷰 객체만 사용하는 꼴이다.

## [error] ANR 이 무엇이고 언제 일어나며, 어떻게 예방할 수 있나요

Android Not Responding 에 약자로 일정시간 Main Thread 태스크가 잡혀있는 것을 말한다.Main Thread에서 실행되는 임의의 method는 최소한의 일을 해야한다.
특히 onCreate( )나 onResume( ) 같은 안드로이드의 핵심 생명주기에 속해있는 method에서는 가능한 적은 일을 수행해야한다.
예시로 onCreate() 함수에서 종료 조건이 없는 while loop 를 지나치게 돌리게되면 ANR 이 발생하기 쉽다.

## [error] LMK?

LMK(Low Memory Killer) 안드로이드에서 가용 메모리(available memory)가 부족할 때 프로세스들을 죽이는 동작이다

- LMK의 목적

LMK의 목적은 바로 가용 메모리를 확보하는 것이다 이것이 부족하면, PC나 휴대폰 등과 같은 시스템들의 성능이 크게 떨어집니다 무지무지 느려지는 거죠 심하면 앱 하나 띄우는데 몇 초 이상의 시간이 걸릴 수도 있습니다 이런 문제를 방지하기 위해서 안드로이드는 사용하지 않는 프로세스들을 메모리에서 지워야 합니다 여러분들이 가지고 계시는 안드로이드 폰들에서 LMK가 바로 이러한 역할을 수행하고 있습니다

- LMK 의 Priority

LMK 는 우선순위를 가지며 우선순위가 낮은 경우 부터 메모리에서 해제된다 (아래로 갈수록 우선순위가 낮다)

- foreground process(현재 포그라운드에 올라온 애플리케이션, 현재 동작하고 있는 서비스)

- visible process(사용자가 화면에서 볼 수 있지만 포그라운드가 아닌 경우 ex 다이얼로그 에 가려진 onPause 상황 )

- service process (직접 화면에 보이지는 않지만, 백그라운드에서 동작하는 데이터 업로드 또는 다운로드 경우, 오랫동안 동작한 서비스)

- cached process (현재 사용하지는 않지만, 메모리에 적재되어 있는 프로그램)

### [error] OOM(Out of memory) Killer와 LMK

안드로이드는 먼저 LMK 로 진행하다가, 더 이상 내릴 프로그램이 없을 때 OOM 순서를 밟는다

## [broadcast receiver] 브로드 캐스트 리시버에서 Toast를 띄우면

브로드캐스트 리시버는 다른 앱에서 브로드캐스팅한 메시지들에 대해 반응을 하기 위한 클래스를 말한다. 예를 들면 다른 앱에서 원격 파일 다운로드를 시행하였고 다운로드가
완료되었을 때 스마트폰에서 어떤 작업을 해야할 필요가 있을 경우, 다운로드 완료시 발생하는 메시지를 브로드캐스트 리시버 클래스를 활용하여 받아 후속작업을 진행할 수
있다. 브로드캐스트 리시버를 개발하는 경우 두가지 작업을 하게 되는 데, 하나는 브로드캐스트 리시브 클래스를 만들어야 하며 또 다른 하나는 시스템에 브로드캐스트 리시버 클래스를 등록하는 것이다.

## [basic] Dagger, Hilt (DI)

의존성 주입을 구현하면 다음과 같은 이점을 누릴 수 있습니다. 코드 재사용 가능, 리팩터링 편의성, 테스트 편의성 라이브러리는 koin 이나 Dagger, Hilt 를 사용할 수 있다.

## [basic] 어플리케이션(application)과 컨텍스트(context)에 대해서 설명

어플리케이션 앱 프로세스가 실행되면 가장 먼저 생성되는 객체로 하나의 어플리케이션 객체는 하나의 앱 프로세스와 대응됩니다 앱이 백그라운드로 내려가도 앱 프로세스는 계속 살아있기 때문에 어플리케이션 객체도 살아있다고 할 수 있습니다 안드로이드의 Application Class 는 액티비티 및 서비스와 같은 다른 모든 구성 요소(액티비티(Activity), 서비스(Service), 브로드캐스트 리시버, 콘텐트 프로바이더, 인텐트(Intent))에 접근 가능한 기본 클래스입니다 또한 애플리케이션 프로세스가 생성될 때, 가장 먼저 초기화 됩니다 그렇기 때문에, 보통 앱 전역에서 일관성있게, `사용하는 요소들을 등록`하여 사용하곤 합니다. 컨텍스트는 안드로이드의 컴포넌트들이 동작하기 위해 필요한 정보를 담고 있는 객체를 말합니다 각각의 컴포넌트들(액티비티, 서비스, 브로드캐스트 리시버 등)은 자신만의 컨텍스트를 가지고 있습니다 컨텍스트 내에는 어플리케이션의 정보(패키지명 등), 컨텍스트가 실행되는데 필요한 정보(테마 등)를 얻거나 시스템 서비스(윈도우 매니저, 레이아웃 인플레이터 등)를 구동하는데 사용됩니다

- Context

  Context 는 리소스에 접근하거나, 데이터베이스나 프리퍼런스(`preference`)에 접근하는 등 기타 등등 역할들을 제공한다 앞으로 비교할 다른 Context 와 다른 중요한 점은 애플리케이션에서 현재 실행되고 있는 환경을 가지고 있다는 것이다

- Application Context

  애플리케이션 라이프 사이클에 종속되어 있다(애플리케이션이 만들어지고 유지되다가, 종료될 때 없어진다) 애플리케이션 컨텍스트는 라이프사이클이 현재 컨텍스트와 상관없는 다른 컨텍스트가 필요하거나 액티비티 활동 범위를 벗어난 컨텍스트를 필요할 때 사용할 수 있습니다 Ex) Dialog 는 액티비티 Context 가 필요하고, Toast 는 Application Context 로 사용할 수 있다 (Toast 는 액티비티와 별개로 Window 를 가지고 있다) Snackbar 는 다를 수 있다

- Activity Context

  액티비티 안에서 사용할 수 있는 Context 로 액티비티 라이프 사이클에 종속되어 있다 액티비티의 라이프사이클과 맞물리는 작업에서 필요할 때 사용한다 제일 많이 사용하는 화면이동에서 A 에서 B 로 이동할 경우, 이때 A 의 액티비티 컨텍스트가 필요하다 물론 Application Context 로도 화면을 실행시킬 수 있지만, 이때는 인텐트에 IntentFLAG_ACTIVITY_NEW_TASK 플래그가 필요하다

## [basic] 노티피케이션(notification)은 무엇인가 (FCM, pending intent)

노티피케이션은 일반적으로 어떠한 서비스에서 푸쉬 메시지를 보내는 것을 말합니다. FCM은 어떤 푸쉬 서버를 두고
Firebase 를 이용을 하여 푸쉬 메시지를 보내는 것입니다. 먼저 앱을 위하여

- 앱을 위한 키를 FCM 서버를 통해 얻는 단계 (초기화 과정)
  모바일에 앱이 설치되는 순간 Firebase 서버에 키 획득을 위한 요청을 보냄
  Firebase 서버에서 키를 만들어 모바일에 전달
  모바일 앱에 전달된 키를 서버에 전송
  서버는 전달받은 키를 db에 저장하여 타겟 모바일의 identification으로 사용

- 서버에서 데이터를 스마트폰에 전달하는 절차 (일반적인 과정)
  서버에서 데이터를 타겟 모바일에 전달하기 위해 DB에서 키를 획득
  DB의 키와 전송하고자 하는 데이터를 HTTP 통신으로 Firebase 서버에 전달
  Firebase 서버에서는 전달받은 키값을 식별해 어떤 모바일의 어떤 앱인지를 식별
  식별된 모바일의 식별된 앱을 실행하여 데이터 전달 (타겟 모바일의 앱은 백그라운드에 있는 상태에서도 리스너로 이벤트를 감지함)

## [basic] 안드로이드 매니페스트(android manifest)

안드로이드 매니페스트는 앱의 이름, 버전, 구성요소, 권한 등 앱의 실행에 있어서 필요한 각종 정보가 저장되어있는 파일입니다
반드시 존재해야하는 xml 형식의 파일로 안드로이드 프로젝트의 최상위에 위치하고 있습니다. 가장 최상위는 manifest 태그가 위치하고 있습니다 manifest 태그에는 패키지명, 앱 버전 코드, 앱 버전 이름을 정의합니다

- application 태그에는 앱 아이콘, 앱 이름을 정의합니다

- activity 태그에는 액티비티의 클래스명과 액티비티 이름을 정의합니다 하위에는 intent-filter 태그를 이용하여 액티비티에 대한 인텐트 작업시 필요한 action과 category를 정의합니다

- service, receiver, provider 태그에는 각각 서비스, 리시버, 프로바이더에 대한 내용을 정의합니다

- permission 태그에는 앱에서 필요한 권한에 내용을 정의합니다

## [basic] 디스플레이(display), 윈도우(window), 서피스(surface), 뷰(view), 뷰 그룹(view group), 뷰 컨테이너(view container), 레이아웃(layout)

디스플레이 : 안드로이드 단말기가 가지고 있는 하드웨어 화면을 의미합니다

윈도우 : 안드로이드에서 실행되는 앱이 그림(뷰)을 그릴 수 있는 영역을 의미합니다 사용자로부터 입력(터치, 키) 이벤트를 받아 앱에 전달합니다

서피스 : 윈도우에 그림(뷰)을 그릴 때 그림이 저장되는 메모리 버퍼를 의미합니다

뷰 : 사용자 인터페이스를 구성하는 최상위 클래스를 말합니다 윈도우의 서피스를 이용하여 화면에 어떤 모양으로 그림을 그릴지와 발생하는 이벤트를 어떻게 처리할 것인지에 대한 기능을 구현하고 있습니다 뷰 중에서 일반적인 제어 역할을 하고 있는 것들을 위젯이라고 합니다

뷰 그룹 : 여러개의 뷰를 포함하고 있는 뷰를 의미합니다

뷰 컨테이너 : 다른 뷰를 포함할 수 있는 뷰를 의미합니다 대표적으로 리스트 뷰(list view), 스크롤 뷰(scroll view), 그리드 뷰(grid view) 등이 있습니다

레이아웃 : 뷰 그룹 중에서 내부에 뷰를 포함하고 있으면서 해당 뷰를 어떻게 윈도우에 배치할지 정의하는 관리자 역할을 하는 클래스 말합니다

## [basic] 인플레이션(inflation)이란 무엇인가

xml 레이아웃 파일로 정의한 정보를 런타임에 액티비티 onCreate() 콜백 함수에서 setContentView ()가 호출됨에 따라 메모리 상에 객체로 만들어주는 과정을 말합니다
이 과정에서 xml 레이아웃 파일에서 뷰에 id를 설정하고 해당 id가 Rjava 파일에 주소 값으로 환원되며 findViewById ()와 id를 이용하여 코드 상으로 뷰 객체를 가져와 제어할 수 있습니다. 리액티브 네이티와 IOS 와는 다르게 선언형 UI 가 아니다. 하지만, Compose 가 등장을 하면서 선언형 UI 를 접목하려는 시도가

## [basic] 안드로이드 MVC, MVP, MVVM

- MVC
  안드로이드에서 뷰는 화면에 실제로 보이는 구성을 만드는 영역으로 View 클래스를 상속하는 클래스를 이용하여 구성할 수 있습니다 다음으로 컨트롤러는 뷰와 모델을 서로 연결하며 제어하는 영역으로 액티비티, 서비스, 브로드캐스트 리시버, 프래그먼트로 구성됩니다 마지막으로 모델은 앱의 다양한 데이터를 저장하는 역할로 SQLite를 이용한 DB, SharedPreference를 이용한 파일 시스템, 콘텐트 프로바이더가 있습니다

- MVP
  ‘MVP 패턴’은 Model, View, Presenter의 앞글자를 따서 이름이 지어졌습니다. 이 패턴의 핵심 아이디어는 사용자 인터페이스(View)와 비즈니스 로직(Model)을 분리하고, 서로간에 상호작용을 다른 객체(Presenter)에 위임해 서로의 영향을 최소화하는 것에 있습니다. 각 파트의 자세한 설명을 살펴보면 아래와 같습니다.

  - Model : 내부적으로 쓰이는 데이터를 저장하고, 처리하는 역할을 합니다. 흔히 ‘비즈니스 로직’ 이라고 부르는 부분입니다. View, Presenter등 다른 어떤 요소에도 의존적이지 않은 독립적인 영역이죠.
  - View : 사용자 인터페이스(User Interface-UI)라 불리는 영역입니다. 안드로이드에서는 Activity, Fragment가 대표적인 예입니다. Model에서 처리된 데이터를 Presenter를 통해 받아서 사용자에게 보여주며, 사용자 액션 및 Activity lifecycle 변화를 감지해서 Presenter에 보내는 역할을 합니다. Presenter를 이용해 데이터를 주고받기 때문에 Presenter에 의존적입니다.
  - Presenter : Model과 View사이의 매개체입니다. View에서 캐치한 유저 액션을 전달 받아서 Model의 로직을 호출하거나, Model의 로직으로부터 나온 결과를 전달 받아서 View에 보내 UI변경을 야기하는 등 둘 사이의 소통의 역할을 합니다. Model, View 모두에 의존적입니다.

- MVVM

  - Model:
  - View:
  - ViewModel:


## [basic] ARM64-v8a(64), ARMv7, ARMx86 등 ABI(Application binary interface)가 무엇인가요

> 안드로이드 디바이스는 다양한 CPU 를 사용하여 만들고, CPU에서 제공하는 명령셋은 다양하다, 대표적인것이 ARMv7 이 있고, 우리가 작성한 코드가 javac에 의해 바이트 코드(class)로 바뀌고, Dalvik VM(현재는 ART VM) 안에서 JIT 컴파일을 통해 기계어로 번역 되는데, 이때 이 기계어를 해석하고 명령하는데, 이때 CPU 마다 명령을 실행하는 방법이 다르고, 실행 가능한 바이너리 형식, 명령 집합 등이 정의되어 있는 것이 애플리케이션 바이너리 인터페이스(ABI) 이다

## [basic] 바이트 코드를 안드로이드에서 바로 실행할 수 있나요?

> 바로 실행할 수 없다 Java 바이트 코드를 실행하려면 JVM (Java Virtual Machine)이 필요하지만, 안드로이드는 JVM 대신 Dalvik VM 을 사용하여, 메모리, 배터리 수명 및 성능에 더 초점을 맞춰 개발이 되었기 때문에 실행할수 없다또한 dx 라는 안드로이드 도구를 사용하여 Java 클래스 파일을 Dalvik 실행 파일(dex 파일)로 바꿔 실행한다

- Dalvik VM : 32비트만 지원 (JIT 컴파일러 - 실행하면 만들어 놓고)

- ART VM : 32비트, 64 비트 모두 지원 (AOT 컴파일러 - 미리 만들어 놓고)

## [basic] SharedPreferences 에서 commit() 과 apply() 의 다른점에 대해 말해주세요

apply 는 부울 반환 값이 없이 반환을 하나 commit 은 부울 값을 반환한다. apply() 비동기로 일어나면 commit() 동기로 일어나나다.

## [basic] 빌드타입이 무엇인가요

빌드타입이란 현재 사용하고 있는 라이브러리, 모듈 등의 빌드 방법을 정의하는 것이다 안드로이드 앱이 패키징 되고, 빌드 될 때 그래들을 사용하여 빌드 타입을 정의할 수있다 빌드할 때 추가되어야하는 리소스를 분리하여 적용할 수 있다 또한 build variant 와 다양하게 조합해서 제품의 flavours 나 build type 을 정의할 수 있다

- flavor = [local, dev, stage, real]

- buildType = [debug, release]

## [basic] 안드로이드 빌드 프로세스에 대해 간략하게 설명

1. Android asset packaging tool (AAPT) 를 사용하여 리소스(/res 이하 파일들)를 컴파일한다 이때 Rjava 라고 불리는 하나의 클래스로 컴파일 되어진다

2. java 파일들이 javac 로 부터 class 파일로 컴파일 된다 그리고 클래스 파일들은 dx 툴(Android SDK tools 아래 포함되어 있다)에 의해 달빅 바이트 코드(classesdex)로 변환된다

3. APKbuilder 에 의해 apk(android packagin key) file이 만들어 진다 현재는 각 디바이스의 해상도, 언어, abi 타입등으로 나눠 들어가 있는 apks 로 제공되어 나중에 디바이스에 필요한 리소스만 가지고, 애플리케이션을 만드는 AAB(android app bundle) 로 사용되기도 한다

## [basic] minsdk, compilesdk, targetsdk

- minSdkVersion : 앱이 실행될 수 있는 최소한의 API 레벨을 일컫는다. minSdkVersion API 레벨 미만의 디바이스는 앱 설치가 안 된다.

- compileSdkVersion : 컴파일 시에 사용할 버전을 일컫는다. 컴파일 시에 어느 버전의 android.jar을 사용할 지 정한다. 예로 소스코드에 API Level 21부터 추가된 메서드를 이용하고 compileSdkVersion을 19로 지정한 경우 컴파일 할 때 해당 메서드가 존재하지 않는다는 오류가 납니다.

- targetSdkVersion : 앱 실행 시 이용되는 설정이다. 실제 API Level에 따른 분기를 코딩할 때 targetSdkVersion을 보고 처리를 나눈다. 따라서 targetSdkVersion이 바뀌면 앱의 동작이 달라질 수 있다. 만약 targetSdkversion을 지정하지 않으면 minSdkVersion과 동일한 값으로 지정된다. 그래서 반드시 지정해야 한다. 또한 단말 버전에 따라 최신 기능을 쓸 수 있기 때문에 높은 API 레벨을 쓰는 것을 추천한다.

## [basic] 안드로이드의 4대 컴포넌트

- 액티비티는 안드로이드에서 `화면을 관리하고 사용자의 다양한 이벤트를 처리하는데 사용`됩니다
- 서비스는 화면에서 보이지 않지만 특정한 기능을 `백그라운드`에서 처리하는데 사용됩니다
- 브로드캐스트 리시버는 안드로이드에서 발생하는 `특정 브로트캐스트 메세지`를 처리하기 위한 컴포넌트입니다. - 다운로드가 완료되었거나 충전이 완료된 것을 의미합니다
- 콘텐트 프로바이더는 앱 사이의 데이터의 공유를 위한 인터페이스를 제공하는 컴포넌트입니다. ex) 갤러리 이미지를 이메일로 공유를 하거나 넘길 때 사용합니다.

### [basic] 쓰레드간 통신방법에 대해 설명

1. Java IO에서 제공하는 파이프를 이용한 방법
2. 쓰레드간의 공유메모리를 통한 접근 (인스턴스 맴버변수,클래스멤버변수)
3. synchronized를 이용한 시그널링
4. BlockingQueue를 이용한 방법

핸들러 - 루퍼 - 메시지 큐 - 메시지

- androidosLooper : UI 스레드에 하나가 존재하며 소비자 스레드와 연관된 메시지 발송자 (데이터를 읽는 역활) (소비자 => 데이터를 읽는다)
- Handler : 큐에 메시지를 삽입하는 생산자 스레드를 위한 인터페이스와 소비자 스레드 메시지 처리, 하나의 Looper 객체는 많은 핸들러를 갖지만 모두 같은 큐에 삽입
- MessageQueue : 소비자 스레드에서 처리할 메시지들이 담긴 무제한의 연결 리스트 모든 루퍼와 스레드는 최대 하나의 메시지 큐를 가진다
- Message : 소비자 스레드에서 실행하는 메시지

## [db] Realm이란 (SQLite와의 비교) [렐름] Jetpack Room

sqlite,realm은 안드로이드 단말에서 사용하는 관계형 데이터베이스입니다

sqlite는 오픈소스 데이터베이스로 OS와 상호작용하기위해 SQLiteOpenHelper인터페이스를 이용합니다 SQLite는 C언어로 되어있고 경량데이터베이스이며 하나의 디스크 파일에 모든 데이터를 저장 할 수 있습니다

Realm은 크로스 플랫폼 기반의 모바일 데이터베이스입니다 IOS와 Android에서 모두 사용이 가능하며 성능 및 효율성이 우수합니다 설치도 간편하며 쿼리 응답속도도 기타 ORMLite나 SQLite보다 더 좋습니다 크로스 플랫폼이기 때문에 협업에서 유용합니다

특징으로는 zero-copy모델을 사용하기 때문에 데이터 객체 자체에서 그대로 작업이 가능합니다 크로스 플랫폼이기 때문에 특정 OS를 가리지 않고 동기화 될 수 있습니다
ACID를 준수합니다

Realm은 데이터베이스 컨테이너의 인스턴스, SQLite 기반의 ORM 프레임워크 입니다

## [intent] PendingIntent에 대해서 설명 (pending:보류)

Intent를 직접 보내지 않고 다른 클래스에서 Intent를 위임해주기 위한 클래스이다 보통 NotificationBar와 상호작용 하는 어플리케이션을 작성할때 사용된다 즉 알림바, 알람, 다른앱에서 startActivity,sendBroadCast,StartService가 실행되게 하고 싶을때 Intent를 PendingIntent에 담아서 호출한다

## [intent] FLAG_ACTIVITY_CLEAR_TASK 와 FLAG_ACTIVITY_CLEAR_TOP 의 차이점은 무엇

- FLAG_ACTIVITY_CLEAR_TASK 는 호출된 클래스의 존재하는 모든 인스턴스들을 포함한 작업(Task)에 있는 모든 액티비티들을 클리어 시킬 때 사용한다 (액티비티 스택에 쌓인 모든 액티비티를 클리어 시키고, 한개의 액티비티를 실행할 때 자주 사용하게 된다)

- FLAG_ACTIVITY_CLEAR_TOP 는 액티비티가 실행될 때 (set), 액티비티 스택에 이미 존재한다면, 그 아래 있는 모든 작업(Task)이 제거 되고, 현재 실행하는 작업(TASK) 이 작업 리스트(Task list)의 루트가 된다 반면에 액티비티 스택에 존재하지 않는다면, 작업 리스트(Task list) 의 루트에 새로운 인스턴스가 생성된다 보통 FLAG_ACTIVITY_NEW_TASK 와 함께 사용하는 것이 추천된다

## [intent] 인텐트란 무엇인가요(암시적/묵시적)

Intent는 메시징 객체로, 다른 앱 구성 요소로부터 작업을 요청하는 데 사용할 수 있습니다. 인텐트가 구성 요소 사이의 통신을 촉진하는 데는 여러 가지 방식이 있지만 기본적인 사용 사례는 크게 세 가지로 나눌 수 있습니다.

- 액티비티 시작
  Activity는 앱 안의 단일 화면을 나타냅니다. Activity의 새 인스턴스를 시작하려면 Intent를 startActivity()로 전달하면 됩니다. Intent는 시작할 액티비티를 설명하고 모든 필수 데이터를 담습니다. 액티비티가 완료되었을 때 결과를 수신하려면, startActivityForResult()를 호출합니다. 액티비티는 해당 결과를 이 액티비티의 onActivityResult() 콜백에서 별도의 Intent 객체로 수신합니다. 자세한 내용은 액티비티 가이드를 참조하세요.

- 서비스 시작
  Service는 사용자 인터페이스 없이 백그라운드에서 작업을 수행하는 구성 요소입니다. Android 5.0(API 레벨 21) 이상부터는 JobScheduler로 서비스를 시작할 수 있습니다. JobScheduler에 대한 자세한 내용은 API-reference documentation을 참조하세요. Android 5.0(API 레벨 21) 이하 버전은 Service 클래스의 메서드를 사용하면 서비스를 시작할 수 있습니다. 서비스를 시작하여 일회성 작업을 수행하도록 하려면(예: 파일 다운로드) Intent를 startService()에 전달하면 됩니다. Intent는 시작할 서비스를 설명하고 모든 필수 데이터를 담고 있습니다. 서비스가 클라이언트-서버 인터페이스로 디자인된 경우, 다른 구성 요소로부터 서비스에 바인딩하려면 Intent를 bindService()에 전달하면 됩니다.

- 브로드캐스트 전달
  브로드캐스트는 모든 앱이 수신할 수 있는 메시지입니다. 시스템은 시스템이 부팅될 때 또는 기기가 충전을 시작할 때 등 시스템 이벤트에 대한 다양한 브로드캐스트를 전달합니다. Intent를 sendBroadcast() 또는 sendOrderedBroadcast()에 전달하면 다른 앱에 브로드캐스트를 전달할 수 있습니다.

- 명시적 인텐트는 인텐트를 충족하는 애플리케이션이 무엇인지 지정합니다. 이를 위해 대상 앱의 패키지 이름 또는 완전히 자격을 갖춘 구성 요소 클래스 이름을     제공합니다. 명시적 인텐트는 일반적으로 앱 안에서 구성 요소를 시작할 때 씁니다. 시작하고자 하는 액티비티 또는 서비스의 클래스 이름을 알고 있기 때문입니다. ex), 사용자 작업에 응답하여 새로운 액티비티를 시작하거나 백그라운드에서 파일을 다운로드하기 위해 서비스를 시작하는 것 등이 여기에 해당됩니다.

- 암시적 인텐트는 특정 구성 요소의 이름을 대지 않지만, 그 대신 수행할 일반적인 작업을 선언하여 다른 앱의 구성 요소가 이를 처리할 수 있도록 해줍니다. ex) 사용자에게 지도에 있는 한 위치를 표시하고자 하는 경우, 암시적 인텐트를 사용하여 해당 기능을 갖춘 다른 앱이 지정된 위치를 지도에 표시하도록 요청할 수 있습니다.

## [intent] Intent 구성요소

- Action
  수행할 작업을 나타내는 문자열이다. 일반적인 Action은 Intent내에 리터럴 상수로 정의되어 있다.

- Data
  작업을 수행할 데이터 및 데이터의 MIME유형을 참조하는 Uri객체 이다.

- Category
  인텐트를 처리해야 하는 컴포넌트의 종류에 대한 추가 정보를 담은 문자열이다.

- Extra
  요청한 작업을 수행하기 위해 필요한 추가 정보를 담고있는 Key:Value이다.

- Flags
  인텐트에 대한 메타데이터 같은 기능을 한다. 액티비티를 시작하는 방법에 대해 명시, 액티비티를 시작한 다음 어떻게 처리해야 할지도 명시

## [intent] 인텐트 필터(intent filter)에 대해서 설명하시오

암시적 인텐트를 통해 사용자로 하여금 어떤 앱을 사용할지 선택하도록 하고자 할 때 IntentFilter가 필요하다. ex) 사용자가 다른 사람들과 공유했으면 하는 콘텐츠를 가지고 있는 경우, "ACTION_SEND"라는 Action을 가진 인텐트를 생성한 다음 공유할 콘텐츠를 지정하는 Extra를 추가한다. 해당 인텐트로 startActivity를 호출하면 사용자가 어느 앱을 통해 콘텐츠를 공유할지 선택 가능하다. 암시적 인텐트를 수신하려면 앱의 컴포넌트에 하나 이상의 <intent-filter>를 메니페스트에 선언

### AAPT?

AAPT는 Android Asset Package Tool의 약자이다. 이것은 패키징 프로세스를 다룬다. 안드로이드 빌드 툴의 일부로 SDK안에 포함되어 있다. 빌드 과정에서는 안드로이드 앱의 소스를 제회한 나머지 파일을 정리하여 apk로 패키징 하는데 쓰인다. R.java파일은 안드로이드 프로젝트에서 사용되는 리소스 들에 대한 액세스를 간편하게 해 주기 위해 자동으로 생성되는 소스 파일이다. 이 파일을 생성하기 위해서는 appt툴을 이용한다.

### NDK?

   NDK는 Native Developmet Kit의 약자이며, Android 앱에C 또는 C++(“네이티브 코드”)를 삽입할 수 있게 해주는 도구 집합이다.

### ANR?

ANR(Application Not Responding) 어플리케이션이 응답하지 않는다는 에러이다. 응용 프로그램이 5초 이상 사용자의 입력에 반응하지 않을 때 
브로드캐스트 리시버가 10초 내로 리턴하지 않을 때

예방 방법

onCreate()나 onResume()같은 핵심 생명주기 메소드에서는 가장 적은일을 수행해야 한다. 시간 소모가 많은 작업은 스레드를 통해 처리한다.
사용자에게 프로그레스바 등을 이용해 작업의 진행 과정을 안내해 기다리도록 한다.

### ADB

ADB는 Android Debug Bridge의 약자로 Android를 위한 Debugging Tool이다. 이 도구는 앱 설치 및 디버깅과 같은 다양한 기기 작업을 쉽게 해주고, 에뮬레이터나 연결된 기기에서 다양한 명령을 실행하는데 사용할 수 있는 Unix 셸 액세스를 제공한다.

### 안드로이드 4대 컴포넌트

- 액티비티

  액티비티는 사용자 인터페이스가 있는 단일화면을 나타낸다. 하나 이상의 view를 가질 수 있다. 다른 어플리케이션의 액티비티에 접근하는 것도 가능하다. 안드로이드에서 화면을 관리하고 사용자의 다양한 이벤트를 처리하는데 사용됩니다.

- 서비스

  서비스는 백그라운드에서 실행되는 컴포넌트이다. 보통 오랜 시간이 걸리는 작업, 원격 프로세스를 위한 작업, 계속 실행해야하는 작업을 할 때 사용 된다. 한번 시작된 서비스는 어플리케이션이 종료되어도 백그라운드에서 실행된다.화면에서 보이지 않지만 특정한 기능을 백그라운드에서 처리하는데 사용됩니다.

   - 브로드캐스트 리시버

   브로드캐스트 수신자는 안드로이드에서 디바이스에서 발생하는 이벤트 및 정보를 받을 수 있게 하는 컴포넌트이다. 전화 및 수신, 네트워크 끊김과 같은 정보를 안드로이드 OS에서 어플리케이션으로 방송해주는데, 이를 받기 위해 사용된다.

   - 콘텐트 프로바이더

   콘텐트 프로바이더는 데이터를 관리하고, 다른 어플리케이션의 데이터를 받을 수 있는 컴포넌트이다. 앱 사이의 데이터의 공유를 위한 인터페이스를 제공하는 컴포넌트

   파일 입출력, SQLite, DB, Web등을 통하여 데이터를 관리 할 수 있다. 어플리케이션 계층과 데이터 계층을 분리하여 중간 가교 역할을 담당한다. 어플리케이션은 콘텐트 프로바이더에 접근하면, 필요한 데이터를 얻어 올 수 있다.

   브로드캐스트 리시버는 안드로이드에서 발생하는 특정 브로트캐스트 메세지를 처리하기 위한 컴포넌트입니다.

### Android Application의 구조?

   AndroidManifest.xml : 앱에 대한 전체적인 정보를 담고있는 파일입니다. 앱의 구성요소와 실행 권한 정보가 정의되어있습니다.

   java

   자바 코드를 저장하는 공간입니다. 표준 자바와 동일하게 패키지를 이용한 하위 디렉토리 생성 방식을 사용합니다.

   res

   리소스(이미지, xml 레이아웃, 메뉴, 값)를 저장하는 공간입니다.

   drawable : 이미지 파일 저장

   mipmap : 아이콘 이미지 저장

   value : 문자열, 색상값, 수치값, 스타일 저장

   gradle

   앱에 대한 컴파일 버전정보, 의존성 프로젝트에 대한 정의가 되어있는 파일입니다.

   project > build.gradle : 프로그래머가 직접 작성한 그래들 빌드 스크립트 파일입니다.

   gradle > build.gradle : 앱에 대한 컴파일 버전정보, 의존성 프로젝트에 대한 정의가 되어있는 파일입니다.

### 컨텍스트란?

어플리케이션 환경에 관한 글로벌 정보를 접근하기 위한 인터페이스. Abstract 클래스이며 실재 구현은 안드로이드 시스템에 의해 제공된다. Context 를 통해, 어플리케이션에 특화된 리소스나 클래스에 접근할 수 있을 뿐만 아니라, 추가적으로, 어플리케이션 레벨의 작업 - Activity 실행, Intent 브로드캐스팅, Intent 수신 등, 을 수행하기 위한 API 를 호출 할 수도 있다.

- Application Context
실행 중인 안드로이드 어플리케이션의 Singleton Instance이다.

- Activity/Service Context

Activity와 Service는 보인 그자체가 Context이다. Activity와 Service 모두 ContextWrapper를 상속 받는다. Activity Context인 경우 자신의 뷰 컴포넌트를 관리하기 위해 Application Context가 아닌, 자신의 Activity Context에 접근해야 한다. "this" 키워드를 이용해서 가능하다.

8. AndroidManifest.xml

   AndroidManifest.xml은 안드로이드 어플리케이션에 대한 각종 정보를 기술한 어플리케이션 명세서 라고 할 수 있다. AndroidManifest.xml에 기술되는 내용은 다음과 같다.

   안드로이드 어플리케이션을 위한 자바 패키지명 정의 이 패키지 명은 전체 시스템 상으로 유일 해야한다.

   안드로이드 어플리케이션을 구성하는 컴포넌트들 (Activity, Service, Broadcast Receiver, Content Provider)을 기술 해야 한다.

   <activity>, <service>, <receiver>,<provider>

   어플리케이션을 구성하는 컴포넌트들에 대한 해당 클래스명을 정의하고, 그 컴포넌트가 처리할 수 있는 기능이 무엇인지 intent-filler을 통해 정의 한다.

   <intent-filter>

   안드로이드 어플리케이션이 안드로이드 플랫폼의 제한된 API에 접근하거나 다른 어플리케이션의 제한된 컴포넌트를 사용하기 위해서 필요한 권한을 설정한다.

   <uses-permission>

   안드로이드 어플리케이션은 자신의 Component를 쉽게 사용할 수 없도록 권한을 설정할 수 있다.

   <permission>

   안드로이드 어플리케이션을 구동하기 위한 최소한의 sdk버전을 정의

   <uses-library>

   매니페스트 파일은 앱의 이름, 버전, 구성요소, 권한등 앱의 실행에서 꼭 필요한 정보가 저장되어 있는 파일입니다.
   xml파일로 프로젝트의 최상위에 존재합니다.

   태그 구성으로 가장 위는 manifest태그가 존재하고 패키지명, 버전 등이 기제됩니다.

   application태그에는 앱 아이콘, 앱 이름등의 정보가 저장됩니다.

   activity태그에는 액티비티 클래스명과 액티비티 이름을 정의합니다.
   activity하위에는 intent-filter태그를 이용하여 엑티비티에 대한 인텐트 작업시 필요한 action과 category를 정의합니다.

   service,receiver,provider 태그에는 서비스,리시버,프로바이더에 대한 내용이 정의되어 있습니다.

   permission태그에는 앱에서 필요한 권한을 정의합니다.

   그밖에 sdk버전을 지칭하는 uses-sdk와 다른 패키지를 등록할 수 있는 uses-library등이 존재합니다.

   안드로이드 매니페스트는 앱의 이름, 버전, 구성요소, 권한 등 앱의 실행에 있어서 필요한 각종 정보가 저장되어있는 파일입니다. 반드시 존재해야하는 xml 형식의 파일로 안드로이드 프로젝트의 최상위에 위치하고 있습니다.

   가장 최상위는 manifest 태그가 위치하고 있습니다. manifest 태그에는 패키지명, 앱 버전 코드, 앱 버전 이름을 정의합니다.

   application 태그에는 앱 아이콘, 앱 이름을 정의합니다.

   activity 태그에는 액티비티의 클래스명과 액티비티 이름을 정의합니다. 하위에는 intent-filter 태그를 이용하여 액티비티에 대한 인텐트 작업시 필요한 action과 category를 정의합니다.

   service, receiver, provider 태그에는 각각 서비스, 리시버, 프로바이더에 대한 내용을 정의합니다.

   permission 태그에는 앱에서 필요한 권한에 내용을 정의합니다.

9. Application 클래스란?

안드로이드에서 Application Class란 어플리케이션 컴포넌트들 사이에서 공동으로 멤버들을 사용할 수 있게 해주는 편리한 공유 클래스이다. 어플리케이션 사이의 컴포넌트들이 공동으로 사용할 수 있기 때문에 공통되게 사용하는 내용을 작성해주면 어디서든 context를 이용한 접근이 가능하다.

   Application class를 상속받는다.

   AndroidManifest.xml에 Applicatgion Class Name을 추가한다.

   어플리케이션 내의 컴포넌트들 사이에서 context를 이용한 접근이 가능하다. (데이터 공유)

10. FCM의 구동 원리? (Firebase Cloud Messaging의 약자)

본연의 서버의 기능을 수행하면서 또 하나의 복잡한 알림 기능까지 포함한다면 서버의 속도는 처리량이 많아 느려질 것이다. 따라서 이러한 해결책으로 알림의 기능은 다른 서버가 제공을 해주고 본 서버는 알림기능을 제공하는 서버에 알림이 있는지 요청을 해서 정보를 가져오는 구조이다.
FCM의 동작을 위해서 HTTP나 XMPP로 FCM과 통신하는 서버와 클라이언트 앱이 필요합니다.

동작 순서

  디바이스에 앱이 설치된후 최초 실행되면서 고유 식별자인 디바이스 토큰이 발급된다. 이 토큰을 앱 서버에 등록한다.

  앱 서버에서 FCM 연결 서버로 푸시 알림을 요청한다. 이때 준비물은 디바이스 토큰과 API 서버 키이다.

  FCM 연결 서버는 토큰을 대상으로 알림 메시지를 푸시한다.

11. Looper란 무엇인지 설명해보세요.

Looper는 스레드간의 신호이므로 handler에 보낸다고 해서 곧바로 처리되는 것이 아닙니다. 동시다발적으로 메세지가 발생할 수 있기 때문에 메세지 큐(Message ueue)에 쌓았다가 처리합니다. 큐(ueue)에 들어있는 내용을 하나하나 꺼내 처리하는 놈이 바로 루퍼입니다. 메인 쓰레드가 looper를 가지고 있으며 무한 루프를 돌며 큐의 내용을 처리합니다.

12. 안드로이드의 메모리 구조

안드로이드의 메모리구조를 보면 램, 내장메모리, 외장메모리로 구분됩니다.

렘 : 프로그램이 실행될때 상주되는 공간입니다. 평상시에 하드에 저장되어있다가 런타임시에 차지되는 공간을 말합니다.

내장메모리 : 간단하게 하드디스크라고 생각해도 됩니다.

외장메모리 : 메모리가 더 필요할때 추가 할 수 있는 메모리입니다.

### 안드로이드 HTTP 라이브러리의 역사

2007년 => 안드로이드 발표 , HttpClient, 아파치의 DefaultHttpClient등이 사용
(HttpClient의 여러 버그들 문제가 있음)

2011년 => Goolge의 Developer 블로그에서 HttpUrlConnetction 사용 권장

이후... => Volley나 Suare의 Okhttp가 등장하여 쉽게 Http 통신을 사용할 수 있게 됨.

2014년 => 롤리팝 이후 HttpClient 가 Deprecated되며 이를 베이스로 하는 Volley
도 Deprecated됨

이후.... => Okhttp와 그 래퍼인 Retrofit이 인기를 가짐.
Retrofit은 클라이언트 부분과 콜백 형식등을 플러그로 변경할수 있다는점에서 인기를 가짐.

1.  디스플레이(display), 윈도우(window), 서피스(surface), 뷰(view), 뷰 그룹(view group), 뷰 컨테이너(view container), 레이아웃(layout)에 대해서 설명하시오.
    디스플레이 : 안드로이드 단말기가 가지고 있는 하드웨어 화면을 의미합니다.

윈도우 : 안드로이드에서 실행되는 앱이 그림(뷰)을 그릴 수 있는 영역을 의미합니다. 사용자로부터 입력(터치, 키) 이벤트를 받아 앱에 전달합니다.

서피스 : 윈도우에 그림(뷰)을 그릴 때 그림이 저장되는 메모리 버퍼를 의미합니다.

뷰 : 사용자 인터페이스를 구성하는 최상위 클래스를 말합니다. 윈도우의 서피스를 이용하여 화면에 어떤 모양으로 그림을 그릴지와 발생하는 이벤트를 어떻게 처리할 것인지에 대한 기능을 구현하고 있습니다. 뷰 중에서 일반적인 제어 역할을 하고 있는 것들을 위젯이라고 합니다.

뷰 그룹 : 여러개의 뷰를 포함하고 있는 뷰를 의미합니다.

뷰 컨테이너 : 다른 뷰를 포함할 수 있는 뷰를 의미합니다. 대표적으로 리스트 뷰(list view), 스크롤 뷰(scroll view), 그리드 뷰(grid view) 등이 있습니다.

레이아웃 : 뷰 그룹 중에서 내부에 뷰를 포함하고 있으면서 해당 뷰를 어떻게 윈도우에 배치할지 정의하는 관리자 역할을 하는 클래스 말합니다.

30. 인플레이션(inflation)이란 무엇인가?
    xml 레이아웃 파일로 정의한 정보를 런타임에 setContentView 메소드가 호출됨에 따라 메모리 상에 객체로 만들어주는 과정을 말합니다. 이 과정에서 xml 레이아웃 파일에서 뷰에 id를 설정하고 해당 id가 R.java 파일에 주소 값으로 환원되며 findViewById 메소드와 id를 이용하여 코드 상으로 뷰 객체를 가져와 제어할 수 있습니다.

31. 안드로이드의 크기를 표현하는 다양한 표현방법에 대해서 설명하시오.

픽셀(px) : 화면의 픽셀을 의미합니다.

밀도 독립적 픽셀(dp, dip) : 160dpi(160인치에 들어가있는 픽셀 수) 화면을 기준으로 한 픽셀을 의미합니다.

축척 독립적 픽셀(sp, sip) : 가변 글꼴을 기준으로 한 픽셀을 의미합니다. 글꼴의 설정에 따라 차이가 있습니다.

텍스트 크기(em) : 글꼴과 상관없이 동일한 텍스트 크기를 표시하기 위한 단위입니다.

그 외 인치(in), 밀리미터(mm)가 있습니다.

1.  안드로이드의 테스크란?

Task는 어플리케이션에서 실행되는 Activity를 관리하는 스택입니다. 선입 후출의 형태로 나중에 적제된 액티비티가 가장 먼저 사용됩니다. 최초적재된 엑티비티는 Root Activity라고 하고 마지막에 적재된 Activity는 Top Activity라고 합니다.

Flag를 이용하여 엑티비티의 흐름을 제어 할 수 있습니다.

16. Realm이란? (SLite와의 비교) [렐름]

slite,realm은 안드로이드 단말에서 사용하는 관계형 데이터베이스입니다.

SQlite는 오픈소스 데이터베이스로 OS와 상호작용하기위해 SQLiteOpenHelper인터페이스를 이용합니다. SQLite는 C언어로 되어있고 경량데이터베이스이며 하나의 디스크 파일에 모든 데이터를 저장 할 수 있습니다.

Realm은 크로스 플랫폼 기반의 모바일 데이터베이스입니다. IOS와 Android에서 모두 사용이 가능하며 성능 및 효율성이 우수합니다. 크로스 플랫폼이기 때문에 협업에서 유용합니다.

특징으로는 zero-copy모델을 사용하기 때문에 데이터 객체 자체에서 그대로 작업이 가능합니다.
크로스 플랫폼이기 때문에 특정 OS를 가리지 않고 동기화 될 수 있습니다. ACID를 준수합니다.

Realm은 데이터베이스 컨테이너의 인스턴스입니다.
SLite 기반의 ORM 프레임워크 입니다.

## 액티비티

1. Activity간 데이터 전달에서 객체를 전달하지 못하는 이유와 해결방법 인텐트를 전달할때는 IPC를 이용한다. 그러나 프로세스간 통신시에는 메모리참조가 안된다. 그래서 파일에 쓰는 방식을 이용하는데 이 때 직렬화, 역직렬화를 통해 파일을 참조한다

2. 액티비티 백 스택 설명
3. 액티비티(activity)가 무엇인지와 액티비티 생명주기에 대해서 설명하시오.
   안도르이드에서 화면을 관리하며 사용자가 발생시키는 다양한 이벤트를 처리하는 컴포넌트입니다.

부모 액티비티에서 새로운 자식 액티비티를 실행하고자 한다면 먼저 매니페스트 파일에 해당 자식 액티비티를 추가 해줘야합니다. 다음으로 부모 액티비티에서 startActivity 메소드에 인텐트를 파라미터로 넘겨 실행하거나 startActivities 메소드를 이용하여 여러개의 액티비티를 한꺼번에 실행할 수 있습니다.

액티비티의 실행과정은 첫 번째로 부모 액티비티에서 자식 액티비티를 생성 및 호출합니다. 두 번째로 액티비티 매니저 서비스가 해당 앱 프로세스에서 인텐트를 복사해온 후 매니페스트 파일에서 해당 인텐트에 명시되어있는 액티비티를 찾고 어떻게 실행시켜야할지 결정합니다. 세 번째로 찾아낸 액티비티를 실행하고 다시 해당 앱 프로세스에 인텐트를 복사하여 넘겨줍니다. 그 외 자식 액티비티 내의 onCreate 메소드에서 setContentView 메소드에 레이아웃의 아이디를 파라미터로 넘겨 해당 액티비티의 화면을 구성하게됩니다.

액티비티는 크게 3가지 상태가 존재합니다. 먼저 실행(running) 상태는 액티비티 스택의 최상위에 있으며 포커스를 가지고 있어 사용자에게 보이는 상태입니다. 다음으로 일시 중지(paused) 상태는 사용자에게 보이기는 하지만 다른 액티비티가 위에 있어 포커스를 받지 못하는 상태를 말합니다. 예를들어 대화상자가 위에 있어 일부가 가려져 있는 경우를 말합니다. 마지막으로 중지 (stopped) 상태는 다른 액티비티에 의해 완전히 가려져 보이지 않는 상태를 말합니다.

액티비티가 처음 만들어지면 onCreate 메소드가 호출되어 레이아웃을 구성합니다. 이후 onStart 메소드가 화면에 보이기 직전에 호출됩니다. 다음으로 onResume 메소드가 사용자 상호작용(화면이 포커스를 얻었을 때)하기 바로 전에 호출됩니다. 이 3가지 메소드가 호출되어 액티비티는 실행 상태를 갖게됩니다. 이후 포커스를 잃었을 때 onPause 메소드가 호출되고 일시 중지 상태가 됩니다. 일시 중지 상태에서 다시 포커스를 획득하면 onResume 메소드가 호출되거나 다른 액티비티에 의해서 완전히 화면이 가려졌는지 여부를 확인하여 가려져 보이지 않는 경우 onStop 메소드가 호출되어 중지 상태가됩니다. 정지 상태에서 다시 화면이 보이기 직전에 onRestart 메소드가 호출되고 onStart 메소드가 차례로 호출됩니다. 그 외 finish 메소드가 실행되어 해당 액티비티가 종료되기 직전에 onDestroy 메소드가 실행됩니다.

가끔은 일시 중지나 중지 상태에서 시스템이 메모리가 부족하다고 판단될 경우 onCreate 메소드부터 다시 해당 액티비티를 구동합니다. 이 경우 onStop, onResume 메소드 호출이 생략됩니다. 따라서 onSaveInstanceState, onRestoreInstanceState 메소드를 이용하여 액티비티가 갑자기 죽을 것을 대비해서 상태를 저장하고 복원하기 위한 작업을 정의해줄 수 있습니다.

36. 액티비티간 데이터 전달에서 임의의 클래스 객체를 바로 전달하지 못하는 이유는 무엇이고 전달하기 위해서는 어떤 처리가 필요한가?
    액티비티간 전달할 수 있는 데이터의 type은 보통 기본형으로 정해져있습니다. 그 이유는 인텐트를 이용하여 액티비티의 데이터를 전달하는 과정에서 현재 실행중인 앱 프로세스가 시스템 프로세스로 실행중인 액티비티 매니저 서비스 프로세스에게 인텐트를 전달합니다. 이 경우 프로세스간 통신이기 때문에 인텐트에 있는 값들을 복사하여 넘기는 방식으로 처리되기 때문에 객체 주소를 바로 넘기지 못하는 문제가 발생합니다. 따라서 이 문제를 해결하기 위해 자신이 임의로 만든 클래스 객체를 전달하기 위해서는 Serilizable이나 Parcelable 인터페이스를 상속받아 객체를 직렬화하여 넘기는 방식을 사용해야합니다.

37. 부모 액티비티에서 자식 액티비티의 결과 값을 받아오기 위해 어떻게 해야하는가?
    먼저 부모 액티비티에서 startActivityForResult 메소드를 이용하여 인텐트와 리퀘스트 코드를 파라미터로 넘깁니다. 이후 자식 액티비티에서 setResult 메소드에 결과 코드와 데이터를 파라미터로 넘깁니다. 다시 부모 액티비티에서 onActivityResult 메소드를 오버라이딩하여 자식 액티비티에서 보낸 결과 코드와 데이터를 받아 처리하는 코드를 작성할 수 있습니다. 이후 실행과정에서 자식 액티비티의 finish 메소드가 호출되면 부모 액티비티가 다시 화면에 나타나면서 onResume 메소드가 실행됩니다. 이때 onActivityResult 메소드가 작동하게 됩니다.

38. 액티비티 런치모드

    - standard (FLAG_ACTIVITY_STANDARD)

    activity를 여러번 생성할 수 있다. 또한 activity의 instance는 어떤 task이던지 존재 할 수 있다.

    - singleTop(FALG_ACTIVITY_SINGLE_TOP)

    target task에 동일한 activity가 top에 위치해 있을 때만 instance를 새로 생성하지 않고, top에 있던 instance의 onNewIntent()를 대신 호출해 준다.

    - singleTask(FALG_ACTIVITY_SINGLE_TASK)

    시스템이 새 태스크 루트에 액티비티를 생성하고, 인텐트를 해당 액티비티로 라우팅 한다. 그러나 액티비티 인스턴스가 이미 존재하는 경우, 시스템은 새 인스턴스를 생성하는 대신 onNewIntent() 메서드를 호출하여 인텐트를 기존의 인스턴스로 라우팅한다.

    - singleInstance(FLAG_ACTIVITY_SINGLE_INSTANCE)

    시스템이 태스크내에 인스턴스를 보유하고 있는 상황에서 새 액티비티 인스턴스를 만들지 않는 점이 singTask와 비슷하나, 액티비티는 항상 해당 태스크의 단일 멤버이다.

39. Activity?

    액티비티는 일종의 어플리케이션 구성요소 로서, 사용자와 상호작용 할 수 있는 화면을 제공한다. 액티비티 마다 layout.xml 파일을 구현 함으로써 사용자에게 인터페이스를 제공 해 줄 수 있다.

    액티비티를 사용하기 위해서는 아래와 같은 내용들을 알아야 한다.

    setContentView()를 이용하여 액티비티의 View를 Draw

    AndroidManifest 파일에 Activity를 등록

    라이프 사이클 콜백 처리

    onCreate, onStart, onResume, onPause, onDestroy

    액티비티 시작시에 정보를 전달하거나 액티비티가 종료될 때 결과를 리턴할 수 있다.

    액티비티의 3가지 상태?

    활성화 (Active) 또는 실행 중 (Running) 상태

    Activity가 전면에 나와서 실행되고 있을 때

    현재 Task에 대한 Activity Stack의 최상위에 존재하고 있을 때

    이 상태의 Activity는 사용자와 상호작용 할 수 있다.

    멈춤(pauese) 상태

    사용자의 포커스를 가지고 있지 않지만 여전히 화면지 보여지고 있을 때

    다른 액티비티가 위에 위치 하지만 그 액티비티가 투명상태 혹은 전체화면을 채우지 못해 아직은 이전 액티비티가 보이는 상태 이 때 이전 액티비티의 상태는 멈춤 상태이다.

    극도로 메모리가 부족한 상태에서는 시스템에 의해 강제로 종료될 수 있다.

    정지(Stopped) 상태

    다른 Activity에 의해서 완전히 가려져, 더 이상 사용자에게 보여지지 않을 때

40. 액티비티 생명 주기

    onCreate()

    액티비티가 최초 생성될 때 한번만 호출

    액티비티의 대부분 초기설정을 이곳에서 수행

    액티비티가 재성생되는 경우 이전상태값을 저장한 번들 객체가 전달

    Bundle savedInstanceState
    onStart()

    액티비티가 사용자에게 보이기 직전 호출

    onResume()

    액티비티가 사용자와 상호작용을 하기 직전 호출

    onPause

    다른 액티비티의 호출로 해당 액티비티가 백그라운드로 진입할때 호출

    CPU를 소모하는 작업들을 중단 시킬 때 이곳에서 수행하면 적절

    이 메소드가 리턴 되기전까지는 다음 액티비티의 실행이 이루어지지 않음 > 되도록 빨리 끝내야함

    onStop

    액티비티가 더 이상 화면에 나오지 않음

    onDestroy

    액티비티가 소멸되기 전에 호출

    개발자가 finish()메소드를 호출 했을 때 혹은 시스템이 메모리를 확보하기 위해 액티비티를 일시적으로 종료 할 때 호출.

    위의 두가지 시나리오는 isFinishing()메소드를 통해 구분가능

    onRestart

    액티비티가 중단 되었다가 다시

    시작되기 직전에 호출

    이 뒤에는 항상 onStart()가 호출

    액티비티 재시작 경우

    onPause() 상태까지 호출 뒤 재시작 된 경우

    onPause() > onResume()

    onStop() 상태까지 호출 뒤 재시작 된 경우

    onStop() > onRestart() > onStart() > onResume()

41. 만약 앱을 사용하는 도중에 카카오톡 메시지가 온다면 사용하던 앱의 TopActivity의 생명주기는 어떤 상태가 되나요?

    - onPause 상태가 됩니다.

42. onRestart는 언제 호출이 되나요?

    - Activity가 중지 상태에서 다시 화면에 표시되기 직전에 호출됩니다. onRestart->onStart->onResume-> ActivityRunning..

43. 안드로이드의 액티비티와 액티비티의 수명주기에 대해서 설명해보세요.

안도르이드에서 화면을 관리하며 사용자가 발생시키는 다양한 이벤트를 처리하는 컴포넌트입니다
부모 액티비티에서 새로운 자식 액티비티를 실행하고자 한다면 먼저 매니페스트 파일에 해당 자식 액티비티를 추가 해줘야합니다. 다음으로 부모 액티비티에서 startActivity 메소드에 인텐트를 파라미터로 넘겨 실행하거나 startActivities 메소드를 이용하여 여러개의 액티비티를 한꺼번에 실행할 수 있습니다.
액티비티의 실행과정은 첫 번째로 부모 액티비티에서 자식 액티비티를 생성 및 호출합니다. 두 번째로 액티비티 매니저 서비스가 해당 앱 프로세스에서 인텐트를 복사해온 후 매니페스트 파일에서 해당 인텐트에 명시되어있는 액티비티를 찾고 어떻게 실행시켜야할지 결정합니다. 세 번째로 찾아낸 액티비티를 실행하고 다시 해당 앱 프로세스에 인텐트를 복사하여 넘겨줍니다. 그 외 자식 액티비티 내의 onCreate 메소드에서 setContentView 메소드에 레이아웃의 아이디를 파라미터로 넘겨 해당 액티비티의 화면을 구성하게됩니다.
액티비티는 크게 3가지 상태가 존재합니다. 먼저 실행(running) 상태는 액티비티 스택의 최상위에 있으며 포커스를 가지고 있어 사용자에게 보이는 상태입니다. 다음으로 일시 중지(paused) 상태는 사용자에게 보이기는 하지만 다른 액티비티가 위에 있어 포커스를 받지 못하는 상태를 말합니다. 예를들어 대화상자가 위에 있어 일부가 가려져 있는 경우를 말합니다. 마지막으로 중지 (stopped) 상태는 다른 액티비티에 의해 완전히 가려져 보이지 않는 상태를 말합니다.
액티비티가 처음 만들어지면 onCreate 메소드가 호출되어 레이아웃을 구성합니다. 이후 onStart 메소드가 화면에 보이기 직전에 호출됩니다. 다음으로 onResume 메소드가 사용자 상호작용(화면이 포커스를 얻었을 때)하기 바로 전에 호출됩니다. 이 3가지 메소드가 호출되어 액티비티는 실행 상태를 갖게됩니다. 이후 포커스를 잃었을 때 onPause 메소드가 호출되고 일시 중지 상태가 됩니다. 일시 중지 상태에서 다시 포커스를 획득하면 onResume 메소드가 호출되거나 다른 액티비티에 의해서 완전히 화면이 가려졌는지 여부를 확인하여 가려져 보이지 않는 경우 onStop 메소드가 호출되어 중지 상태가됩니다. 정지 상태에서 다시 화면이 보이기 직전에 onRestart 메소드가 호출되고 onStart 메소드가 차례로 호출됩니다. 그 외 finish 메소드가 실행되어 해당 액티비티가 종료되기 직전에 onDestroy 메소드가 실행됩니다.
가끔은 일시 중지나 중지 상태에서 시스템이 메모리가 부족하다고 판단될 경우 onCreate 메소드부터 다시 해당 액티비티를 구동합니다. 이 경우 onStop, onResume 메소드 호출이 생략됩니다. 따라서 onSaveInstanceState, onRestoreInstanceState 메소드를 이용하여 액티비티가 갑자기 죽을 것을 대비해서 상태를 저장하고 복원하기 위한 작업을 정의해줄 수 있습니다.

49. 태스크(task)란 무엇인가?
    예를들어 어떤 앱에서 앨범 앱을 실행하는 기능이 있다면 이 앱은 두개의 앱을 실행하는 형태가 되지만 사용자 입장에서는 하나의 앱에서 화면이 전환된다고 판단합니다. 이와 같은 사용자 입장에서 논리적인 화면 구성의 단위를 태스크라고 말합니다.

### 프레그먼트

14. 프레그먼트

    액티비티 내에 배치되어 어플리케이션 사용자 인터페이스를 구성하는 안드로이드 구성요소이다.

    액티비티를 분할하여 화면의 한부분을 정의한다.

    액티비티와 같이 레이아웃, 동작 처리, 생명주기를 가지는 독립적인 모듈이다.

    다른 액티비티에서도 사용 할 수 있어 재사용성이 뛰어나다.

    액티비티 내에서 실행 중에 추가, 제거가 가능하다.

15. Fragment를 생성 할 때 default 생성자만 사용하길 추천하는 이유?

프로그먼트를 만들 때는 생성자를 오버로딩 하지 않고 생성 시 파라미터를 Bundle에 담아 setArgument() 함수를 호출하는 방식을 사용하는 것이 일반적이다. 왜냐하면 안드로이드에 의해서 프래그먼트가 복원될 때는 프래그먼트의 기본 생성자를 호출하기 때문에 오버로딩된 생성자의 호출이 보장되지 않는다.

16. 프래그먼트사이의 커뮤니케이션은 어떤 방식으로 하는가?

서로 다른 fragment들 끼리는 직접적으로 정보를 주고 받을 수 없다. Fragment끼리의 통신은 반드시 host activity(프래그먼트들이 바인딩되어 있는 activity)를 거쳐서 이루어져야 한다. 프래그먼트에 콜백함수를 정의하고 액티비티에 해당 콜백함수를 구현 함으로써 프래그먼트 사이 통신이 가능하다.

17. 프래그먼트 생명주기

onAttach함수가 OnCreate이전에 호출됩니다. 그 이후 OnCreate함수가 호출되고 OncreateView에서 LayoutInflater로 UI관련 잡업을 할 수 있습니다. 그리고 화면이 포커스를 잃었을때는 onPause OnStop onDestroyView가 호출되고
종료시에 onDestory onDetach()가 호출됩니다.

1. 프레그먼트(fragment)가 와 프레그먼트 생명주기에 설명하시오.
   프레그먼트는 액티비티의 일부분에만 배치되는 화면 및 동작을 조작하기 위한 객체입니다. 안드로이드 3.0(허니콤)에서 화면이 비교적 큰 태블릿의 등장으로 작은 단위의 화면의 생명주기 관리할 필요가 있어 추가되었습니다. 프레그먼트 매니저를 통해서 여러개의 프레그먼트를 조작할 수 있습니다. 레이아웃 xml 파일에서 다른 뷰들과 함께 배치될 수 있습니다.

   액티비티가 생성되면 프레그먼트 매니저는 초기화(initializing) 상태가 됩니다. 프레그먼트가 매니저에 의해 추가되면 onAttach, onAttachFragment, onCreate 메소드가 차례로 실행됩니다. 다음으로 액티비티의 onCreate 메소드 호출 이후 매니저는 생성(created) 상태로 변경됩니다. 이때 onCreateView, onViewCreated, onActivityCreated 메소드가 차례로 호출됩니다. 다음으로 액티비티의 onStart 메소드가 호출되면 매니저는 시작(started) 상태로 onStart 메소드를 호출합니다. 이후 액티비티의 onResume 메소드가 호출되면 매니저 역시 재시작(resume) 상태로 변하며 onResume 메소드를 호출합니다. 그 외 액티비티가 화면에서 보이지 않을경우 호출되는 onStop 메소드 호출 이후 매니저는 중지(stop) 상태가 되며 액티비티의 onDestroy 메소드 호출 이후 매니저는 onDestroyView 메소드를 호출합니다.

## 서비스

1. 백그라운드에서 UI 업데이트 하는 방법
2. startService와 bindService의 차이

3. 서비스(service)가 무엇인지와 서비스 생명주기에 대해서 설명하시오.
   서비스는 백그라운드에서 실행되는 구성 요소입니다. 서비스는 사용자에게 보이는 화면이 존재하지 않으며, 정해지지 않은 시간 동안 운영됩니다. 각각의 서비스는 매니페스트 파일에 서비스 태그를 이용하여 선언해야합니다. 서비스는 Service 클래스를 상속받아 onStartCommand 또는 onBind 메소드를 재정의하여 구현할 수 있습니다.

   서비스는 다른 구성 요소들처럼 메인 쓰레드에서 동작합니다. 따라서 CPU를 많이 사용하거나 대기 상태를 필요로 하는 경우 새로운 쓰레드를 이용하여 생성해야합니다. 또한 서비스의 객체는 단말에서 오직 1개만 생성되어 관리합니다.

   먼저 서비스가 startService 메소드로 실행되는 경우 서비스가 생성될 때 onCreate 메소드가 실행됩니다. 이후 서비스가 실행을 시작할 때 onStartCommand 메소드가 호출되며 서비스의 상태가 실행중으로 변경됩니다. 이후 stopService 메소드가 실행되면 서비스가 종료되며 onDestroy 메소드를 호출하며 서비스의 상태가 종료로 변경됩니다.

   다음으로 서비스가 bindService 메소드로 실행되는 경우 서비스가 생성될 때 onBind 메소드가 호출됩니다. 다음으로 unbindService 메소드가 호출되어 바인딩이 해제되면 onUnbind 메소드가 호출됩니다. 이후 완전히 종료될 때 onDestroy 메소드가 호출됩니다.

## 브로드캐스트 리시버

안드로이드 4대 컴포넌트 중 하나로 시스템이나 앱 등에서 이벤트 발생시 사용자에게 방송을 해주는 개념이다. 이렇게 방송된 이벤트는 각 앱에서 필요한 방송 이벤트를 받아들이고 이벤트에 대한 처리를 리시버를 통해 할 수 있게 해준다.

Local Broadcast와 LocalBroadcastManager?

Global Broadcast

일반적으로 이야기하는 BroadCast. 프로세스 경계를 무시하고 안드로이드 시스템 상 등록된 모든 Receiver 들에게 전달되는 Broadcast이다.

Local Broadcast

현재 프로레스 안에서만 유효한 Broadcast이다. GlobalBroadcast에 비해 훨씬 시스템 부하가 적다. 액티비티 내부의 객체간에 상호 의존성을 낮추어 깔끔한 프로그램 구조를 만들 수 있다. Local Broadcast를 등록하는 방법은 LocalBroadcastManager의 객체를 getInstance()를 통해 얻어와 해당 매니져에 등록해야 한다.

LocalBroadcastManager.getInstance( getContext() ).registerReceiver( myReceiver, myFilter );
Broadcast를 보내는 방법도 LocalBroadcastManager를 이용한다.

LocalBroadcastManager.getInstance( getContext() ).sendBroadcast( new Intent( myAction ));

## 콘텐트 프로바이더

## 뷰, 커스텀 뷰

1. 안드로이드에서 View란 무엇인가?

   View는 액티비티에서 화면을 구성하는 최소 단위로 화면에 보이는 모든것은 View이다. 또 다른말로 위젯이라고도 하며 대표적으로 ImageView, TextView, EditText, Button 등이 View를 상속 받아 만든 클래스이다.

2. View.GONE과 View.INVISIBLE의 차이

- GONE

  보이지도 않고 영역도 차지하지 않는다. (아예 사라짐)

- INVISIBLE

  보이지는 않지만 영역은 차지하고 있다.

3. View와 ViewGroup의 차이점?

ViewGroup은 n개의 View를 담을 수 있는 컨테이너로 ViewGroup 또한 View를 상속받아 만든 클래스 입니다. 또 다른 말로 레이아웃이라고도 하며 대표적으로 LinearLayout, RelativeLayout, FrameLayout, ConstraintLayout 등이 있다.

그래서 ViewGroup안에 View 뿐만아니라 ViewGroup을 담을 수 있다.

21. SurfaceView란?

SurfaceView는 View를 상속받는 클래스이다. 일반 View는 onDraw메소드를 시스템에서 자동으로 호출해줌으로써 화면을 그린다. SurfaceView는 그리기를 시스템에 맡기는 것이 아니라 스레드를 이용해 강제로 화면에 그림으로써 원하는 시점에 바로 화면에 그릴 수 있다. 애니메이션이나 동영상과 같이 연산처리가 많이 필요한 뷰를 위해 사용된다.

SurfaceView에는 다음 장 화면을 미리 그려두고, 그리기가 끝나면 바로 전환하는 더블버퍼링이라는 기능이 있어 처리 속도를 빠르게 할 수 있다.

22. RelativeLayout과 LinearLayout, Constraint Layout

LinearLayout

뷰가 가로 또는 세로로 순차적으로 나열되는 레이아웃이다.

android:orientation속성으로 Horizontal 또는 Vertical 설정 가능하다.

기본값은 Horizontal이다.

RelativeLayout

따로 위치를 지정하지 않으면 뷰가 0,0위치에 계속 쌓이는 레이아웃이다.

최상위 부모 레이아웃 상대위치 또는 다른 view의 id 를 참조해 특정 뷰에 대해 상대적인 위치를 지정할 수 있다.

Constraint Layout

복잡한 레이아웃을 단순한 계층구조를 이용하여 표현할 수 있는 ViewGroup

형제 View들과의 관계를 정의해서 레이아웃을 구성하여, RelativeLayout과 비슷하지만 더 유연하고 강력한 기능들을 제공한다.

RelativeLayout에서 불가능했던 자식 뷰간의 상호관계 정의가능

LinearLayout을 써야만 했던 뷰 비율 조정도 간단하게 가능

뷰 계층을 간단하게 구성하여 유지보수, 성능 향상

1. 리스트뷰에서 사용되는 뷰홀더(ViewHolder Pattern) 패턴에 대해서 아시는 만큼 설명해주세요.

   - 리스트뷰에서 리스트의 개수가 많은 상황에서 findViewById를 통한 XML 리소스 접근이 빈번할 경우 성능저하가 발생하기 때문에 View 객체를 ViewHolder에 홀드시켜 성능을 개선하기 위한 패턴입니다.

2. 커스텀뷰를 만들어 봤는지 설명해주세요.

## 기타

1. 코틀린의 장점에 대해 설명하시오

기존의 자바 코드의 보일러 플레이트 구문을 최소화 시킬 수 있습니다.

기존의 자바에서도 람다표현식을 이용하여 코드의 간소화를 위해 노력했습니다.
java8에서는 Retrolambda라이브러리를 사용하지 않고 람다표현식이 가능합니다.
그렇지만 안드로이드 스튜디오 2.4버전 이상부터 JDK 1.8로 빌드가 가능하고 minsdk도 24부터이기때문에
실질적으로 사용하지 못합니다. 즉 JDK 1.6기반의 API와 문법적으로 조금 추가된 형태로 빌드 할 수 있다고 봅니다.

안드로이드의 대표적인 보일러 플레이트 구문은 레이아웃에 정의한 뷰 레퍼런스를 가지고 오는 부분이나 SLite트랜젝션을 처리하는 부분 등이 있습니다.

또 자바 8의 스트림 API를 사용할 수도 없습니다.

스트림에 대한 대비로는 streamsupport, Lightweight-Strem-API가 있습니다.

RxJAVA또한 자바 8 스트림의 훌륭한 대안이고 안드로이드 커뮤니티에서 많이 쓰이고 있습니다.

하지만 위의 라이브러리들의 의존성문제와 기존 라이브러리에 대한 학습등이 부담으로 다가온다는 사실이 있습니다.

코틀린의 좋은점으로는 NullPointerException다루기, 보일러 플레이트 개선하기, Collections에 filter,map,foreach같은 고차함수를 적용할 수 있고, 변경가능한 컬렉션과 불가능한 컬렉션을 엄격히 구분합니다. 서버에서 수신받은 데이터를 컬렉션으로 다룰 일이 많기때문에 코드를 보다 간결하고, 안전하게 만드는 데 도움이 됩니다. 또 확장함수(이미 존재하는 클래스에 새로운 함수를 추가)라는 강력한 기능도 있습니다.

또 자바와 호완성이 무척 좋고 기존의 라이브러리를 제약없이 사용 할 수 있습니다.

하지만 새로운 언어를 배워야 한다는 점에대한 부담감과 기술적 이슈가 발생했을때 대응기간이 상대적으로 길어 질 수 있다는 단점도 분명 존재합니다.

1. 어플리케이션(application)과 컨텍스트(context)에 대해서 설명하시오.
   어플리케이션 앱 프로세스가 실행되면 가장 먼저 생성되는 객체로 하나의 어플리케이션 객체는 하나의 앱 프로세스와 대응됩니다. 앱이 백그라운드로 내려가도 앱 프로세스는 계속 살아있기 때문에 어플리케이션 객체도 살아있다고 할 수 있습니다.

   컨텍스트는 안드로이드의 컴포넌트들이 동작하기 위해 필요한 정보를 담고 있는 객체를 말합니다. 각각의 컴포넌트들(액티비티, 서비스, 브로드캐스트 리시버 등)은 자신만의 컨텍스트를 가지고 있습니다. 컨텍스트 내에는 어플리케이션의 정보(패키지명 등), 컨텍스트가 실행되는데 필요한 정보(테마 등)를 얻거나 시스템 서비스(윈도우 매니저, 레이아웃 인플레이터 등)를 구동하는데 사용됩니다.

2. 안드로이드에서 로그(log)를 출력하는 방법과 종류를 설명하시오.
3. 스타일(style), 테마(theme)에 대해서 설명하시오.
4. 나인패치(9patch)란 무엇인가?
5. 안드로이드의 메모리 관리 방식에 대해서 설명하시오.
   안드로이드는 액티비티, 서비스, 리시버, 프로바이더를 실행하기 위해 앱이 실행되는 과정에서 프로세스를 생성합니다. 실행중인 모든 앱은 컴포넌트가 모두 종료되어도 다음에 이 앱을 다시 실행할 가능성이 높기 때문에 프로세스를 바로 제거하지 않습니다. 바로 종료하지 않는 이유는 앱을 실행하기 위해 프로세스를 생성하는 과정에서 딜레이가 발생하는데 이 딜레이를 줄이기 위함입니다. 따라서 사용자에 의해 다시 앱이 실행되면 남아있던 프로세스가 존재하는 경우 바로 실행됩니다. 이 과정에서 쌓여있던 많은 프로세스로 인해 메모리가 부족해지는 경우 프로세스의 우선순위(사용빈도)에 따라 프로세스를 종료하여 메모리를 확보합니다.
6. ANR, LMK, OOM
7. Asynctask, coroutine, retrofit
8. Data binding, View binding
9. AIDL
10. 데이터 저장 방식 file, db, shared preference property, network
11. startService, BindService
12. 콘텐트 프로바이더와 콘텐트 리조버 차이
13. xml, view가 그려지는 과정 (커스텀 뷰를 만드는 과정)
14. Room과 SharedPreferences 비교
15. 리스트뷰와 리사이클러뷰 비교
16. 리사이클러뷰의 어댑터가 무엇인가? 무슨 역할을 하나?
17. DI 란?