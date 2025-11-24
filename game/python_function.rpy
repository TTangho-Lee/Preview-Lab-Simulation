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




