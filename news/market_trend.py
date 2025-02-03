import os
import argparse
import logging
from snownlp import SnowNLP

def determine_trend(text):
    """
    根据股评内容判断股票走势。

    Args:
        text (str): 股评文本内容。

    Returns:
        str: "上涨"、"下跌" 或 "持平"。
    """
    s = SnowNLP(text)
    sentiment = s.sentiments  # 情感得分，0到1之间
    if sentiment > 0.6:
        return "上涨"
    elif sentiment < 0.4:
        return "下跌"
    else:
        return "持平"

def main():
    parser = argparse.ArgumentParser(description="分析股评并预测股票走势。")
    parser.add_argument('file_path', type=str, help='包含股评的本地文件路径。')
    args = parser.parse_args()

    # 配置日志
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if not os.path.exists(args.file_path):
        logging.error(f"文件不存在: {args.file_path}")
        return

    with open(args.file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    trend = determine_trend(content)
    print(f"预测股票走势: {trend}")

if __name__ == "__main__":
    main()