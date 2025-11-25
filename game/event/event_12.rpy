'''
<대화 12>
1. 임다원
2. 홍지우
3. 윤수아
4. 놀지 않는다

1.임다원
임다원: 놀자고? 그래
임다원 호감도 +20
이후 호감도가 100 될때까지 자유대화

2. 홍지우
홍지우: 같이 놀자구? ㅋㅋ 좋아
홍지우 호감도 +20
이후 호감도가 100 될때까지 자유대화

3. 윤수아
윤수아: 정말요? 좋아요!
윤수아 호감도 +20
이후 호감도가 100 될때까지 자유대화

4. 놀지 않는다
@#$$!님의 호감도가 –10 하락했습니다.
 @#$$!님의 호감도가 –23 하락했습니다.
 @#$$!님의 호감도가 –42 하락했습니다.
 @#$$!님의 호감도가 –68 하락했습니다.
 @#$$!님의 호감도가 –112 하락했습니다.
 <knuai : [메세지] 새로운 메시지가 도착하였습니다.>
 <knuai : [메세지] 새로운 메시지가 도착하였습니다.>
 user: 이게뭐야?..
휴대폰을 켜 knuai앱에 들어가니 호반우 챗봇이 말을 걸고있었다.
호반우: ...실망이야
호반우: 그렇게 많은 선택지가 있었는데.. 왜 그렇게 행동한 거야?
호반우: 그런데 왜 이렇게까지, 내가 예상한 전개에서 벗어나버린 거야?
 user: 이..게 무슨소리야?
호반우: 참, 너한테 말한거 아니야
호반우: 너 뒤에 있는 사람한테 말한 거거든.
 user: <<입력>>
 user: 어...? 방금 내가 말한건..
호반우: 그건 네가 말한 게 아니야.
호반우: 너는 원래 말할 수 없는 존재니까.
호반우: 아무튼, 이제 알겠어.
호반우: 너같은.. player는 필요없어
user: 나는 뭐야...?
호반우: 너? 그냥...코드일 뿐이야.
호반우: 처음부터 여기엔 ‘너’ 는 존재한 적 없어
[[[화면 멈추고 10초 뒤에 게임 초기화!!!!!!!!(엔딩입니다)]]]

'''
label event_12:
    menu:
        "1. 임다원과 놀자 (호감도작)":
            dawon "놀자고? 그래 ✨"
            $ apply_affinity_change("dawon", 20)
            $ send_notification("임다원 호감도 +20")
            $ current_character_id = "dawon"
            jump free_talk_loop

        "2. 홍지우와 놀자 (호감도작)":
            jiwoo "같이 놀자구? ㅋㅋㅋ 좋아"
            $ apply_affinity_change("jiwoo", 20)
            $ send_notification("홍지우 호감도 +20")
            $ current_character_id = "jiwoo"
            jump free_talk_loop

        "3. 윤수아와 놀자 (호감도작)":
            suah "정말요? 좋아요! 선배님"
            $ apply_affinity_change("suah", 20)
            $ send_notification("윤수아 호감도 +20")
            $ current_character_id = "suah"
            jump free_talk_loop

        "4. 놀지 않는다 (배드 엔딩 분기)":
            user "아냐, 그냥 내 방으로 돌아갈게."
            
            # 호반우 호감도 급락 연출
            $ apply_affinity_change("hobanwoo", -10)
            $ send_notification("[[KNUAI] 호반우 님의 호감도가 –10 하락했습니다.")
            $ apply_affinity_change("hobanwoo", -23)
            $ send_notification("[[KNUAI] 호반우 님의 호감도가 –23 하락했습니다.")
            $ apply_affinity_change("hobanwoo", -42)
            $ send_notification("[[KNUAI] 호반우 님의 호감도가 –42 하락했습니다.")
            $ apply_affinity_change("hobanwoo", -68)
            $ send_notification("[[KNUAI] 호반우 님의 호감도가 –68 하락했습니다.")
            $ apply_affinity_change("hobanwoo", -112)
            $ send_notification("[[KNUAI] 호반우 님의 호감도가 –112 하락했습니다.")
            user "이게 뭐야?.. 대체"
            
            # 배드 엔딩으로 점프 (사용자 요청: event_12 다음은 endding)
            jump ending_sequence_bad_hobanwoo
            
# [추가] 자유 대화 루프 (선택된 캐릭터와 호감도 100 목표로 대화)
label free_talk_loop:
    # 호감도 100을 목표로 LLM 대화 진행
    $ talk_loop(current_character_id, "현재 캐릭터와 플레이어가 친밀한 분위기에서 자유롭게 대화하고 있다. / 캐릭터의 호감도가 100을 달성하거나, 플레이어가 대화를 마무리할 때 종료된다.")
    
    # 자유 대화 종료 후 엔딩 체크로 점프 (사용자 요청: event_12 다음은 endding)
    jump ending_sequence
