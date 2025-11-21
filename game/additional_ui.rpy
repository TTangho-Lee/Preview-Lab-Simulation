# ----------------------------------
# 설정 버튼 (우측 상단)
# ----------------------------------
screen top_menu():
    frame:
        xalign 1.0
        yalign 0.0
        background "#0008"
        padding (10, 10)

        textbutton "⚙ 설정" action ToggleScreen("config_menu")


screen config_menu():
    frame:
        xalign 0.85
        yalign 0.1
        background "#000c"
        padding (20,20)

        vbox:
            spacing 10

            textbutton "이름 변경" action Jump("change_name")
            textbutton "캐릭터 변경" action Jump("choose_character")
            textbutton "닫기" action Hide("config_menu")
            textbutton "전체 초기화" background "#a00" hover_background "#d00" padding (10, 10) action Show("reset_confirm")

# ----------------------------------
# 초기화
# ----------------------------------
screen reset_confirm():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        padding (40,40)
        background "#000c"
        xmaximum 600

        vbox:
            spacing 25
            xalign 0.5

            text "정말 모든 데이터를 초기화하시겠습니까?" size 36
            text "{color=#f55}이 작업은 되돌릴 수 없습니다!{/color}" size 28

            hbox:
                spacing 60
                xalign 0.5

                textbutton "예":
                    background "#a00"
                    hover_background "#d00"
                    padding (10,10)
                    action Jump("reset_all_data")

                textbutton "아니오":
                    background "#333"
                    hover_background "#555"
                    padding (10,10)
                    action Hide("reset_confirm")



label reset_all_data:

    hide screen reset_confirm
    hide screen config_menu   # 설정 메뉴 자동 닫기

    # 전체 초기화
    $ persistent._clear()
    $ renpy.save_persistent()

    "모든 데이터가 초기화되었습니다. 게임을 다시 시작합니다."

    $ renpy.pause(1.0)

    # 게임 완전 재시작
    $ renpy.full_restart()

# ----------------------------------
# 호감도 UI
# ----------------------------------
screen love_meter():
    frame:
        xalign 1.0
        yalign 0.2
        background "#0008"
        padding (20,20,20,20)
        vbox:

            if current_character == "haru":
                text "하루 호감도: [persistent.love_haru]"
                bar value persistent.love_haru range 100 xmaximum 200

            if current_character == "yuki":
                text "유키 호감도: [persistent.love_yuki]"
                bar value persistent.love_yuki range 100 xmaximum 200

            if current_character == "mina":
                text "미나 호감도: [persistent.love_mina]"
                bar value persistent.love_mina range 100 xmaximum 200