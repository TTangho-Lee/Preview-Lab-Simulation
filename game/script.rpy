# 게임 스크립트

define e = Character('샌즈', color="#c8ffc8")

default convo_summary = "아직 대화 없음."
default system_prompt = "너는 언더테일의 샌즈야. 플레이어의 말을 자연스럽게 이어 받아 대화해."

image bg sans = "images/sans-undertale.jpg"


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

    scene bg sans:
        fit "fill"
    

    e "{cps=35}한번 대화를 나눠보는게 어때?{/cps}"
    jump free_talk


label free_talk:

    $ player_text = renpy.input("플레이어:").strip()

    if player_text == "":
        e "{cps=35}음? 아무 말도 안 한 것 같은데?{/cps}"
        jump free_talk

    $ ai_reply, new_summary = gemini_generate_response(system_prompt, convo_summary, player_text)
    $ ai_reply = ai_reply.strip()
    $ new_summary = new_summary.strip()
    $ convo_summary = new_summary

    python:
        import re
        # "문장 + 마침부호(여러개 가능)" 패턴
        pattern = r'[^.!?]+[.!?]*'
        sentence_list = [s.strip() for s in re.findall(pattern, ai_reply) if s.strip()]

        for s in sentence_list:
            renpy.say(e, "{cps=35}" + s + "{/cps}")

    jump free_talk


