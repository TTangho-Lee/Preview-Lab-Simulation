init python:
    def talk_loop(charactor, finish_condition, max_turn=3):
        global player_name, dawon_affinity, jiwoo_affinity, suah_affinity, hobanwoo_affinity, professor_affinity
        global system_prompt_dawon, system_prompt_jiwoo, system_prompt_suah, system_prompt_hobanwoo, system_prompt_professor
        
        summary = []
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트

        # 캐릭터별 초기 설정
        if charactor == "dawon":
            current_affinity = dawon_affinity
            sys_prompt = system_prompt_dawon
        elif charactor == "jiwoo":
            current_affinity = jiwoo_affinity
            sys_prompt = system_prompt_jiwoo
        elif charactor == "suah":
            current_affinity = suah_affinity
            sys_prompt = system_prompt_suah
        elif charactor == "hobanwoo":
            current_affinity = hobanwoo_affinity
            sys_prompt = system_prompt_hobanwoo
        elif charactor == "professor":
            current_affinity = professor_affinity
            sys_prompt = system_prompt_professor

        while True:
            # [안전장치 1] 10턴이 넘어가면 강제 종료 (무한 루프 방지)
            if turn_count >= max_turn+2:
                return

            user_msg = renpy.input(f"{player_name}:").strip()

            if user_msg == "":
                # 빈 입력은 턴 수에 포함하지 않거나, 그냥 넘어감
                continue
            
            turn_count += 1 # 유효한 대화 1턴 증가

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