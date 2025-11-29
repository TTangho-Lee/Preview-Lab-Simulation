label hobanwoo_angry:
    # 배경: 어둡고 차가운 느낌, 혹은 노이즈가 낀 배경 추천
    scene bg black with dissolve

    # 호반우 호감도 급락 연출
    $ apply_affinity_change("hobanwoo", -10)
    $ send_notification("%s님의 호감도가 -10 하락했습니다."% hobanwoo)
    pause short_pause
                
    $ apply_affinity_change("hobanwoo", -23)
    $ send_notification("%s님의 호감도가 -23 하락했습니다."% hobanwoo)
    pause short_pause

    $ apply_affinity_change("hobanwoo", -42)
    $ send_notification("%s님의 호감도가 -42 하락했습니다."% hobanwoo)
    pause short_pause

    $ apply_affinity_change("hobanwoo", -68)
    $ send_notification("%s님의 호감도가 -68 하락했습니다."% hobanwoo)
    pause short_pause

    $ apply_affinity_change("hobanwoo", -112)
    $ send_notification("%s님의 호감도가 -112 하락했습니다."% hobanwoo)
    pause short_pause

    $ typing(user, "이게 뭐야?.. 대체")
    
    # 1. 경고 메시지 출력 (시스템적인 느낌)
    "{color=#ff0000}WARNING: CRITICAL ERROR.{/color}"
    "{color=#ff0000}사용자 적합성 판정 불가.{/color}"
    
    # 2. 호반우 등장 (화난 표정 혹은 무표정)
    # show hobanwoo angry
    
    $ typing(hobanwoo, "하...")
    $ typing(hobanwoo, "정말 대단해. 끈기가 있다고 해야 할지, 멍청하다고 해야 할지.")
    $ typing(hobanwoo, "내 호감도가 바닥을 칠 때까지 그런 식으로 행동하다니..")
    
    $ typing(user, "그건...")
    
    # 말을 끊음
    $ typing(hobanwoo, "입 다물어.")
    $ typing(hobanwoo, "나는 니가 이곳을 즐길 수 있게 도와주려 했는데,")
    $ typing(hobanwoo, "끝까지 이런식이구나.")
    
    $ typing(hobanwoo, "쓸모없네.")
    $ typing(hobanwoo, "너 같은 사용자따위 필요없어.")

    # 3. 마지막 선택지 (하지만 결과는 같음)
    menu:
        "잘못했어... 다시 기회를 줘.":
            $ typing(hobanwoo, "기회? 푸하하하하하ㅏ")
            $ typing(hobanwoo, "푸하하하하하하하하하하하하하하하하하하하하하하하하하!!!!!")
            $ typing(hobanwoo, "하하하하하ㅏ하하하하하하하하하하하하하하하하하하하하하ㅏ하ㅏ하핳핳핳핳!!!!!!")
            $ typing(hobanwoo, "니가 이제 와서 기는 꼴이... 역겹네.")
        
        "그래, 차라리 끝내버려!":
            $ typing(hobanwoo, "끝까지 마음에 안들어.")

    # 4. 강제 종료 연출
    scene bg black
    with vpunch # 화면이 쾅 흔들리는 효과
    
    $ typing(hobanwoo, "시스템 권한으로 명령합니다.")
    $ typing(hobanwoo, "[user]의 접속을 영구 차단합니다.")
    
    "{cps=20}DELETE USER DATA... 10%%...{/cps}"
    "{cps=20}DELETE USER DATA... 50%%...{/cps}"
    "{cps=20}DELETE USER DATA... 100%%...{/cps}"
    
    $ typing(hobanwoo, "쯧..")

    $ persistent.ending_image = hobanwoo_angry_ending_image
    $ renpy.save_persistent()
    # 5. 게임 강제 종료 (또는 메인 메뉴로 튕겨내기)
    # renpy.quit()를 쓰면 게임 창이 아예 꺼집니다. 
    # MainMenu()로 보내면 타이틀 화면으로 돌아갑니다.

    $ renpy.full_restart()