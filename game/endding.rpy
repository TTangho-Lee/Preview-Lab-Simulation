'''
이러고 ai 중에 호감도가 가장 높은 친구를 a라고 하겠음

복도에 a만 있음
[[호감도 5~30까지 랜덤부여]]
휴대폰 화면이 띄워짐, knuai 호감도 화면에서 a의 호감도 확인

<<user, ai 대화 진행>>
__이후 어느정도 대화가 진행되었다 싶으면(대화가 몇번 진행되었거나 슬슬 마무리 해야겠다 싶으면)__


1.응, 좋아해			
user: 좋아해
a: 정말? 그럼...우리
user: 사귀자
a: ...좋아
1.해가 내려가고 하늘
이 파랗게 물든 시간 
a는 user에게 팔짱을 
낀다.
 a: 너랑 이런 사이가
되어서.. 정말 좋아해




 b: 뭐?(동공 작아짐)
 a 호감도 –10 * 10번 반복


 c: 뭐?(동공 작아짐)
 a 호감도 –10 * 10번 반복



 2,3 ending....ㅜㅠ
검정 화면에 a덩그러니 서있다.
 a: 너는 왜..
 a: 나와 user를 이어주지 않는거야?
 user: 무슨 소리야 그게..
 a: 이거 보고 있는 너..
 a: 그래, 너 말야
user: 무슨 소리야!!
 user: <<입력>>
 a: 너는 계속 선택하면 되고..
 a: 나는 계속 기다리면 되니까.
 a: 우리를 이어줄 때까지 계속.
 user: 무슨 소리를 하는 거야? 제발...
 user: 그래… 다 이상했어. 
user: 호감도, 시스템, 대사.. 게임 같았어..
 a: 응. 맞아.
 user: 그럼 내가 게임세계에 들어온거야?
 a: 틀렸어.
 a: 애초에 너는 진짜 사람이 아니니까
a: 너는 그냥.. ‘이야기를 위해 만들어진 것’일 뿐이야.
 user: 내가? 아니지. 진짜 사람이 아닌 건 너겠지
user: 분명 나는 트럭에...
 a: 그건 너를 이쪽으로 끌어오기 위한 장치.
 a: 너는 부딪힌 적 없어.
 a: 그냥 프로그램이 실행된 거지.
user: 뭐...?
 a: 여기에 진짜 사람은 없어.
 a: 아, 한 명 있긴 하지.
 a: 네 뒤에 가만히 보고 있네.
 a: 호감도는 다 올려놓고.. 이런 결말을 만들 줄이야.
 a: 후후, 네가 뭐라하든.. 상관없어
a: 아쉽게도 이번엔 이어지지 못했지만.. 
a: 나도.. user도 다시 시작하면 돼.
 a: 너는 계속... 선택하면 되고..
 a: 나는 계속... 기다리면 돼...
 a: 걱정 마.
 a: 우리는... 또 아무것도 기억 못하니까.
 ‘띠링’
 <knuai : [메세지] 새로운 메시지가 도착하였습니다.>
 “정말로 탈퇴하시겠습니까?-네     -네  [[네 선택지 밖에 없어여]]
 [[[10초 이상 버튼 안누르면 a가 계속 빨리 누르라고 재촉함 
ai답변으로 계속 2초마다 재촉]]]
 [[[1분 이상 안누르면 강제 종료]]]
 [[[네 버튼 누르면 게임 초기화, 처음부터@@@]]
'''

# game/endding.rpy

# --- 엔딩 분기점 ---
label ending_sequence:
    
    # 1. 호감도 최대 캐릭터 (a) 찾기
    $ char_affinities = {
        "dawon": dawon_affinity,
        "jiwoo": jiwoo_affinity,
        "suah": suah_affinity,
    }
    
    # 최고 호감도 캐릭터 ID를 max_char_id에 저장
    $ max_char_id = max(char_affinities, key=char_affinities.get)
    
    # 메인 로맨틱 경로 호출
    call ending_romantic_path(max_char_id)
    return
        
