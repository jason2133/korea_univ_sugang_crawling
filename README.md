# 고려대학교 개설예정과목 크롤링
- [고려대학교 수강신청 시스템](https://sugang.korea.ac.kr/)

### 반영 학기
|Num|학기|
|:------:|:------:|
|1|2022년 1학기|
|2|2022년 여름학기|
|3|2022년 2학기|

### 타 학과 개설예정과목 크롤링 시
- 전공과목영문코드 입력변수인 your_major에서 각 학과 코드만 바꿔서 입력하면 됨. (ex. 통계학과 : STAT)

### 학년도, 학기를 변경하고 싶은 경우
~~~
url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2022&term=1R&grad_cd=0136&col_cd=9999&dept_cd=4653&cour_cd=" + your_major + str(number)
~~~
- 위 링크에서 **year=** 을 수정하면 학년도 변경.
- 위 링크에서 **term=** 을 수정하면 학기 변경. (1학기 : 1R, 2학기 : 2R, 여름 계절학기 : 1S, 겨울 계절학기 : 2W)

<!---
# 2022년 제20대 대한민국 대통령 선거 기념
- [president_20.py](https://github.com/jason2133/korea_univ_sugang_crawling/blob/master/president_20.py)
- 2022년 3월 9일 (수)
- 더불어민주당 이재명 vs 국민의힘 윤석열의 개표율 및 각 후보 득표율, 그리고 차이값을 1분 단위로 크롤링하는 코드를 추가해놓았습니다. 
--->
