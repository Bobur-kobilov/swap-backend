# Swap Tool - backend

### Getting Started
Swap tool은 기존의 hdac 코인을 새로운 atolo 코인으로 swap하는 데 사용됩니다.

### Prerequisites
    * Python 3.8.5
    * Django 2.1.5
    * pip 20.2.2
    * Docker version 19.03.12
    * Docker-compose version 1.26.0

### Native host로 설치 및 실행 
### 설치 (Redis)
```bash
  $ ./start_redis.sh
```
### 실행(Worker)
```bash
  $ ./start_worker.sh
```

### 실행(REST Server)
```bash
  $ ./start_dev.sh
```
### Docker Container로 설치 및 실행 
```bash
  $ ./1.build_container.sh
  $ ./2.run_container.sh
```


### Architecture
![Architecture](https://ap-swap.s3.ap-northeast-2.amazonaws.com/images/swap_backend.png)
### TODO-LIST
  * <del>TX bypass API 작업
  * <del> Swap frontend랑 연동 작업
  * <del>TX buffer worker 작업
  * <del>email 전송 작업
    * 이미 swap된 이메일 전송
    * KYC 정상 등록 이메일 전송
    * KYC 오류 이메일 전송
    * Swap Success 이메일 전송
    * 주소 오류 이메일 전송
  * <del>KYC API 작업(Argos 공유 필요)
  * <del>KYC 정보로 TX 생성 및 DB 저장
  * <del> Redis container script 작업
  * Refactoring (진행중)
  * 테스트(진행중)
    * Unit testing
    * E2E testing