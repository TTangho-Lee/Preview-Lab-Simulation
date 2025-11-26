label event_10:
    while True:
        menu:
            "제출한다":
                $ send_notification("과제가 성공적으로 제출되었습니다! ✨")
                $ apply_affinity_change("hobanwoo", 10)
                jump talk_11

            "제출하지 않는다":
                $ typing(user, "제출 안 하면... 어떻게 되는거지?")
                $ send_notification("※경고 '과제 및 평가'는 안내된 제출 기한을 엄수하여 제출해 주세요.")
                $ apply_affinity_change("hobanwoo", -10)
                $ typing(user, "이게.. 뭐야")


