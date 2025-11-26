label talk_12:
    # --- 1. 대화 종료 및 퇴장 ---
    $ typing(professor, "...") 
    "교수님은 밖으로 나가셨다." 
    hide professor
    user "하아... 좀 쉴까." 
    

    # --- 2. 휴식 및 대화 상대 선택 (호감도작) ---
    $ typing(user, "(누구한테 물어볼까?)")

    
    jump event_12