label event_2:
    menu:
        "먹는다":
            # --- 1. 식사 수락 및 이동 ---
            $ apply_affinity_change("suah", 4)
            $ send_notification(f"윤수아 호감도 +4 (현재: {suah_affinity})")
            
            $ typing(dawon, "수아, 먹고 싶은 거 없어?")
            $ typing(suah, "저, 햄버거요!")
            $ typing(user, "그러자.")
            
            scene bg restaurant with fade
            "식당에 도착했다."
            show suah normal at right
            $ typing(suah, "뭐 드실래요?")

            # --- 2. 자유 대화 1: 메뉴 주문 ---
            $ talk_loop("suah", "너의 역할은 수아야. 햄버거 가게에 도착해서 메뉴를 고르고 주문하는 상황에서 수아가 뭐 먹을지 물어본 상황이다./ 플레이어가 뭘 먹을지 결정하면 종료된다.")

            # --- 3. 음식 나옴 및 대화 전환 ---
            "잠시 후, 주문한 음식이 나왔다."
            
            $ typing(suah, "선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?")

            # --- 4. 자유 대화 2: 방과 후 일정 ---
            $ talk_loop_all_charactor("음식을 먹으며 방과 후 일정에 대해 이야기하는 상황이다. 플레이어의 말에 따라 반응하라./ 일정에 대한 대화를 3~5턴 정도 진행하면 종료된다.")
            hide suah normal
            jump talk_3


        "먹지 않는다":
            # --- 거절 루트 ---
            $ typing(suah, "아… 그러면 저는 그냥 혼자 먹고 올게요…")
            $ typing(dawon, "뭐야. 안 먹는다고? 이상하네 진짜.")

            $ apply_affinity_change("suah", -4)
            $ apply_affinity_change("dawon", -4)
            $ send_notification("윤수아, 임다원 호감도 -4")

            "둘은 조금 어색한 분위기 속에서 자리를 떴다."

            jump talk_3