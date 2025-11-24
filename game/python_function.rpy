init python:
    def apply_love_change(delta):
        global love_haru, love_yuki, love_mina
        if delta is None:
            return
        if current_character == "haru":
            love_haru = max(0, min(100, love_haru + delta))
        elif current_character == "yuki":
            love_yuki = max(0, min(100, love_yuki + delta))
        elif current_character == "mina":
            love_mina = max(0, min(100, love_mina + delta))

    def get_character_expression(love):
        if love < 30:
            return "angry"
        elif love < 50:
            return "normal"
        elif love < 70:
            return "happy"
        elif love < 90:
            return "shy"
        else:
            return "love"

    def get_background(love):
        if love < 40:
            return "classroom"
        elif love < 70:
            return "park"
        elif love < 90:
            return "night"
        else:
            return "rooftop"

    def check_event(character):
        global talk_haru, talk_yuki, talk_mina
        global love_haru, love_yuki, love_mina

        if character == "haru":
            talk = talk_haru or 0
            love = love_haru or 0
        elif character == "yuki":
            talk = talk_yuki or 0
            love = love_yuki or 0
        elif character == "mina":
            talk = talk_mina or 0
            love = love_mina or 0
        else:
            talk = 0
            love = 0

        if talk >= 5 and love >= 40:
            return f"event_{character}_1"
        if talk >= 10 and love >= 60:
            return f"event_{character}_2"
        if talk >= 20 and love >= 90:
            return f"ending_{character}"
        return None
    def split_sentences(text):
        sentences = []
        current = []
        end_marks = {'.', '!', '?'}

        i = 0
        n = len(text)

        while i < n:
            ch = text[i]
            current.append(ch)

            # 문장 끝 문장부호 시작
            if ch in end_marks:
                # 뒤에 동일한 종류의 문장부호가 연속되면 하나로 묶기
                j = i + 1
                while j < n and text[j] in end_marks:
                    current.append(text[j])
                    j += 1

                # 문장 종료
                sentence = ''.join(current).strip()
                if sentence:
                    sentences.append(sentence)
                current = []

                i = j
                continue

            i += 1

        # 마지막 문장 (문장부호 없이 끝났을 때)
        if current:
            sentence = ''.join(current).strip()
            if sentence:
                sentences.append(sentence)

        return sentences




