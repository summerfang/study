from openai import OpenAI
import os
import textwrap

def split_text(text, max_chunk_size=4000):
    """Split text into chunks of maximum size."""
    return textwrap.wrap(text, max_chunk_size, break_long_words=False, break_on_hyphens=False)

def summarize_file(file_path, api_key, num_sentences=3):
    client = OpenAI(api_key=api_key)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into chunks if it's too large
    chunks = split_text(content)
    chunk_summaries = []
    
    # Summarize each chunk
    for chunk in chunks:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"用{num_sentences}句话总结以下内容:\n\n{chunk}"}
            ],
            max_tokens=150
        )
        chunk_summaries.append(response.choices[0].message.content.strip())
    
    # If we have multiple chunks, summarize the summaries
    if len(chunk_summaries) > 1:
        final_text = "\n\n".join(chunk_summaries)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"用{num_sentences}句话总结以下内容:\n\n{final_text}"}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    
    return chunk_summaries[0]

if __name__ == '__main__':
    # Example usage
    file_path = 'downloads/特斯拉见顶了么, NVDA在筑底么。苹果还能涨么？.txt'
    api_key = os.getenv('OPENAI_API_KEY')
    
    try:
        summary = summarize_file(file_path, api_key)
        print("文件摘要:")
        print(summary)
    except Exception as e:
        print(f"发生错误: {str(e)}")
