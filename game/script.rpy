# script.rpy

# ----------------------------------
# 플레이어 이름 입력
# ----------------------------------
default persistent.player_name = "플레이어"

# ----------------------------------
# 3명의 캐릭터 정보
# ----------------------------------
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


# 현재 선택된 캐릭터
default current_character = "haru"

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

image bg classroom = "images/background/classroom.jpg"
image bg park = "images/background/park.jpg"
image bg night = "images/background/night.jpg"
image bg rooftop = "images/background/rooftop.jpg"


# ----------------------------------
# 호감도 UI
# ----------------------------------
screen love_meter():
    frame:
        xalign 1.0
        yalign 0.2
        background "#0008"
        padding (20,20,20,20)
        vbox:

            if current_character == "haru":
                text "하루 호감도: [persistent.love_haru]"
                bar value persistent.love_haru range 100 xmaximum 200

            if current_character == "yuki":
                text "유키 호감도: [persistent.love_yuki]"
                bar value persistent.love_yuki range 100 xmaximum 200

            if current_character == "mina":
                text "미나 호감도: [persistent.love_mina]"
                bar value persistent.love_mina range 100 xmaximum 200


# ----------------------------------
# 타자기 효과음
# ----------------------------------
init python:
    import random
    import re
    TYPE_SOUND = "sfx/type.ogg"

    def typer_filter(what):
        result = ""
        for ch in what:
            renpy.play(TYPE_SOUND, channel="sound")
            renpy.pause(random.uniform(0.015, 0.030))
            result += ch
        return result

    config.say_menu_text_filter = typer_filter


# ----------------------------------
# 호감도 적용
# ----------------------------------
init python:
    def apply_love_change(delta):
        if delta is None:
            return

        if current_character == "haru":
            persistent.love_haru = max(0, min(100, persistent.love_haru + delta))
        elif current_character == "yuki":
            persistent.love_yuki = max(0, min(100, persistent.love_yuki + delta))
        elif current_character == "mina":
            persistent.love_mina = max(0, min(100, persistent.love_mina + delta))

init python:
    def get_character_expression(love):
        if love < 30:
            return "angry"
        elif love < 50:
            return "normal"
        elif love < 70:
            return "happy"
        elif love < 90:
            return "shy"
        else:
            return "love"

    def get_background(love):
        if love < 40:
            return "classroom"
        elif love < 70:
            return "park"
        elif love < 90:
            return "night"
        else:
            return "rooftop"

init python:
    def check_event(character):
        love = getattr(persistent, f"love_{character}")
        talk = getattr(persistent, f"talk_{character}")

        # 이벤트 1
        if talk >= 5 and love >= 40:
            return f"event_{character}_1"

        # 이벤트 2
        if talk >= 10 and love >= 60:
            return f"event_{character}_2"

        # 엔딩
        if talk >= 20 and love >= 90:
            return f"ending_{character}"

        return None

# ----------------------------------
# 게임 시작
# ----------------------------------
label start:

    $ persistent.player_name = renpy.input("당신의 이름은?").strip()
    if persistent.player_name == "":
        $ persistent.player_name = "플레이어"

    call choose_character


# ----------------------------------
# 캐릭터 선택
# ----------------------------------
label choose_character:
    scene bg classroom

    show haru normal at center
    haru "{cps=35}안녕~ 나는 하루야. 만나서 반가워.
나는 조용하고 다정한 편이라, 네 이야기를 들어주고 싶어.
힘든 일이 있으면 언제든 말해줘. 내가 들어주고, 조금이라도 위로가 되어줄게.{/cps}"

    show yuki normal at left
    yuki "{cps=35}…나는 유키야. 그냥 알맞게 알아두면 돼.
말이 많진 않지만, 필요한 건 솔직하게 말할게.
너랑 어떻게 지낼지는, 서로 알아가면서 결정하면 될 것 같아.{/cps}"


    show mina normal at right
    mina "{cps=35}야호~ 나는 미나야! 만나서 반가워~!
나는 항상 밝고 신나는 걸 좋아해! 같이 즐겁게 놀면서 얘기하자~!
응응~ 너랑 있으면 나까지 신나지 않을까?{/cps}"


    menu:
        "하루 (상냥한 소녀)":
            $ current_character = "haru"
            jump start_talk

        "유키 (시크한 소녀)":
            $ current_character = "yuki"
            jump start_talk

        "미나 (발랄한 소녀)":
            $ current_character = "mina"
            jump start_talk
            



# ----------------------------------
# 첫 대사
# ----------------------------------
label start_talk:

    show screen love_meter

    if current_character == "haru":
        scene bg classroom
        show haru normal at center
        haru "{cps=35}어… 안녕! 오늘은 무슨 얘기하고 싶어?{/cps}"

    elif current_character == "yuki":
        scene bg classroom
        show yuki normal at center
        yuki "{cps=35}왔어? …뭐, 얘기 정도는 들어줄게.{/cps}"

    elif current_character == "mina":
        scene bg classroom
        show mina normal at center
        mina "{cps=35}오! 드디어 왔네~ 뭐 물어볼 거 있어~?{/cps}"

    jump free_talk


