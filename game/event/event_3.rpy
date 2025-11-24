label event_3:
    menu:
        "마신다.":
            "{cps=[text_speed]}쌍화탕을 받아 마신다. 따뜻한 기운이 퍼진다.{/cps}"
            jiwoo "{cps=[text_speed]}다행이다. 안 마시면 좀 애매해질 뻔했거든.{/cps}"
            jump talk_4

        "마시지 않는다.":
            jiwoo "{cps=[text_speed]}아… 그렇구나. 뭐, 안 마셔도 되긴 해.{/cps}"
            "{cps=[text_speed]}지우는 쌍화탕을 잠시 바라보며 고개를 끄덕였다.{/cps}"
            jump talk_4
