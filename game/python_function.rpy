init python:
    def apply_affinity_change(name,delta):
        global dawon_affinity, jiwoo_affinity, suah_affinity, hobanwoo_affinity, professor_affinity
        if delta is None:
            return
        if name == "dawon":
            dawon_affinity = max(0, min(100, dawon_affinity + delta))
        elif name == "jiwoo":
            jiwoo_affinity = max(0, min(100, jiwoo_affinity + delta))
        elif name == "suah":
            suah_affinity = max(0, min(100, suah_affinity + delta))
        elif name=="hobanwoo":
            hobanwoo_affinity = max(0, min(100, hobanwoo_affinity + delta))
        elif name=="professor":
            professor_affinity = max(0, min(100, professor_affinity + delta))

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


    def eunneun(name):
        # 받침이 있으면 "은", 없으면 "는"
        return "은" if is_jong(name) else "는"

    def iga(name):
        # 받침이 있으면 "이", 없으면 "가"
        return "이" if is_jong(name) else "가"
    
    def eulreul(name):
        # 받침 있으면 '을', 없으면 '를'
        ch = ord(name[-1]) - 0xAC00
        jong = ch % 28
        return "을" if jong != 0 else "를"

    def is_jong(name):
        # 한글 받침 여부 확인
        if len(name) == 0:
            return False
        ch = ord(name[-1]) - 0xAC00
        jong = ch % 28
        return jong != 0



