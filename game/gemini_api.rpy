init python:
    import requests
    import json
    import renpy

    # 🚨 보안 경고: 실제 배포 시 API 키를 코드에 직접 노출하는 것은 위험합니다.
    GEMINI_API_KEY = "AIzaSyBkdW7VhfUjVolfR_ceNsg1hO4W6HjkNfE"
    GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key=" + GEMINI_API_KEY

    # [수정] player_name 매개변수 추가 및 모든 return 경로가 3개의 값을 반환하도록 수정
    def gemini_generate_response(system_prompt, summary, user_msg, current_affinity, player_name, event_goal=None):
        event_instruction = ""
        if event_goal:
            event_instruction = f"""
            --- EVENT INSTRUCTION ---
            지금부터는 스토리상 매우 중요한 이벤트가 진행 중입니다. 당신의 목표는:
            {event_goal}
            이 목표를 달성할 때까지, 플레이어의 말에 맞춰 자연스럽게 대화하며 목표를 향해 대화를 이끌어 나가세요.
            -------------------------
            """
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": f"""
System Instruction:
{system_prompt}
{event_instruction}

Previous Summary:
{summary}

Current Affinity Score (Out of 100):
{current_affinity}

Player Name: {player_name} # <--- 이름 추가

Player Said:
{user_msg}

Assistant Response Instruction:
1) 응답 형식 그대로 따르세요.
2) 대화 내용을 바탕으로 플레이어와의 관계가 긍정적이면 +1~+5, 부정적이면 -1~-5를 더한 **새 호감도 점수**를 100점 만점으로 계산하세요.
3) 대화 시 {player_name} 님을 이름으로 불러주세요. # <--- 이름 사용 지침 추가
---
assistant_reply: <AI의 대답>
updated_summary: <기존 summary + 이번 대화를 반영한 업데이트 요약>
new_affinity: <업데이트된 호감도 점수 (숫자만)>
---
"""}
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        try:
            # 타임아웃 추가하여 게임 멈춤 방지
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload), timeout=30) 
            result = response.json()

            # ====== 디버그용 전체 응답 출력 ======
            print("=== Gemini Raw Response ===")
            print(json.dumps(result, indent=4, ensure_ascii=False))

            # ====== 실패 처리: candidates 없음 ======
            if "candidates" not in result:
                print("Gemini API 오류 발생 - candidates 없음")
                error_msg = result.get("error", {}).get("message", "Unknown error")
                print("Error:", error_msg)
                # 오류 시 3개 값 반환 (호감도 유지)
                return "죄송해요, 지금은 대답을 생성할 수 없어요.", summary, current_affinity

            text = result["candidates"][0]["content"]["parts"][0]["text"]

            # ---- 응답 파싱 ----
            reply = ""
            updated_summary = summary
            new_affinity_str = str(current_affinity) 

            for line in text.split("\n"):
                if line.startswith("assistant_reply:"):
                    reply = line.replace("assistant_reply:", "").strip()
                elif line.startswith("updated_summary:"):
                    updated_summary = line.replace("updated_summary:", "").strip()
                elif line.startswith("new_affinity:"):
                    new_affinity_str = line.replace("new_affinity:", "").strip()
            
            # 비어 있을 경우 안전 처리
            if reply == "":
                reply = "흠... 방금 말한 내용을 조금 더 자세히 설명해줄 수 있을까?"
            
            # 호감도 숫자로 변환
            try:
                new_affinity = int(new_affinity_str)
            except ValueError:
                new_affinity = current_affinity # 파싱 실패 시 현재 값 유지

            # 최종 성공 반환
            return reply, updated_summary, new_affinity # <--- 올바른 위치와 반환값

        except Exception as e:
            # 네트워크/파싱 예외 처리 시 3개 값 반환
            print("Gemini Exception:", str(e))
            return "지금은 연결 상태가 좋지 않아. 잠시 후 다시 말해줘!", summary, current_affinity