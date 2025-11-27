label ending_choice:
    
    # 1. 호감도 최대 캐릭터 (인간 캐릭터 중) 찾기
    $ char_affinities = {
        "dawon": dawon_affinity,
        "jiwoo": jiwoo_affinity,
        "suah": suah_affinity,
    }
    
    # 2. 최고 호감도 캐릭터 (a) 선택
    $ max_char_id = max(char_affinities, key=char_affinities.get)
    $ max_affinity = char_affinities[max_char_id]

    # 3. 최고 호감도 캐릭터에 따른 고백 대사 출력 (대답 없음, 고백만)
    if max_char_id == "dawon":
        # 임다원 고백
        $ typing(dawon, "…야, [player_name].")
        $ typing(dawon, "나… 너 좋아한다. 괜히 빙빙 돌고 싶지도 않고.")
        $ typing(dawon, "됐어, 이 정도면 알아들었겠지.")

    elif max_char_id == "jiwoo":
        # 홍지우 고백
        $ typing(jiwoo, "[player_name], 사실… 계속 말하고 싶었어.")
        $ typing(jiwoo, "나, 너 좋아해. 편해서가 아니라… 마음이 가서.")
        $ typing(jiwoo, "이제는 숨기기 싫다.")

    elif max_char_id == "suah":
        # 윤수아 고백
        $ typing(suah, "선배님… 저… 용기 내서 말할게요.")
        $ typing(suah, "저… 선배님을 좋아해요. 오래전부터요.")
        $ typing(suah, "말하고 나니까… 좀 떨리네요.")

    menu:
        "1. 고백을 받는다":
            jump happy_ending

        "3. 거절한다":
            if max_affinity>=80:
                jump bad_ending
            elif max_affinity>=60:
                jump lab_ending
            else:
                jump normal_ending