# gemini_api.rpy

init python:
    import requests
    import json
    # 🚨 API 키 (보안 주의)
    GEMINI_API_KEY = "AIzaSyBkdW7VhfUjVolfR_ceNsg1hO4W6HjkNfE" 
    GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key=" + GEMINI_API_KEY

    def gemini_generate_response(system_prompt, summary, user_msg, current_affinity, player_name, context_instruction=None):
        
        # 추가 지시사항(스토리 상황)이 있으면 포함
        extra_inst = ""
        if context_instruction:
            extra_inst = f"\n[현재 상황/목표]: {context_instruction}\n"

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": f"""
System Instruction:
{system_prompt}
{extra_inst}

Previous Summary:
{summary}

Current Affinity: {current_affinity}
Player Name: {player_name}

Player Said:
{user_msg}

Assistant Response Instruction:
1. 반드시 아래 포맷을 지켜라.
2. 'new_affinity'는 대화 결과에 따라 현재 호감도에 더할 값(정수)이다. (-5 ~ +5)
3. 'is_ai_suspected': 만약 플레이어가 AI 여부를 의심하면 'true', 아니면 'false'로 적어라.

---
assistant_reply: <답변 내용>
updated_summary: <요약>
new_affinity: <숫자>
is_ai_suspected: <true/false>
---
"""}
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload), timeout=10)
            result = response.json()

            if "candidates" not in result:
                return "...", summary, current_affinity, False

            text = result["candidates"][0]["content"]["parts"][0]["text"]

            # 파싱
            reply = ""
            updated_summary = summary
            affinity_delta = 0
            is_suspected = False

            for line in text.split("\n"):
                if line.startswith("assistant_reply:"):
                    reply = line.replace("assistant_reply:", "").strip()
                elif line.startswith("updated_summary:"):
                    updated_summary = line.replace("updated_summary:", "").strip()
                elif line.startswith("new_affinity:"):
                    try:
                        affinity_delta = int(line.replace("new_affinity:", "").strip())
                    except:
                        affinity_delta = 0
                elif line.startswith("is_ai_suspected:"):
                    val = line.replace("is_ai_suspected:", "").strip().lower()
                    if val == "true":
                        is_suspected = True

            # 최종 호감도 계산
            final_affinity = max(0, min(100, current_affinity + affinity_delta))

            return reply, updated_summary, final_affinity, is_suspected

        except Exception as e:
            print(f"Gemini Error: {e}")
            return "지금은 대화가 어렵습니다.", summary, current_affinity, False