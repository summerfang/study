import os
import sys
import openai
from dotenv import load_dotenv
import argparse

load_dotenv()

# 设置 OpenAI API 密钥从 .env 文件中读取
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY not found in environment variables.")
    sys.exit(1)


def summarize_article(article_text):
    try:

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # 使用支持的聊天模型
            messages=[
                {"role": "system", "content": "你是一个有帮助的助理。"},
                {"role": "user", "content": f"请总结以下文章的内容，并判断市场趋势是“上升”、“下降”还是“持平”：\n\n{article_text}\n\n总结："}
            ],
            max_tokens=150,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        summary = response.choices[0].message['content'].strip()
        return summary
    # except openai.error.OpenAIError as e:
    #     print(f"OpenAI API 错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    return None

def judge_trend(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            article_text = file.read()
            if not article_text.strip():
                print("文件为空。")
                return

        summary = summarize_article(article_text)
        if summary:
            print(f"总结与市场趋势判断:\n{summary}")
        else:
            print("无法生成总结。")
    except FileNotFoundError:
        print("未找到文件。")
    except IOError as io_err:
        print(f"I/O 错误: {io_err}")
    except Exception as e:
        print(f"发生错误: {e}")

def main():
    parser = argparse.ArgumentParser(description="使用 OpenAI API 总结文章并判断市场趋势。")
    parser.add_argument("file_path", type=str, help="输入文章文件的路径。")
    args = parser.parse_args()
    judge_trend(args.file_path)

if __name__ == "__main__":
    main()