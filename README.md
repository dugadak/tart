※ redis 사용해야합니다
1) docker 사용시 docker run -p 6379:6379 -d redis:5 명령어 사용
2) docker X(Windows) https://github.com/tporadowski/redis/releases에서 Redis-x64-5.0.14.1.msi설치
3) docker X(MAC) brew install redis 명령어 사용

python manage.py runserver 명령어 사용
http://127.0.0.1:8000/chat/ 접속시 원하는 채팅방의 이름으로 개설 또는 접속 가능
ex) 123 입력

enter 버튼 클릭 or enter

해당 채팅방에서 소켓을 통한 실시간 채팅 가능

해당 대화내역은 채팅방의 이름별로 로컬DB(SQLite)에 저장되도록 하였습니다.

