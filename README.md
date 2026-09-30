# MY_monami — 모나미 DART 재무분석 Agent

[![🔗 대시보드 바로가기](https://img.shields.io/badge/🔗%20대시보드%20바로가기-183B56?style=for-the-badge)](https://hsc-class01.github.io/MY_monami/)

모나미(005360, DART corp_code 00121288)의 DART 정기보고서를 수집하고 주요 재무수치와 재무비율을 계산하여 GitHub Pages 대시보드로 제공하는 자동화 프로젝트입니다.

## 핵심 기능
- 2010년부터 현재까지 사업보고서·반기보고서·분기보고서 공시목록 수집
- OpenDART 구조화 재무제표(2015년 이후) 수집
- 2010–2014년 공시 원문 ZIP 보관 및 레거시 표 추출 시도
- 연결(CFS) 기준 우선, 없으면 별도(OFS) 기준
- 성장성·수익성·현금흐름·재무안정성·활동성·자본효율 지표 계산
- Annual / Half-year / Quarterly 대시보드
- 매월 1일 GitHub Actions 자동 업데이트
- GitHub Pages 자동 배포
- 국내 Peer Firms 표를 README와 대시보드 하단에 표시

## API Key
Settings → Secrets and variables → Actions → New repository secret에 DART_API_KEY를 등록합니다. 키는 코드나 Pages에 저장하지 않습니다.

## 대시보드
https://hsc-class01.github.io/MY_monami/

GitHub Pages의 Source는 GitHub Actions로 설정합니다.

## 주요 분석 수치
총자산, 현금및현금성자산, 매출채권, 재고자산, 유형자산, 총부채, 이자부차입금, 자본총계, 매출액, 매출총이익, 판관비, 영업이익, 세전이익, 당기순이익, 지배주주순이익, EBITDA, CFO, CFI, CFF, CAPEX, FCF, 순차입금 등을 대상으로 합니다.

## 주요 비율
매출총이익률, 영업이익률, 순이익률, EBITDA 마진, ROA, ROE, ROIC(자료가 충분한 경우), 유동비율, 당좌비율, 부채비율, 자기자본비율, 차입금의존도, 이자보상배율, 순차입금/EBITDA, 총자산회전율, DSO, DIO, DPO, CCC, 매출증가율, CFO/순이익, PER, PBR, EV/EBITDA 등을 단계적으로 확장할 수 있도록 구성했습니다.

## 국내 Peer Firms
| 기업 | 비교 근거 | 상장 여부 |
|---|---|---|
| 한국쓰리엠(3M Korea) | 국내 문구·사무용품 산업의 인접 대형 사업자 | 비상장 |
| 아트박스 | 문구·팬시·생활용품 유통/소매 | 비상장 |
| 오피스디포코리아 | 사무용품·문구 유통 | 비상장 |
| 알파 | 문구·사무용품 유통 | 비상장 |
| 월드페이퍼 | 문구·사무용품 관련 동종업계 | 비상장 |

Peer는 투자등급이나 우열을 의미하지 않고 산업 비교군으로만 사용합니다.

## 데이터 주의사항
OpenDART의 fnlttSinglAcntAll은 사업연도 2015년 이후 구조화 재무제표 정보를 제공합니다. 따라서 2010–2014년은 같은 API의 구조화 재무제표로 완전히 동일하게 채울 수 없으며, 공시검색 API와 document.xml 원문을 별도 보관하고 레거시 표 추출을 시도합니다. 추출되지 않는 항목은 임의로 보정하지 않고 결측으로 남깁니다.

금융감독원 OpenDART는 정기보고서(사업·반기·분기보고서) 및 XBRL 재무정보를 제공합니다.
