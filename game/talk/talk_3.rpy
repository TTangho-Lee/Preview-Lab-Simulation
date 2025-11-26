label talk_3:
    scene bg lab with fade
    hide suah
    

    # --- 1. 임다원과 단둘이 남음 ---
    $ typing(dawon, "....")
    $ typing(user, "....")
    "연구실에 남아있는 [user]와 임다원. 각자의 일을 하다가 갑자기 문이 열린다."
    

    # --- 2. 홍지우 등장 ---
    show jiwoo normal at right with moveinright
    $ typing(jiwoo_blind, "임다원! 언니가 마실 것 좀 사왔어.")
    $ typing(dawon, "언니!")
    "[user_eunneun]는 멀뚱멀뚱 쳐다보기만 한다."
    $ typing(jiwoo_blind, "근데 이 친구는 누구? 처음 보는데? 연구실 이번에 들어온 거야?")
    $ typing(dawon, "응 [user]라고, 들어온 지 얼마 안 됐어. 나랑 동갑.")
    $ typing(jiwoo_blind, "[user] 안녕?")
    $ typing(user, "안녕하세요.")
    $ typing(jiwoo, "나는 홍지우라고 해.")
    $ apply_affinity_change("jiwoo",30)
    $ typing(user, "안녕하세요.")
    
    
    # --- 3. 호감도 획득 분기 ---
    $ typing(jiwoo, "[user] 있는지 모르고 하나만 사와버렸는데... 이거라도 마실래?")
    

    # --- 4. 쌍화차 먹기 선택지 이벤트로 이동 ---
    jump event_3