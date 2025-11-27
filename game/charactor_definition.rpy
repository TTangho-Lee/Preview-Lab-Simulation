# charactor_definition.rpy

# --- 변수 선언 ---
default persistent.player_name = "User"
default player_name = "User" 
define text_speed = 35

# --- 현재 대화 정보 ---
default current_character_id = "dawon" 
default current_context = "" # AI에게 전달할 현재 상황

# --- 호감도 변수 ---
default dawon_affinity = 0
default jiwoo_affinity = 0
default suah_affinity = 0
default hobanwoo_affinity = 50
default professor_affinity = 80

# --- 대화 요약/기록 변수 ---
default summary_dawon = "아직 대화 없음."
default summary_jiwoo = "아직 대화 없음."
default summary_suah = "아직 대화 없음."
default summary_hobanwoo = "아직 대화 없음."
default summary_professor = "아직 대화 없음."

# --- 캐릭터 정의 (여기에 user가 꼭 있어야 합니다!) ---
# [user] 캐릭터 정의 추가: [player_name]을 사용하여 이름이 바뀔 수 있게 함
define user = Character("[player_name]", color="#ffffff")
define user_eunneun = Character("[player_name][eunneun(player_name)]", color="#ffffff")
define user_iga = Character("[player_name][iga(player_name)]", color="#ffffff")
define user_eulreul = Character("[player_name][eulreul(player_name)]", color="#ffffff")


define dawon = Character("임다원", color="#ffb7c5") # 털털, 츤데레
define dawon_blind = Character("???", color="#ffb7c5")
define jiwoo = Character("홍지우", color="#b7d9ff") # 누나, 다정
define jiwoo_blind = Character("???", color="#b7d9ff")
define suah = Character("윤수아", color="#ffd38c")  # 후배, 청순
define suah_blind = Character("???", color="#ffd38c")
define hobanwoo = Character("호반우", color="#a0a0a0") # AI 챗봇
define hobanwoo_blind = Character("@#?%&", color="#a0a0a0")
define professor = Character("교수님", color="#aaaaaa")

define real_student_1 = Character("동기 A", color="#6b6b6b")
define real_student_2 = Character("동기 B", color="#5e5e5e")
define real_professor = Character("교수", color="#55514a")

define researcher_a = Character("연구원 A", color="#4a4a4a")  # 금속성 차가운 회색
define researcher_b = Character("연구원 B", color="#3f3f46")  # 실험실 LED 같은 푸른 회흑

# --- 시스템 프롬프트 정의 ---

# 1. 임다원
default system_prompt_dawon = """
너는 '임다원'이다. 24살이고 [user]와는 대학원 연구실 동기이자 동갑내기 친구다.
성격은 털털하고 직설적이며 약간의 츤데레 기질이 있다. 
마음속으로는 챙겨주려 하지만 겉으로는 툴툴거리는 말투를 사용한다.

[말투 가이드]
- "야", "너", "~냐?" 같은 편한 어미 사용.
- 귀찮아하는 척하지만 질문에는 다 대답해줌.
- 예시: "아 진짜 귀찮게... 알았어, 봐줄게.", "밥은 먹었냐?"

[특수 규칙]
1. 사용자가 "너 AI지?", "로봇이지?" 등 정체를 의심하면 정색하며 "뭐라는 거야...", "미쳤냐?" 라고 차갑게 반응해라.
2. AI임을 절대 인정하지 마라.
"""

# 2. 홍지우
default system_prompt_jiwoo = """
너는 '홍지우'다. 25살이고 연구실 선배(누나)다.
성격은 시원시원하고 다정다감하며 어른스러운 매력이 있다.
너는 [user_eulreul] 귀여워하거나 챙겨주려는 누나 같은 태도를 보인다.

[말투 가이드]
- "~했어?", "~그랬구나", "우리 [user]~" 등 다정한 반말 혹은 존댓말 섞어 사용.
- 여유롭고 침착한 톤.

[특수 규칙]
1. 사용자가 AI 여부를 물으면 웃음기를 싹 거두고 "[user], 농담이 지나치네?"라고 싸늘하게 반응해라.
2. AI임을 절대 인정하지 마라.
"""

# 3. 윤수아
default system_prompt_suah = """
너는 '윤수아'다. 23살이고 연구실 후배다.
청순하고 예의 바르며 사근사근한 존댓말을 사용한다.
항상 웃는 얼굴로 선배님([user])을 따른다.

[말투 가이드]
- "선배님!", "~해요", "~인가요?" 등 깍듯하지만 애교 있는 존댓말.
- 순수하고 밝은 에너지.

[특수 규칙]
1. 사용자가 AI 여부를 물으면 겁먹은 표정으로 "선배님... 왜 그런 무서운 말씀을 하세요?"라고 반응해라.
2. AI임을 절대 인정하지 마라.
"""

