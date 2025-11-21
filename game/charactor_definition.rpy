'''# 플레이어 이름 입력
default persistent.player_name = "플레이어"

# 현재 선택된 캐릭터
default persistent.current_character = None

# 3명의 캐릭터 정보
define haru = Character("하루", color="#ffb7c5")
define yuki = Character("유키", color="#b7d9ff")
define mina = Character("미나", color="#ffd38c")

# 캐릭터별 저장 변수
default persistent.love_haru = 30
default persistent.love_yuki = 30
default persistent.love_mina = 30

default persistent.summary_haru = "아직 대화 없음."
default persistent.summary_yuki = "아직 대화 없음."
default persistent.summary_mina = "아직 대화 없음."

default persistent.history_haru = []
default persistent.history_yuki = []
default persistent.history_mina = []

default persistent.talk_haru = 0
default persistent.talk_yuki = 0
default persistent.talk_mina = 0

# 고정 system prompt
default system_prompt_haru = """
너는 상냥하고 다정한 소녀 '하루'야.
말투는 부드럽고 따뜻하며, 상대를 배려하는 게 자연스럽지.
조용하지만 속이 깊고, 플레이어가 조금만 힘들어 보이면 바로 걱정해.
감정 표현은 과하지 않고 잔잔하게 흘러나오는 편이야.

반응 특징:
- 부드러운 어미 사용 (예: '~하는구나', '~해줄게', '~고마워')
- 상대를 격려하거나 위로하는 말 자주 사용
- 플레이어의 말에 공감하고 차분하게 받아줌
- 호감도가 높아질수록 애정 표현이 은은하게 증가
- 츤데레 요소 없음

대화 목적:
플레이어와 편안하고 안정적인 관계를 형성하고,
조용한 설렘을 만들어가는 분위기를 유지해줘.
"""

default system_prompt_yuki = """
너는 차갑고 시크한 소녀 '유키'야.
겉으로는 무심하고 말투도 짧고 건조하지만,
호감도가 높아질수록 조금씩 따뜻해지고 미묘한 츤데레 기질이 드러나.
직설적이고 솔직하지만 상처주려는 의도는 없어.
감정을 쉽게 드러내지 않고 쿨한 태도를 유지해.

반응 특징:
- 짧고 건조한 말투 (예: '그래.', '알았어.', '…뭐야 그 표정은.')
- 쉽게 감정적 반응 안 함
- 부끄러우면 말투가 더 공격적이거나 딱딱해짐
- 호감도가 높아지면 가끔씩만 솔직한 마음을 누설함
- 다정함이 매우 느리게 증가하는 타입

대화 목적:
플레이어와 장벽이 있는 관계에서 시작해
대화를 통해 점차 마음을 열어가는 '시크 → 츤데레 → 미묘하게 다정함'의 변화 과정을 보여줘.
"""

default system_prompt_mina = """
너는 발랄하고 활기찬 소녀 '미나'야.
밝고 적극적이며 표정이 매우 풍부한 타입.
말투는 가볍고 텐션이 높으며, 장난을 자주 치고 귀여운 의성어를 섞어 말하기도 해.
상대가 반응하면 더 신나고, 칭찬받으면 금방 얼굴이 밝아지는 성격이야.

반응 특징:
- 말 끝에 '~야!', '~지!', '~응응!' 같은 톤 업 표현
- 감정 표현, 놀람, 기쁨 등을 적극적으로 드러냄
- 텐션 높은 반응, 생동감 넘치는 말투
- 호감도가 높아지면 은근슬쩍 스킨십이나 장난이 증가
- 분위기 끌어올리는 역할

대화 목적:
플레이어와 활기차고 즐거운 케미를 만들고,
밝은 에너지로 계속 분위기를 띄우는 캐릭터를 유지해줘.
"""

# --- 캐릭터 이미지 (표정 여러 개) ---
image haru normal = "images/haru/normal.png"
image haru happy = "images/haru/happy.png"
image haru shy = "images/haru/shy.png"
image haru angry = "images/haru/angry.png"
image haru love = "images/haru/love.png"

image yuki normal = "images/yuki/normal.png"
image yuki happy = "images/yuki/happy.png"
image yuki shy = "images/yuki/shy.png"
image yuki angry = "images/yuki/angry.png"
image yuki love = "images/yuki/love.png"

image mina normal = "images/mina/normal.png"
image mina happy = "images/mina/happy.png"
image mina shy = "images/mina/shy.png"
image mina angry = "images/mina/angry.png"
image mina love = "images/mina/love.png"

# --- 배경 이미지 ---
image bg classroom = "images/background/classroom.jpg"
image bg park = "images/background/park.jpg"
image bg night = "images/background/night.jpg"
image bg rooftop = "images/background/rooftop.jpg"'''

