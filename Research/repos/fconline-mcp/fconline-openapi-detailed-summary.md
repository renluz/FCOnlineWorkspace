# FC Online OpenAPI 상세 정리

수집일: 2026-03-06

문서 출처:
- https://openapi.nexon.com/ko/game/fconline/?id=2
- https://openapi.nexon.com/ko/game/fconline/?id=3
- https://openapi.nexon.com/ko/game/fconline/?id=4
- https://openapi.nexon.com/ko/game/fconline/?id=5
- https://openapi.nexon.com/ko/game/fconline/?id=6

실제 YAML 명세:
- `id=2`: `https://openapi.nexon.com/static/api/fconline/2_script00000000000000.yaml`
- `id=3`: `https://openapi.nexon.com/static/api/fconline/3_ko_script20250318015633.yaml`
- `id=4`: `https://openapi.nexon.com/static/api/fconline/4_script00000000000000.yaml`
- `id=5`: `https://openapi.nexon.com/static/api/fconline/5_script00000000000000.yaml`
- `id=6`: `https://openapi.nexon.com/static/api/fconline/6_script00000000000000.yaml`

## 공통 규칙

- 계정/매치/랭커/메타데이터 API 서버: `https://open.api.nexon.com`
- 이미지 API 서버: `https://fco.dn.nexoncdn.co.kr`
- 인증 헤더: `x-nxopen-api-key` (모든 JSON API에서 필수)
- 공통 에러 응답:
  - `400 Bad Request`
  - `403 Forbidden`
  - `429 Too Many Requests`
  - `500 Internal Server Error`
- 공통 에러 스키마 `ErrorMessage`
  - `error`: object
  - `error.name`: string, 에러 명, example `"string"`
  - `error.message`: string, 에러 설명, example `"stirng"`
- 데이터 갱신 주기:
  - 매시 정각 기준, 두 시간 전의 게임 데이터가 업데이트됨
  - 예시로 오후 3시 5분 조회 시 당일 오후 1시까지의 데이터 조회 가능
- 페이지 공지:
  - API를 통해 데이터를 크롤링했다면 30일 이내 갱신 의무가 있음

## 개발 관점 핵심 흐름

문서 기반 추론:

- 닉네임 기반 조회 흐름
  - `GET /fconline/v1/id` 로 `nickname -> ouid`
  - 이후 `ouid` 로 `user/basic`, `user/maxdivision`, `user/match` 호출
- 매치 상세 조회 흐름
  - `GET /fconline/v1/user/match` 또는 `GET /fconline/v1/match` 로 `matchId` 목록 확보
  - `GET /fconline/v1/match-detail` 로 상세 조회
- 메타데이터 연계 흐름
  - `matchType` -> `matchtype.json`
  - `spid` -> `spid.json`
  - `seasonId` -> `seasonid.json`
  - `spPosition` -> `spposition.json`
  - `division` -> `division.json`
  - 볼타 등급 -> `division-volta.json`
- 이미지 연계 흐름
  - `spid` 또는 `pid` 로 PNG 이미지 직접 조회
  - `pid` 기반 경로는 선행 `0` 제거 필요

## 문서상 주의점

- `matchtype` 파라미터 타입이 엔드포인트마다 일관되지 않음
  - `/fconline/v1/user/match` 에서는 `integer`
  - `/fconline/v1/match` 에서는 `string`
- 메타데이터 응답 예시에서 정수 필드 example 이 문자열로 적힌 항목이 있음
  - 예: `matchtype`, `id`, `seasonId`, `divisionId`
- `/fconline/v1/user/trade` 는 `ouid` 파라미터가 없고 설명상 "본인 거래 기록만 조회 가능" 이라고 되어 있음
  - 즉, API 키 소유자 본인 거래 이력에 종속될 가능성이 높음
- 이미지 API는 Open API 서버가 아니라 CDN 서버를 사용함
- `id=3` 명세 파일명만 타임스탬프가 포함된 별도 YAML 이름을 사용함

