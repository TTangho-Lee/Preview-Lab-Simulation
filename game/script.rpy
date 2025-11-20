# 게임 스크립트

define e = Character('아이린', color="#c8ffc8")

default convo_summary = "아직 대화 없음."
default system_prompt = "너는 상냥하고 감정 표현이 풍부한 소녀 NPC이다. 플레이어의 말을 자연스럽게 이어 받아 대화한다."

# 타자기 효과음 초기화
init python:
    import random
    import re  # 문장 단위 분리용
    TYPE_SOUND = "sfx/type.ogg"

    def typer_filter(what):
        result = ""
        for ch in what:
            renpy.play(TYPE_SOUND, channel="sound")
            renpy.pause(random.uniform(0.015, 0.030))  # 랜덤 속도
            result += ch
        return result

    config.say_menu_text_filter = typer_filter

label start:

    e "{cps=35}이제부터 키보드로 직접 대화할 수 있어!{/cps}"
    jump free_talk


label free_talk:

    $ player_text = renpy.input("말을 입력하세요:").strip()

    if player_text == "":
        e "{cps=35}음? 아무 말도 안 한 것 같은데?{/cps}"
        jump free_talk

    $ ai_reply, new_summary = gemini_generate_response(system_prompt, convo_summary, player_text)
    $ ai_reply = ai_reply.strip()
    $ new_summary = new_summary.strip()
    $ convo_summary = new_summary

    python:
        import re
        sentences = re.split(r'([.!?]\s*)', ai_reply)
        sentence_list = []
        i = 0
        n = len(sentences)
        while i < n-1:
            sentence_list.append(sentences[i] + sentences[i+1])
            i += 2

        for s in sentence_list:
            renpy.say(e, "{cps=35}" + s + "{/cps}")

    jump free_talk

