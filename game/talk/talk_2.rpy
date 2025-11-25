label talk_2: 
    # --- 1. 논문 확인 및 호감도 변화 ---
    "[user_iga] 컴퓨터를 켜서 USB 안의 '논문.docx' 이라고 적힌 파일을 열어본다."
    $ show_center_notice(
        "모바일 디바이스에서 근거리 객체 탐지를 위한",
        "YOLOv8 모델 경량화 연구",
        "",
        "Optimization of YOLOv8 Model for Lightweight",
        "Near-Object Detection on Mobile Devices"
        )
    $ typing(user, "고맙다. 헛고생할 뻔 했네.")
    $ apply_affinity_change("dawon", 1)
    $ typing(dawon, "도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었어 ✨")
    $ send_notification(f"임다원 호감도 +1 (현재: {dawon_affinity})")
    $ typing(user, "이게 오른다고?")
    $ typing(user, "말투는 왜 저래")
    

    # --- 2. 유튜브 대화 (메타 질문 회피) ---
    $ typing(dawon, "뭔데? 뭐 보는데.")
    $ typing(user, "아 어.")
    $ typing(user, "아, 별건 아니고. 유튜브 알림.")
    $ typing(dawon, "뭐? 그게 뭔...")
    

    # --- 3. 윤수아 등장 ---
    "연구실의 문이 열리고 꽃향기를 풍기는 생머리 여자 한 명이 들어온다."
    show suah normal at right with moveinright
    $ typing(suah_blind, "선배님들 같이 계셨네요?")
    "임다원에게 속닥거리며 물어본다."
    $ typing(user, "쟤는 누구야...?")
    $ typing(dawon, "너 이 정도면 기억상실 아니야? 수아잖아, 윤수아.")
    $ apply_affinity_change("suah",30)
    $ typing(user, "아, 그래?")
    $ typing(suah, "배 안고프세요? 곧 저녁시간인데 같이 밥 먹으러 가요!")
    

    # --- 4. 밥 먹기 선택지 이벤트로 이동 ---
    jump event_2