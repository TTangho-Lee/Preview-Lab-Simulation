init python:
    import requests
    import json

    GEMINI_API_KEY = "AIzaSyBkdW7VhfUjVolfR_ceNsg1hO4W6HjkNfE"
    GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key=" + GEMINI_API_KEY

    def gemini_generate_response(system_prompt, summary, user_msg):
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": f"""
System Instruction:
{system_prompt}

Previous Summary:
{summary}

Player Said:
{user_msg}

Assistant Response Instruction:
1) 아래 응답 형식 그대로 따르세요:
---
assistant_reply: <AI의 대답>
updated_summary: <기존 summary + 이번 대화를 반영한 업데이트 요약>
---
"""}
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))
            result = response.json()

            # ====== 디버그용 전체 응답 출력 ======
            print("=== Gemini Raw Response ===")
            print(json.dumps(result, indent=4, ensure_ascii=False))

            # ====== 실패 처리 ======
            if "candidates" not in result:
                print("Gemini API 오류 발생 - candidates 없음")
                error_msg = result.get("error", {}).get("message", "Unknown error")
                print("Error:", error_msg)

                # 게임이 멈추지 않도록 기본 응답 처리
                return "죄송해요, 지금은 대답을 생성할 수 없어요.", summary

            text = result["candidates"][0]["content"]["parts"][0]["text"]

            # ---- 응답 파싱 ----
            reply = ""
            updated_summary = summary

            for line in text.split("\n"):
                if line.startswith("assistant_reply:"):
                    reply = line.replace("assistant_reply:", "").strip()
                elif line.startswith("updated_summary:"):
                    updated_summary = line.replace("updated_summary:", "").strip()

            # 비어 있을 경우 안전 처리
            if reply == "":
                reply = "흠... 방금 말한 내용을 조금 더 자세히 설명해줄 수 있을까?"

            return reply, updated_summary

        except Exception as e:
            # 네트워크/파싱 예외 처리
            print("Gemini Exception:", str(e))
            return "지금은 연결 상태가 좋지 않아. 잠시 후 다시 말해줘!", summary
