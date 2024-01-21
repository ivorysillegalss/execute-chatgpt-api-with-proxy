import openai
import requests

proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890'
}

openai.api_key = 'sk-api'

response = requests.post(
    "https://api.openai.com/v1/engines/gpt-3.5-turbo-instruct/completions",
    headers={
        "Authorization": "Bearer " + openai.api_key,
    },
    json={
        "prompt": "你有历史记录功能吗",
        "max_tokens": 60
    },
    proxies=proxies
)

print(response.json())

