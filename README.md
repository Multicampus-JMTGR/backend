## REST API - 수녕부분 

### GET /user/ALL

- 모든 사용자 정보 목록을 가져옴
- return: user[]



### POST /user/ALL

- 사용자 정보 저장
- body: {email: str(이메일-pk), interest: str(관심카테고리), name:str(사용자이름), phone_number: str(핸드폰번호)}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST



### GET /user/Detail/\<str:email> - 뭘좀 바꿔서 다시 테스트 해봐야함

- 특정 사용자 정보 가져옴, 사용자 없으면 404 return
- email : 로그인 사용자 email
- 기능 
  - 사용자 존재 여부 확인
- return: user | HTTP_404_NOT_FOUND



### PUT /user/Detail/\<str:email> - 뭘좀 바꿔서 다시 테스트 해봐야함

- 특정 사용자 정보 수정
- email : 로그인 사용자 email
- body: {email: str(이메일-pk), interest: str(관심카테고리), name:str(사용자이름), phone_number: str(핸드폰번호)}
- 기능
  - 로그인 진행과정 > 이미 우리 사이트 데이터베이스에 존재하는 회원일 경우(혹시 정보가 바꼈을 수 있으니 update해줌)
  - 로그인 성공 후 > 회원 정보 수정 클릭 시
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST





### GET /certificate/CertificatesFilter/

- 키워드에 해당하는 자격증 정보 조회
- parameter : { keyword : 검색어 }
- 기능 
  - 메인페이지 노출
  - 자격증 검색 기능 (키워드 : 카테고리명, 자격증명, 키워드 없을 시 전체 자격증 조회)
- return: certificate[] 또는 category[]+certificate[]



### GET /certificate/CertRecomByExaminee/

- 전체 자격증 중 **필기** 응시자 수 많은 순으로 8개씩 조회
- 기능
  - 메인페이지 노출
- return: certificate[]



### GET /certificate/CertRecomByExamineeSil/ - 뭘좀 바꿔서 다시 테스트 해봐야함

- 전체 자격증 중 **실기** 응시자 수 많은 순으로 8개 조회
- 기능
  - 메인페이지 노출
- return: certificate[]



### GET /certificate/CertRecomByInterest/ - 아직 테스트 중

- 회원 > 관심카테고리 > 해당 카테고리에 해당하는 자격증 중 인기자격증 8개 조회
- 기능 
  - 메인페이지 노출
- return: certificate[]



### GET /certificate/CertRecomByRandom/ - 아직 테스트 중

- 비회원 > 랜덤 카테고리 > 해당 카테고리에 해당하는 자격증 중 인기자격증 8개 조회
- 기능 
  - 메인페이지 노출
- return: certificate[]



### GET / certificate/OrderingFilter/ - 아직 테스트 중

- 시험 결과 날자가 임박한 자격증 졍렬
- 기능
  - 메인 페이지 노출
- return: certificateSchedule[]+certificate[]



## REST API - 민지 부분 

### GET /certschedule
- 자격증 스케쥴 전체 리스트 겟

### GET /certschedule/<int:pk>
- 자격증 스케쥴 pk를 이용해서 자격증 상세 정보 표시

### GET /certificate
- 자격증 전체 리스트 겟

### GET /certificate/<int:pk>
- 자격증 번호를 이용해서 자격증 상세 정보 표시

### GET /category
- 카테고리 전체 리스트 겟

### GET /certificate/<int:pk>
- 카테고리 번호를 이용해서 카테고리 상세 정보 표시

### POST /cert_like/<str:email>/<str:cert_id> (좋아요 기능 두개중 어떤게 더 적합한지 아직 테스트중)
- email을 통해 유저 정보를 호출
- cert_id에 매핑된 자격증 정보를 유저 cert_likes에 추가 (like)
- 이미 동일한 cert_id가 존재한다면 자격증을 cert_likes에서 삭제 (unlike)
- 기능
  - 마이페이지 / 자격증 리스트에서 자격증 좋아요 추가
