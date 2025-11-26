label talk_10:
    # --- 1. 날짜 변경 및 장소 이동 ---
    "다음날 아침이 밝았다."
    scene bg lab with fade
    "연구실." 
    

    # --- 2. KNUAI 알림 ---
    "띠링"
    $ send_notification("[[메시지] 새로운 메시지가 도착하였습니다.")
    $ show_normal_notice("[[논문 제출] 제출 기한이 0일 남았습니다.")
    $ typing(user, "아 맞다, 논문 제출!")
    $ typing(user, "프린트 해둔게...~")
    
    
    jump event_10