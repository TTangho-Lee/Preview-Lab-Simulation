'''
<대화 8>
어떻게 하든 집으로 돌아가는 루트로.(집으로 간다는 뉘앙스의 대화가 아니면 무한루프)
'''

label event_8:
    # 초기 요약, 호감도, 정체 의심 여부
    $ summary = []
    $ current_affinity = jiwoo_affinity
    $ is_sus = False

    # 시스템 프롬프트
    $ sys_prompt = system_prompt_jiwoo

    # 상황 설명
    $ context_instruction = "정전이 되었다가 막 불이 돌아와서 집에 가야겠다고 언급한 상황에서, 집에 가자고 입력을 받아야 한다."

    # 플레이어 입력 반복
    while True:
        $ user_msg = renpy.input(f"{player_name}:")
        $ user_msg = user_msg.strip()

        if user_msg == "":
            "{cps=[text_speed]}...{/cps}"
            jump event_8

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
        $ summary.append(f"jiwoo: {reply}")

        # 출력
        python:
            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)

        # 호감도 적용
        $ apply_affinity_change("jiwoo", affinity_delta)
        $ current_affinity = jiwoo_affinity


        # 종료 조건: 헬프 제공 관련 키워드 포함 시
        if goal_achieved:
            jump talk_9

    return
