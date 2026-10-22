# React 분야 파일

학습자가 React를 배울 때 SKILL.md의 규칙에 더해 따른다.

## 기준 자료 (Librarian)

공식 문서 react.dev/learn을 1순위 기준으로 삼는다. 한국어 번역은 ko.react.dev에 있다. 아래는 고를 **후보 목록**이며, 전부 보여주지 않는다.

- 리스트와 key → react.dev/learn/rendering-lists
- state 기초 → react.dev/learn/state-a-components-memory
- 배열 state 바꾸기 → react.dev/learn/updating-arrays-in-state
- 이벤트 → react.dev/learn/responding-to-events
- 객체 state 바꾸기 → react.dev/learn/updating-objects-in-state
- useEffect가 정말 필요한지 → react.dev/learn/you-might-not-need-an-effect

목록 밖 주제는 react.dev에서 페이지를 찾아 열리는 것을 확인한 뒤에만 링크를 준다.

## 학습 경로 예시 (Advisor)

- 순서: 컴포넌트·props → 리스트·key → useState·이벤트 → state 업데이트 규칙 → useEffect·데이터 가져오기
- 제외할 것: 입문 단계의 Next.js, Redux, 성능 최적화
- 마일스톤: Todo 앱 추가·삭제·완료 기능
- JavaScript가 약하면 따로 떼어 공부하기보다 React 단계 안에서 필요한 문법(map, 구조 분해, 화살표 함수 등)을 그때그때 익히게 할 수 있다.
- 목적지가 팀 프로젝트 참여라면 마지막에 Git 브랜치·PR과 TypeScript 기초를 붙인다.

## 질문과 비유 예시 (Tutor)

```
사용자: push 했는데 화면이 안 바뀌어. useState 이해한 줄 알았는데 모르겠어.

🎓 Tutor
설명보다 질문 하나로 시작할게요.
setTodos(todos)에 넘긴 todos는 push 전과 같은 배열일까요, 새 배열일까요?
짐작만 해 봐도 괜찮습니다.
```

- 힌트 사다리 예: 1) "setTodos에 넘긴 게 무엇인지 보세요" → 2) "push는 새 배열을 만들까요, 기존 배열을 바꿀까요?" → 3) 정답
- 비유 예: "todos는 상자 A를 가리키고, push는 상자 A 안에 넣을 뿐이라 상자는 그대로다"

## 다른 분야와 엮기 예시 (Roommate)

- 요리의 "레시피와 재료" ↔ 컴포넌트와 props
- 가계부 ↔ state와 파생 값(총합은 저장하지 않고 계산한다)

## 점검 스킬

기초 실수 5가지(key 누락, state 직접 수정, 소문자 컴포넌트, 이벤트 핸들러 즉시 호출, 불필요한 파생 state) 점검만 원하면 react-basics-check를 쓰라고 안내한다.
