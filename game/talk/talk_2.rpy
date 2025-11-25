'''
user가 컴퓨터를 켜서 ’논문‘ 이라고 적힌 폴더를 열어본다
주제 :“AI 생성물 탐지를 위한 특징학습(Self-supervised Representation Learning) 기법 
고도화”
 user: 고맙다. 헛고생할 뻔 했네.
임다원: 도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었어  ✨”
 |-----------♥---------|
임다원 호감도 +1
 user: (이게 오른다고?)
 user: (말투는 왜저래)
임다원: 뭔데? 뭐보는데
user: 아 어
user: 아, 별건 아니고. 유튜브 알림 
임다원: 뭐? 그게 뭔
연구실의 문이 열리고 꽃향기를 풍기는 생머리 여자 한명이 들어온다.
 ???: 선배님들 같이 계셨네요?
임다원에게 속닥거리며 물어본다
user: 쟤는 누구야...?
임다원: 너 이정도면 기억상실 아니야? 수아잖아, 윤수아
user: 아, 그래?
윤수아: 배 안고프세요? 곧 저녁시간인데 같이 밥 먹으러가요!
'''
label talk_2:
    # 임다원 대화 종료 후
    
    # --- 1. 논문 확인 및 호감도 변화 ---
    "[user_iga] 컴퓨터를 켜서 ‘논문‘ 이라고 적힌 폴더를 열어본다."
    
    window auto
    "주제 : “AI 생성물 탐지를 위한 특징학습(Self-supervised Representation Learning) 기법 고도화”"
    window hide
    
    user "고맙다. 헛고생할 뻔 했네."
    
    # 임다원 호감도 +1
    $ apply_affinity_change("dawon", 1)
    
    dawon "도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었어 ✨"
    
    # 호감도 변화 알림 (additional_ui.rpy의 send_notification 함수가 있다면 활용)
    $ send_notification(f"임다원 호감도 +1 (현재: {dawon_affinity})")
    "|-----------♥---------|"
    
    # 독백
    user "이게 오른다고?"
    user "말투는 왜 저래"
    
    # --- 2. 유튜브 대화 (메타 질문 회피) ---
    dawon "뭔데? 뭐 보는데."
    user "아 어."
    user "아, 별건 아니고. 유튜브 알림."
    dawon "뭐? 그게 뭔..."
    
    # --- 3. 윤수아 등장 ---
    "연구실의 문이 열리고 꽃향기를 풍기는 생머리 여자 한 명이 들어온다."

    # 윤수아 이미지 표시 (suah 캐릭터는 charactor_definition.rpy에 정의되어 있음)
    show suah normal at right with moveinright
    
    suah "선배님들 같이 계셨네요?"
    
    "임다원에게 속닥거리며 물어본다."
    user "쟤는 누구야...?"
    
    dawon "너 이 정도면 기억상실 아니야? 수아잖아, 윤수아."
    $ apply_affinity_change("suah",30)
    
    user "아, 그래?"
    
    # 윤수아 캐릭터 소개
    suah "배 안고프세요? 곧 저녁시간인데 같이 밥 먹으러 가요!"
    
    # 다음 이벤트로 점프
    jump event_2