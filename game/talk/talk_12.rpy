'''
교수님:　...
교수님은 밖으로 나가셨다.
user: 하아...좀 쉴까
'''
label talk_12:
    # --- 1. 대화 종료 및 퇴장 ---
    prof "..." 
    "교수님은 밖으로 나가셨다." 
    hide professor
    
    user_char "하아... 좀 쉴까." 
    
    # --- 2. 휴식 및 대화 상대 선택 (호감도작) ---
    user_char "(누구한테 물어볼까?)"
    jump event_12