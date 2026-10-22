# claude-skills

Claude Code에서 쓰는 직접 만든 스킬 모음입니다.

| 스킬 | 하는 일 |
|---|---|
| [alter-coach](alter-coach/SKILL.md) | 학습자가 부딪힌 벽을 진단해 ALTER 역할(Advisor·Librarian·Tutor·Editor·Roommate)로 돕는 학습 코치. 계획표·자료·기록·리뷰를 HTML로 남길 수 있다 |
| [doc-visualizer](doc-visualizer/SKILL.md) | 문서(URL, PDF, Markdown, Word, 텍스트)를 읽고 흐름도·표·타임라인으로 시각화한 HTML을 만든다 |
| [react-basics-check](react-basics-check/SKILL.md) | React 입문자 코드의 기초 실수 5가지를 점검하고 이유를 설명한다 |
| [react-basic-study](react-basic-study/SKILL.md) | React에서 배열을 바꿨는데 화면이 안 바뀌는 문제를 입문자 눈높이로 설명한다 |

## 설치

스킬 폴더를 `~/.claude/skills/`에 두거나 심볼릭 링크로 연결합니다.

```bash
git clone https://github.com/sanggyu111/claude-skills.git ~/dev/claude-skills
ln -s ~/dev/claude-skills/alter-coach ~/.claude/skills/alter-coach
```
