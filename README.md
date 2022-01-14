# 고려대학교 개설예정과목 크롤링
- 2022년 1학기 반영
- [고려대학교 수강신청 시스템](https://sugang.korea.ac.kr/)

### 타 학과 개설예정과목 크롤링 시
- 전공과목영문코드 입력변수인 your_major에서 각 학과 코드만 바꿔서 입력하면 됨. (ex. 통계학과 - STAT)

### 학년도, 학기를 변경하고 싶은 경우
- url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2022&term=1R&grad_cd=0136&col_cd=9999&dept_cd=4653&cour_cd=" + your_major + str(number)
- 위 링크에서 **year=** 을 수정하면 학년도 변경
- 위 링크에서 **term=** 을 수정하면 학기 변경. (1학기 : 1R, 2학기 : 2R)
