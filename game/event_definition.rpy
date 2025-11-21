# ------------------------------------------------
# 이벤트 레이블 예시 (캐릭터별)
# ------------------------------------------------
label event_haru_1:
    show haru happy
    haru "{cps=35}어? 우리 벌써 이렇게 친해진 거야? 고마워…{/cps}"
    return

label event_haru_2:
    show haru shy
    haru "{cps=35}이런 말 해도 되나... 좀 부끄럽네.{/cps}"
    return

label ending_haru:
    show haru love
    scene bg rooftop
    haru "{cps=35}정말…너랑 있으면 마음이 편해져. 좋아해.{/cps}"
    return

label event_yuki_1:
    show yuki normal
    yuki "{cps=35}흥, 네가 그렇게 말하다니. 조금은 인정해줄게.{/cps}"
    return

label event_yuki_2:
    show yuki shy
    yuki "{cps=35}…그만 놀려. 진짜로 기뻐질 수도 있잖아.{/cps}"
    return

label ending_yuki:
    show yuki love
    scene bg night
    yuki "{cps=35}네가 옆에 있어서… 이상하게 편하네. 좋아해.{/cps}"
    return

label event_mina_1:
    show mina happy
    mina "{cps=35}우와! 대화 진짜 재밌다~ 더 해보자!{/cps}"
    return

label event_mina_2:
    show mina shy
    mina "{cps=35}이런 분위기 너무 좋아~ 꺄르르{/cps}"
    return

label ending_mina:
    show mina love
    scene bg rooftop
    mina "{cps=35}너랑 있는 시간, 진짜 소중해! 좋아해!!{/cps}"
    return