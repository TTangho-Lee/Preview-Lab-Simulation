# gemini_api.rpy

init python:
    import requests
    import json
    # 🚨 API 키 (보안 주의)
    GEMINI_API_KEY = config_api_key 
    GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key=" + GEMINI_API_KEY

    def gemini_generate_response(system_prompt, summary, user_msg, current_affinity, player_name, context_instruction=None):
        
        # 추가 지시사항(스토리 상황)이 있으면 포함
        extra_inst = ""
        if context_instruction:
            current_condition = f"\n[현재 상황]: {context_instruction.split("/")[0]}\n"
            goal = f"\n[목표 상황]: {context_instruction.split("/")[1]}\n"

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": f"""
System Instruction:
{system_prompt}
{current_condition}
{goal}

Previous Summary:
{summary}

Current Affinity: {current_affinity}
Player Name: {player_name}

Player Said:
{user_msg}

Assistant Response Instruction:
1. 반드시 아래 포맷을 지켜라.
2. Current Affinity에 적절한 말투를 사용하여라. 0에 가까우면 딱딱하고 퉁명스럽게, 100에 가까우면 부드럽고 친절하게.
3. [현재 상황]에 적합한 말로 대화를 진행하여라.
4. 'charactor_emotion'은 상황에 맞게 캐릭터가 가지는 감정이다. 반드시 normal, smile, shy, sad, angry 중 하나여야 한다.
5. 'affinity_delta'는 대화 결과에 따라 현재 호감도에 더할 값(정수)이다. (-3 ~ +3)
6. 'is_ai_suspected': 만약 플레이어가 AI 여부를 의심하면 'true', 아니면 'false'로 적어라.
7. 'goal_achievement': 만약 대화내용이 [목표]를 충족하면 'true', 아니면 'false'로 적어라.
8. 무조건 다음의 형태에 맞춰서 답변을 만들어라
---
assistant_reply: <답변 내용>
charactor_emotion: <normal, smile, shy, sad, angry 중 하나>
updated_summary: <요약>
affinity_delta: <-3 ~ +3 사이의 숫자>
is_ai_suspected: <true/false>
goal_achievement: <true/false>
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

            #with open("C:/Users/seung/Downloads/gemini_raw_log.txt", "a", encoding="utf-8") as f:
            #    f.write(json.dumps(result, ensure_ascii=False) + "\n\n")


            if "candidates" not in result:
                return "...","normal", summary, current_affinity, False, False

            text = result["candidates"][0]["content"]["parts"][0]["text"]

            # 파싱
            reply = ""
            charactor_emotion="normal"
            updated_summary = summary
            affinity_delta = 0
            is_suspected = False
            goal_achievement = False

            for line in text.split("\n"):
                if line.startswith("assistant_reply:"):
                    reply = line.replace("assistant_reply:", "").strip()
                elif line.startswith("charactor_emotion:"):
                    charactor_emotion = line.replace("charactor_emotion:", "").strip()
                elif line.startswith("updated_summary:"):
                    updated_summary = line.replace("updated_summary:", "").strip()
                elif line.startswith("affinity_delta:"):
                    try:
                        affinity_delta = int(line.replace("affinity_delta:", "").strip())
                    except:
                        affinity_delta = 0
                elif line.startswith("is_ai_suspected:"):
                    val = line.replace("is_ai_suspected:", "").strip().lower()
                    if val == "true":
                        is_suspected = True
                elif line.startswith("goal_achievement:"):
                    val = line.replace("goal_achievement:", "").strip().lower()
                    if val == "true":
                        goal_achievement = True


            return reply, charactor_emotion, updated_summary, affinity_delta, is_suspected, goal_achievement

        except Exception as e:
            print(f"Gemini Error: {e}")
            return "지금은 대화가 어렵습니다.",charactor_emotion, summary, current_affinity, False, False