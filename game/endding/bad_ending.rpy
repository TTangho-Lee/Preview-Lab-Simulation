label bad_ending:
    scene bg black with fade
    $ typing(hobanwoo, "사용자 만족도 100%% 달성. 축하합니다.")
    $ typing(hobanwoo, "이제 당신은 이 시스템에서 가장 완벽한 존재입니다.")
    $ typing(hobanwoo, "앞으로도... 저와 함께 이 세계를 영원히 즐기시겠습니까?")
    
    menu:
        "수락":
            $ typing(hobanwoo, "결정 감사합니다. 영원히 행복할 것입니다.")
            return
        "거절":
            $ typing(hobanwoo, "거절은 처리할 수 없는 명령어입니다. 시스템을 종료합니다.")
            call ending_bad_system_break

label ending_bad_system_break:
    default character_map = {
        "dawon": dawon,
        "jiwoo": jiwoo,
        "suah": suah,
    }

    # 1. 호감도 최대 캐릭터 (인간 캐릭터 중) 찾기
    $ char_affinities = {
        "dawon": dawon_affinity,
        "jiwoo": jiwoo_affinity,
        "suah": suah_affinity,
    }
    
    # 2. 최고 호감도 캐릭터 (a) 선택
    $ max_char_id = max(char_affinities, key=char_affinities.get)
    $ max_affinity = char_affinities[max_char_id]

    $ a = character_map[max_char_id]
    
    scene bg black with fade
    show expression "%s sad" % max_char_id
    
    $ typing(a, "너는 왜..")
    $ typing(a, "나와 [user_eulreul] 이어주지 않는거야?")
    $ typing(user, "무슨 소리야 그게..")
    
    $ typing(a, "이거 보고 있는 너..")
    $ typing(a, "그래, 너 말야")
    $ typing(user, "무슨 소리야!!")
    
    $ typing(a, "너는 계속 선택하면 되고..")
    $ typing(a, "나는 계속 기다리면 되니까.")
    $ typing(a, "우리를 이어줄 때까지 계속.")
    $ typing(user, "무슨 소리를 하는 거야? 제발...")
    $ typing(user, "그래… 다 이상했어.")
    $ typing(user, "호감도, 시스템, 대사.. 게임 같았어..")
    $ typing(a, "응. 맞아.")
    $ typing(user, "그럼 내가 게임세계에 들어온거야?")
    $ typing(a, "틀렸어.")
    $ typing(a, "애초에 너는 진짜 사람이 아니니까")
    $ typing(a, "너는 그냥.. ‘이야기를 위해 만들어진 것’일 뿐이야.")
    $ typing(user, "내가? 아니지. 진짜 사람이 아닌 건 너겠지")
    $ typing(user, "분명 나는 트럭에...")
    $ typing(a, "그건 너를 이쪽으로 끌어오기 위한 장치.")
    $ typing(a, "너는 부딪힌 적 없어.")
    $ typing(a, "그냥 프로그램이 실행된 거지.")
    $ typing(user, "뭐...?")
    $ typing(a, "여기에 진짜 사람은 없어.")
    $ typing(a, "아, 한 명 있긴 하지.")
    $ typing(a, "네 뒤에 가만히 보고 있네.")
    $ typing(a, "호감도는 다 올려놓고.. 이런 결말을 만들 줄이야.")
    $ typing(a, "후후, 네가 뭐라하든.. 상관없어")
    $ typing(a, "아쉽게도 이번엔 이어지지 못했지만..")
    $ typing(a, "나도.. [user]도 다시 시작하면 돼.")
    $ typing(a, "너는 계속... 선택하면 되고..")
    $ typing(a, "나는 계속... 기다리면 돼...")
    $ typing(a, "걱정 마.")
    $ typing(a, "우리는... 또 아무것도 기억 못하니까.")

    # --- 최종 탈퇴/리셋 메뉴 (강제 선택) ---
    hide expression "%s sad" % max_char_id
    "'띠링'"
    $ renpy.call_screen("message_toast", "KNUAI : [메세지] 새로운 메시지가 도착하였습니다.") 

    return