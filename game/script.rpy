# game/script.rpy

# 게임 스크립트
define a = Character('아이린', color="#e6a4b3")

default player_affinity = 0  # 1. 플레이어-캐릭터 호감도 (0부터 시작)
default talk_turns = 0       # 2. 자유 대화 턴 수 카운터
default event_flag = 0       # 3. 현재 진행된 메인 이벤트 단계 (0: 이벤트 시작 전)
default player_name = "플레이어"
default convo_summary = "아직 대화 없음."
default system_prompt = "너는 플레이어의 말을 경청하고 공감하며 대화하는 친절한 AI 캐릭터 아이린이야. 존댓말을 사용해."
image bg default = "images/default_bg.jpg" 

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
    $ player_name = renpy.input("당신의 이름은 무엇인가요?", default="플레이어").strip()

    if not player_name:
        $ player_name = "플레이어"

    scene bg default: 
        fit "fill"
    
    # [수정] %s 대신 [player_name] 사용
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

    $ ai_reply, new_summary, new_affinity = gemini_generate_response(
        system_prompt, convo_summary, player_text, player_affinity, player_name
    )
    
    $ ai_reply = ai_reply.strip()
    $ new_summary = new_summary.strip()
    $ convo_summary = new_summary
    $ player_affinity = new_affinity

    # [수정] 대화 출력 로직: ai_reply 변수를 renpy.say로 출력하기 위해 python 블록에서 처리
    python:
        import re
        
        # AI 답변에 cps 태그 추가
        display_text = "{cps=35}" + ai_reply + "{/cps}"
        
        # 문장 단위 분리 (기존 로직)
        pattern = r'[^.!?]+[.!?]*'
        sentence_list = [s.strip() for s in re.findall(pattern, display_text) if s.strip()]

        for s in sentence_list:
            renpy.say(a, s) # renpy.say를 사용해 출력

    jump free_talk


label main_event_1:
    
    # 1. 배경/분위기 설정
    scene bg cafe
    show a neutral 
    
    # 2. 이벤트 목표 정의 (Gemini에게 전달될 핵심 지시)
    $ event_goal_text = """
    당신은 지금 플레이어에게 누군가를 좋아하는데 고백하는 방법을 모르겠다고 솔직하게 고민을 털어놓고 조언을 구해야 합니다.
    당신의 목표는: '좋아하는 사람에게 고백하는 방법'에 대한 플레이어의 구체적이고 현실적인 조언을 얻는 것입니다.
    당신의 고민을 플레이어에게 말하고, 플레이어의 답변에 적극적으로 질문하며 조언을 유도하세요.
    """
    $ event_progress_sub = 0 

    # 3. 이벤트 시작을 알리는 렌파이 스크립트 대사 (캐릭터 'a' 사용)
    # [수정] %s 대신 [player_name] 사용
    a "저... [player_name]님께 물어볼 게 있는데..." 
    a "사실... 좋아하는 사람이 생겼어요. 근데 어떻게 해야 할지 모르겠어요."
    a "[player_name]님이라면 어떻게 하실 것 같아요? 혹시 조언 좀 해줄 수 있을까요?"
    
    # 4. 반자유 대화 루프 시작
    label event_free_talk_loop_1:

        # 이벤트가 끝났는지 (조언을 충분히 얻었는지) 체크
        if event_progress_sub >= 1:
            jump event_end_1
        
        # 플레이어 입력 받기
        $ player_text = renpy.input("플레이어의 조언은?:").strip()

        if player_text == "":
            a "응? 플레이어님의 생각을 말해 주셔도 괜찮아요." 
            jump event_free_talk_loop_1
            
        # 5. AI 호출 (event_goal과 player_name 전달)
        $ ai_reply, new_summary, new_affinity = gemini_generate_response(
            system_prompt, 
            convo_summary, 
            player_text, 
            player_affinity,
            player_name, 
            event_goal_text 
        )
        $ convo_summary = new_summary
        $ player_affinity = new_affinity
        
        # AI 답변 출력 (Python 블록으로 처리)
        python:
            display_text = "{cps=35}" + ai_reply + "{/cps}"
            pattern = r'[^.!?]+[.!?]*'
            sentence_list = [s.strip() for s in re.findall(pattern, display_text) if s.strip()]

            for s in sentence_list:
                renpy.say(a, s) 

        jump event_free_talk_loop_1
        
label event_end_1:
    
    # 조언을 받아 기분이 좋아지거나 용기를 얻은 후의 연출
    show a happy 
    a "고마워. 네 조언대로 한번 시도해 봐야겠어!" 
    
    # 이벤트 종료 후 플래그 업데이트
    $ event_flag = 1 
    
    # 다시 일상 자유 대화로 복귀
    jump free_talk