# gemini_api.rpy

init python:
    import requests
    import json

    GEMINI_API_KEY = "AIzaSyBkdW7VhfUjVolfR_ceNsg1hO4W6HjkNfE"
    GEMINI_URL = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.0-flash-lite:generateContent?key=" + GEMINI_API_KEY
    )


    def gemini_generate_response(system_prompt, summary, user_msg):

        # 최근 3개 대화 포함
        history_text = "\n".join(persistent.dialog_history)

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": f"""
System Instruction:
{system_prompt}

현재 호감도: {persistent.love}
지금까지 대화 횟수: {persistent.talk_count}

최근 대화 3개:
{history_text}

이전 요약:
{summary}

플레이어 입력:
{user_msg}

==============================
### 반드시 아래 형식으로만 답변해라 ###
assistant_reply: <샌즈의 말투로 대답>
love_change: <-5에서 +5 사이 숫자>
updated_summary: <새 요약>
==============================

주의:
- 샌즈 특유의 건조한 개그톤 유지.
- 호감도가 높을수록 말투가 더 부드러워짐.
- love_change는 대화 분위기 기반으로 설정.
"""}
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))
            result = response.json()

            print("=== Gemini Raw Response ===")
            print(json.dumps(result, indent=4, ensure_ascii=False))

            if "candidates" not in result:
                print("Gemini API 오류 - candidates 없음")
                error_msg = result.get("error", {}).get("message", "Unknown error")
                print("Error:", error_msg)
                return "오류가 발생했어. 다시 말해줘.", 0, summary

            text = result["candidates"][0]["content"]["parts"][0]["text"]

            reply = ""
            love_change = 0
            updated_summary = summary

            for line in text.split("\n"):
                if line.startswith("assistant_reply:"):
                    reply = line.replace("assistant_reply:", "").strip()

                elif line.startswith("love_change:"):
                    try:
                        love_change = int(line.replace("love_change:", "").strip())
                    except:
                        love_change = 0

                elif line.startswith("updated_summary:"):
                    updated_summary = line.replace("updated_summary:", "").strip()


            if reply == "":
                reply = "흠… 방금 한 말을 다시 한번 설명해줄래?"

            return reply, love_change, updated_summary


        except Exception as e:
            print("Gemini Exception:", str(e))
            return "지금은 연결이 불안정하네. 잠시 후 다시 시도해줘!", 0, summary
