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

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{
                        "text": f"""
System Instruction:
{system_prompt}

플레이어 이름: {persistent.player_name}

최근 3개 대화:
{summary}

플레이어가 말했다:
{user_msg}

--- 반드시 아래 형식으로만 대답 ---
assistant_reply: <캐릭터 말투의 대사>
love_change: <-5 ~ +5 정수>
updated_summary: <대화 요약>
------------------------------------
""" }]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))
            result = response.json()

            text = result["candidates"][0]["content"]["parts"][0]["text"]

            reply = ""
            delta = 0
            new_summary = summary

            for line in text.split("\n"):
                if line.startswith("assistant_reply:"):
                    reply = line.replace("assistant_reply:", "").strip()

                elif line.startswith("love_change:"):
                    try:
                        delta = int(line.replace("love_change:", "").strip())
                    except:
                        delta = 0

                elif line.startswith("updated_summary:"):
                    new_summary = line.replace("updated_summary:", "").strip()

            return reply, delta, new_summary

        except:
            return "지금은 연결이 좋지 않아… 다시 말해줄래?", 0, summary
