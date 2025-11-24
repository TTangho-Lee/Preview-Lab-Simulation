label event_4:

    while True:

        # 1차 질문 출력
        "{cps=[text_speed]}탈퇴하시겠습니까?{/cps}"

        menu:
            "네":
                "{cps=[text_speed]}정말로 탈퇴하시겠습니까? 탈퇴를 하고 난 후의 패널티가 적용됩니다.{/cps}"

                # 2차 질문
                menu:
                    "네":
                        "{cps=[text_speed]}<knuai : [메세지] 새로운 메시지가 도착하였습니다.>{/cps}"
                        "{cps=[text_speed]}@#$$!님의 호감도가 –25 하락했습니다.{/cps}"

                        # 호감도 적용
                        $ apply_affinity_change("hobanwoo", -25)

                        # 루프 계속
                        pass

                    "아니오":
                        "{cps=[text_speed]}...취소되었습니다.{/cps}"
                        jump talk_5

            "아니오":
                "{cps=[text_speed]}...취소되었습니다.{/cps}"
                jump talk_5
