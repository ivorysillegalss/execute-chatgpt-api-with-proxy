import httpx
from openai import OpenAI

client = OpenAI(
    api_key='sk-api',
    http_client=httpx.Client(proxies={'http://': 'http://localhost:7890', 'https://': 'http://localhost:7890'})
)

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",  # 替换为当前可用的模型
    prompt="翻译 'Hello, world' 成中文",
    max_tokens=5
)

print(response)