## 계정 정보 조회 (id=2)

서버: `https://open.api.nexon.com`

### GET `/fconline/v1/id`

- 요약: 계정 식별자(ouid) 조회
- 설명: 계정 식별자(ouid)를 조회합니다.
- operationId: `fconline_get_user_by_nickname`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `nickname`: query, required, `string`, 닉네임
- `200 SUCCESS` 응답: `User`
  - `ouid`: `string`, 계정 식별자

### GET `/fconline/v1/user/basic`

- 요약: 기본 정보 조회
- 설명: 기본 정보를 조회합니다.
- operationId: `fconline_get_user_by_id`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `ouid`: query, required, `string`, 유저 고유 식별자
- `200 SUCCESS` 응답: `UserBasic`
  - `ouid`: `string`, 계정 식별자
  - `nickname`: `string`, 유저 닉네임, example `"닉네임"`
  - `level`: `integer`, 유저 레벨, example `1`

### GET `/fconline/v1/user/maxdivision`

- 요약: 역대 최고 등급 조회
- 설명: 유저별 역대 최고 등급과 달성일자를 조회합니다.
- operationId: `fconline_get_maxdivision_by_id`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `ouid`: query, required, `string`, 계정 식별자
- `200 SUCCESS` 응답: `MaxDivision`
  - `matchType`: `integer`, 매치 종류, `/metadata/matchtype` 참고, example `50`
  - `division`: `integer`, 등급 식별자, 공식경기는 `/metadata/division`, 볼타는 `/metadata/division-volta` 참고, example `1100`
  - `achievementDate`: `string`, 최고 등급 달성 일자 (UTC0), example `"2023-12-14T22:23:00"`

### GET `/fconline/v1/user/match`

- 요약: 유저의 매치 기록 조회
- 설명:
  - 유저의 매치 종류별 기록을 조회합니다.
  - 유저가 플레이한 매치의 매치 고유 식별자 목록이 반환됩니다.
  - 반환 순서는 가장 최근 플레이한 매치부터 내림차순입니다.
  - `offset`, `limit` 으로 pagination 가능합니다.
- operationId: `fconline_get_match_by_id (중복되지 않아야 합니다.)`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `ouid`: query, required, `string`, 계정 식별자
  - `matchtype`: query, required, `integer`, 매치 종류, `/metadata/matchtype` 참고
  - `offset`: query, optional, `integer`, 리스트에서 가져올 시작 위치
  - `limit`: query, optional, `integer`, 리스트에서 가져올 개수, 최대 100
- `200 SUCCESS` 응답: `MatchIdList`
  - `[].matchId`: `string`, 매치 고유 식별자

### GET `/fconline/v1/user/trade`

- 요약: 유저의 거래 기록 조회
- 설명:
  - 거래 종류 `tradetype` 으로 유저의 이적시장 거래 종류별 기록을 조회합니다.
  - 본인 거래 기록만 조회 가능하다고 명시되어 있습니다.
  - 유저가 거래한 선수의 아이디, 등급, 가치가 반환됩니다.
  - 반환 순서는 가장 최근 거래 이력부터 내림차순입니다.
  - `offset`, `limit` 으로 pagination 가능합니다.
- operationId: `fconline_get_market_by_tradetype`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `tradetype`: query, required, `string`, 거래 종류, `buy` 또는 `sell`
  - `offset`: query, optional, `integer`, 리스트에서 가져올 시작 위치
  - `limit`: query, optional, `integer`, 리스트에서 가져올 개수, 최대 100
- `200 SUCCESS` 응답: `TradeList`
  - `[].tradeDate`: `string`, 거래 일자 (UTC0), 구매는 구매 등록 시점, 판매는 판매 완료 시점, example `"2023-12-14T09:55:45"`
  - `[].saleSn`: `string`, 거래 고유 식별자, example `"5dfecf50eff20f2468e00000"`
  - `[].spid`: `integer`, 선수 고유 식별자, `/metadata/spid` 참고, example `298199236`
  - `[].grade`: `integer`, 거래 선수 강화 등급, example `1`
  - `[].value`: `integer`, 거래 선수 가치(BP), example `10000`

