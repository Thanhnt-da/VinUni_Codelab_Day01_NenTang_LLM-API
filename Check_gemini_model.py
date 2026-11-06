import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY chưa được thiết lập trong biến môi trường.")

client = genai.Client(api_key=api_key)

print("=== CÁC MODEL BẠN ĐƯỢC PHÉP DÙNG ===")
for model in client.models.list():
    # In ra tên định danh của model
    print(model.name)