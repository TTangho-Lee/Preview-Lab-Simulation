'''
label event_2:
    scene bg restaurant
    menu:
        "먹는다":
            # 초기 대사
            $ apply_affinity_change("suah", 4)
            $ send_notification(f"임다원 호감도 +4 (현재: {dawon_affinity})")
            dawon "{cps=[text_speed]}수아, 먹고 싶은 거 없어?{/cps}"
            suah "{cps=[text_speed]}저, 햄버거요!{/cps}"
            user "{cps=[text_speed]}그러자.{/cps}"
            "{cps=[text_speed]}둘과 함께 학교 근처 식당으로 향했다.{/cps}"

            # 식당 도착
            suah "{cps=[text_speed]}뭐 드실래요?{/cps}"
            $ turn_count = 0
            $ summary = []
            $ current_affinity_suah = suah_affinity
            $ current_affinity_dawon = dawon_affinity

            while turn_count < 3:

                # 유저 입력
                $ user_msg = renpy.input(f"{player_name}:")
                $ user_msg = user_msg.strip()
                $ user_msg = renpy.input(f"{player_name}:").strip()
                if user_msg == "":
                    $ turn_count -= 1
                    python:
                        pass

                # 기록
                $ summary.append(f"user: {user_msg}")

                # AI 답변: suah
                $ reply_suah, summary_text, affinity_delta_suah, is_sus, goal = gemini_generate_response(
                    system_prompt_suah,
                    "\n".join(summary),
                    user_msg,
                    current_affinity_suah,
                    player_name
                )
                $ summary.append(f"suah: {reply_suah}")
                $ apply_affinity_change("suah", affinity_delta_suah)
                $ current_affinity_suah = suah_affinity

                # AI 답변: dawon
                $ reply_dawon, summary_text, affinity_delta_dawon, is_sus, goal = gemini_generate_response(
                    system_prompt_dawon,
                    "\n".join(summary),
                    user_msg,
                    current_affinity_dawon,
                    player_name
                )
                $ summary.append(f"dawon: {reply_dawon}")
                $ apply_affinity_change("dawon", affinity_delta_dawon)
                $ current_affinity_dawon = dawon_affinity

                # 출력
                python:
                    from store import split_sentences
                    for s in split_sentences(reply_suah):
                        renpy.say("suah", "{cps=[text_speed]}"+s+"{/cps}")
                    for s in split_sentences(reply_dawon):
                        renpy.say("dawon", "{cps=[text_speed]}"+s+"{/cps}")

                $ turn_count += 1

            # 마지막 호감도 증가
            $ apply_affinity_change("suah", 3)
            $ apply_affinity_change("dawon", 2)

            jump talk_3


        "먹지 않는다":
            # 대사 진행
            suah "{cps=[text_speed]}아… 그러면 저는 그냥 혼자 먹고 올게요…{/cps}"
            dawon "{cps=[text_speed]}뭐야. 안 먹는다고? 이상하네 진짜.{/cps}"

            # 호감도 적용
            $ apply_affinity_change("suah", -4)
            $ apply_affinity_change("dawon", -4)

            "{cps=[text_speed]}둘은 조금 어색한 분위기 속에서 자리를 떴다.{/cps}"

            jump talk_3
'''
label event_2:
    jump talk_6
    menu:
        "먹는다":
            # --- 1. 식사 수락 및 이동 ---
            $ apply_affinity_change("suah", 4)
            $ send_notification(f"윤수아 호감도 +4 (현재: {suah_affinity})")
            
            dawon "{cps=[text_speed]}수아, 먹고 싶은 거 없어?{/cps}"
            suah "{cps=[text_speed]}저, 햄버거요!{/cps}"
            user "{cps=[text_speed]}그러자.{/cps}"
            
            scene bg restaurant with fade
            "{cps=[text_speed]}식당에 도착했다.{/cps}"
            show suah normal at right
            suah "{cps=[text_speed]}뭐 드실래요?{/cps}"

            # --- 2. 자유 대화 1: 메뉴 주문 ---
            # 기존 talk_loop 함수 사용 (약 3턴 진행 후 종료 조건)
            $ talk_loop("suah", "햄버거 가게에 도착해서 메뉴를 고르고 주문하는 상황이다. / 메뉴 주문에 대한 대화를 3턴 정도 진행하거나 주문이 완료되면 종료된다.")

            # --- 3. 음식 나옴 및 대화 전환 ---
            "{cps=[text_speed]}잠시 후, 주문한 음식이 나왔다.{/cps}"
            
            suah "{cps=[text_speed]}선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?{/cps}"

            # --- 4. 자유 대화 2: 방과 후 일정 ---
            # 호감도 변동 (-3 ~ +2)은 AI 프롬프트(finish_condition)에 포함하여 지시
            # 여기서는 대화의 주체를 임다원으로 설정하여 진행 (talk_loop는 1:1 대화 기준이므로)
            $ talk_loop("dawon", "음식을 먹으며 방과 후 일정에 대해 이야기하는 상황이다. 플레이어의 말에 따라 호감도를 -3에서 +2 사이로 변경하며 반응하라. / 일정에 대한 대화를 3~5턴 정도 진행하면 종료된다.")
            hide suah normal
            jump talk_3


        "먹지 않는다":
            # --- 거절 루트 ---
            suah "{cps=[text_speed]}아… 그러면 저는 그냥 혼자 먹고 올게요…{/cps}"
            dawon "{cps=[text_speed]}뭐야. 안 먹는다고? 이상하네 진짜.{/cps}"

            $ apply_affinity_change("suah", -4)
            $ apply_affinity_change("dawon", -4)
            $ send_notification("윤수아, 임다원 호감도 -4")

            "{cps=[text_speed]}둘은 조금 어색한 분위기 속에서 자리를 떴다.{/cps}"

            jump talk_3