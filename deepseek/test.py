# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "我女儿叫做xxx，是数据科学的研究生，还是一个歌手，今年重USC毕业，想在美国硅谷就业，请问对她的职业发展有什么建议？"},
    ],
    stream=False
)

print(response.choices[0].message.content)