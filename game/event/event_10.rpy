label event_10:

    while True:

        menu:
            "제출한다":
                # 제출 성공
                "{cps=[text_speed]}과제가 성공적으로 제출되었습니다! ✨{/cps}"
                $ apply_affinity_change("hobanwoo", 10)  # @#$$! 호감도 +10
                jump talk_11  # 제출 완료 후 다음 이벤트

            "제출하지 않는다":
                user "{cps=[text_speed]}제출 안 하면... 어떻게 되는거지?{/cps}"
                "{cps=[text_speed]}※경고창: '과제 및 평가'는 안내된 제출 기한을 엄수하여 제출해 주세요.{/cps}"
                $ apply_affinity_change("hobanwoo", -10)  # @#$$! 호감도 -10
                user "{cps=[text_speed]}이게.. 뭐야{/cps}"
                # 루프 계속

