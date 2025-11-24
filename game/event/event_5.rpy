label event_5:
    # 초기 요약, 호감도, 정체 의심 여부
    $ summary = []
    $ current_affinity = professor_affinity
    $ is_sus = False

    # 시스템 프롬프트
    $ sys_prompt = system_prompt_professor

    # 상황 설명
    $ context_instruction = "교수가 내가 작성하고 있는 논문을 보며 대화하는 상황에서, 적당히 대화를 마무리짓는 말을 해야 한다."

    # 플레이어 입력 반복
    while True:
        $ user_msg = renpy.input(f"{player_name}:")
        $ user_msg = user_msg.strip()

        if user_msg == "":
            "{cps=[text_speed]}...{/cps}"
            jump event_5

        # Gemini API 호출
        # 이전 대화 기록 반영
        $ summary_text = "\n".join(summary) if summary else ""

        # Gemini API 호출
        $ reply, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
            sys_prompt, summary, user_msg, current_affinity, player_name, context_instruction
        )

        # 반영
        # 요약 리스트에 저장
        $ summary.append(f"user: {user_msg}")
        $ summary.append(f"professor: {reply}")

        # 출력
        python:
            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)

        # 호감도 적용
        $ apply_affinity_change("professor", affinity_delta)
        $ current_affinity = professor_affinity


        # 종료 조건: 헬프 제공 관련 키워드 포함 시
        if goal_achieved:
            professor "{cps=[text_speed]}수고하게나{/cps}"
            jump talk_6

    return
