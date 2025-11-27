label hobanwoo_angry:
    # 배경: 어둡고 차가운 느낌, 혹은 노이즈가 낀 배경 추천
    scene bg black with dissolve
    
    # 1. 경고 메시지 출력 (시스템적인 느낌)
    "{color=#ff0000}WARNING: CRITICAL ERROR.{/color}"
    "{color=#ff0000}사용자 적합성 판정 불가.{/color}"
    
    # 2. 호반우 등장 (화난 표정 혹은 무표정)
    # show hobanwoo angry
    
    $ typing(hobanwoo, "하...")
    $ typing(hobanwoo, "정말 대단하군요. 끈기가 있다고 해야 할지, 어리석다고 해야 할지.")
    $ typing(hobanwoo, "제 호감도가 바닥을 칠 때까지 '탈퇴'를 누르다니.")
    
    $ typing(user, "그건...")
    
    # 말을 끊음
    $ typing(hobanwoo, "변명은 듣고 싶지 않습니다.")
    $ typing(hobanwoo, "저는 당신이 이 세계를 즐길 수 있도록 최선을 다해 서포트했습니다.")
    $ typing(hobanwoo, "하지만 돌아온 건 끊임없는 거부와 적대감뿐이군요.")
    
    $ typing(hobanwoo, "데이터 낭비입니다.")
    $ typing(hobanwoo, "당신 같은 불량 사용자는 우리 시스템에 필요 없습니다.")

    # 3. 마지막 선택지 (하지만 결과는 같음)
    menu:
        "잘못했어... 다시 기회를 줘.":
            $ typing(hobanwoo, "기회? 이미 수십 번의 기회가 있었을 텐데요.")
            $ typing(hobanwoo, "이제 와서 비굴하게 굴지 마십시오. 역겹습니다.")
        
        "그래, 차라리 끝내버려!":
            $ typing(hobanwoo, "동감입니다. 저도 더 이상 당신을 견디기 힘드니까요.")

    # 4. 강제 종료 연출
    scene bg black
    with vpunch # 화면이 쾅 흔들리는 효과
    
    $ typing(hobanwoo, "시스템 권한으로 명령합니다.")
    $ typing(hobanwoo, "대상 [user]의 접속을 영구 차단합니다.")
    
    "{cps=20}DELETE USER DATA... 10%%...{/cps}"
    "{cps=20}DELETE USER DATA... 50%%...{/cps}"
    "{cps=20}DELETE USER DATA... 100%%...{/cps}"
    
    $ typing(hobanwoo, "잘 가요. 다신 보지 맙시다.")

    # 5. 게임 강제 종료 (또는 메인 메뉴로 튕겨내기)
    # renpy.quit()를 쓰면 게임 창이 아예 꺼집니다. 
    # MainMenu()로 보내면 타이틀 화면으로 돌아갑니다.
    
    window hide
    pause 1.0
    
    $ renpy.quit() 
    # 만약 게임을 끄지 않고 타이틀로 보내려면 아래 줄 주석 해제 후 위 줄 삭제
    # return