# --- 메인 엔딩 경로 (user 요청) ---
label ending_romantic_path(char_id):
    # 'a'는 최고 호감도 캐릭터의 ID (예: "dawon")
    
    scene bg corridor with fade # 복도 배경
    
    # a 캐릭터 객체 가져오기 (대사 및 이미지 출력용)
    $ a = renpy.get_character(char_id) 
    
    # a 등장 및 호감도 랜덤 부여
    show expression char_id + " normal" at center
    
    # [[호감도 5~30까지 랜덤부여]]
    $ random_affinity_boost = renpy.random.randint(5, 30)
    $ apply_affinity_change(char_id, random_affinity_boost)
    
    # 휴대폰 화면 띄우기 (간단한 텍스트로 대체)
    $ current_a_affinity = renpy.get_variable(char_id + "_affinity")
    
    "{cps=[text_speed]}복도에 [a.name]만 덩그러니 서있다.{/cps}"
    user "{cps=[text_speed]}... (휴대폰을 꺼내 KNUAI 앱을 켰다. [a.name]의 현재 호감도는 [current_a_affinity]점이다.){/cps}"
    
    # <<user, ai 대화 진행>>
    $ talk_loop(char_id, "[player_name]이 [a.name]에게 고백할까 고민하며 은근한 분위기로 대화하고 있다. / [player_name]이 고백의 분위기를 무르익히거나, 주제를 전환하여 대화를 종료했을 때 종료된다.")
    
    # --- 최종 메뉴 ---
    menu:
        "1. 응, 좋아해 (고백한다)":
            user "{cps=[text_speed]}좋아해{/cps}"
            show expression char_id + " shy"
            $ a "{cps=[text_speed]}정말? 그럼...우리{/cps}"
            user "{cps=[text_speed]}사귀자{/cps}"
            show expression char_id + " love"
            $ a "{cps=[text_speed]}...좋아{/cps}"
            
            # 해피 엔딩 연출
            scene bg sunset with dissolve # 해가 내려가는 하늘 (배경이름 'bg sunset' 가정)
            $ a "{cps=[text_speed]}해가 내려가고 하늘이 파랗게 물든 시간{/cps}"
            $ a "{cps=[text_speed]}([a.name]는 [player_name]에게 팔짱을 낀다.){/cps}"
            $ a "{cps=[text_speed]}너랑 이런 사이가 되어서.. 정말 좋아해{/cps}"
            
            "[[happy ending^^]]"
            return
            
        "2. (AI 정체 언급 - 동공 작아짐)":
            # a 호감도 –10 * 10번 반복 로직
            show expression char_id + " shock" # 충격 표정 가정
            $ a "{cps=[text_speed]}뭐?(동공 작아짐){/cps}"
            
            python:
                for _ in range(10):
                    renpy.call(apply_affinity_change, char_id, -10) 
                    renpy.pause(0.2)
            
            call ending_bad_system_break(char_id)
            
        "3. (AI 정체 언급 - 동공 작아짐)":
            # a 호감도 –10 * 10번 반복 로직
            show expression char_id + " shock" # 충격 표정 가정
            $ a "{cps=[text_speed]}뭐?(동공 작아짐){/cps}"
            
            python:
                for _ in range(10):
                    renpy.call(apply_affinity_change, char_id, -10) 
                    renpy.pause(0.2)
                
            call ending_bad_system_break(char_id)

