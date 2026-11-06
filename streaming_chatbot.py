import os
import sys
from google import genai
from google.genai import types

# 1. Khởi tạo client (hoặc import client từ CALL_GEMINI_API)
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    from CALL_GEMINI_API import client
else:
    client = genai.Client(api_key=api_key)

model = "gemini-3.5-flash-lite"

# 2. Khai báo danh sách lưu lịch sử hội thoại trước khi bắt đầu chat
formatted_history = []

print("=== CHATBOT STREAMING (Gõ 'exit' hoặc 'quit' để dừng) ===")

while True:
    user_prompt = input("\nBạn: ").strip()
    if not user_prompt:
        continue
    if user_prompt.lower() in ["exit", "quit"]:
        print("Tạm biệt!")
        break

    # Thêm câu hỏi của người dùng vào lịch sử theo định dạng Content
    formatted_history.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_prompt)]
        )
    )

    print("AI: ", end="", flush=True)

    try:
        # Gửi toàn bộ lịch sử hội thoại vào contents
        response_stream = client.models.generate_content_stream(
            model=model,
            contents=formatted_history
        )

        full_response_text = ""
        for chunk in response_stream:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                full_response_text += chunk.text
        print()

        # Lưu câu trả lời của AI vào lịch sử để duy trì ngữ cảnh cho câu hỏi kế tiếp
        formatted_history.append(
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=full_response_text)]
            )
        )

    except Exception as e:
        print(f"\nLỗi khi stream nội dung: {e}", file=sys.stderr)