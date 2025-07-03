import requests
from config import DEEPSEEK_API_KEY

def ask_llm(prompt, context=""):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    full_prompt = f"""You are an assistant that answers questions based on the document below.

Context:
{context}

Question:
{prompt}
"""

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": full_prompt}],
        "temperature": 0.7
    }

    response = response = requests.post(url, headers=headers, json=payload, verify=False)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ DeepSeek API Error: {response.text}"