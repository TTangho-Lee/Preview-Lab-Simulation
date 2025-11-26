label lab_ending:
    # 여자들과의 대화는 '루틴 붕괴 직전의 짧은 흔적' 수준으로 최소화
    $ typing(dawon, "…그런 말 하면… 우리")
    "지직—"

    $ typing(jiwoo, "걱정… 하지… 마.")
    "찌익—"

    $ typing(suah, "선배… 제발…")
    "——신호 끊김——"

    scene black with fade
    "…삐…—"

    $ typing(researcher_a, "가상체 전부 다운. 피험자, 자각 단계 진입 확인.")
    $ typing(researcher_b, "이번엔 빠르네요. 알고리즘이 너무 익었나 봅니다.")

    $ typing(researcher_a, "루프 13이었죠? 10 이후로 매번 자각 속도가 줄고 있어요.")
    $ typing(researcher_b, "정서 모델이 약한 건가… 아니면 피험자 쪽 적응 문제인가…")

    "철컥— 기계가 설정값을 변경하는 소리."

    $ typing(researcher_a, "전극 신호 세팅. 두피 전면부 센서 값 0.12 올라갔습니다.")
    $ typing(researcher_b, "괜찮아요. 그 정도는 견딜 겁니다.")
    
    scene bg lab_ending with fade

    $ typing(user, "…어디…야…")
    $ typing(researcher_a, "반응 왔다. 안정제 투입해.")
    $ typing(researcher_b, "투입합니다. 3ml.")

    "톡— 액체 주입음."

    $ typing(user, "으… 머…리가…")
    $ typing(researcher_a, "자각 반응입니다. 자연스러운 현상.")

    $ typing(researcher_b, "루프 재설정 준비 완료. 어떤 루프로 진행할까요?")
    $ typing(researcher_a, "13번 루프처럼 트럭으로 시작합시다. 그때가 가장 몰입도가 높았으니까요.")

    "삐—삐— 기계가 빠르게 신호 패턴을 맞춘다."

    $ typing(researcher_b, "전극 강도 레벨 3까지 상승.")
    $ typing(user, "그만…! 제발…!")
    $ typing(researcher_a, "신호 차단하세요. 외부 음성 들리면 초기화가 깨집니다.")

    scene black with fade

    $ typing(researcher_b, "차단 완료. 뇌파 안정화 중.")
    $ typing(researcher_a, "좋아요. 루프 24로 돌립니다.")

    "찰칵—"

    $ typing(researcher_b, "재부팅 들어갑니다.")
    "—시스템 재기동—"

    jump talk_1
