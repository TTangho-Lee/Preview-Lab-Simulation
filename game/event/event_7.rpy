label event_7:

    menu:
        "윤수아의 손을 잡는다":
            $ apply_affinity_change("suah", 30)
            suah "{cps=[text_speed]}......{/cps}"
            jump talk_8

        "홍지우의 손을 잡는다":
            $ apply_affinity_change("jiwoo", 30)
            jiwoo "{cps=[text_speed]}.......{/cps}"
            jump talk_8

        "임다원의 손을 잡는다":
            $ apply_affinity_change("dawon", 30)
            dawon "{cps=[text_speed]}......{/cps}"
            jump talk_8

        "아무것도 잡지 않는다":
            $ apply_affinity_change("hobanwoo",-10)
            user "{cps=[text_speed]}(이게, 뭐지..?){/cps}"
            jump talk_8
