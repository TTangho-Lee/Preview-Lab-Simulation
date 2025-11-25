label talk_6:
    $ typing(professor, "... 수고하지")
    "교수님은 밖으로 나가셨다." 
    hide professor
    
    # --- 1. 동료들 재등장 ---
    show jiwoo normal at left
    show suah normal at right
    $ typing(jiwoo, "이쯤하고~ 오늘은 좀 놀까?")
    $ typing(suah, "그니까요! 제가 간식 가져왔어요!") 
    $ typing(user, "그럴까.. 우선 마무리만 좀 할게요")
    $ typing(jiwoo, "그래 우리끼리 놀고 있을게")
    

    # --- 2. 논문 자동 완성 확인 ---
    "'논문.docx' 파일을 클릭하자 이미 논문이 전부 작성되어 있었다." 
    $ typing(user, "(뭐야, 그러면 제출만 하면 되는거였네?)")
    $ typing(user, "다원아 이거 한글 파일로 제출하면 끝이야?")
    $ typing(dawon, "너 진짜 핵심을 찔렀어!")
    $ typing(dawon, "완전 정답이야 ✨ 프린트 해서 직접 드려야 인정돼!")
    $ typing(user, "..?")
    

    # --- 3. 인쇄 선택지 이벤트로 이동 ---
    jump event_6