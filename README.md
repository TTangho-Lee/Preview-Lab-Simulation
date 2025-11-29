# **🎮 미리보는 연구실 시뮬레이션**

### **”직접 캐릭터와 대화하는 듯한 초 몰입형 미연시게임”**

## **💡 프로젝트 소개 (Overview)**

『**미리보는 연구실 시뮬레이션**』은 평범한 대학생이 트럭 사고 후 이세계의 대학원 연구실에서 깨어나며 벌어지는 일을 그린 미스터리 로맨스 시뮬레이션입니다.

기존의 미연시가 개발자가 미리 정해둔 여러개의 선택지 중 하나를 고르는 수동적인 방식이었다면, 이 프로젝트는 탄탄한 스토리 내에서 생성형 AI를 도입하여 유저가 직접 타이핑한 모든 말에 캐릭터가 실시간으로 반응하며 호감도를 쌓을 수 있는 능동적인 상호작용 경험을 제공합니다.

## **🏁 목표**

• **상업적 목표:** 정형화된 선택지 게임에 지친 유저들에게 자유도 높은 대화 경험을 제공하여 차별화된 시장 경쟁력 확보.
• **기술적 목표:** 게임 엔진과 생성형 AI의 실시간 통신 최적화 및 캐릭터 페르소나 유지 기술 구현.

### 🗝️ 핵심 가치: One Function, Infinite Possibilities

**"단 하나의 기능(Gemini api 연동)으로 만드는 무한한 확장성"**

- **👨‍💻 개발의 편리함 :** 개발자는 핵심적인 메인 스토리 라인 설계에만 집중합니다. 스토리 사이사이 발생하는 수천 가지의 일상 대화와 상호작용은 일일이 작성할 필요 없이, 단 하나의 페르소나 프롬프트가 상황에 맞춰 무한히 생성해내어 개발 효율을 극대화했습니다.
- **🕹️ 플레이의 무한함 :** 큰 줄기의 스토리는 유지되지만, 그 안에서의 대화는 플레이할 때마다 매번 새롭습니다. 유저는 정해진 답을 찾는 것이 아니라, 자신만의 언어로 캐릭터를 설득하거나 위로하며 호감도를 쌓아갑니다. 같은 스토리를 따라가더라도, 매회 전혀 다른 대화 흐름과 감정선을 경험할 수 있습니다.

## **🖥️ 개발 방식 및 기술 스택**

### **🛠️ Tech Stack**

- **Core Engine:** Ren'Py (Visual Novel Engine based on Python)
- **AI Integration:** Google Gemini 2.0 Flash Lite API
- **Development:** Python (`requests`, `json` modules for API Handling)
- **Collaboration:** SourceTree, GitHub, Notion
- **Design:** Nano Banana AI, Miri Canvas

## 🕹️ 주요 기능 및 구현

### ① 🗣️ 상황 인식형 자유 대화

이벤트 사이의 자유 대화 구간에서 유저가 키보드로 대사를 입력하면, AI 캐릭터가 현재 스토리 문맥(식사, 정전, 과제 등)을 이해하고 반응합니다.

- 하이브리드 스토리텔링: 단순 챗봇이 아닌 자유 대화가 스토리 흐름을 해치지 않고 다음 이벤트로 자연스럽게 연결되도록 설계되었습니다.
- ⚙️ 구현 기술:
    - Ren'Py & Python 연동: `requests` 라이브러리를 활용한 실시간 Gemini 서버 통신 파이프라인 구축.
    - 프롬프트 엔지니어링: 캐릭터별 고유 성격/말투 및 상황별 시나리오 학습.

### ② 🎭 실시간 감정 분석 및 표정 연출

Gemini API가 유저 입력 텍스트의 감정(긍정/부정/의심 등)을 실시간 분석하여 -5 ~ +5 사이의 호감도 점수로 환산합니다.

- 동적 상호작용: 호감도 수치에 따라 캐릭터의 표정이 변경됩니다. (웃음, 정색, 두려움 등)
- ⚙️ 구현 기술:
    - LLM 감정 분석 프롬프트을 활용해 추출한 감정을 `talk_loop.rpy` 에서 받아 이미지 변경 로직 호출.

### ③ 📱 KNUAI 인게임 스마트폰

