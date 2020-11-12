## REST API - 수녕부분 

### GET api/user

- 모든 사용자 정보 목록을 가져옴
- return: user[]



### POST api/user

- 사용자 정보 저장
- body: {email: str(이메일-pk), interest: str(관심카테고리), name:str(사용자이름), phone_number: str(핸드폰번호)}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST



### GET api/user/\<str:email>

- 특정 사용자 정보 가져옴, 사용자 없으면 404 return
- email : 로그인 사용자 email
- 기능 
  - 사용자 존재 여부 확인
- return: user | HTTP_404_NOT_FOUND



### PUT api/user/\<str:email>

- 특정 사용자 정보 수정
- email : 로그인 사용자 email
- body: {email: str(이메일-pk), interest: str(관심카테고리), name:str(사용자이름), phone_number: str(핸드폰번호)}
- 기능
  - 로그인 진행과정 > 이미 우리 사이트 데이터베이스에 존재하는 회원일 경우(혹시 정보가 바꼈을 수 있으니 update해줌)
  - 로그인 성공 후 > 회원 정보 수정 클릭 시
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST





### GET api/certificate/CertificatesFilter/

- 키워드에 해당하는 자격증 정보 조회
- parameter : { keyword : 검색어 }
- 기능 
  - 메인페이지 노출
  - 자격증 검색 기능 (키워드 : 자격증명, 주최기관, 키워드 없을 시 전체 자격증 조회)
          - 특정 단어를 포함한 경우 다 나오도록 구현함
- return: certificate[]



### GET api/certificate/CertRecomByExaminee/

- 전체 자격증 중 **필기** 응시자 수 많은 순으로 8개씩 조회
- 기능
  - 메인페이지 노출
- return: certificate[]



### GET api/certificate/CertRecomByExamineeSil/

- 전체 자격증 중 **실기** 응시자 수 많은 순으로 8개 조회
- 기능
  - 메인페이지 노출
- return: certificate[]



### GET api/certificate/CertRecomByInterest/

- 회원 > 관심카테고리 > 해당 카테고리에 해당하는 자격증 중 **필기** 인기자격증 8개 조회
- 비회원 > 램덤카테고리 > 해당 카테고리에 해당하는 자격증 중 **필기** 인기자격증 8개 조회
- (여기서 회원 비회원 여부는 백엔드에서 처리했음)
- parameter : { email : 사용자이메일 } - 비회원인 경우 param에 아무것도 들어가지 
- 기능 
  - 메인페이지 노출
- return: certificate[]



### GET api/certificate/CertRecomByInterestSil/

- 회원 > 관심카테고리 > 해당 카테고리에 해당하는 자격증 중 **실기** 인기자격증 8개 조회
- 비회원 > 램덤카테고리 > 해당 카테고리에 해당하는 자격증 중 **실기** 인기자격증 8개 조회
- (여기서 회원 비회원 여부는 백엔드에서 처리했음)
- parameter : { email : 사용자이메일 } - 비회원인 경우 param에 아무것도 들어가지 
- 기능 
  - 메인페이지 노출
- return: certificate[]



### GET api/certificate/OrderingFilter/

- 시험 결과 날자가 임박한 자격증 졍렬
- 기능
  - 메인 페이지 노출
- return: certificateSchedule + certificate.name []



## REST API Category Name - 수녕
### GET api/basicCategory/
- 카테고리 이름만 조회
- 기능
  - 로그인 시 관심 분야 선택하는 곳에서 사용
- return: category[{}]



## REST API USER PART 

### GET /api/user
- 유저 기본정보만 포함한 리스트 출력 (이름, 이메일 등등..)

### GET /api/user/detail
- 유저 기본정보 + 좋아요한 카테고리 / 자격증 포함한 리스트 출력

### GET /api/user/<str:pk>
- 유저 한명의 모든 상세정보 출력
- 기본정보 + 좋아요 한 카테고리 / 자격증 + 스터디 플랜

### GET /api/studyplan
- 스터디 플랜 전체 리스트 겟

### POST /api/cert_like/<str:email>/<str:cert_id>
- email을 통해 유저 정보를 호출
- cert_id에 매핑된 자격증 정보를 유저 cert_likes에 추가 (like)
- 이미 동일한 cert_id가 존재한다면 자격증을 cert_likes에서 삭제 (unlike)
- 기능
  - 마이페이지 / 자격증 리스트에서 자격증 좋아요 추가