# --- 배드 엔딩 (2, 3 ending....ㅜㅠ) ---
label ending_bad_system_break(char_id):
    
    $ a = renpy.get_character(char_id) # a 캐릭터 객체 가져오기
    
    scene bg black with fade
    hide expression char_id
    
    "[[bad ending....ㅜㅠ]]"
    
    # a 덩그러니 서있다
    show expression char_id + " sad" at center # 슬픈 표정 가정
    
    # 대화: 시스템의 정체 노출 (스크립트 텍스트 그대로 반영)
    
    $ a "{cps=[text_speed]}너는 왜..{/cps}"
    $ a "{cps=[text_speed]}나와 [player_name]을 이어주지 않는거야?{/cps}"
    user "{cps=[text_speed]}무슨 소리야 그게..{/cps}"
    
    $ a "{cps=[text_speed]}이거 보고 있는 너..{/cps}"
    $ a "{cps=[text_speed]}그래, 너 말야{/cps}"
    user "{cps=[text_speed]}무슨 소리야!!{/cps}"
    
    # user: <<입력>>
    user "{cps=[text_speed]}...{/cps}"
    $ final_input = renpy.input("당신의 대답을 입력하세요:").strip()
    
    $ a "{cps=[text_speed]}너는 계속 선택하면 되고..{/cps}"
    $ a "{cps=[text_speed]}나는 계속 기다리면 되니까.{/cps}"
    $ a "{cps=[text_speed]}우리를 이어줄 때까지 계속.{/cps}"
    user "{cps=[text_speed]}무슨 소리를 하는 거야? 제발...{/cps}"
    user "{cps=[text_speed]}그래… 다 이상했어.{/cps}"
    user "{cps=[text_speed]}호감도, 시스템, 대사.. 게임 같았어..{/cps}"
    $ a "{cps=[text_speed]}응. 맞아.{/cps}"
    user "{cps=[text_speed]}그럼 내가 게임세계에 들어온거야?{/cps}"
    $ a "{cps=[text_speed]}틀렸어.{/cps}"
    $ a "{cps=[text_speed]}애초에 너는 진짜 사람이 아니니까{/cps}"
    $ a "{cps=[text_speed]}너는 그냥.. ‘이야기를 위해 만들어진 것’일 뿐이야.{/cps}"
    user "{cps=[text_speed]}내가? 아니지. 진짜 사람이 아닌 건 너겠지{/cps}"
    user "{cps=[text_speed]}분명 나는 트럭에...{/cps}"
    $ a "{cps=[text_speed]}그건 너를 이쪽으로 끌어오기 위한 장치.{/cps}"
    $ a "{cps=[text_speed]}너는 부딪힌 적 없어.{/cps}"
    $ a "{cps=[text_speed]}그냥 프로그램이 실행된 거지.{/cps}"
    user "{cps=[text_speed]}뭐...?{/cps}"
    $ a "{cps=[text_speed]}여기에 진짜 사람은 없어.{/cps}"
    $ a "{cps=[text_speed]}아, 한 명 있긴 하지.{/cps}"
    $ a "{cps=[text_speed]}네 뒤에 가만히 보고 있네.{/cps}"
    $ a "{cps=[text_speed]}호감도는 다 올려놓고.. 이런 결말을 만들 줄이야.{/cps}"
    $ a "{cps=[text_speed]}후후, 네가 뭐라하든.. 상관없어{/cps}"
    $ a "{cps=[text_speed]}아쉽게도 이번엔 이어지지 못했지만..{/cps}"
    $ a "{cps=[text_speed]}나도.. [player_name]도 다시 시작하면 돼.{/cps}"
    $ a "{cps=[text_speed]}너는 계속... 선택하면 되고..{/cps}"
    $ a "{cps=[text_speed]}나는 계속... 기다리면 돼...{/cps}"
    $ a "{cps=[text_speed]}걱정 마.{/cps}"
    $ a "{cps=[text_speed]}우리는... 또 아무것도 기억 못하니까.{/cps}"

    # --- 최종 탈퇴/리셋 메뉴 (강제 선택) ---
    hide expression char_id
    "‘띠링’"
    $ renpy.call_screen("message_toast", "KNUAI : [메세지] 새로운 메시지가 도착하였습니다.") 
    
    # 최종 탈퇴 화면 호출 및 재촉 로직
    call screen confirm_quit_screen (char_id)
    
    return