## 매치 정보 조회 (id=3)

서버: `https://open.api.nexon.com`

### GET `/fconline/v1/match`

- 요약: 모든 매치 기록 조회
- 설명:
  - 모든 매치의 종류별 기록을 조회합니다.
  - 모든 매치의 매치 고유 식별자 목록이 반환됩니다.
  - 반환 순서는 가장 최근 플레이한 매치부터 내림차순입니다.
  - `offset`, `limit` 으로 pagination 가능합니다.
- operationId: `fconline_get_matches_by_matchtype`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `matchtype`: query, required, `string`, 매치 종류, `/metadata/matchtype` 참고
  - `offset`: query, optional, `integer`, 리스트에서 가져올 시작 위치
  - `limit`: query, optional, `integer`, 리스트에서 가져올 개수, 최대 100
  - `orderby`: query, optional, `string`, 정렬 순서, 설명상 `desc` 는 가장 최근 매치부터
- `200 SUCCESS` 응답: `MatchIdList`
  - `[].matchId`: `string`, 매치 고유 식별자

### GET `/fconline/v1/match-detail`

- 요약: 매치 상세 기록 조회
- 설명:
  - 매치 고유 식별자 `matchid` 로 매치 상세 정보를 조회합니다.
  - 매치 시점, 매치 종류, 참여 유저별 상세 통계가 반환됩니다.
  - 매치 통계 생성 전에 상대방이 종료하면 상대방 매치 정보가 누락될 수 있다고 명시되어 있습니다.
- operationId: `fconline_get_match_by_matchid`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `matchid`: query, required, `string`, 매치 고유 식별자
- `200 SUCCESS` 응답: `MatchDetail`

최상위 필드:
- `matchId`: `string`, 매치 고유 식별자, example `"64f0000c00007210005f0000"`
- `matchDate`: `string`, 매치 일자 (UTC0), example `"2023-10-29T12:22:48"`
- `matchType`: `integer`, 매치 종류, `/metadata/matchtype` 참고, example `52`
- `matchInfo`: `array<object>`, 매치 참여 플레이어별 매치 상세

`matchInfo[]` 기본 정보:
- `matchInfo[].ouid`: `string`, 계정 식별자
- `matchInfo[].nickname`: `string`, 유저 닉네임, example `"닉네임"`

`matchInfo[].matchDetail`:
- `seasonId`: `integer`, 시즌 ID, example `202311`
- `matchResult`: `string`, 매치 결과, `"승"`, `"무"`, `"패"`, example `"승"`
- `matchEndType`: `integer`, 매치 종료 타입, `0 정상종료`, `1 몰수승`, `2 몰수패`, example `0`
- `systemPause`: `integer`, 게임 일시정지 수, example `0`
- `foul`: `integer`, 파울 수, example `0`
- `injury`: `integer`, 부상 수, example `1`
- `redCards`: `integer`, 받은 레드카드 수, example `0`
- `yellowCards`: `integer`, 받은 옐로카드 수, example `0`
- `dribble`: `integer`, 드리블 거리(야드), example `78`
- `cornerKick`: `integer`, 코너킥 수, example `0`
- `possession`: `integer`, 점유율, example `46`
- `OffsideCount`: `integer`, 오프사이드 수, example `1`
- `averageRating`: `number`, 경기 평점, example `1.18889`
- `controller`: `string`, 사용 컨트롤러 타입, `keyboard`, `pad`, `etc` 중 하나, example `"keyboard"`

