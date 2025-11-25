'''
갑자기 정전된다. ㅎㅎ
윤수아: 꺄악.~!~!~!~!~~!
홍지우: 갑자기 뭐야!?
임다원: 뭐야...왜 이래...
'''
label talk_7:
    # 논문 확인 후
    
    "갑자기 정전된다. ㅎㅎ" 
    scene bg black with fade
    
    # 캐릭터 이미지 숨기기
    hide dawon
    hide suah
    hide jiwoo
    
    # 대사
    suah "꺄악.~!~!~!~!~~!" 
    jiwoo "갑자기 뭐야!?" 
    dawon "뭐야...왜 이래..."
    
    # 다음 이벤트 (정전 중 선택지)로 점프
    jump event_8