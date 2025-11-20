# scripy.rpy

define e = Character('샌즈', color="#c8ffc8")

# --------------------------
# 저장될 값들 (persistent 사용)
# --------------------------
default persistent.love = 30                     # 호감도
default persistent.dialog_history = []           # 최근 3개 대화 저장
default persistent.convo_summary = "아직 대화 없음."
default persistent.talk_count = 0                # 대화 횟수
default system_prompt = "너는 언더테일의 샌즈야. 플레이어의 말을 자연스럽게 이어 받아 대화해."

image bg sans = "images/sans-undertale.jpg"


# --------------------------
# UI : 오른쪽에 호감도 바 고정
# --------------------------
screen love_meter():
    frame:
        xalign 1.0
        yalign 0.2
        background "#0008"
        padding (20,20,20,20)
        vbox:
            text "호감도: [persistent.love]" size 22 color "#ffffff"
            bar:
                value persistent.love
                range 100
                xmaximum 200
                ymaximum 20
                left_bar "#ff6688"
                right_bar "#555555"


# --------------------------
# 타자기 효과
# --------------------------
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


# --------------------------
# GPT가 준 love_change 적용 함수
# --------------------------
init python:
    def apply_love_change(delta):
        """
        GPT가 반환한 호감도 변화값 적용
        """
        if delta is None:
            return
        persistent.love = max(0, min(100, persistent.love + delta))


label start:

    show screen love_meter

    scene bg sans:
        fit "fill"

    e "{cps=35}한번 대화를 나눠보는게 어때?{/cps}"
    jump free_talk


label free_talk:

    $ player_text = renpy.input("플레이어:").strip()

    if player_text == "":
        e "{cps=35}음? 아무 말도 안 한 것 같은데?{/cps}"
        jump free_talk

    # GPT 호출 → ai_reply, love_delta, new_summary
    $ ai_reply, love_delta, new_summary = gemini_generate_response(system_prompt, persistent.convo_summary, player_text)

    # 요약 업데이트
    $ persistent.convo_summary = new_summary

    # 대화 횟수 증가
    $ persistent.talk_count += 1

    # 최근 대화 업데이트
    $ persistent.dialog_history.append(f"Player:{player_text} / Sans:{ai_reply}")
    $ persistent.dialog_history = persistent.dialog_history[-3:]

    # GPT가 준 호감도 변화 적용
    $ apply_love_change(love_delta)

    # 문장 단위로 샌즈 대사 출력
    python:
        import re
        pattern = r'[^.!?]+[.!?]*'
        sentence_list = [s.strip() for s in re.findall(pattern, ai_reply) if s.strip()]
        for s in sentence_list:
            renpy.say(e, "{cps=35}" + s + "{/cps}")

    # 이벤트 체크
    if persistent.talk_count >= 10 and persistent.love >= 60:
        jump event_1
    if persistent.love >= 90:
        jump event_good_end

    jump free_talk


# --------------------------
# 이벤트 1
# --------------------------
label event_1:
    e "{cps=35}흠… 너랑 대화하는 게 점점 즐거워지네.{/cps}"
    e "{cps=35}이런 말 하는건 좀 낯설지만… 고맙다구.{/cps}"
    return


# --------------------------
# 호감도 90 이상 엔딩
# --------------------------
label event_good_end:
    e "{cps=35}…이렇게까지 될 줄은 몰랐는데.{/cps}"
    e "{cps=35}너랑 얘기하는 시간이… 솔직히 정말 좋았어.{/cps}"
    e "{cps=35}앞으로도… 계속 대화해줄거지?{/cps}"
    return
