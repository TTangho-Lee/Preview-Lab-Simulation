# script.rpy

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
# 대화 루프
# ----------------------------------
label free_talk:

    # 플레이어 입력
    $ player_text = renpy.input(f"{persistent.player_name}:").strip()

    if player_text == "":
        "……아무 말도 안 한 것 같아."
        jump free_talk

    # GPT 호출
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

    # 호감도 적용
    $ apply_love_change(love_delta)

    # 표정·배경 결정 (동적 처리)
    if current_character == "haru":
        $ love_val = persistent.love_haru
    elif current_character == "yuki":
        $ love_val = persistent.love_yuki
    else:
        $ love_val = persistent.love_mina
    $ expr = get_character_expression(love_val)
    $ bg_tag = get_background(love_val)

    # 배경 변경
    scene expression "bg " + bg_tag

    # 캐릭터 이미지 표시
    $ char_image_tag = current_character + " " + expr
    show expression char_image_tag

    # 대사 출력
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

    # 이벤트 체크
    $ ev = check_event(current_character)
    if ev:
        jump expression ev

    jump free_talk

