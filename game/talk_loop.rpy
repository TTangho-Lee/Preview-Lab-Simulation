init python:
    def talk_loop(charactor,finish_condition):
        global player_name, dawon_affinity, jiwoo_affinity, suah_affinity, hobanwoo_affinity, professor_affinity
        global system_prompt_dawon, system_prompt_jiwoo, system_prompt_suah, system_prompt_hobanwoo, system_prompt_professor
        summary = []
        is_sus = False

        if charactor=="dawon":
            current_affinity = dawon_affinity
            sys_prompt = system_prompt_dawon
        elif charactor=="jiwoo":
            current_affinity = jiwoo_affinity
            sys_prompt = system_prompt_jiwoo
        elif charactor=="suah":
            current_affinity = suah_affinity
            sys_prompt = system_prompt_suah
        elif charactor=="hobanwoo":
            current_affinity = hobanwoo_affinity
            sys_prompt = system_prompt_hobanwoo
        elif charactor=="professor":
            current_affinity = professor_affinity
            sys_prompt = system_prompt_professor

        while True:
            user_msg = renpy.input(f"{player_name}:").strip()

            if user_msg == "":
                renpy.say("{cps=[text_speed]}...{/cps}")
                continue

            summary_text = "\n".join(summary) if summary else ""

            reply, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, finish_condition
            )

            summary.append(f"user: {user_msg}")

            if charactor=="dawon":
                summary.append(f"dawon: {reply}")
            elif charactor=="jiwoo":
                summary.append(f"jiwoo: {reply}")
            elif charactor=="suah":
                summary.append(f"suah: {reply}")
            elif charactor=="hobanwoo":
                summary.append(f"hobanwoo: {reply}")
            elif charactor=="professor":
                summary.append(f"professor: {reply}")
            

            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                if charactor=="dawon":
                    renpy.say(dawon, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor=="jiwoo":
                    renpy.say(jiwoo, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor=="suah":
                    renpy.say(suah, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor=="hobanwoo":
                    renpy.say(hobanwoo, "{cps=[text_speed]}%s{/cps}" % safe_s)
                elif charactor=="professor":
                    renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)
                

            if charactor=="dawon":
                apply_affinity_change("dawon", affinity_delta)
                current_affinity = dawon_affinity
            elif charactor=="jiwoo":
                apply_affinity_change("jiwoo", affinity_delta)
                current_affinity = jiwoo_affinity
            elif charactor=="suah":
                apply_affinity_change("suah", affinity_delta)
                current_affinity = suah_affinity
            elif charactor=="hobanwoo":
                apply_affinity_change("hobanwoo", affinity_delta)
                current_affinity = hobanwoo_affinity
            elif charactor=="professor":
                apply_affinity_change("professor", affinity_delta)
                current_affinity = professor_affinity


            if goal_achieved:
                return

        return
