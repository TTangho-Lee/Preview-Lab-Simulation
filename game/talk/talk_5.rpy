label talk_5:
    # --- 1. 탈퇴 유혹 회피 ---
    $ typing(user, "그래, 괜히 탈퇴했다가...")
    "다시 컴퓨터 화면을 바라보며" 
    $ typing(user, "근거리 객체 탐지를 위한 YOLOv8 모델 경량화에 대한거라..." )
    

    # --- 2. 교수님 등장 ---
    "문이 열리며 교수님이 들어오신다." 
    show professor normal at center with moveinright
    $ typing(professor, "두고 간 게 있어서 잠시 들렸는데, 다들 집 안 가니?" )
    $ typing(user, "네 교수님… 아직 논문 작성이 끝이 안 나서요." )
    $ typing(professor, "한번 볼까?" )
    

    # --- 3. 교수와의 대화 이벤트로 이동 ---
    jump event_5