`matchInfo[].shoot`:
- `shootTotal`: `integer`, 총 슛 수, example `3`
- `effectiveShootTotal`: `integer`, 총 유효슛 수, example `3`
- `shootOutScore`: `integer`, 승부차기 슛 수, example `0`
- `goalTotal`: `integer`, 총 골 수, 실제 골 수, `goalInPenalty + goalOutPenalty + goalPenaltyKick`, example `2`
- `goalTotalDisplay`: `integer`, 게임 종료 후 유저에게 노출되는 골 수, example `2`
- `ownGoal`: `integer`, 자책골 수, example `0`
- `shootHeading`: `integer`, 헤딩 슛 수, example `2`
- `goalHeading`: `integer`, 헤딩 골 수, example `1`
- `shootFreekick`: `integer`, 프리킥 슛 수, example `0`
- `goalFreekick`: `integer`, 프리킥 골 수, example `0`
- `shootInPenalty`: `integer`, 인패널티 슛 수, example `3`
- `goalInPenalty`: `integer`, 인패널티 골 수, example `2`
- `shootOutPenalty`: `integer`, 아웃패널티 슛 수, example `0`
- `goalOutPenalty`: `integer`, 아웃패널티 골 수, example `0`
- `shootPenaltyKick`: `integer`, 패널티킥 슛 수, example `0`
- `goalPenaltyKick`: `integer`, 패널티킥 골 수, example `0`

`matchInfo[].shootDetail[]`:
- `goalTime`: `integer`, 슛 시간, example `786`
  - `2^24*0 ~ 2^24*1 - 1`: 전반전, 그대로 사용
  - `2^24*1 ~ 2^24*2 - 1`: 후반전, `2^24*1` 차감 후 `45*60` 초 더함
  - `2^24*2 ~ 2^24*3 - 1`: 연장 전반, `2^24*2` 차감 후 `90*60` 초 더함
  - `2^24*3 ~ 2^24*4 - 1`: 연장 후반, `2^24*3` 차감 후 `105*60` 초 더함
  - `2^24*4 ~ 2^24*5 - 1`: 승부차기, `2^24*4` 차감 후 `120*60` 초 더함
- `x`: `number`, 슛 x좌표, 전체 경기장 기준, example `0.9499898435243544`
- `y`: `number`, 슛 y좌표, 전체 경기장 기준, example `0.4995435465846854`
- `type`: `integer`, 슛 종류, example `2`
  - `1 normal`
  - `2 finesse`
  - `3 header`
  - `4 lob`
  - `5 flare`
  - `6 low`
  - `7 volley`
  - `8 free-kick`
  - `9 penalty`
  - `10 KNUCKLE`
  - `11 BICYCLE`
  - `12 super`
- `result`: `integer`, 슛 결과, `1 ontarget`, `2 offtarget`, `3 goal`, example `1`
- `spId`: `integer`, 슈팅 선수 고유 식별자, `/metadata/spid` 참고, example `272167135`
- `spGrade`: `integer`, 슈팅 선수 강화 등급, example `5`
- `spLevel`: `integer`, 슈팅 선수 레벨, example `5`
- `spIdType`: `boolean`, 슈팅 선수 임대 여부, 임대면 `true`, example `true`
- `assist`: `boolean`, 어시스트 받은 골 여부, example `false`
- `assistSpI`: `integer`, 어시스트 선수 고유 식별자, `/metadata/spid` 참고, example `-1`
- `assistX`: `number`, 어시스트 x좌표, example `0.5`
- `assistY`: `number`, 어시스트 y좌표, example `0.5`
- `hitPost`: `boolean`, 골포스트 맞춤 여부, example `false`
- `inPenalty`: `boolean`, 페널티박스 안에서 넣은 슛 여부, example `true`

