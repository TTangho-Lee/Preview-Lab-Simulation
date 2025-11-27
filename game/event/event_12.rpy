label event_12:
    scene bg lab
    menu:
        "1. 임다원과 놀자":
            show dawon smile
            $ typing(dawon, "놀자고? 그래 ✨")
            $ apply_affinity_change("dawon", 20)
            $ send_notification("임다원 호감도 +20")
            $ talk_loop("dawon", "너의 역할은 다원이야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ 캐릭터의 호감도가 80 이상을 달성하거나, 플레이어가 대화를 마무리하려는 말을 할 때 종료된다.")

            jump ending_choice

        "2. 홍지우와 놀자":
            show jiwoo smile
            $ typing(jiwoo, "같이 놀자구? ㅋㅋㅋ 좋아")
            $ apply_affinity_change("jiwoo", 20)
            $ send_notification("홍지우 호감도 +20")
            $ talk_loop("jiwoo", "너의 역할은 지우야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ 캐릭터의 호감도가 80 이상을 달성하거나, 플레이어가 대화를 마무리하려는 말을 할 때 종료된다.")
            jump ending_choice

        "3. 윤수아와 놀자":
            show suah smile
            $ typing(suah, "정말요? 좋아요! 선배님")
            $ apply_affinity_change("suah", 20)
            $ send_notification("윤수아 호감도 +20")
            $ talk_loop("suah", "너의 역할은 수아야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ 캐릭터의 호감도가 80 이상을 달성하거나, 플레이어가 대화를 마무리하려는 말을 할 때 종료된다.")
            jump ending_choice

        "4. 놀지 않는다":
            $ typing(user, "아냐, 그냥 내 방으로 돌아갈게.")
            
            jump dream_ending
            
