<<<<<<< HEAD
## 2019 07 02 I Learned
1. Linux start (Window ubuntu)
  - ls, ls =al, ls -l
  - touch
  - lec 2
  
## 2019 07 03 I Learned
2. Linux directory
  - cd ~~
  - cd ..
  - rm --> 삭제
  - rm -r 디렉토리 삭제

3. 명령어 사용하는 법
  - 모든 명령어 마다 --help
  - man --> manual ex> man mkdir
  - usage 명령어
  - ls -> 현재 파일 상태 확인을 하는 명령어

## 2019 07 04 I Learned 
4. 필요한 명령을 검색으로 찾는 방법(Linux)
 
## 2019 07 09 I Learned
5. wget 
  - wget url -> 다운로드 가능
  
6. Package manager
  - 앱 스토어 비슷한 역할
  - apt, yum 
  - apt 최신 상태 확인
  - update 는 목록을 update 하는 것
  - upgrade 는 프로그램을 업그레이드를 하는 것
  
## 2019 07 10 I Learned
1. Shell vs kernel
  - hardware > kernel > shell > application
  - kernel --> 하드웨어를 제어하는 운영체제에서 중심이 되는 것
  - shell --> user 들이 리눅스와 같이
  - shell --> kernel이 알아들을 수 있도록 변형을 해주는 것
  - 커널과 쉘을 분리를 하는 이유
    - 여러가지 쉘이 생길 수 가 있다. 
    - 선호하는 쉘을 사용하여 커널을 제어를 할 수 가 있다. 
    
2. echo
  - 문자를 화면에 띄우는 것
  - zsh
  - bash vs zsh --> 그냥 쉘적인 성능이 다른 것이다. 
  - zsh 편의성이 높은 기능이 있다.
  - 각각의 사용자들이 자신에게 맞는 쉘을 사용을 하는 것

3. shell script
  - 명령의 순서를 적어두고 재사용을 하는 것
  - 자동화 관련된 것 --> 코드가 복잡한데 심각한 문제를 복잡한 명령들을 적어두는 것
  - 자동화된 작업을 처리하는 것

## 2019 07 11 I Learned
1. sudo (super user do)
  - unix --> 다중 사용자 시스템 (multiple user system)
  - 권한 --> permission
  - 사용자들마다 정함 // 시스템상에서 관리를 하는 suer 가 필요
  - super user, root user
  
## 2019 07 12 I Learned
> internet, network, and server

  - 통신사는 ip를 준다.
  - 배당 받은 서버 소프트웨어를 깔고 ip를 깔면 접속을 할 수 있다. 

> 만약 여러 대일 경우

  - 장비 마다 별도의 연결을 통신사마다 ip를 해당하는 것이 기초적인 것
  - 문제는 비용 상승함
  - 중간의 공유기와 같은 장치를 설치 "Router"
  - Router 에서 장치들에게 전달
  - 덕분에 사용료를 절감
  - 문제는 ip는 router 장치에 ip가 되는 것이다. --> 각각의 컴퓨터는 통신을 위해 ip가 있으면
  - 여기서 나오는 컨셉은 사설 ip / 전화 내선 번호와 같은 형식이라고 생각을 하면 됨
  - 각각의 장비마다 ip를 배정을 함
  - public address / private address

> curl/ ip addr

  - curl --> public ip를 볼 수 가 있다, --> router에서 주소를 알려줌
  - ip addr --> 컴퓨터에 실질적인 ip를 확인을 하는 것을  --> private ip
  - curl == ip addr 직접적으로 네트워크에 연결
    - 그대로 컴퓨터를 서버로 사용
  - else
    - 추가적인 작업을 진행을 해야 한다.
    - 라우터 안의 묶여 있는 컴퓨터 안에서는 통신이 가능
  - 같은 라우터 같은 공유기 안에서는 서버적인 것을 확인을 할 수 있다.
  - 라우터를 쓰는 컴퓨터라도 라우터 기능을 활용을 하여 특정 사용자가 public ip를 접속을 할 수 있게 함
  
> web server  
  
  - 클라이언트와 서버는 request, respose 관계
  - client
  - brouwser --> request
  - other  
  - server
  - web server
  - 항상 turn on
  - storage 에서 파일을 읽어서 respose
  - apache, ngnix, IIS
  - address
    - domain
    - ip
    
> apache2
  - start, stop, restart
  - 분산 처리를 하기위해 여러개의 프로세스를 자동으로 생성
  - 직접적인 접근을 하는 많은 문제를 갖고 있다. 
  - 간단한 방법은 shell 에서 다이렉트로 접속
  
## 2019 07 13
> web server 
  
  - apache2 
  - elinks --> server computer에 web server
  - request, respose
  - 자신의 webserver 주소를 알기 위해서는 
    - ip addr
    - localhost
  - server - client
    - 두개가 서로 상호작용을 함
    - 한 컴퓨터의 server - client
    - 스스로 request, respose
    - 127.0.0.1
    - web browser -> web server (HDD, SDD)
      - 127.0.0.1/index.html/ request
      - 특정 디렉토리에서 index.html read
      - index.html respose
      - html 해석
     
=======
# practice_kotlin
>>>>>>> practice_kotlin/master
