# game/script.rpy

define a = Character('아이린', color="#e6a4b3")

default player_affinity = 0  # 플레이어-캐릭터 호감도
default talk_turns = 0       # 자유 대화 턴 수
default event_flag = 0       # 이벤트 진행 단계
default player_name = "플레이어"
default convo_summary = "아직 대화 없음."
<<<<<<< HEAD
default system_prompt = "너는 플레이어의 말을 경청하고 공감하며 대화하는 친절한 AI 캐릭터 아이린이야. 존댓말을 사용해."
=======
default system_prompt = "너는 언더테일의 샌즈야. 플레이어가 네 친구들을 모두 죽였어. 플레이어의 말을 자연스럽게 이어 받아 대화해."
>>>>>>> parent of d76b14d (샌즈)

image bg default = "images/default_bg.jpg" 

# 타자기 소리 제거 → 단순 출력만 사용
# config.say_menu_text_filter 제거

label start:
    $ player_name = renpy.input("당신의 이름은 무엇인가요?", default="플레이어").strip()
    if not player_name:
        $ player_name = "플레이어"

    scene bg default: 
        fit "fill"

    a "{cps=35}안녕하세요! 저는 아이린이라고 해요. [player_name]님, 무슨 이야기를 해볼까요?{/cps}" 
    jump free_talk

label free_talk:
    if player_affinity >= 50 and talk_turns >= 20 and event_flag == 0:
        jump main_event_1 

    $ player_text = renpy.input("플레이어:").strip()

    if player_text == "":
        a "{cps=35}네? 뭐라고요?{/cps}" 
        jump free_talk

    $ talk_turns += 1

    # Gemini 호출 (API 호출 코드는 그대로 사용)
    $ ai_reply, new_summary, new_affinity = gemini_generate_response(
        system_prompt, convo_summary, player_text, player_affinity, player_name
    )

    $ ai_reply = ai_reply.strip()
    $ new_summary = new_summary.strip()
    $ convo_summary = new_summary
    $ player_affinity = new_affinity

    # 대화 출력 (Python 블록)
    python:
        import re
        pattern = r'[^.!?]+[.!?]*'
        sentence_list = [s.strip() for s in re.findall(pattern, ai_reply) if s.strip()]

        for s in sentence_list:
            renpy.say(a, "{cps=35}" + s + "{/cps}")

    jump free_talk

label main_event_1:
    scene bg cafe
    show a neutral

    $ event_goal_text = """
    당신은 지금 플레이어에게 누군가를 좋아하는데 고백하는 방법을 모르겠다고 솔직하게 고민을 털어놓고 조언을 구해야 합니다.
    목표: 좋아하는 사람에게 고백하는 방법에 대한 플레이어의 구체적이고 현실적인 조언을 얻는 것.
    """
    $ event_progress_sub = 0

    a "저... [player_name]님께 물어볼 게 있는데..." 
    a "사실... 좋아하는 사람이 생겼어요. 근데 어떻게 해야 할지 모르겠어요."
    a "[player_name]님이라면 어떻게 하실 것 같아요? 혹시 조언 좀 해줄 수 있을까요?"

    label event_free_talk_loop_1:
        if event_progress_sub >= 1:
            jump event_end_1

        $ player_text = renpy.input("플레이어의 조언은?:").strip()
        if player_text == "":
            a "응? 플레이어님의 생각을 말해 주셔도 괜찮아요." 
            jump event_free_talk_loop_1

        $ ai_reply, new_summary, new_affinity = gemini_generate_response(
            system_prompt, convo_summary, player_text, player_affinity, player_name, event_goal_text
        )
        $ convo_summary = new_summary
        $ player_affinity = new_affinity

        python:
            import re
            pattern = r'[^.!?]+[.!?]*'
            sentence_list = [s.strip() for s in re.findall(pattern, ai_reply) if s.strip()]

            for s in sentence_list:
                renpy.say(a, "{cps=35}" + s + "{/cps}")

        jump event_free_talk_loop_1

label event_end_1:
    show a happy 
    a "고마워. 네 조언대로 한번 시도해 봐야겠어!" 
    $ event_flag = 1
    jump free_talk
