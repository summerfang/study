import google.generativeai as genai
import os

def summarize_file_in_chinese(file_path):
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)

    myfile = genai.upload_file(file_path)
    print(f"{myfile=}")

    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(
        [myfile, "\n\n", "请用中文总结文件的内容。"]
    )
    return result.text

# Example usage
if __name__ == "__main__":
    media = "/Users/fjb/study/stock/easystock/downloads/"
    file_path = media + "/美股年度推演, 2025美股还能涨么。涨到哪里, 会回调么.txt"
    summary = summarize_file_in_chinese(file_path)
    print(f"Summary: {summary}")