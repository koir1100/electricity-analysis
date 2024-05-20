# electricity-analysis
## 전력거래소 데이터 기반 대시보드 제작

### 개요
  - 본 프로젝트는 전력 산업의 여러 측면을 종합적으로 이해하는 것을 목적으로, 전력데이터 개발 포털 시스템에서 발전통계(발전량, 전력 수급)와 판매통계(판매금액, 판매 전력량) 데이터를 수집하고 대시보드에 시각화하여 분석을 진행한 프로젝트이다.

### 설명
<img src="https://github.com/koir1100/electricity-analysis/assets/4710834/2041eb40-54d8-49f9-b959-190476b918d9" width="75%" alt="DE2차_SW아키텍처2.drawio" style="margin: 5px auto;" /></center>
<br/>
  - 상기 그림과 같이 CSV 파일을 (필요시 전처리 과정을 수행한 다음) S3로 적재한 후 데이터 웨어하우스인 Snowflake에 적재하는 ETL 과정 수행
  - 이후, 적재된 데이터 기반으로 요약 테이블을 제작하는 ELT를 수행하여, 분석에 용이한 BI 툴인 Preset에 각종 차트를 대시보드에 추가

### 사용 스택
#### Data Lake
  - AWS S3

#### Data Warehouse
  - Snowflake

#### Dashboard
  - Preset.io

#### Communication & Collaboration Tools
  - Zepeto
  - Slack
  - Notion
<br/>
  
---
  
### PART: 공통
  - sql  
    - 01_전력수급: 전력 수급 관련 쿼리문  
    - 02_발전량_04_판매금액: 발전량 및 판매금액 관련 쿼리문  
    - 03_판매전력량: 판매전력량 관련 쿼리문  
<br/>
  
---
  

### PART: 전력거래소 전력수급 데이터, 기상청 기상자료개방포털 내 기후 데이터 관련

### 디렉터리 구조 및 파일 설명
  - charts-code  
    - Apache Superset 에서 제작한 각종 차트에 대한 Export 한 파일임 (Preset에 import 하는 용도로 활용)  
  - cleansing  
    - erase_whitespace_rows.py: 각 파일 별로 처음 몇 줄은 데이터에 대한 기본 정보를 표시하는 내용임에 따라 이를 각 파일별로 제거하는 프로그램임.  
      단, 습도와 풍속은 이 과정을 수행한 이후 다음과 같은 예의 데이터로 인해 추가로 처리과정이 필요하여 추가 프로그램을 제작하였음.  
      구체적으로, 열에 대한 구분자 역할을 하는 콤마에 대해 큰따옴표로 묶어 있지 않아 이를 묶는 로직을 추가  
      습도: `7,경남, 2016-01-14,56,29,울산,진주,김해시` ⇒ `7,경남,2016-01-14,56,29,"울산,진주,김해시"`  
      풍속: `5,충남, 2021-11-26,0.9,3.5,부여,금산,세종,6.4,부여,금산` ⇒ `5,충남,2021-11-26,0.9,3.5,"부여,금산,세종",6.4,"부여,금산"`  
    - clear_whitespace_all_csv.py: 기상 데이터를 최초 수집에 활용한 로직으로, 지역(권역)별로 수집한 데이터를 하나의 데이터로 병합하고자 활용한 프로그램임.  
      첫 번째 행만 열 이름을 위한 용도로 살리고 나머지 데이터는 중복하지 않는 로직을 포함하였음.  
    - combine_all_csv.py: 기상청 기상자료개방포털에서 제공한 데이터를 최초 2012년부터 2022년 자료만 수집하였으나,  
      추후 타 데이터에도 활용할 것을 고려, 2002년부터 2011년 데이터를 추가로 수집하였음.  
      이 두 데이터(최초 수집 데이터와 추가로 수집한 데이터)를 하나의 csv 파일로 합치는 프로그램임.  
  - scraping  
    - 전력수급 데이터는 2012년 6월 1일부터 2023년 4월 30일까지 데이터가 존재함에 따라 2023년 5월 1일부터 2023년 12월 31일에 대한 데이터를 별도로 수집하는 프로그램임(각 월별로 반자동 수행).  
      [전력거래소 - 전력통계정보시스템 - 실시간 전력수급](https://epsis.kpx.or.kr/epsisnew/selectEkgeEpsMepRealChart.do?menuId=030300) 페이지를 Selenium 기반 스크래핑 작업 수행  
  - source-data  
    - 수집한 각종 데이터를 전처리한 데이터 source임(encoding: euc-kr).  
    - climate 폴더 내 전처리 과정을 제시하고자 여러 폴더를 두었음.  
      - example-data: 최초 [기상자료개방포털](https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do?pgmNo=179)에서 다운로드한 파일 예  
      - 2002-2011, 2012-2022: 1차로 erase_whitespace_rows.py 프로그램을 통한 공백 제거한 결과  
      - wind: erase_whitespace_rows.py 및 erase_whitespace_rows(wind).py 프로그램을 수행한 결과  
      - 실행 순서는 ① erase_whitespace_rows.py → ② clear_whitespace_all_csv.py → (②-1 humidity, ②-2 wind 추가 수행) → ③ combine_all_csv.py 순서로 실행하여야 함.  
    - merge_total_temperature.csv, humidity.csv, rainfall.csv, wind_speed.csv: climate 폴더 내 전처리 및 병합을 통해 실제 S3에 업로드한 기후 데이터(기온, 습도, 강수량, 풍속)  
    - power_demand_amount.csv: [공공데이터포털 - 한국전력거래소_5분단위 전력수급현황](https://www.data.go.kr/data/15099819/fileData.do) 데이터  