# ----------------------------------
# 대화 루프 (기존 기능 그대로 유지)
# ----------------------------------
label free_talk:

    # 플레이어 입력
    $ player_text = renpy.input(f"{persistent.player_name}:").strip()

    if player_text == "":
        "……아무 말도 안 한 것 같아."
        jump free_talk

    # --- GPT 호출 ---
    if current_character == "haru":
        $ ai_reply, love_delta, new_summary = gemini_generate_response(system_prompt_haru, persistent.summary_haru, player_text)
        $ persistent.summary_haru = new_summary
        $ persistent.talk_haru += 1
        $ persistent.history_haru.append(f"{persistent.player_name}:{player_text} / 하루:{ai_reply}")
        $ persistent.history_haru = persistent.history_haru[-3:]

    elif current_character == "yuki":
        $ ai_reply, love_delta, new_summary = gemini_generate_response(system_prompt_yuki, persistent.summary_yuki, player_text)
        $ persistent.summary_yuki = new_summary
        $ persistent.talk_yuki += 1
        $ persistent.history_yuki.append(f"{persistent.player_name}:{player_text} / 유키:{ai_reply}")
        $ persistent.history_yuki = persistent.history_yuki[-3:]

    elif current_character == "mina":
        $ ai_reply, love_delta, new_summary = gemini_generate_response(system_prompt_mina, persistent.summary_mina, player_text)
        $ persistent.summary_mina = new_summary
        $ persistent.talk_mina += 1
        $ persistent.history_mina.append(f"{persistent.player_name}:{player_text} / 미나:{ai_reply}")
        $ persistent.history_mina = persistent.history_mina[-3:]

    # --- 호감도 적용 ---
    $ apply_love_change(love_delta)

    # --- 표정·배경 결정 (동적 처리) ---
    if current_character == "haru":
        $ love_val = persistent.love_haru
    elif current_character == "yuki":
        $ love_val = persistent.love_yuki
    else:
        $ love_val = persistent.love_mina

    $ expr = get_character_expression(love_val)        # ex: "happy"
    $ bg_tag = get_background(love_val)           # ex: "park"

    # 배경 변경 (동적)
    scene expression "bg " + bg_tag

    # 캐릭터 이미지 태그 문자열 생성 (예: "haru happy")
    $ char_image_tag = current_character + " " + expr

    # 캐릭터 표시 (동적): 'show expression <python-variable>' 형태 사용
    show expression char_image_tag

    # --- 대사 출력 (타입라이터 문장 단위) ---
    python:
        import re
        sentences = [s.strip() for s in re.findall(r'[^.!?]+[.!?]*', ai_reply) if s.strip()]
        for s in sentences:
            if current_character == "haru":
                renpy.say(haru, "{cps=35}" + s + "{/cps}")
            elif current_character == "yuki":
                renpy.say(yuki, "{cps=35}" + s + "{/cps}")
            else:
                renpy.say(mina, "{cps=35}" + s + "{/cps}")


    # --- 이벤트 체크 ---
    $ ev = check_event(current_character)
    if ev:
        jump expression ev

    jump free_talk

# ------------------------------------------------
# 이벤트 레이블 예시 (캐릭터별)
# ------------------------------------------------
label event_haru_1:
    show haru happy
    haru "{cps=35}어? 우리 벌써 이렇게 친해진 거야? 고마워…{/cps}"
    return

label event_haru_2:
    show haru shy
    haru "{cps=35}이런 말 해도 되나... 좀 부끄럽네.{/cps}"
    return

label ending_haru:
    show haru love
    scene bg rooftop
    haru "{cps=35}정말…너랑 있으면 마음이 편해져. 좋아해.{/cps}"
    return

label event_yuki_1:
    show yuki normal
    yuki "{cps=35}흥, 네가 그렇게 말하다니. 조금은 인정해줄게.{/cps}"
    return

label event_yuki_2:
    show yuki shy
    yuki "{cps=35}…그만 놀려. 진짜로 기뻐질 수도 있잖아.{/cps}"
    return

label ending_yuki:
    show yuki love
    scene bg night
    yuki "{cps=35}네가 옆에 있어서… 이상하게 편하네. 좋아해.{/cps}"
    return

label event_mina_1:
    show mina happy
    mina "{cps=35}우와! 대화 진짜 재밌다~ 더 해보자!{/cps}"
    return

label event_mina_2:
    show mina shy
    mina "{cps=35}이런 분위기 너무 좋아~ 꺄르르{/cps}"
    return

label ending_mina:
    show mina love
    scene bg rooftop
    mina "{cps=35}너랑 있는 시간, 진짜 소중해! 좋아해!!{/cps}"
    return