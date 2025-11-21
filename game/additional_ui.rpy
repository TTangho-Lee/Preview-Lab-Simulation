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
    modal True

    # 화면 전체 클릭 시 설정창 닫기
    button:
        background Solid("#0000")  # 투명
        action Hide("config_menu")
        xysize (config.screen_width, config.screen_height)

    frame:
        xalign 0.85
        yalign 0.1
        background "#000c"
        padding (20,20)

        vbox:
            spacing 10

            textbutton "이름 변경" action Jump("change_name")
            textbutton "캐릭터 변경" action Jump("choose_character")
            # 메인 메뉴로 돌아가기 버튼
            textbutton "메인 메뉴" action MainMenu()
            # 게임 종료 버튼
            textbutton "나가기" action Quit(confirm=True)

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
                text "하루 호감도: [love_haru]"
                bar value love_haru range 100 xmaximum 200

            if current_character == "yuki":
                text "유키 호감도: [love_yuki]"
                bar value love_yuki range 100 xmaximum 200

            if current_character == "mina":
                text "미나 호감도: [love_mina]"
                bar value love_mina range 100 xmaximum 200