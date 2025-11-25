label talk_1:
    # --- 1. 트럭 사고 씬 ---
    scene bg black with fade
    "[user_eunneun] 경북대학교 전자과에 재학 중인 3학년."
    "저녁 수업을 마치고 환승연애를 보며 횡단보도를 건너게 된다."
    play sound "audio/truck_horn.ogg"
    with vpunch
    "하지만 빠르게 달려오는 대형트럭을 보지 못한 채 그대로 치인다."
    

    # --- 2. 깨어남 씬 ---
    scene bg lab with dissolve
    "눈을 뜬 [user], 책상에서 엎드린 상태였다."
    $ typing(user, "뭐야, 나 방금 트럭에 치인 거 아니였나?")
    $ typing(user, "꿈이라기엔 너무 생생했는데, 여긴 어디.. 연구실?")


    # --- 3. KNUAI 앱 알림 ---
    "‘띠링’"
    play sound "audio/notification.ogg"
    $ send_notification("[메시지] 새로운 메시지가 도착하였습니다.")
    "휴대폰의 알람이 울렸다. [user_iga] 이 낯선 장소로 오기 전의 본인의 휴대폰과 정확히 일치했다."
    "하지만 새로운 앱 **KNUAI**가 설치되어 있었다."
    show screen phone_overlay
    $ typing(user, "KNUAI는 뭐지? KNUPiA가 아니고?")
    "글을 확인하는 [user], 새로운 글에는 'KNUAI 사용 유의사항'이 적혀있었다."
    "KNUPiA와 똑같은 화면이었지만 하나의 기능이 더 추가되어있었다. **'호감도 표시'**"
    $ typing(user, "호감도 표시는 뭐야 미연시야?ㅋㅋ")
    "호감도 표시 버튼을 눌러본다."
    hide screen phone_overlay
    

    # --- 4. 임다원 등장 ---
    "갑작스럽게 어깨에 손을 대는 누군가."
    play sound "audio/tap_shoulder.ogg"
    show dawon normal at left with moveinright 
    "황급히 뒤를 돌아보니 낯선 여자가 얼굴을 들이밀고 [user_eulreul] 바라보고 있었다."
    $ typing(dawon_blind, "뭐해?")
    $ typing(user, "어? 어")
    $ typing(dawon_blind, "뭐하냐니까.")
    $ typing(user, "그러게..")
    $ typing(dawon_blind, "미쳤니?")
    $ typing(user, "아니 그보다 넌 누군데?")
    $ typing(dawon_blind, "기억을 왜 못해?")
    "[user_eunneun] 갑작스럽게 이곳에 오게 된 것을 이해하지 못했지만, 어떻게든 상황을 파악하려 자연스럽게 대화를 이어가려 한다."
    $ typing(user, "미안 사실은 내가 사람을 잘 기억못해..")
    $ typing(dawon_blind, "우리 어제 연구실 회식 때 옆자리였잖아, 내 이름도 물어봐 놓고선.")
    $ typing(user, "내가 좀 취했었나봐, 이름 좀 ...")
    $ typing(dawon, "임다원이다.")
    $ apply_affinity_change("dawon",30)


    # --- 5. 두 번째 KNUAI 알림 & 호감도 표시 ---
    "'띠링'"
    play sound "audio/notification.ogg"
    "휴대폰의 알람이 다시 울렸다. 아까 들어간 호감도 표시 버튼을 눌러 들어가진 창에서 알람이 울린 것이다."
    "그 창에는 한 사람의 이름이 추가되어 있었다."
    $ send_notification("**'임다원'**의 호감도를 확인하시겠습니까?")
    $ typing(user, "tlqkf 이게 뭐야")
    $ typing(dawon, "갑자기 왜 욕해?")
    $ typing(user, "아 미안, 약간 감탄사야.")
    "일단 누르고 보는 [user], 버튼을 클릭하자 길다란 막대의 모습이 보였다."
    show screen phone_overlay
    pause 5.0
    hide screen phone_overlay
    

    # --- 6. 논문 대화 ---
    $ typing(dawon, "너 교수님이 써오라 하신 논문, 어떻게 돼 가는데? 저번 주부터 막막해하더니.")
    $ typing(user, "나 논문 써야 해?")
    $ typing(dawon, "그럼 안 써?")
    $ typing(user, "어.. (아니 애초에 지금 이 상황이 이해도 안 되는데)")
    $ typing(user, "(꿈도 아닌 것 같은데, 이 호감도 표시 기능도 말이 안 돼)")
    $ typing(user, "(뭐 이세계?......너무 갔나)")
    

    # --- 7. 나폴리탄 괴담 경고 ---
    "'띠링'"
    $ send_notification("[메시지] 새로운 메시지가 도착하였습니다.")
    "클릭하자 장문의 글이 적혀져 있었다."
    $ show_red_notice(
        "※경북대학교 재학 주의사항",
        "1. 상대방의 호감도를 일정 수준 이하(상) 가지 않도록 항상 유의해 주세요.",
        "2. '과제 및 평가'는 안내된 제출 기한을 엄수하여 제출해 주세요.",
        "{color=#FF5733}3. [hobanwoo_blind]임을 묻지 마세요.{/color}",
        "4. 궁금한 사항은 호반우 챗봇에게 문의해 주세요."
    )
    $ typing(user, "(인스타에서 보던 나폴리맛? 나폴리탄 괴담 그거잖아...)")
    $ typing(user, "제출기한은?")
    $ typing(dawon, "뭐야, 곧 제출인데?")
    $ typing(user, "뭐?")
    $ show_red_notice("2. '과제 및 평가'의 제출 기한을 지켜주세요.")
    $ typing(dawon, "도와줄까?")

    # --- 8. 논문 찾기 대화 이벤트로 이동 ---
    jump event_1