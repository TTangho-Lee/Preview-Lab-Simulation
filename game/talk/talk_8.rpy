'''
정전되었던 불이 다시 켜진다.
윤수아: 뭐,뭐죠?
임다원: 원래 정전이 이렇게 갑자기 오는 거야?
홍지우: 심장 떨어지는 줄 알았네...
홍지우: 그냥... 오늘은 집으로 돌아가는게 좋겠어..
'''
label talk_8:
    # 정전 중 선택지 (이전 이벤트에서 선택 후 여기로 돌아왔다고 가정)
    
    # (이전 스크립트에서 정전 중 손잡기 선택 후 호감도 변화 발생)
    
    "정전되었던 불이 다시 켜진다."
    scene bg lab with fade
    
    # 캐릭터 이미지 재표시 (수동으로 다시 show 해줘야 합니다)
    show dawon normal at center
    show suah normal at right
    show jiwoo normal at left
    
    suah "뭐,뭐죠?"
    dawon "원래 정전이 이렇게 갑자기 오는 거야?" 
    jiwoo "심장 떨어지는 줄 알았네..." 
    
    jiwoo "그냥... 오늘은 집으로 돌아가는게 좋겠어.." 
    
    jump event_8 # 새로운 라벨로 가정