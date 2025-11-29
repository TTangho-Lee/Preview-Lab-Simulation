label event_7:
    menu:
        "윤수아의 손을 잡는다":
            $ apply_affinity_change("suah", 5)
            scene bg hand with dissolve
            $ typing(suah, "......")
            jump talk_8

        "홍지우의 손을 잡는다":
            $ apply_affinity_change("jiwoo", 5)
            scene bg hand with dissolve
            $ typing(jiwoo, ".......")
            jump talk_8

        "임다원의 손을 잡는다":
            $ apply_affinity_change("dawon", 5)
            scene bg hand with dissolve
            $ typing(dawon, "......")
            jump talk_8

        "아무것도 잡지 않는다":
            $ apply_affinity_change("hobanwoo",-10)
            jump talk_8
