label talk_4:
    # --- 1. 시간 경과 및 강제 알림 ---
    scene bg black with fade
    "시간이 흐른다."
    play sound "audio/notification.ogg"
    "'띠링'"
    $ send_notification("[메시지] 새로운 메시지가 도착하였습니다.")
    $ send_notification("[논문 제출] 제출 기한이 1일 남았습니다.")
    $ typing(user, "구라, 논문 제출이 하루 남았다고?")
    $ typing(user, "애초에 여기도 꿈인지 현실인지.. 아무튼, 이세계든 뭐든, 내가 살던 곳이 아닌 건 맞잖아.")
    $ typing(user, "잠시만 KNUAI 앱...")
    

    # --- 2. KNUAI 앱 진입 및 탈퇴 버튼 강조 ---
    "휴대폰을 열어 KNUAI 앱에 들어간다."
    show screen phone_overlay
    "왜인지 **[[탈퇴하기]** 버튼이 유난히 눈에 띄었다."
    $ exit_pressed = renpy.call_screen("phone_overlay")
    if exit_pressed:
        jump event_4


    # --- 3. 탈퇴 선택지 이벤트로 이동 ---
    return