'''
임다원:....
 user:....
연구실에 남아있는 user와 임다원. 각자의 일을하다가 갑자기 문이 열린다.
 ???: 임다원! 언니가 마실것좀 사왔어
임다원: 언니! 
user는 멀뚱멀뚱 쳐다보기만 한다.
???:근데 이 친구는 누구? 처음보는데? 연구실 이번에 들어온거야?
임다원: 응 user라고, 들어온지 얼마 안됐어. 나랑 동갑
???: user 안녕?
 user: 안녕하세요
홍지우: 나는 홍지우라고 해 
user: 안녕하세요 
홍지우: user 있는지 모르고 하나만 사와버렸는데... 이거라도 마실래?
쌍화차
'''
label talk_3:
    # 윤수아와 만난 후
    
    scene bg lab with fade # 배경 유지
    hide suah # 수아는 잠시 퇴장하거나, 이미 퇴장했다고 가정 (필요시 show suah 유지)
    
    # --- 1. 임다원과 단둘이 남음 ---
    dawon "...."
    user "...."
    
    "연구실에 남아있는 user와 임다원. 각자의 일을 하다가 갑자기 문이 열린다."
    
    # --- 2. 홍지우 등장 ---
    # 홍지우 이미지 표시 (jiwoo 캐릭터는 charactor_definition.rpy에 정의되어 있음)
    show jiwoo normal at right with moveinright
    
    jiwoo "임다원! 언니가 마실 것 좀 사왔어."
    dawon "언니!"
    
    "user는 멀뚱멀뚱 쳐다보기만 한다."
    
    # ??? -> jiwoo로 변경
    jiwoo "근데 이 친구는 누구? 처음 보는데? 연구실 이번에 들어온 거야?"
    
    dawon "응 user라고, 들어온 지 얼마 안 됐어. 나랑 동갑."
    
    jiwoo "user 안녕?"
    user "안녕하세요."
    
    # 이름 공개
    jiwoo "나는 홍지우라고 해."
    user "안녕하세요."
    
    # --- 3. 호감도 획득 분기 ---
    jiwoo "user 있는지 모르고 하나만 사와버렸는데... 이거라도 마실래?"
    
    menu:
        "쌍화차를 받는다":
            user "감사합니다. 잘 마실게요."
            $ apply_affinity_change("jiwoo", 2) # 홍지우 호감도 +2
            $ send_notification(f"홍지우 호감도 +2 (현재: {jiwoo_affinity})")
            jiwoo "마시고 힘내!"
            pass
        
        "괜찮다고 거절한다":
            user "괜찮습니다. 마음만 받을게요."
            jiwoo "그래? 알았어. 다음엔 꼭 사다 줄게."
            pass
            
    # 다음 이벤트로 점프
    jump event_3