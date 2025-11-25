'''
user는 컴퓨터에서 논문 파일을 빠르게 프린트하고 집으로 돌아간다.
user의 집
user: 도대체 이게 무슨 일이야...
'''
label talk_9:
    # 정전 이벤트 종료 후
    
    # --- 1. 귀가 및 씬 전환 ---
    "user는 컴퓨터에서 논문 파일을 빠르게 프린트하고 집으로 돌아간다." 
    
    scene bg black with fade
    "..."
    
    scene bg home with dissolve # 집 배경 (새로운 이미지 'bg home'이 필요합니다)
    user "도대체 이게 무슨 일이야..." 

    # 다음 이벤트로 점프
    jump event_9