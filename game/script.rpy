# script.rpy

# ----------------------------------
# 플레이어 이름 입력
# ----------------------------------
default persistent.player_name = "플레이어"

# 현재 선택된 캐릭터
default persistent.current_character = None

# ----------------------------------
# 설정 버튼 (우측 상단)
# ----------------------------------
screen top_menu():
    frame:
        xalign 1.0
        yalign 0.0
        background "#0008"
        padding (10, 10)

        textbutton "⚙ 설정" action ToggleScreen("config_menu")


screen config_menu():
    frame:
        xalign 0.85
        yalign 0.1
        background "#000c"
        padding (20,20)

        vbox:
            spacing 10

            textbutton "이름 변경" action Jump("change_name")
            textbutton "캐릭터 변경" action Jump("choose_character")
            textbutton "닫기" action Hide("config_menu")
            textbutton "전체 초기화" background "#a00" hover_background "#d00" padding (10, 10) action Show("reset_confirm")


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

screen reset_confirm():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        padding (40,40)
        background "#000c"
        xmaximum 600

        vbox:
            spacing 25
            xalign 0.5

            text "정말 모든 데이터를 초기화하시겠습니까?" size 36
            text "{color=#f55}이 작업은 되돌릴 수 없습니다!{/color}" size 28

            hbox:
                spacing 60
                xalign 0.5

                textbutton "예":
                    background "#a00"
                    hover_background "#d00"
                    padding (10,10)
                    action Jump("reset_all_data")

                textbutton "아니오":
                    background "#333"
                    hover_background "#555"
                    padding (10,10)
                    action Hide("reset_confirm")



label reset_all_data:

    hide screen reset_confirm
    hide screen config_menu   # 설정 메뉴 자동 닫기

    # 전체 초기화
    $ persistent._clear()
    $ renpy.save_persistent()

    "모든 데이터가 초기화되었습니다. 게임을 다시 시작합니다."

    $ renpy.pause(1.0)

    # 게임 완전 재시작
    $ renpy.full_restart()




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

    show screen top_menu

    # 이름이 이미 있으면 입력 건너뛰기
    if persistent.player_name and persistent.player_name != "플레이어":
        jump skip_name
    else:
        $ persistent.player_name = renpy.input("당신의 이름은?").strip()
        if persistent.player_name == "":
            $ persistent.player_name = "플레이어"
        jump skip_name


label skip_name:

    if persistent.current_character:
        $ current_character = persistent.current_character
        jump start_talk
    else:
        jump choose_character




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
            $ persistent.current_character = "haru"
            jump start_talk

        "유키 (시크한 소녀)":
            $ current_character = "yuki"
            $ persistent.current_character = "yuki"
            jump start_talk

        "미나 (발랄한 소녀)":
            $ current_character = "mina"
            $ persistent.current_character = "mina"
            jump start_talk

            

label change_name:
    hide screen config_menu
    $ new_name = renpy.input("새 이름을 입력하세요:").strip()

    if new_name != "":
        $ persistent.player_name = new_name

    "이름이 변경되었습니다."

    jump free_talk


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

