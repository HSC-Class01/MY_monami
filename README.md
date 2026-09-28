# MY_monami — 모나미 DART 재무분석 에이전트

모나미(005360, DART corp_code 00121288)의 OpenDART 재무데이터를 수집하고
재무비율을 계산하여 GitHub Pages 대시보드에 표시하는 프로젝트입니다.

## API Key 설정

GitHub 저장소에서:

`Settings → Secrets and variables → Actions → New repository secret`

- Name: `DART_API_KEY`
- Secret: OpenDART 인증키

로 등록하세요.

로컬 실행 시에는 환경변수 `DART_API_KEY`를 사용합니다.

## 자동 업데이트

`.github/workflows/update.yml`은 매월 1일 자동 실행되며,
수동 실행도 가능합니다.

## 대상 데이터

- 2010년부터 현재까지
- 사업보고서
- 반기보고서
- 분기보고서
- 주요 재무수치
- 유동성/안정성/활동성/수익성 관련 비율

## GitHub Pages

저장소 `Settings → Pages → Source`에서 `GitHub Actions`를 선택하면
`dashboard/`가 Pages로 배포되도록 구성되어 있습니다.
