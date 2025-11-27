init python:
    import random
    def talk_loop_all_charactor(finish_condition, max_turn=5):
        global player_name, dawon_affinity, jiwoo_affinity, suah_affinity, hobanwoo_affinity, professor_affinity
        global system_prompt_dawon, system_prompt_jiwoo, system_prompt_suah, system_prompt_hobanwoo, system_prompt_professor
        emotion_map = {
            "normal": "normal",
            "smile": "smile",
            "sad": "sad",
            "shy": "shy",
            "angry": "angry",
        }
        summary = []
        summary.append(f"suah: 선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?")
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트
        renpy.show("suah normal", at_list=[store.center])

        while True:
            if turn_count >= max_turn+2:
                return
            user_msg = renpy.input(f"{player_name}:").strip()
            if user_msg == "":
                continue
            turn_count += 1
            charactor = ask_llm_for_next_character(summary, user_msg)

            if charactor == "dawon":
                current_affinity = dawon_affinity
                sys_prompt = system_prompt_dawon

            elif charactor == "suah":
                current_affinity = suah_affinity
                sys_prompt = system_prompt_suah


            # [핵심 수정] 3턴 이상 진행되면 종료 유도 프롬프트 추가
            # finish_condition 문자열 뒤에 시스템 메시지를 덧붙여 LLM에게 종료를 압박합니다.
            current_condition = finish_condition
            if turn_count >= max_turn:
                current_condition = f"현재 대화가 {turn_count}턴 진행되었다. 대화가 마무리되는 대사를 입력하여라./ 반드시 'goal_achievement: true'를 출력하여 대화를 종료하여라."

            summary_text = "\n".join(summary) if summary else ""

            # AI 응답 생성
            # finish_condition 대신 수정된 current_condition을 전달합니다.
            reply, charactor_emotion, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )

            # 요약 저장
            summary.append(f"user: {user_msg}")
            
            if charactor == "dawon":
                summary.append(f"dawon: {reply}")
            elif charactor == "suah":
                summary.append(f"suah: {reply}")
            
            # 대사 출력 (기존 로직 유지)
            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                if charactor == "dawon":
                    if charactor_emotion in emotion_map:
                        show_expression = emotion_map[charactor_emotion]
                        renpy.show(dawon_{show_expression}, at_list=[store.left])
                    renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)

                elif charactor == "suah":
                    if charactor_emotion in emotion_map:
                        show_expression = emotion_map[charactor_emotion]
                        renpy.show(suah_{show_expression}, at_list=[store.center])
                    renpy.say(suah, "{cps=[text_speed]}%s{/cps}" % safe_s)
                

            if charactor == "dawon":
                apply_affinity_change("dawon", affinity_delta)
                current_affinity = dawon_affinity
            elif charactor == "suah":
                apply_affinity_change("suah", affinity_delta)
                current_affinity = suah_affinity

            # [안전장치 2] 목표 달성 시 종료
            if goal_achieved:
                return

        return

    import requests
    import json

    def ask_llm_for_next_character(summary, user_msg):
        global GEMINI_URL, GEMINI_API_KEY

        # 대화 요약 문자열 생성
        summary_text = "\n".join(summary) if summary else ""

        prompt = f"""
    당신은 '등장 캐릭터 선택 시스템'입니다.

    대화 요약:
    {summary_text}

    유저의 최신 발화:
    {user_msg}

    등장 가능한 캐릭터는 다음 2명이다:
    - dawon
    - suah

    현재 상황에서 가장 자연스럽게 다음 턴에 발화할 캐릭터 1명을 선택해라.

    출력 형식:
    character: 이름

    설명이나 부가 문장은 절대 출력하지 말고,
    'character: dawon' 같은 형식 ONLY.
    """

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 50
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload), timeout=10)
            result = response.json()

            if "candidates" not in result:
                return random.choice(["dawon", "suah"])

            text = result["candidates"][0]["content"]["parts"][0]["text"]
            text = text.lower().strip()

            # 출력 예시: "character: jiwoo"
            if text.startswith("character:"):
                name = text.replace("character:", "").strip()
                if name in ["dawon", "suah"]:
                    return name

            # 비정상 출력 fallback
            return random.choice(["dawon", "suah"])

        except Exception as e:
            # 실패 시 랜덤 fallback
            return random.choice(["dawon", "suah"])
