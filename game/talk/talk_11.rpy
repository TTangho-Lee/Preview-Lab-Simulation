label talk_11:
    # --- 1. 교수님 등장 및 분위기 조성 ---
    scene bg lab with fade
    show professor normal at center with moveinright
    "문이 열리고 교수님이 들어오신다. 표정이 오늘따라 유난히 싸늘하다." 
    

    # --- 2. 논문 핵심 질의응답 (LLM 대화 시작) ---
    $ typing(professor, "그래서 [player_name]. 자네가 제출했던 논문, 핵심이 뭐지?")


    jump event_11