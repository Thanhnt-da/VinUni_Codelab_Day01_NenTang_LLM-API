# CALL_GEMINI_API.py
import os
from google import genai
from google.genai import types

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY chưa được thiết lập.")

# Khởi tạo client dùng chung cho toàn bộ dự án
client = genai.Client(api_key=api_key)

# Chỉ chạy phần test bên dưới khi bạn gõ: python CALL_GEMINI_API.py
if __name__ == "__main__":
    model = "gemini-3.5-flash-lite"
    prompt = "Explain quantum computing in one simple sentence."
    response = client.models.generate_content(model=model, contents=prompt)
    print("Test Call:", response.text)

# 2. Define inputs and model parameters
model = "gemini-3.5-flash-lite"
prompt = "Explain quantum computing in one simple sentence."
temperature = 0.7
top_p = 0.95
max_tokens = 100

# 3. Build config
config = types.GenerateContentConfig(
    temperature=temperature,
    top_p=top_p,
    max_output_tokens=max_tokens,
)

# 4. Generate content (single, valid call)
response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=config,
)

# 5. Output response and token counts
print("Response:\n", response.text)

if response.usage_metadata:
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    print(f"\nPrompt Tokens: {input_tokens}")
    print(f"Output Tokens: {output_tokens}")