`matchInfo[].pass`:
- `passTry`: `integer`, 패스 시도 수, example `92`
- `passSuccess`: `integer`, 패스 성공 수, example `83`
- `shortPassTry`: `integer`, 숏 패스 시도 수, example `55`
- `shortPassSuccess`: `integer`, 숏 패스 성공 수, example `55`
- `longPassTry`: `integer`, 롱 패스 시도 수, example `3`
- `longPassSuccess`: `integer`, 롱 패스 성공 수, example `3`
- `bouncingLobPassTry`: `integer`, 바운싱 롭 패스 시도 수, example `1`
- `bouncingLobPassSuccess`: `integer`, 바운싱 롭 패스 성공 수, example `0`
- `drivenGroundPassTry`: `integer`, 드리븐 땅볼 패스 시도 수, example `10`
- `drivenGroundPassSuccess`: `integer`, 드리븐 땅볼 패스 성공 수, example `10`
- `throughPassTry`: `integer`, 스루 패스 시도 수, example `19`
- `throughPassSuccess`: `integer`, 스루 패스 성공 수, example `14`
- `lobbedThroughPassTry`: `integer`, 로빙 스루 패스 시도 수, example `4`
- `lobbedThroughPassSuccess`: `integer`, 로빙 스루 패스 성공 수, example `1`

`matchInfo[].defence`:
- `blockTry`: `integer`, 블락 시도 수, example `3`
- `blockSuccess`: `integer`, 블락 성공 수, example `0`
- `tackleTry`: `integer`, 태클 시도 수, example `11`
- `tackleSuccess`: `integer`, 태클 성공 수, example `9`

`matchInfo[].player[]`:
- `spId`: `integer`, 선수 고유 식별자, `/metadata/spid` 참고, example `277205401`
- `spPosition`: `integer`, 선수 포지션, `/metadata/spposition` 참고, example `28`
- `spGrade`: `integer`, 선수 강화 등급, example `3`

`matchInfo[].player[].status`:
- `shoot`: `integer`, 슛 수, example `0`
- `effectiveShoot`: `integer`, 유효 슛 수, example `0`
- `assist`: `integer`, 어시스트 수, example `0`
- `goal`: `integer`, 득점 수, example `0`
- `dribble`: `integer`, 드리블 거리(야드), example `256`
- `intercept`: `integer`, 인터셉트 수, example `1`
- `defending`: `integer`, 디펜딩 수, example `0`
- `passTry`: `integer`, 패스 시도 수, example `12`
- `passSuccess`: `integer`, 패스 성공 수, example `11`
- `dribbleTry`: `integer`, 드리블 시도 수, example `12`
- `dribbleSuccess`: `integer`, 드리블 성공 수, example `11`
- `ballPossesionTry`: `integer`, 볼 소유 시도 수, example `4`
- `ballPossesionSuc`: `integer`, 볼 소유 성공 수, example `2`
- `aerialTry`: `integer`, 공중볼 경합 시도 수, example `3`
- `aerialSuccess`: `integer`, 공중볼 경합 성공 수, example `0`
- `blockTry`: `integer`, 블락 시도 수, example `0`
- `block`: `integer`, 블락 성공 수, example `0`
- `tackleTry`: `integer`, 태클 시도 수, example `1`
- `tackle`: `integer`, 태클 성공 수, example `1`
- `yellowCards`: `integer`, 옐로카드 수, example `0`
- `redCards`: `integer`, 레드카드 수, example `0`
- `spRating`: `number`, 선수 평점, example `6.4`

## 랭커 정보 조회 (id=4)

서버: `https://open.api.nexon.com`

### GET `/fconline/v1/ranker-stats`

- 요약: TOP 10,000 랭커 유저가 사용한 선수의 20경기
- 설명:
  - TOP 10,000 랭커 유저가 사용한 선수의 20경기 평균 스탯을 조회합니다.
  - 선수의 고유 식별자와 포지션 목록으로 랭커 유저 평균 스탯을 조회할 수 있습니다.
  - 선수 목록을 너무 많이 넣으면 `413 Request Entity Too Large` 가 날 수 있으며, 문서 예시는 1회 50명 정도를 권장합니다.
- operationId: `fconline_get_ranker_stat`
- 파라미터
  - `x-nxopen-api-key`: header, required, `string`, API KEY
  - `matchtype`: query, required, `integer`, 매치 종류, `/metadata/matchtype` 참고
  - `players`: query, required, `string`, 조회 선수 목록, URL 인코딩한 JSON Array
    - 각 요소는 `id`, `po` 필드를 가져야 함
    - `id`: 선수 고유 식별자 `spid`
    - `po`: 선수 포지션 `spposition`
    - 문서 예시 원본: `[{"id":100167680,"po":18}]`
    - 문서 예시 인코딩: `%5B%7B%22id%22%3A100167680%2C%22po%22%3A18%7D%5D`
