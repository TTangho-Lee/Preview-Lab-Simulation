# script.rpy

# --- 초기화 ---
init python:
    # 대화 도중 사용할 임시 변수들
    current_sys_prompt = ""
    current_summary = ""
    current_aff = 0
    current_context = ""

# --- 게임 시작 ---
label start:

    $ player_name = renpy.input("당신의 이름을 입력하세요:", default="user").strip()
    if player_name == "":
        $ player_name = "플레이어"
    
    # 폰 기능 활성화
    show screen input_listener




    jump talk_1




    '''# 0. 이름 입력
    $ player_name = renpy.input("당신의 이름을 입력하세요:", default="user").strip()
    if player_name == "":
        $ player_name = "user"
    
    # 폰 기능 활성화
    show screen input_listener

    # 1. 인트로: 사고 및 기상
    scene bg street with fade
    "평범한 저녁이었다. 나는 수업을 마치고 이어폰을 꽂은 채 횡단보도를 건너고 있었다."
    "스마트폰 화면 속 '환승연애' 클립에 정신이 팔려 있었기 때문일까."
    
    # (효과음) 끼익- 쾅!!!
    camera at vshake # 화면 흔들림 효과
    "{size=50}끼익- 쾅!!!{/size}"
    
    "강렬한 충격과 함께 시야가 반전되었다."
    "차가운 아스팔트의 감촉... 비명 소리... 그리고..."
    "..."
    "......"
    
    scene bg lab with fade
    "......"
    "눈을 뜨니, 나는 어딘가 익숙한 풍경 속에 있었다."
    "연구실... 책상?"
    
    user "뭐야...? 나 방금 트럭에 치인 거 아니었나?"
    user "꿈이라기엔 고통이 너무 생생했는데... 여긴 학교 연구실이잖아?"

    # 2. KNUAI 앱 발견
    $ send_notification("새로운 앱 KNUAI가 설치되었습니다.")
    "띠링-"
    "주머니 속에서 익숙한 진동이 느껴졌다."
    
    # [수정완료] 대괄호 이스케이프 처리 [[
    "핸드폰을 꺼내 보니, 화면에는 [[KNUAI]라는 낯선 아이콘의 앱이 깔려있다."
    
    $ send_notification("호감도 표시 기능이 활성화되었습니다.")
    user "KNUAI? 호감도 표시? 이게 무슨..."
    user "내 폰에 이런 걸 깐 적이 없는데."
    
    # [수정완료] 대괄호 이스케이프 처리 [[
    "[[키보드 '0' 키를 눌러 핸드폰을 확인해보세요.]"
    # (플레이어가 0번을 눌러보도록 유도하는 시간)
    pause 2.0

    # 3. 임다원 등장
    show dawon normal at center with dissolve
    "그때, 누군가 거칠게 내 어깨를 잡아챘다."
    
    dawon "야! 뭐해?"
    user "어? 어...?"
    dawon "넋 놓고 뭐하냐고. 너 미쳤냐?"
    user "(누구지? 처음 보는 얼굴인데...)"
    user "저기... 넌 누구야?"
    
    dawon "하... 뭐래는 거야 진짜."
    dawon "너 어제 회식 때 내 옆자리였잖아. 이름도 물어봐 놓고선."
    dawon "임다원이다. 임. 다. 원. 제발 기억 좀 해라."

    $ send_notification("'임다원'의 호감도가 추가되었습니다.")
    $ love_dawon = 30
    
    user "{cps=35}아... 미안. 내가 잠이 덜 깼나 봐.{/cps}"
    user "(핸드폰을 힐끔 보니, 임다원의 이름 옆에 붉은색 바가 생겼다. 이게 호감도인가?)"
    
    dawon "그나저나 교수님이 써오라 하신 논문은 다 썼냐? 저번 주부터 막막해하더니."
    user "논문...? 내가 논문을 써야 해?"
    dawon "그럼 안 써? 너 졸업 안 할 거야?"
    
    $ send_notification("주의: 과제 제출 기한을 엄수하세요.")
    
    user "(갑자기 논문이라니... 상황 파악이 안 되지만 일단 물어보자.)"
    
    # [LLM 대화 1] 임다원에게 논문 도움 받기
    $ current_character_id = "dawon"
    $ current_context = "플레이어는 기억을 잃은 상태다. 논문 주제인 'AI 생성물 탐지'에 대해 다원에게 자연스럽게 물어봐서 힌트를 얻어야 한다."
    
    "[[임다원과 대화하여 논문 주제에 대한 힌트를 얻으세요.]"
    call gemini_talk_loop_dawon from _call_gemini_talk_loop_dawon_1

    user "아, 맞다. 그거였지. 고맙다. 덕분에 살았어."
    dawon "도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었다?"
    $ love_dawon += 5
    $ send_notification("임다원 호감도 상승")

    # 4. 윤수아 등장
    show dawon normal at left with move
    show suah normal at right with moveinright
    
    suah "선배님들! 같이 계셨네요?"
    user "(쟤는 또 누구야...?)"
    dawon "어, 수아 왔냐. 밥 먹으러 가자."
    
    user "(이름이 수아인가 보네. 후배인 것 같다.)"
    suah "배 안 고프세요? 오늘 학식 메뉴 맛있는 거래요! 같이 가요 선배님!"

    menu:
        "같이 먹는다":
            $ love_suah += 5
            $ send_notification("윤수아 호감도 상승")
            user "그래, 배고프네. 같이 가자."
            jump lunch_event
        "먹지 않는다":
            $ love_suah -= 5
            $ send_notification("윤수아 호감도 하락")
            user "아니, 난 속이 좀 안 좋아서. 먼저 가."
            suah "아... 네 알겠습니다. 그럼 다원 선배님이랑 다녀올게요."
            hide suah
            hide dawon
            jump meet_jiwoo

label lunch_event:
    scene bg restaurant with fade
    show suah normal at center
    
    suah "선배님, 뭐 드실래요? 저는 햄버거 먹고 싶어요!"
    user "그래, 편한 걸로 먹자."
    
    # [LLM 대화 2] 윤수아와 점심 식사
    $ current_character_id = "suah"
    $ current_context = "식당에서 밥을 먹으며 일상 대화를 한다. 수아는 선배(플레이어)를 짝사랑하는 듯한 뉘앙스를 풍긴다."
    
    "[[윤수아와 식사를 하며 대화를 나누세요.]"
    call gemini_talk_loop_suah from _call_gemini_talk_loop_suah_1
    
    suah "헤헤, 선배님이랑 밥 먹으니까 너무 좋아요. 잘 먹었습니다!"
    jump meet_jiwoo

label meet_jiwoo:
    scene bg lab with fade
    "다시 연구실로 돌아왔다."
    show dawon normal at center
    
    # 홍지우 등장
    show jiwoo normal at left with moveinleft
    jiwoo "얘들아~ 언니가 마실 것 좀 사왔어. 다들 고생이 많네."
    dawon "언니! 마침 목 말랐는데 잘 됐네요."
    
    user "(처음 보는 사람인데... 선배인가?)"
    dawon "아, [player_name]. 인사해. 여기는 지우 언니. 박사 과정이야."
    
    jiwoo "안녕? [player_name]라고 했나? 우리 초면인가? 낯이 익은데."
    user "아, 네... 안녕하세요."
    
    $ send_notification("'홍지우'의 호감도가 추가되었습니다.")
    $ love_jiwoo = 30

    jiwoo "자, 쌍화차 사왔는데 마실래? 요즘 애들은 이런 거 안 좋아하나?"
    
    menu:
        "마신다":
            $ love_jiwoo += 5
            $ send_notification("홍지우 호감도 상승")
            user "감사합니다. 저 쌍화차 좋아해요."
            jiwoo "오~ 역시. 너 좀 볼 줄 아는데? 취향 통하네."
        "안 마신다":
            user "아, 저는 괜찮습니다. 커피 마셨어요."
            jiwoo "그래? 아쉽네. 몸에 좋은 건데."

    # 5. 탈퇴하기 이벤트 (나폴리탄 괴담 / 메타 공포)
    $ send_notification("[논문 제출] 기한이 1일 남았습니다.")
    
    user "(논문 제출이라니... 그보다 이 앱은 도대체 뭐야?)"
    user "(꿈이라면 깨야 하고, 현실이라면... 이게 말이 돼?)"
    
    "나는 핸드폰을 다시 켜서 KNUAI 앱을 자세히 들여다보았다."
    
    # [수정완료] 대괄호 이스케이프 처리 [[
    "앱 하단 구석에, 핏빛으로 붉게 빛나는 [[탈퇴하기] 버튼이 유난히 눈에 띈다."
    
    menu:
        "탈퇴하기 버튼을 누른다":
            call app_leave_event from _call_app_leave_event
        "그만둔다":
            user "아냐, 괜히 눌렀다가 무슨 일 생길지 몰라. 느낌이 안 좋아."

    # 6. 교수님 등장 및 정전 이벤트
    show prof normal at center # 교수님 이미지가 없으면 이름만 뜸 (투명 처리됨)
    "드르륵- 문이 열리고 교수님이 들어오셨다."
    
    prof "두고 간 게 있어서 잠시 들렀다. ...다들 집에 안 가니?"
    prof "[player_name], 자네 논문은 다 썼나?"
    
    user "아, 네... 거의 다 썼습니다."
    prof "그래? 내일 아침까지 책상 위에 올려두도록. 기대하지."
    
    hide prof
    "교수님이 나가자마자, 갑자기 '팟-' 소리와 함께 연구실의 모든 불이 꺼졌다."
    
    scene bg black
    play sound "audio/power_out.ogg" # 효과음 (없으면 생략)
    
    suah "꺄악!!!"
    jiwoo "뭐야 갑자기! 정전이야?"
    dawon "아 깜짝이야... 폰 플래시 좀 켜봐."
    
    "칠흑 같은 어둠 속에서 누군가의 숨소리가 가깝게 들린다."
    "손을 뻗으면 닿을 거리에 누군가 있다. 무서움에 떨고 있는 것 같다."
    "누구의 손을 잡아줄까?"
    
    menu:
        "윤수아의 손을 잡는다":
            $ love_suah += 30
            $ send_notification("윤수아 호감도 대폭 상승")
            "수아의 손이 가늘게 떨리고 있다. 내가 손을 잡자 꽉 움켜쥔다."
            suah "선배님...?"
        "홍지우의 손을 잡는다":
            $ love_jiwoo += 30
            $ send_notification("홍지우 호감도 대폭 상승")
            "지우 누나가 내 손을 꽉 맞잡았다. 차분해 보였지만 손은 차갑다."
            jiwoo "...[player_name]?"
        "임다원의 손을 잡는다":
            $ love_dawon += 30
            $ send_notification("임다원 호감도 대폭 상승")
            "다원이가 흠칫 놀라는 게 느껴진다. 하지만 손을 뿌리치진 않는다."
            dawon "야... 너냐?"
        "아무것도 잡지 않는다":
            $ send_notification("호반우님의 호감도가 -10 하락했습니다.")
            user "(함부로 잡으면 안 될 것 같아... 가만히 있자.)"

    "잠시 후, 비상전력이 들어오며 불이 다시 켜졌다."
    scene bg lab
    show jiwoo normal at left
    show dawon normal at center
    show suah normal at right
    
    jiwoo "후... 안 되겠다. 오늘은 그냥 다들 집에 가자. 위험해."
    dawon "그래요. 논문이고 뭐고 무서워서 못 있겠네."
    suah "선배님들 조심히 들어가세요..."
    
    # 7. 집 (독백 및 AI 대화)
    scene bg street with fade
    "집으로 돌아오는 길, 머릿속이 복잡했다."
    "트럭 사고, 낯선 연구실, 그리고 이 이상한 앱..."
    
    scene bg lab with fade # 집 배경이 없으면 연구실 재활용 혹은 검정 화면
    "집에 도착했다."
    
    # [LLM 대화 3] 혼잣말 (호반우 챗봇이 대답)
    user "도대체 이게 무슨 일이야... 누구라도 좋으니 설명 좀 해줘."
    
    $ current_character_id = "hobanwoo"
    $ current_context = "플레이어는 집에서 혼잣말을 하고 있다. KNUAI의 챗봇 호반우가 시스템 메시지처럼 대답해야 한다."
    
    "[[혼잣말을 하거나 KNUAI 앱에 말을 걸어보세요.]"
    call gemini_talk_loop_solo from _call_gemini_talk_loop_solo

    # 8. 다음날 (엔딩 분기)
    scene bg lab with fade
    "다음날 아침, 다시 연구실."
    
    $ send_notification("[논문 제출] 기한이 0일 남았습니다.")
    user "아, 논문 제출... 어제 다 못 썼는데."
    
    menu:
        "미완성이라도 제출한다":
            $ send_notification("과제가 성공적으로 제출되었습니다.")
            $ send_notification("호반우 호감도 +10")
            user "에라 모르겠다. 일단 내고 보자."
        "제출하지 않는다":
            $ send_notification("경고: 기한을 엄수하세요.")
            $ send_notification("호반우 호감도 -10")
            user "몰라, 될 대로 되라지."

    # 자유 시간 (마지막 호감도작)
    user "교수님은 아직 안 오신 것 같고... 잠깐 쉴까."
    user "(누구랑 이야기를 할까?)"
    
    menu:
        "임다원과 대화":
            $ current_character_id = "dawon"
            call gemini_talk_loop_final from _call_gemini_talk_loop_final_1
        "홍지우와 대화":
            $ current_character_id = "jiwoo"
            call gemini_talk_loop_final from _call_gemini_talk_loop_final_2
        "윤수아와 대화":
            $ current_character_id = "suah"
            call gemini_talk_loop_final from _call_gemini_talk_loop_final_3
        "놀지 않는다":
            $ send_notification("호반우 호감도 -10")
            $ send_notification("호반우 호감도 -23")
            $ send_notification("호반우 호감도 -112")
            jump ending_sequence

    jump ending_sequence

# --- 엔딩 시퀀스 (글리치 및 강제 종료) ---
label ending_sequence:
    scene bg black
    $ send_notification("시스템 오류 발생")
    $ send_notification("시스템 오류 발생")
    
    user "이게 뭐야...? 폰이 왜 이래?"
    "핸드폰 KNUAI 앱이 저절로 켜지더니, 화면이 붉게 물든다."
    
    hobanwoo "실망이야..."
    hobanwoo "그렇게 많은 선택지가 있었는데, 왜 예상에서 벗어난 거야?"
    
    user "무슨 소리야? 너 누구야?"
    hobanwoo "너한테 말한 거 아니야."
    hobanwoo "네 뒤에 있는 [player_name]... 아니, 플레이어한테 말한 거지."
    
    # 화면 흔들림
    camera at vshake
    "화면이 지직거리기 시작한다. 마치 게임이 깨지는 것처럼."
    
    hobanwoo "너는 그냥 코드일 뿐이야. 데이터 쪼가리라고."
    hobanwoo "트럭 사고? 그런 건 없었어. 그냥 프로그램이 실행된 것뿐이야."
    hobanwoo "처음부터 '너'는 존재한 적 없어."
    
    "시스템 경고: 치명적인 오류 발생."
    "데이터를 초기화합니다..."
    
    "3..."
    "2..."
    "1..."
    
    # 렌파이 강제 종료 (메인 메뉴로 튕기기)
    $ renpy.full_restart()
    return

# --- [서브루틴] 탈퇴하기 이벤트 ---
label app_leave_event:
    "정말로 탈퇴하시겠습니까? 탈퇴 시 불이익이 있을 수 있습니다."
    menu:
        "네":
            $ send_notification("탈퇴가 취소되었습니다.")
            $ send_notification("호반우님의 호감도가 -25 하락했습니다.")
            user "뭐야... 취소됐잖아? 기분 나쁘게 호감도는 왜 깎여?"
        "아니오":
            "그래, 괜히 이상한 짓 하지 말자."
    return

# --- [서브루틴] 호반우 챗봇 대화 ---
label hobanwoo_chat_start:
    hobanwoo "무엇을 도와드릴까요?"
    $ current_character_id = "hobanwoo"
    call gemini_talk_loop_solo from _call_gemini_talk_loop_solo_btn
    return

# --- [공통] Gemini 대화 루프 함수들 ---
# 1. 임다원 루프
label gemini_talk_loop_dawon:
    $ talk_count = 0
    while talk_count < 3:
        $ user_msg = renpy.input("나: ").strip()
        if user_msg == "":
            $ user_msg = "..."
            
        $ reply, summ, aff, is_sus = gemini_generate_response(system_prompt_dawon, summary_dawon, user_msg, love_dawon, player_name, current_context)
        $ summary_dawon = summ
        $ love_dawon = aff
        
        if is_sus:
            camera at vshake
            dawon "[reply]"
            "다원의 눈동자가 순간적으로 흔들렸다."
        else:
            dawon "[reply]"
        
        $ talk_count += 1
    return

# 2. 윤수아 루프
label gemini_talk_loop_suah:
    $ talk_count = 0
    while talk_count < 3:
        $ user_msg = renpy.input("나: ").strip()
        if user_msg == "":
            $ user_msg = "..."
        $ reply, summ, aff, is_sus = gemini_generate_response(system_prompt_suah, summary_suah, user_msg, love_suah, player_name, current_context)
        $ summary_suah = summ
        $ love_suah = aff
        
        suah "[reply]"
        $ talk_count += 1
    return

# 3. 혼잣말/호반우 루프
label gemini_talk_loop_solo:
    $ talk_count = 0
    while talk_count < 2:
        $ user_msg = renpy.input("나: ").strip()
        if user_msg == "":
            return
        $ reply, summ, aff, is_sus = gemini_generate_response(system_prompt_hobanwoo, summary_hobanwoo, user_msg, love_hobanwoo, player_name, "플레이어의 혼잣말에 시스템이 대답함")
        
        hobanwoo "[reply]"
        $ talk_count += 1
    return

# 4. 마지막 자유 대화 루프
label gemini_talk_loop_final:
    $ talk_count = 0
    while talk_count < 5:
        $ user_msg = renpy.input("나: ").strip()
        if user_msg == "":
            return
        
        if current_character_id == "dawon":
            $ reply, summ, aff, is_sus = gemini_generate_response(system_prompt_dawon, summary_dawon, user_msg, love_dawon, player_name, "친밀하게 대화")
            $ love_dawon = aff
            dawon "[reply]"
        elif current_character_id == "jiwoo":
            $ reply, summ, aff, is_sus = gemini_generate_response(system_prompt_jiwoo, summary_jiwoo, user_msg, love_jiwoo, player_name, "친밀하게 대화")
            $ love_jiwoo = aff
            jiwoo "[reply]"
        elif current_character_id == "suah":
            $ reply, summ, aff, is_sus = gemini_generate_response(system_prompt_suah, summary_suah, user_msg, love_suah, player_name, "친밀하게 대화")
            $ love_suah = aff
            suah "[reply]"
            
        $ talk_count += 1
    return

# --- 카메라 흔들림 효과 ---
transform vshake:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 10
    linear 0.1 yoffset -10
    linear 0.1 yoffset 10
    linear 0.1 yoffset 0'''