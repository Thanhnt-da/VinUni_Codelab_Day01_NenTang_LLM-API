import os
from openai import OpenAI

# Khởi tạo client (tự động đọc biến môi trường OPENAI_API_KEY nếu không truyền tham số)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Truyền đầy đủ model và messages vào hàm create
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Model tối ưu cho test/bài tập codelab
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in one simple sentence."}
    ],
    temperature=0.7,
    max_tokens=100
)

# Lấy nội dung phản hồi
print("Response:\n", response.choices[0].message.content)

# Lấy thông số token sử dụng
if response.usage:
    print(f"\nPrompt Tokens: {response.usage.prompt_tokens}")
    print(f"Completion Tokens: {response.usage.completion_tokens}")
    print(f"Total Tokens: {response.usage.total_tokens}")