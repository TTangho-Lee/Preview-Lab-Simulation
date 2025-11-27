# script.rpy

# --- 초기화 ---
init python:
    # 대화 도중 사용할 임시 변수들
    current_sys_prompt = ""
    current_summary = ""
    current_aff = 0
    current_context = ""

# --- 게임 시작 ---
label start:

    $ player_name = renpy.input("당신의 이름을 입력하세요:", default="user").strip()
    if player_name == "":
        $ player_name = "플레이어"
    
    # 폰 기능 활성화
    show screen input_listener




    jump event_2