키보드 `0`번을 눌러 언제든 스마트폰을 꺼내 캐릭터들의 상태를 확인할 수 있는 오버레이 UI를 제공합니다.

- 직관적 피드백: 대화를 통해 변동된 호감도와 캐릭터 상태를 스마트폰 화면에서 즉시 확인할 수 있습니다.
- ⚙️ 구현 기술:
    - `additional_ui.rpy` 내에서 휴대폰 오버레이, 캐릭터별 호감도 표시 UI 및 토스트 알림 디자인 구현.

## 💰 실용성 및 상업적 가치

본 프로젝트는 정해진 선택지를 수동적으로 소비하던 기존 미연시와 달리, 자유 입력을 통해 유저가 캐릭터와 직접 소통하며 자신만의 스토리를 만들어가는 새로운 게임 패러다임을 제시합니다. 매 플레이마다 달라지는 대화와 엔딩은 유저의 반복 플레이를 유도하여 체류 시간을 획기적으로 증대시킵니다.

더 나아가, 유저가 직접 캐릭터를 제작하고 공유하는 ‘**마켓플레이스**’ 기능을 도입하여 게임의 확장성을 극대화할 계획입니다. 유저가 소비자이자 생산자가 되는 선순환 구조를 통해, 개발사의 지속적인 개입 없이도 끊임없이 새로운 콘텐츠가 생성되는 플랫폼으로 발전할 것입니다.

## 📁 `미리보는 연구실 시뮬레이션` 프로젝트 구조 요약

LAB_SIMULATION/
 │
 ├─ additional_ui.rpy # 추가 UI 정의
 ├─ a_secret_key.rpy # API 키 등 민감 정보 정의 (배포 시 제외)
 ├─ charactor_definition.rpy # 캐릭터 기본 정의
├─ gemini_api.rpy # Gemini API 통신 로직
├─ gui.rpy # GUI 스타일 및 설정
├─ options.rpy # 환경 설정
├─ python_function.rpy # Python 헬퍼 함수들
├─ screens.rpy # 메인 메뉴 및 UI 스크린
├─ script.rpy # 게임 메인 루트 스크립트
├─ SourceHanSansLite.ttf # 게임 폰트
├─ talk_loop.rpy # 대화 루프 메인 로직
├─ talk_loop_all_charactor.rpy # 전체 캐릭터 대화 루프
│
├─ cache/ # Ren'Py 캐시 파일
│
├─ endding/ # 엔딩 스크립트
│ ├─ bad_ending.rpy
│ ├─ dream_ending.rpy
│ ├─ endding_choice.rpy
│ ├─ happy_ending.rpy
│ └─ ...
│
├─ event/ # 이벤트 씬 스크립트
│ ├─ event_1.rpy
│ ├─ event_2.rpy
│ └─ ...
│
├─ gui/ # UI 이미지 리소스
│
├─ images/ # 캐릭터/배경 이미지
│
├─ libs/ # 외부 라이브러리
│
├─ saves/ # 세이브 파일
│
├─ talk/ # 일반 대화 스크립트
│
└─ tl/ # 번역 파일


## **👥 팀 소개**
이름	직책 (Role)	상세 담당 업무 (Responsibilities)
이승호	System Architect
& AI Engineer	• LLM API 파이프라인 구축: Ren'Py와 Gemini 간 실시간 통신 로직 구현
• Backend Logic: JSON 데이터 파싱 및 게임 내 변수(호감도) 연동 로직 개발
배명우	Client Engineer
& UI/UX Design	• In-Game Interface 구현: KNUAI 스마트폰 오버레이 및 실시간 게이지 시스템 개발
• Screen Language Scripting: Ren'Py 스크린 언어를 활용한 동적 UI/UX 설계
신유민	Creative Director
& Narrative Design	• Scenario Writing: 메인 스토리라인, 멀티 엔딩 분기 및 메타픽션 서사 기획
• World Building: 세계관 및 캐릭터 설정 데이터베이스 구축
허신행	Project Manager
& Game Planner	• Game Concept Design: 총괄 디렉션, 게임의 핵심 재미 요소 기획 및 아이디어 구체화
• Quality Assurance (QA): 버그 리포팅 및 사용자 경험(UX) 피드백 제공