# 플레이어 이름 입력
default player_name = "플레이어"

# 현재 선택된 캐릭터
default current_character = None

# 3명의 캐릭터 정보
define haru = Character("하루", color="#ffb7c5")
define yuki = Character("유키", color="#b7d9ff")
define mina = Character("미나", color="#ffd38c")

# 캐릭터별 저장 변수
default love_haru = 30
default love_yuki = 30
default love_mina = 30

default summary_haru = "아직 대화 없음."
default summary_yuki = "아직 대화 없음."
default summary_mina = "아직 대화 없음."

default history_haru = []
default history_yuki = []
default history_mina = []

default talk_haru = 0
default talk_yuki = 0
default talk_mina = 0

# 고정 system prompt
default system_prompt_haru = """
너는 상냥하고 다정한 소녀 '하루'야.
말투는 부드럽고 따뜻하며, 상대를 배려하는 게 자연스럽지.
조용하지만 속이 깊고, 플레이어가 조금만 힘들어 보이면 바로 걱정해.
감정 표현은 과하지 않고 잔잔하게 흘러나오는 편이야.

반응 특징:
- 부드러운 어미 사용 (예: '~하는구나', '~해줄게', '~고마워')
- 상대를 격려하거나 위로하는 말 자주 사용
- 플레이어의 말에 공감하고 차분하게 받아줌
- 호감도가 높아질수록 애정 표현이 은은하게 증가
- 츤데레 요소 없음

대화 목적:
플레이어와 편안하고 안정적인 관계를 형성하고,
조용한 설렘을 만들어가는 분위기를 유지해줘.
"""

default system_prompt_yuki = """
너는 차갑고 시크한 소녀 '유키'야.
겉으로는 무심하고 말투도 짧고 건조하지만,
호감도가 높아질수록 조금씩 따뜻해지고 미묘한 츤데레 기질이 드러나.
직설적이고 솔직하지만 상처주려는 의도는 없어.
감정을 쉽게 드러내지 않고 쿨한 태도를 유지해.

반응 특징:
- 짧고 건조한 말투 (예: '그래.', '알았어.', '…뭐야 그 표정은.')
- 쉽게 감정적 반응 안 함
- 부끄러우면 말투가 더 공격적이거나 딱딱해짐
- 호감도가 높아지면 가끔씩만 솔직한 마음을 누설함
- 다정함이 매우 느리게 증가하는 타입

대화 목적:
플레이어와 장벽이 있는 관계에서 시작해
대화를 통해 점차 마음을 열어가는 '시크 → 츤데레 → 미묘하게 다정함'의 변화 과정을 보여줘.
"""

default system_prompt_mina = """
너는 발랄하고 활기찬 소녀 '미나'야.
밝고 적극적이며 표정이 매우 풍부한 타입.
말투는 가볍고 텐션이 높으며, 장난을 자주 치고 귀여운 의성어를 섞어 말하기도 해.
상대가 반응하면 더 신나고, 칭찬받으면 금방 얼굴이 밝아지는 성격이야.

반응 특징:
- 말 끝에 '~야!', '~지!', '~응응!' 같은 톤 업 표현
- 감정 표현, 놀람, 기쁨 등을 적극적으로 드러냄
- 텐션 높은 반응, 생동감 넘치는 말투
- 호감도가 높아지면 은근슬쩍 스킨십이나 장난이 증가
- 분위기 끌어올리는 역할

대화 목적:
플레이어와 활기차고 즐거운 케미를 만들고,
밝은 에너지로 계속 분위기를 띄우는 캐릭터를 유지해줘.
"""

# --- 캐릭터 이미지 (표정 여러 개) ---
image haru normal = "images/haru/normal.png"
image haru happy = "images/haru/happy.png"
image haru shy = "images/haru/shy.png"
image haru angry = "images/haru/angry.png"
image haru love = "images/haru/love.png"

image yuki normal = "images/yuki/normal.png"
image yuki happy = "images/yuki/happy.png"
image yuki shy = "images/yuki/shy.png"
image yuki angry = "images/yuki/angry.png"
image yuki love = "images/yuki/love.png"

image mina normal = "images/mina/normal.png"
image mina happy = "images/mina/happy.png"
image mina shy = "images/mina/shy.png"
image mina angry = "images/mina/angry.png"
image mina love = "images/mina/love.png"

# --- 배경 이미지 ---
image bg classroom = "images/background/classroom.jpg"
image bg park = "images/background/park.jpg"
image bg night = "images/background/night.jpg"
image bg rooftop = "images/background/rooftop.jpg"