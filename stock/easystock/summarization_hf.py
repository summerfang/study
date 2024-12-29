from transformers import pipeline

def summarize_file(file_path, num_sentences=3, chunk_size=1000):
    # Load the summarization pipeline with a model that supports Chinese
    summarizer = pipeline("summarization", model="uer/pegasus-large-chinese")

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into chunks
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

    # Summarize each chunk
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=num_sentences * 20, min_length=num_sentences * 10, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Combine the summaries into a final summary
    final_summary = ' '.join(summaries)

    return final_summary

# Example usage
if __name__ == '__main__':
    file_path = 'downloads/特斯拉见顶了么, NVDA在筑底么。苹果还能涨么？.txt'
    summary = summarize_file(file_path)
    print(summary)