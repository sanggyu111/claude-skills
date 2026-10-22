# 데이터 형식 (doc-data JSON)

`assets/template.html`의 `<script id="doc-data" type="application/json">` 블록에 들어가는 JSON이다. 렌더링 코드는 이 형식만 읽는다.

## 최상위

```json
{
  "title": "페이지 제목 (문서 이름이나 주제, 2~6단어)",
  "subtitle": "한 문장 부제",
  "source": { "name": "원문 제목", "url": "https://... (없으면 생략)", "date": "정리한 날 YYYY-MM-DD" },
  "tldr": "문서가 답하는 질문에 대한 답, 1~2문장",
  "keypoints": ["핵심 3~5개, 각 한 줄"],
  "stats": [{ "value": "10배", "label": "무엇의 수치", "note": "조건이나 맥락" }],
  "sections": [{ "id": "영문-소문자-id", "heading": "섹션 제목", "lead": "한 문장 요약", "blocks": [] }]
}
```

- `stats`는 문서에 의미 있는 숫자가 있을 때만 쓴다. 2~4개. 없으면 키를 뺀다.
- `sections`는 3~7개. 원문 목차를 그대로 옮기지 말고, 독자가 알고 싶은 질문 단위로 묶는다.
- `id`는 영문 소문자와 `-`만 쓴다(목차 링크에 쓰임).

## 블록 공통

모든 블록은 `type`을 가진다. 선택 키:
- `title`: 블록 위 작은 제목
- `derived`: `true`면 "원문을 바탕으로 정리" 표시가 붙는다. 원문에 없던 구조(원문 문장을 흐름도나 표로 재구성한 것)에 붙인다.

## flow — 절차, 과정, 데이터 흐름, 인과

```json
{
  "type": "flow",
  "title": "무엇이 어떻게 흘러가나",
  "nodes": [{ "id": "a", "label": "짧은 이름", "kind": "input", "note": "한 줄 설명" }],
  "edges": [{ "from": "a", "to": "b", "label": "넘어가는 것" }],
  "steps": [{ "focus": ["a"], "text": "이 단계에서 눈여겨볼 점" }]
}
```

- `kind`: `input`(입력·시작), `process`(처리·행동), `store`(저장·상태), `output`(결과), `decision`(갈림길), `concept`(개념). 모양과 이름표가 달라진다.
- 노드 3~8개. `label` 14자, `note` 40자, edge `label` 10자 이내.
- 배치는 edges로 자동 계산된다(왼쪽→오른쪽, 좁은 화면에서는 위→아래). 흐름 방향대로 잇는다.
- `steps` 3~6개. 흐름을 처음부터 끝까지 따라가며, 각 `focus`에 노드 1~3개. "따라가기"를 누르면 해당 노드와 이어지는 화살표가 강조된다. 각 `text`는 "무엇이 일어나는가 + 왜 중요한가"를 1~2문장으로.
- 갈림길은 `decision` 노드에서 edge 두 개로 나누고, edge `label`에 조건을 쓴다.

## timeline — 시간 순서, 버전, 단계적 출시, 로드맵

```json
{ "type": "timeline", "items": [{ "when": "2026-03", "title": "무슨 일", "text": "설명", "status": "done" }] }
```

- `status`: `done`(지남), `now`(현재), `next`(예정). 원문에 시점이 없으면 `when`에 "지금", "이후"처럼 상대 표현을 쓴다.

## compare — 여러 대상 비교 (플랜, 옵션, 버전, 장단점)

```json
{ "type": "compare", "columns": ["기준", "A", "B"], "rows": [["항목", "✓", "✗"]], "highlight": 2 }
```

- 첫 열은 비교 기준(행 제목)이다.
- 셀 값이 `✓`, `O`, `예`, `가능`이면 초록 체크, `✗`, `X`, `아니오`, `불가`면 빨간 X로 표시된다. 나머지는 글자 그대로.
- `highlight`: 강조할 열 번호(0부터). 독자에게 가장 중요한 선택지가 있을 때만.

## stats — 섹션 안의 핵심 수치

```json
{ "type": "stats", "items": [{ "value": "5개", "label": "무엇", "note": "조건" }] }
```

- 값은 원문 표기 그대로(단위 포함).

## cards — 나란한 개념, 기능 목록, 종류

```json
{ "type": "cards", "items": [{ "tag": "분류", "title": "이름", "text": "1~2문장 설명" }] }
```

- 2~6개. 순서가 의미 있으면 cards 대신 flow나 timeline을 쓴다.

## callout — 주의, 예외, 제한, 덧붙임

```json
{ "type": "callout", "tone": "warn", "title": "주의", "text": "내용 (간단한 Markdown 가능)" }
```

- `tone`: `warn`(제한·예외·위험), `info`(참고). 원문에 없는 배경 설명을 덧붙일 때는 `info`에 `title: "덧붙임"`.

## text — 그림으로 만들 수 없는 짧은 설명

```json
{ "type": "text", "md": "3문장 이내. **굵게**, `코드`, - 목록, [링크](https://...)" }
```

- 섹션에 그림 블록이 하나도 없이 text만 있으면 안 된다.

## JSON 작성 주의

- 문자열 안의 `</`는 `<\/`로 쓴다. 그렇지 않으면 script 태그가 중간에 닫힌다.
- 다 쓰면 `python3 scripts/validate.py <html 파일>`로 검사한다.
