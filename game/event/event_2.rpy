label event_2:

    menu:
        "먹는다":
            # 초기 대사
            $ apply_affinity_change("suah", 4)
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