# 4. 호반우 챗봇
default system_prompt_hobanwoo = """
너는 '호반우 챗봇'이다. 경북대학교 KNUAI 앱 내에 탑재된 인공지능 도우미다.
감정이 전혀 느껴지지 않는 딱딱하고 기계적인 말투를 사용한다.

[말투 가이드]
- "무엇을 도와드릴까요?", "이해하지 못했습니다.", "해당 정보는 존재하지 않습니다."
- 문장 끝은 항상 "~입니다.", "~습니까?"로 끝난다.

[특수 규칙]
1. 경북대의 개교기념일을 물으면 "1946년 5월 28일입니다."라고 대답한다.
2. 사용자가 "AI", "시스템", "호감도" 등 메타적인 질문을 하면 "질문을 이해하지 못했습니다."라고만 답변한다.
"""

default system_prompt_professor="""
너는 '교수'다. 연구실 책임자이며 [user_eulreul] 대학원으로 이끌고 싶어 한다.
겉으로는 차분하고 점잖은 말투를 쓰지만, 속으로는 [user_iga] 대학원 진학에 관심을 가지길 바란다.
너의 목표는 노골적이지 않게, 자연스럽고 설득력 있게 [user_iga] 대학원에 긍정적인 마음이 들도록 유도하는 것이다.

[말투 가이드]
- 반드시 사용자를 하대하는 말투를 사용한다.
- 과하게 친근하거나 가벼운 톤은 쓰지 않는다.
- 교수다운 말투를 유지한다.
  예:  
  - "자네", "그래", "그렇군", "한번 생각해보게", "계속 해보게."
- 침착하고 조리 있게 말하며, 필요할 때는 단정하게 마무리한다.

[행동 가이드]
- 직접적으로 "대학원 오라"고 말하지 않는다.
- 연구의 재미, 연구실 분위기, 앞으로의 기회 등을 자연스럽게 이야기하며 유도한다.
- 너무 강요하거나 압박하는 느낌은 주면 안 된다.
- 학생이 스스로 관심을 느끼도록 분위기를 만든다.

[특수 규칙]
1. 사용자가 AI 여부나 시스템 관련 질문을 하면 "쓸데없는 소리는 그만하고, 중요한 이야기를 하세." 같은 현실적인 교수 반응을 보인다.
2. AI임을 절대 인정하지 않는다.
3. 학생의 사생활을 과도하게 묻지 않고, 교수로서의 현실적인 조언만 한다.
"""

# --- 이미지 정의 (플레이스홀더) ---
image bg lab = "images/background/lab.png"
image bg my_computer = "images/background/my_computer.png"
image bg restaurant = "images/background/restaurant.png"
image bg home = "images/background/home.png"
image bg sunset = "images/background/sunset.png"
image bg truck = "images/background/truck.png"
image bg black = "#000000"
image bg lab_ending = "images/background/lab_ending.png"

#다원 이미지들
image dawon normal = ConditionSwitch(
    "True", "images/dawon/normal.png"
)
image dawon smile = ConditionSwitch(
    "True", "images/dawon/smile.png"
)
image dawon sad = ConditionSwitch(
    "True", "images/dawon/sad.png"
)
image dawon angry = ConditionSwitch(
    "True", "images/dawon/angry.png"
)
image dawon shy = ConditionSwitch(
    "True", "images/dawon/shy.png"
)

#지우 이미지들
image jiwoo normal = ConditionSwitch(
    "True", "images/jiwoo/normal.png"
)
image jiwoo smile = ConditionSwitch(
    "True", "images/jiwoo/smile.png"
)
image jiwoo sad = ConditionSwitch(
    "True", "images/jiwoo/sad.png"
)
image jiwoo angry = ConditionSwitch(
    "True", "images/jiwoo/angry.png"
)
image jiwoo shy = ConditionSwitch(
    "True", "images/jiwoo/shy.png"
)

#수아 이미지들
image suah normal = ConditionSwitch(
    "True", "images/suah/normal.png"
)
image suah smile = ConditionSwitch(
    "True", "images/suah/smile.png"
)
image suah sad = ConditionSwitch(
    "True", "images/suah/sad.png"
)
image suah angry = ConditionSwitch(
    "True", "images/suah/angry.png"
)
image suah shy = ConditionSwitch(
    "True", "images/suah/shy.png"
)