- `200 SUCCESS` 응답: `RankerStats`
  - `[].spId`: `integer`, 선수 고유 식별자, `/metadata/spid` 참고, example `100167680`
  - `[].spPosition`: `integer`, 선수 포지션, `/metadata/spposition` 참고, example `18`
  - `[].status`: `object`, 선수 경기 스탯
  - `[].status.shoot`: `number`, 평균 슛 수, example `0`
  - `[].status.effectiveShoot`: `number`, 평균 유효 슛 수, example `0`
  - `[].status.assist`: `number`, 평균 어시스트 수, example `0`
  - `[].status.goal`: `number`, 평균 득점 수, example `0`
  - `[].status.dribble`: `number`, 평균 드리블 거리(야드), example `165`
  - `[].status.dribbleTry`: `number`, 평균 드리블 시도 수, example `9`
  - `[].status.dribbleSuccess`: `number`, 평균 드리블 성공 수, example `9`
  - `[].status.passTry`: `number`, 평균 패스 시도 수, example `14`
  - `[].status.passSuccess`: `number`, 평균 패스 성공 수, example `11`
  - `[].status.block`: `number`, 평균 블락 성공 수, example `0`
  - `[].status.tackle`: `number`, 평균 태클 성공 수, example `0`
  - `[].status.matchCount`: `integer`, 해당 포지션으로 경기 참여한 횟수, example `1`
  - `[].createDate`: `string`, 집계 시간 (UTC0), example `"2023-12-14T01:12:34"`

## 메타데이터 정보 조회 (id=5)

서버: `https://open.api.nexon.com`

### GET `/static/fconline/meta/matchtype.json`

- 요약: 매치 종류 메타데이터 조회
- 설명: `matchtype` 메타데이터를 조회합니다.
- operationId: `fconline_get_matchtype`
- 파라미터: 없음
- `200 SUCCESS` 응답: `MatchTypeMeta`
  - `[].matchtype`: `integer`, 매치 종류, example `"30"`
  - `[].desc`: `string`, 매치 종류명, example `"리그 친선"`

### GET `/static/fconline/meta/spid.json`

- 요약: 선수 고유 식별자 메타데이터 조회
- 설명:
  - Path 정보만 제공한다고 적혀 있습니다.
  - 선수 고유 식별자 `spid` 는 시즌 아이디 `seasonid` 3자리 + 선수 아이디 `pid` 6자리로 구성됩니다.
  - 시즌 아이디는 `/static/fconline/meta/seasonid.json` 으로 조회합니다.
- operationId: `fconline_get_spid`
- 파라미터: 없음
- `200 SUCCESS` 응답: `SpidMeta`
  - `[].id`: `integer`, 선수 고유 식별자 `spid`, example `"100000051"`
  - `[].name`: `string`, 선수명, example `"앨런 시어러"`

### GET `/static/fconline/meta/seasonid.json`

- 요약: 시즌 아이디 메타데이터 조회
- 설명: 시즌 아이디는 선수가 속한 클래스를 나타냅니다.
- operationId: `fconline_get_seasonid`
- 파라미터: 없음
- `200 SUCCESS` 응답: `SeasonIdMeta`
  - `[].seasonId`: `integer`, 시즌 아이디, example `"100"`
  - `[].className`: `string`, 선수가 속한 클래스, example `"ICONTM (ICON The Moment)"`
  - `[].seasonImg`: `string`, 이미지 경로, example `"https://ssl.nexon.com/s2/game/fc/online/obt/externalAssets/season/icontm.png"`

### GET `/static/fconline/meta/spposition.json`

