label happy_ending:
    # 1. 호감도 최대 캐릭터 (인간 캐릭터 중) 찾기
    $ char_affinities = {
        "dawon": dawon_affinity,
        "jiwoo": jiwoo_affinity,
        "suah": suah_affinity,
    }
    
    # 2. 최고 호감도 캐릭터 (a) 선택
    $ max_char_id = max(char_affinities, key=char_affinities.get)
    $ max_affinity = char_affinities[max_char_id]

    if max_char_id == "dawon":
        show dawon shy
        $ typing(dawon, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show dawon love
        $ typing(dawon, "...좋아")
        scene bg sunset with dissolve
        "해가 내려가고 하늘이 파랗게 물든 시간"
        "(다원은 [player_name]에게 팔짱을 낀다.)"
        $ typing(dawon, "너랑 이런 사이가 되어서.. 정말 좋아해")
        return

    elif max_char_id == "jiwoo":
        show jiwoo shy
        $ typing(jiwoo, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show jiwoo love
        $ typing(jiwoo, "...좋아")
        scene bg sunset with dissolve
        "해가 내려가고 하늘이 파랗게 물든 시간"
        "(지우는 [player_name]에게 팔짱을 낀다.)"
        $ typing(jiwoo, "너랑 이런 사이가 되어서.. 정말 좋아해")
        return

    elif max_char_id == "suah":
        show suah shy
        $ typing(suah, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show suah love
        $ typing(suah, "...좋아")
        scene bg sunset with dissolve
        "해가 내려가고 하늘이 파랗게 물든 시간"
        "(수아는 [player_name]에게 팔짱을 낀다.)"
        $ typing(suah, "너랑 이런 사이가 되어서.. 정말 좋아해")
        return

    