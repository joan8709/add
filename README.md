# Git 팀 협업 실습

2-3명이 팀을 이루어 Git 협업 워크플로우를 실습합니다.

---

## 학습 목표

- Feature Branch 전략 이해 및 실습
- Pull Request 생성 및 코드 리뷰 경험
- Git 충돌 발생 및 해결
- pytest를 활용한 테스트 주도 개발

---

## 프로젝트 구조

```
Day02_Git-Team-Collaboration/
├── README.md                 # 현재 파일
├── requirements.txt          # 의존성 (pytest)
├── pytest.ini               # pytest 설정
│
├── docs/                    # 가이드 문서
│   ├── 01_pytest_기초.md     # pytest 기초 설명
│   ├── 02_팀_워크플로우.md    # 협업 가이드
│   └── 03_충돌_해결.md       # 충돌 해결 가이드
│
├── src/                     # 소스 코드 (구현 대상)
│   ├── calculator.py        # 팀원 A 담당
│   ├── statistics.py        # 팀원 B 담당
│   └── utils.py             # 팀원 C 담당
│
├── tests/                   # 테스트 코드 (미리 작성됨)
│   ├── test_calculator.py
│   ├── test_statistics.py
│   └── test_utils.py
│
└── scenarios/               # 충돌 실습용
    └── SHARED_CONFIG.py
```

---

## 빠른 시작

### 1. 저장소 Clone

```bash
git clone <저장소-URL>
cd Day02_Git-Team-Collaboration
```

### 2. 환경 설정

```bash
# 가상환경 생성 (권장)
python -m venv venv

# Mac/Linux:
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### 3. 테스트 실행

```bash
# 모든 테스트 실행 (처음엔 모두 실패)
pytest

# 특정 모듈만 테스트
pytest tests/test_calculator.py -v
```

---

## 실습 순서

| 순서 | 내용 |
|------|------|
| 1 | [pytest 기초](docs/01_pytest_기초.md) |
| 2 | [팀 워크플로우](docs/02_팀_워크플로우.md) |
| 3 | [충돌 해결](docs/03_충돌_해결.md) |

---

## 역할 분담

### 3인 팀

| 역할 | 담당 파일 | 구현 함수 | 브랜치 |
|------|----------|----------|--------|
| 팀원 A | `src/calculator.py` | add, subtract, multiply, divide | `feature/calculator` |
| 팀원 B | `src/statistics.py` | mean, median, mode, variance | `feature/statistics` |
| 팀원 C | `src/utils.py` | validate_numbers, round_result, format_output | `feature/utils` |

### 2인 팀

| 역할 | 담당 파일 | 브랜치 |
|------|----------|--------|
| 팀원 A | `calculator.py` + `utils.py` | `feature/calculator`, `feature/utils` |
| 팀원 B | `statistics.py` | `feature/statistics` |

---

## 완료 체크리스트

### Phase 1: 환경 설정
- [ ] 저장소 Fork 완료 (팀장)
- [ ] 팀원 Collaborator 초대 완료
- [ ] 모든 팀원 Clone 완료
- [ ] pytest 설치 및 동작 확인

### Phase 2: pytest 학습
- [ ] pytest 기초 문서 읽기
- [ ] 테스트 실행 방법 이해
- [ ] assert 문 사용법 이해

### Phase 3: Feature Branch 작업
- [ ] 팀원 A: calculator.py 구현 완료
- [ ] 팀원 B: statistics.py 구현 완료
- [ ] 팀원 C: utils.py 구현 완료
- [ ] 각자 테스트 통과 확인

### Phase 4: Pull Request
- [ ] 모든 팀원 PR 생성 완료
- [ ] 코드 리뷰 완료 (최소 1명 Approve)
- [ ] 모든 PR Merge 완료

### Phase 5: 충돌 해결
- [ ] SHARED_CONFIG.py 동시 수정
- [ ] 충돌 발생 확인
- [ ] 충돌 해결 완료

---

## 커밋 메시지 컨벤션

```
<타입>: <제목>

<본문 (선택)>
```

**타입:**
- `feat`: 새 기능
- `fix`: 버그 수정
- `docs`: 문서 수정
- `refactor`: 리팩토링
- `test`: 테스트 추가/수정
- `chore`: 기타 변경

**예시:**
```
feat: 사칙연산 함수 구현

- add: 두 수의 합 반환
- subtract: 두 수의 차 반환
- 0으로 나누기 예외 처리 포함
```

---

## 문제 해결

### pytest 모듈을 찾을 수 없음

```
ModuleNotFoundError: No module named 'src'
```

→ 프로젝트 루트 디렉토리에서 pytest 실행

### Push 권한 없음

```
remote: Permission denied
```

→ 팀장이 Settings → Collaborators에서 팀원 추가 확인

### 충돌 발생

```
CONFLICT (content): Merge conflict in ...
```

→ [충돌 해결 가이드](docs/03_충돌_해결.md) 참조

---

## 참고 자료

- [Git 공식 문서](https://git-scm.com/doc)
- [GitHub Pull Request 가이드](https://docs.github.com/en/pull-requests)
- [pytest 공식 문서](https://docs.pytest.org/)