- 요약: 선수 포지션 메타데이터 조회
- 설명: 선수 포지션 `spposition` 메타데이터를 조회합니다.
- operationId: `fconline_get_spposition`
- 파라미터: 없음
- `200 SUCCESS` 응답: `SppositionMeta`
  - `[].spposition`: `integer`, 선수 포지션, example `0`
  - `[].desc`: `string`, 선수 포지션명, example `"GK"`

### GET `/static/fconline/meta/division.json`

- 요약: 등급 식별자 메타데이터 조회
- 설명: 등급 식별자 `division` 메타데이터를 조회합니다.
- operationId: `fconline_get_division`
- 파라미터: 없음
- `200 SUCCESS` 응답: `DivisionMeta`
  - `[].divisionId`: `integer`, 등급 식별자, example `"800"`
  - `[].divisionName`: `string`, 등급 식별자명, example `"슈퍼챔피언스"`

### GET `/static/fconline/meta/division-volta.json`

- 요약: 볼타 공식경기 등급 식별자 메타데이터 조회
- 설명: 볼타 공식경기 등급 식별자 메타데이터를 조회합니다.
- operationId: `fconline_get_division_volta`
- 파라미터: 없음
- `200 SUCCESS` 응답: `DivisionVoltaMeta`
  - `[].divisionId`: `integer`, 볼타 경기 등급 식별자, example `1100`
  - `[].divisionName`: `string`, 볼타 경기 등급 식별자명, example `"월드 스타"`

## 이미지 정보 조회 (id=6)

서버: `https://fco.dn.nexoncdn.co.kr`

이미지 응답은 모두 `image/png` 입니다.

### GET `/live/externalAssets/common/playersAction/p{spid}.png`

- 요약: 선수 고유 식별자 `spid` 로 선수 액션샷 이미지 조회
- 설명:
  - `spid` 로 선수 액션샷을 가져옵니다.
  - 특정 선수는 이미지가 없을 수 있습니다.
- operationId: `fconline_get_action_img_by_spid`
- 파라미터
  - `spid`: path, required, `integer`, 선수 고유 식별자
- `200 SUCCESS`: `image/png`

### GET `/live/externalAssets/common/playersAction/p{pid}.png`

- 요약: 선수 식별자 `pid` 로 선수 액션샷 이미지 조회
- 설명:
  - `pid` 로 선수 액션샷을 가져옵니다.
  - 특정 선수는 이미지가 없을 수 있습니다.
  - `pid` 가 `0` 으로 시작하면 앞의 `0` 을 모두 제거해야 정상 조회됩니다.
  - 문서 예시: `"000401"` 이면 `"401"` 로 조회
- operationId: `fconline_get_action_img_by_pid`
- 파라미터
  - `pid`: path, required, `integer`, 선수 식별자
- `200 SUCCESS`: `image/png`

### GET `/live/externalAssets/common/players/p{spid}.png`

- 요약: 선수 고유 식별자 `spid` 로 선수 이미지 조회
- 설명:
  - `spid` 로 선수 이미지를 가져옵니다.
  - 특정 선수는 이미지가 없을 수 있습니다.
- operationId: `fconline_get_img_by_spid`
- 파라미터
  - `spid`: path, required, `integer`, 선수 고유 식별자, `/fconline/v1/meta/spid` 참고라고 적혀 있으나 실제 메타데이터 문서는 `/static/fconline/meta/spid.json`
- `200 SUCCESS`: `image/png`

### GET `/live/externalAssets/common/players/p{pid}.png`

- 요약: 선수 식별자 `pid` 로 선수 이미지 조회
- 설명:
  - `pid` 로 선수 이미지를 가져옵니다.
  - 특정 선수는 이미지가 없을 수 있습니다.
  - `pid` 가 `0` 으로 시작하면 앞의 `0` 을 모두 제거해야 정상 조회됩니다.
  - 문서 예시: `"000401"` 이면 `"401"` 로 조회
- operationId: `fconline_get_img_by_pid`
- 파라미터
  - `pid`: path, required, `integer`, 선수 식별자, `spid` 뒤 6자리
- `200 SUCCESS`: `image/png`
