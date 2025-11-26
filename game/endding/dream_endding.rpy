# 고백 거절 시의 엔딩

label dream_ending_1:
    scene black with fade
    "끼익…."

    $ typing(real_student_1, "또 자고 있어요.")
    $ typing(real_student_2, "웃고 있는데요.")
    $ typing(real_student_1, "진짜네요.")

    $ typing(real_professor, "놔둬라.")
    $ typing(real_professor, "꿈이 더 낫겠지.")

    $ typing(real_student_2, "논문은요?")
    $ typing(real_student_1, "마감 지났어요.")

    $ typing(real_professor, "현실 볼 자신 없나 보지.")
    $ typing(real_student_2, "그래서 저 표정인가요.")
    $ typing(real_professor, "깨우지 마라.")

    return

label dream_ending_2:
    scene black with fade
    "끼익…."

    $ typing(real_student_1, "교수님, 또 여기서 자고 있어요.")
    $ typing(real_student_2, "근데… 표정 좀 보세요. 웃고 있는데요?")
    $ typing(real_student_1, "진짜네. 뭐가 그렇게 좋은 꿈이길래.")

    $ typing(real_professor, "건들지 마라. 깨우지 말고.")
    $ typing(real_professor, "…저 표정이면 뭐든 현실보다 나은 꿈이겠지.")

    $ typing(real_student_2, "그래도 논문은요? 마감 지났잖아요.")
    $ typing(real_student_1, "우리 셋 다 밤새고 있는데… 혼자 저렇게 행복하네.")

    $ typing(real_professor, "꿈속에서라도 잘 나가는 기분을 느껴보나 보지.")
    $ typing(real_professor, "현실에서는 불가능하니까.")

    $ typing(real_student_1, "근데 계속 웃어요. 소름 돋을 정도로.")
    $ typing(real_student_2, "깨우면 충격받겠죠? 꿈이랑 현실 차이가 너무 커서.")
    
    $ typing(real_professor, "깨우지 마. 계속 자게 둬라.")
    $ typing(real_professor, "…적어도 꿈에서는 누군가와 잘 지내고 있을 테니까.")

    return

label dream_ending_3:
    scene black with fade
    "끼이익…."
    "누군가 문을 밀어 연다. 차갑고 건조한 공기가 방 안으로 스며든다."

    $ typing(real_student_1, "교수님… 저 사람 또 책상에 엎드려 자고 있어요.")
    "[real_student_1]의 목소리가 무표정하게 뚝뚝 떨어진다."

    $ typing(real_student_2, "근데 왜 저렇게… 웃고 있어요? 진짜 소름 돋는데.")
    "잠든 [user_eunneun]. 여전히 옅은 미소를 머금고 있다."

    $ typing(real_professor, "건들지 마. 깨우지도 말고.")
    $ typing(real_professor, "…꿈이 아주 달콤한 모양이군.")
    "교수의 말투는 마치 차가운 관찰자 같다."

    $ typing(real_student_1, "논문 마감 지나간 거 아시죠? 현실은 난리인데 혼자 구원받은 표정이네.")
    $ typing(real_student_2, "진짜요. 우리 다 밤새고 있는데… 저 사람은 아직도 저러고 있고.")

    $ typing(real_professor, "그래. 꿈에서라도 만족하면… 그걸로 된 거겠지.")
    $ typing(real_professor, "현실에서는 아무것도 이루지 못했으니까.")

    "세 사람의 시선이 잠든 [user] 위로 조용히 내려앉는다."
    "현실의 형광등은 참혹할 만큼 밝다. 그리고 [user_eunneun] 그 잔혹한 밝음조차 모른 채, 계속 웃고만 있다."

    return
