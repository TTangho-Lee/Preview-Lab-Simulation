label event_1:
    # 초기 요약, 호감도, 정체 의심 여부
    $ summary = []
    $ current_affinity = dawon_affinity
    $ is_sus = False

    # 시스템 프롬프트
    $ sys_prompt = system_prompt_dawon

    # 상황 설명
    $ context_instruction = "과제가 어디있는지 찾는걸 도와달라고 묻는 상황에서, 결국 도움을 주는 말을 해줘야 한다."

    # 플레이어 입력 반복
    while True:
        $ user_msg = renpy.input(f"{player_name}:")
        $ user_msg = user_msg.strip()

        if user_msg == "":
            "{cps=[text_speed]}...{/cps}"
            jump event_1

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
        $ summary.append(f"dawon: {reply}")

        # 출력
        python:
            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)

        # 호감도 적용
        $ apply_affinity_change("dawon", affinity_delta)
        $ current_affinity = dawon_affinity


        # 종료 조건: 헬프 제공 관련 키워드 포함 시
        if goal_achieved:
            dawon "{cps=[text_speed]}너 USB 완전 신 모시듯 가지고 있었잖아. 거기 있는거 아니야?{/cps}"
            jump talk_2

    return
