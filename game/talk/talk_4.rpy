'''
<knuai : [메세지] 새로운 메시지가 도착하였습니다.>
 [논문 제출] 제출 기한이 1일 남았습니다.
 user: (구라, 논문 제출이 하루 남았다고?)
 user: (애초에 여기도 꿈인지 현실인지.. 아무튼, 이세계든 뭐든, 내가 살던 곳이 아닌 건 맞
잖아)
 user: (잠시만 knuai 앱..)
휴대폰을 열어 knuai 앱에 들어간다, 
왜인지 탈퇴하기 버튼이 유난히 눈에 띄었다.
 [탈퇴하기] 버튼을 누르자 “정말로 탈퇴하시겠습니까?” 라는 문구가 뜬다.
'''
label talk_4:
    # 홍지우 등장 후
    
    # --- 1. 시간 경과 및 강제 알림 ---
    scene bg black with fade
    "시간이 흐른다."
    
    # play sound "audio/notification.ogg"
    "‘띠링’"
    
    # 알림 (additional_ui.rpy의 send_notification 함수 활용)
    $ send_notification("[메시지] 새로운 메시지가 도착하였습니다.")
    $ send_notification("[논문 제출] 제출 기한이 1일 남았습니다.")
    
    # 독백
    user "구라, 논문 제출이 하루 남았다고?"
    user "애초에 여기도 꿈인지 현실인지.. 아무튼, 이세계든 뭐든, 내가 살던 곳이 아닌 건 맞잖아."
    user "잠시만 KNUAI 앱..."
    
    # --- 2. KNUAI 앱 진입 및 탈퇴 버튼 강조 ---
    "휴대폰을 열어 KNUAI 앱에 들어간다."
    
    show screen phone_overlay
    
    "왜인지 **[탈퇴하기]** 버튼이 유난히 눈에 띄었다."
    
    # (additional_ui.rpy에 정의된 phone_overlay 화면에 탈퇴하기 버튼이 이미 존재한다고 가정)
    
    # [탈퇴하기] 버튼을 누르는 연출
    "**[탈퇴하기]** 버튼을 누르자 **“정말로 탈퇴하시겠습니까?”** 라는 문구가 뜬다."
    
    # 다음 이벤트로 점프
    jump event_4