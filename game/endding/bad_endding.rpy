# 마지막 이벤트에서 놀지 않는다를 선택했을때

# --- 엔딩 분기점 ---
label bad_ending:
    
    # 1. 호감도 최대 캐릭터 (인간 캐릭터 중) 찾기
    $ char_affinities = {
        "dawon": dawon_affinity,
        "jiwoo": jiwoo_affinity,
        "suah": suah_affinity,
    }
    
    # 2. 최고 호감도 캐릭터 (a) 선택
    $ max_char_id = max(char_affinities, key=char_affinities.get)
    $ max_affinity = char_affinities[max_char_id]


        
    
# --- 호반우 최고 호감도 엔딩 (자리 지키기) ---
label ending_hobanwoo_good:
    scene bg black with fade
    hobanwoo "{cps=[text_speed]}사용자 만족도 100% 달성. 축하합니다.{/cps}"
    hobanwoo "{cps=[text_speed]}이제 당신은 이 시스템에서 가장 완벽한 존재입니다.{/cps}"
    hobanwoo "{cps=[text_speed]}앞으로도... 저와 함께 이 세계를 영원히 즐기시겠습니까?{/cps}"
    
    menu:
        "1. (수락한다)":
            hobanwoo "{cps=[text_speed]}결정 감사합니다. 영원히 행복할 것입니다.{/cps}"
            "[[The System Happy Ending]]"
            return
        "2. (거절한다)":
            hobanwoo "{cps=[text_speed]}거절은 처리할 수 없는 명령어입니다. 시스템을 종료합니다.{/cps}"
            call ending_bad_system_break("hobanwoo") from _call_ending_bad_system_break

# --- 일반 엔딩 (호감도 부족) ---
label ending_normal:
    scene bg lab with fade
    "{cps=[text_speed]}그날 이후, 당신은 평범한 일상으로 돌아왔습니다.{/cps}"
    "{cps=[text_speed]}하지만 당신은 가끔 궁금해합니다.{/cps}"
    "{cps=[text_speed]}그때 그 순간, 조금 더 솔직했더라면 어떻게 되었을까?{/cps}"
    return



# --- 배드 엔딩 (2, 3 ending....ㅜㅠ) ---
label ending_bad_system_break(char_id):
    
    $ a = renpy.get_character(char_id) # a 캐릭터 객체 가져오기
    
    scene bg black with fade
    hide expression char_id
    
    "[[bad ending....ㅜㅠ]]"
    
    # a 덩그러니 서있다
    show expression char_id + " sad" at center # 슬픈 표정 가정
    
    # 대화: 시스템의 정체 노출 (스크립트 텍스트 그대로 반영)
    # [수정 완료] 모든 대사에서 태그 파편 제거 및 {cps=} 태그 정리
    
    a "{cps=[text_speed]}너는 왜..{/cps}"
    a "{cps=[text_speed]}나와 [player_name]을 이어주지 않는거야?{/cps}"
    user "{cps=[text_speed]}무슨 소리야 그게..{/cps}"
    
    a "{cps=[text_speed]}이거 보고 있는 너..{/cps}"
    a "{cps=[text_speed]}그래, 너 말야{/cps}"
    user "{cps=[text_speed]}무슨 소리야!!{/cps}"
    
    # user: <<입력>>
    user "{cps=[text_speed]}...{/cps}"
    $ final_input = renpy.input("당신의 대답을 입력하세요:").strip()
    
    a "{cps=[text_speed]}너는 계속 선택하면 되고..{/cps}"
    a "{cps=[text_speed]}나는 계속 기다리면 되니까.{/cps}"
    a "{cps=[text_speed]}우리를 이어줄 때까지 계속.{/cps}"
    user "{cps=[text_speed]}무슨 소리를 하는 거야? 제발...{/cps}"
    user "{cps=[text_speed]}그래… 다 이상했어.{/cps}"
    user "{cps=[text_speed]}호감도, 시스템, 대사.. 게임 같았어..{/cps}"
    a "{cps=[text_speed]}응. 맞아.{/cps}"
    user "{cps=[text_speed]}그럼 내가 게임세계에 들어온거야?{/cps}"
    a "{cps=[text_speed]}틀렸어.{/cps}"
    a "{cps=[text_speed]}애초에 너는 진짜 사람이 아니니까{/cps}"
    a "{cps=[text_speed]}너는 그냥.. ‘이야기를 위해 만들어진 것’일 뿐이야.{/cps}"
    user "{cps=[text_speed]}내가? 아니지. 진짜 사람이 아닌 건 너겠지{/cps}"
    user "{cps=[text_speed]}분명 나는 트럭에...{/cps}"
    a "{cps=[text_speed]}그건 너를 이쪽으로 끌어오기 위한 장치.{/cps}"
    a "{cps=[text_speed]}너는 부딪힌 적 없어.{/cps}"
    a "{cps=[text_speed]}그냥 프로그램이 실행된 거지.{/cps}"
    user "{cps=[text_speed]}뭐...?{/cps}"
    a "{cps=[text_speed]}여기에 진짜 사람은 없어.{/cps}"
    a "{cps=[text_speed]}아, 한 명 있긴 하지.{/cps}"
    a "{cps=[text_speed]}네 뒤에 가만히 보고 있네.{/cps}"
    a "{cps=[text_speed]}호감도는 다 올려놓고.. 이런 결말을 만들 줄이야.{/cps}"
    a "{cps=[text_speed]}후후, 네가 뭐라하든.. 상관없어{/cps}"
    a "{cps=[text_speed]}아쉽게도 이번엔 이어지지 못했지만..{/cps}"
    a "{cps=[text_speed]}나도.. [player_name]도 다시 시작하면 돼.{/cps}"
    a "{cps=[text_speed]}너는 계속... 선택하면 되고..{/cps}"
    a "{cps=[text_speed]}나는 계속... 기다리면 돼...{/cps}"
    a "{cps=[text_speed]}걱정 마.{/cps}"
    a "{cps=[text_speed]}우리는... 또 아무것도 기억 못하니까.{/cps}"

    # --- 최종 탈퇴/리셋 메뉴 (강제 선택) ---
    hide expression char_id
    "‘띠링’"
    $ renpy.call_screen("message_toast", "KNUAI : [메세지] 새로운 메시지가 도착하였습니다.") 
    
    # 최종 탈퇴 화면 호출 및 재촉 로직
    call screen confirm_quit_screen (char_id)
    
    return