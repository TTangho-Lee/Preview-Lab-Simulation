init python:
    import random
    def talk_loop_all_charactor(finish_condition, max_turn=5):
        global player_name, dawon_affinity, jiwoo_affinity, suah_affinity, hobanwoo_affinity, professor_affinity
        global system_prompt_dawon, system_prompt_jiwoo, system_prompt_suah, system_prompt_hobanwoo, system_prompt_professor
        
        summary = []
        summary.append(f"suah: 선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?")
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트


        while True:
            # [안전장치 1] 10턴이 넘어가면 강제 종료 (무한 루프 방지)
            if turn_count >= max_turn+2:
                return

            user_msg = renpy.input(f"{player_name}:").strip()

            if user_msg == "":
                # 빈 입력은 턴 수에 포함하지 않거나, 그냥 넘어감
                continue
            
            turn_count += 1 # 유효한 대화 1턴 증가
            
            charactor = ask_llm_for_next_character(summary, user_msg)

            # 캐릭터별 초기 설정
            if charactor == "dawon":
                current_affinity = dawon_affinity
                sys_prompt = system_prompt_dawon
                renpy.hide("suah normal")
                renpy.show("dawon normal", at_list=[store.left])
            elif charactor == "jiwoo":
                current_affinity = jiwoo_affinity
                sys_prompt = system_prompt_jiwoo
            elif charactor == "suah":
                current_affinity = suah_affinity
                sys_prompt = system_prompt_suah
                renpy.hide("dawon normal")
                renpy.show("suah normal", at_list=[store.center])
            elif charactor == "hobanwoo":
                current_affinity = hobanwoo_affinity
                sys_prompt = system_prompt_hobanwoo
            elif charactor == "professor":
                current_affinity = professor_affinity
                sys_prompt = system_prompt_professor

            # [핵심 수정] 3턴 이상 진행되면 종료 유도 프롬프트 추가
            # finish_condition 문자열 뒤에 시스템 메시지를 덧붙여 LLM에게 종료를 압박합니다.
            current_condition = finish_condition
            if turn_count >= max_turn:
                current_condition = f"현재 대화가 {turn_count}턴 진행되었다. 대화가 마무리되는 대사를 입력하여라./ 반드시 'goal_achievement: true'를 출력하여 대화를 종료하여라."

            summary_text = "\n".join(summary) if summary else ""

            # AI 응답 생성
            # finish_condition 대신 수정된 current_condition을 전달합니다.
            reply, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )

            # 요약 저장
            summary.append(f"user: {user_msg}")
            
            if charactor == "dawon":
                summary.append(f"dawon: {reply}")
            elif charactor == "jiwoo":
                summary.append(f"jiwoo: {reply}")
            elif charactor == "suah":
                summary.append(f"suah: {reply}")
            elif charactor == "hobanwoo":
                summary.append(f"hobanwoo: {reply}")
            elif charactor == "professor":
                summary.append(f"professor: {reply}")
            
            # 대사 출력 (기존 로직 유지)
            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                if charactor == "dawon":
                    renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor == "jiwoo":
                    renpy.say(jiwoo, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor == "suah":
                    renpy.say(suah, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor == "hobanwoo":
                    renpy.say(hobanwoo, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor == "professor":
                    renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)
                
            # 호감도 변화 제한 및 적용
            if affinity_delta >= 4 or affinity_delta <= -4:
                affinity_delta = 0

            expression = "normal" # 기본 표정
            if affinity_delta >= 2:
                expression = "smile" # 호감도 크게 증가 시 웃는 표정
            elif affinity_delta <= -2:
                expression = "angry" # 호감도 크게 감소 시 웃는 표정
            
            # 캐릭터별 표정 적용 (이미지 태그: "char_id expression")
            if charactor in ["dawon", "jiwoo", "suah"]: # 이미지가 있는 캐릭터만
                renpy.show(f"{charactor} {expression}")

            if charactor == "dawon":
                apply_affinity_change("dawon", affinity_delta)
                current_affinity = dawon_affinity
            elif charactor == "jiwoo":
                apply_affinity_change("jiwoo", affinity_delta)
                current_affinity = jiwoo_affinity
            elif charactor == "suah":
                apply_affinity_change("suah", affinity_delta)
                current_affinity = suah_affinity
            elif charactor == "hobanwoo":
                apply_affinity_change("hobanwoo", affinity_delta)
                current_affinity = hobanwoo_affinity
            elif charactor == "professor":
                apply_affinity_change("professor", affinity_delta)
                current_affinity = professor_affinity

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
