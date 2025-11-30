init python:
    def talk_loop(charactor, finish_condition, max_turn=3, last_char_line=""):
        global player_name, dawon_affinity, jiwoo_affinity, suah_affinity, professor_affinity
        global system_prompt_dawon, system_prompt_jiwoo, system_prompt_suah, system_prompt_professor
        emotion_map = {
            "normal": "normal",
            "smile": "smile",
            "sad": "sad",
            "shy": "shy",
            "angry": "angry",
        }
        all_emotions = ["normal", "smile", "sad", "shy", "angry"]
        summary = []
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트
        last_reply = last_char_line

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
        elif charactor == "professor":
            current_affinity = professor_affinity
            sys_prompt = system_prompt_professor

        while True:
            # [안전장치 1] 10턴이 넘어가면 강제 종료 (무한 루프 방지)
            if turn_count >= max_turn+2:
                return

            # AI를 통해 선택지 생성
            choices = gemini_generate_choices(sys_prompt, summary, last_reply, current_affinity, player_name, finish_condition)
            
            # 메뉴 표시
            choice = renpy.display_menu(
                [
                    (choices[0], choices[0]),
                    (choices[1], choices[1]),
                    ("직접 입력", "direct_input")
                ]
            )

            if choice == "direct_input":
                user_msg = renpy.input(f"{player_name}:").strip()
            else:
                user_msg = choice

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
            reply, charactor_emotion, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )
            last_reply = reply # 다음 턴의 선택지 생성을 위해 현재 응답을 저장
            reply = reply.replace("{", "{{").replace("}", "}}")
            sentences=[s for s in split_sentences(reply)]
            # 요약 저장
            summary.append(f"user: {user_msg}")
            

            for emo in all_emotions:
                renpy.hide("dawon " + emo)
                renpy.hide("suah " + emo)
                renpy.hide("jiwoo " + emo)
                renpy.hide("professor " + emo)

            if charactor_emotion in emotion_map:
                show_expression = emotion_map[charactor_emotion]
                if charactor=="dawon":
                    renpy.show(charactor + " " + show_expression, at_list=[store.left])
                elif charactor=="jiwoo":
                    renpy.show(charactor + " " + show_expression, at_list=[store.center])
                elif charactor=="suah":
                    renpy.show(charactor + " " + show_expression, at_list=[store.right])
                elif charactor=="professor":
                    renpy.show(charactor + " " + show_expression, at_list=[store.center])

            if charactor == "dawon":
                summary.append(f"dawon: {reply}")
                apply_affinity_change("dawon", affinity_delta)
                current_affinity = dawon_affinity
                for s in sentences:
                    # %, [, {, } 기호를 모두 이스케이프 처리하여 오류 방지
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "jiwoo":
                summary.append(f"jiwoo: {reply}")
                apply_affinity_change("jiwoo", affinity_delta)
                current_affinity = jiwoo_affinity
                for s in sentences:
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(jiwoo, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "suah":
                summary.append(f"suah: {reply}")
                apply_affinity_change("suah", affinity_delta)
                current_affinity = suah_affinity
                for s in sentences:
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(suah, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "professor":
                summary.append(f"professor: {reply}")
                apply_affinity_change("professor", affinity_delta)
                current_affinity = professor_affinity
                for s in sentences:
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)
            

            # [안전장치 2] 목표 달성 시 종료
            if goal_achieved:
                return

        return


    def talk_loop_center(charactor, finish_condition, max_turn=5, last_char_line=""):
        global player_name, dawon_affinity, jiwoo_affinity, suah_affinity, professor_affinity
        global system_prompt_dawon, system_prompt_jiwoo, system_prompt_suah, system_prompt_professor
        emotion_map = {
            "normal": "normal",
            "smile": "smile",
            "sad": "sad",
            "shy": "shy",
            "angry": "angry",
        }
        all_emotions = ["normal", "smile", "sad", "shy", "angry"]
        summary = []
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트
        last_reply = last_char_line

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
        elif charactor == "professor":
            current_affinity = professor_affinity
            sys_prompt = system_prompt_professor

        while True:
            # [안전장치 1] 10턴이 넘어가면 강제 종료 (무한 루프 방지)
            if turn_count >= max_turn+2:
                return

            # AI를 통해 선택지 생성
            choices = gemini_generate_choices(sys_prompt, summary, last_reply, current_affinity, player_name, finish_condition)
            
            # 메뉴 표시
            choice = renpy.display_menu(
                [
                    (choices[0], choices[0]),
                    (choices[1], choices[1]),
                    ("직접 입력", "direct_input")
                ]
            )

            if choice == "direct_input":
                user_msg = renpy.input(f"{player_name}:").strip()
            else:
                user_msg = choice

            if user_msg == "":
                # 빈 입력은 턴 수에 포함하지 않거나, 그냥 넘어감
                continue
            
            turn_count += 1 # 유효한 대화 1턴 증가

            # [핵심 수정] 3턴 이상 진행되면 종료 유도 프롬프트 추가
            # finish_condition 문자열 뒤에 시스템 메시지를 덧붙여 LLM에게 종료를 압박합니다.
            current_condition = finish_condition

            summary_text = "\n".join(summary) if summary else ""

            # AI 응답 생성
            # finish_condition 대신 수정된 current_condition을 전달합니다.
            reply, charactor_emotion, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )
            last_reply = reply # 다음 턴의 선택지 생성을 위해 현재 응답을 저장
            reply = reply.replace("{", "{{").replace("}", "}}")
            sentences=[s for s in split_sentences(reply)]
            # 요약 저장
            summary.append(f"user: {user_msg}")
            

            for emo in all_emotions:
                renpy.hide("dawon " + emo)
                renpy.hide("suah " + emo)
                renpy.hide("jiwoo " + emo)
                renpy.hide("professor " + emo)

            if charactor_emotion in emotion_map:
                show_expression = emotion_map[charactor_emotion]
                if charactor=="dawon":
                    renpy.show(charactor + " " + show_expression, at_list=[store.center])
                elif charactor=="jiwoo":
                    renpy.show(charactor + " " + show_expression, at_list=[store.center])
                elif charactor=="suah":
                    renpy.show(charactor + " " + show_expression, at_list=[store.center])
                elif charactor=="professor":
                    renpy.show(charactor + " " + show_expression, at_list=[store.center])

            if charactor == "dawon":
                summary.append(f"dawon: {reply}")
                apply_affinity_change("dawon", affinity_delta)
                current_affinity = dawon_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "jiwoo":
                summary.append(f"jiwoo: {reply}")
                apply_affinity_change("jiwoo", affinity_delta)
                current_affinity = jiwoo_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(jiwoo, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "suah":
                summary.append(f"suah: {reply}")
                apply_affinity_change("suah", affinity_delta)
                current_affinity = suah_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(suah, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "professor":
                summary.append(f"professor: {reply}")
                apply_affinity_change("professor", affinity_delta)
                current_affinity = professor_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)
            

            # [안전장치 2] 목표 달성 시 종료
            if goal_achieved:
                return

        return