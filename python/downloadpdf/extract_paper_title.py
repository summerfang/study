import re
from paper2pdf_url import paper_title2url
from download_pdf_selenium import download_pdf_by_webdriver

def download_papers_from_conference(file_name, store_path):
    paper_source = open(file_name,'r')
    paper_source_string = paper_source.read()
    paper_source.close()

    pattern_string = 'Paper [0-9]+:.*\n'
    paper_titles_with_order = re.findall(pattern_string,paper_source_string, re.MULTILINE)

    paper_titles = []
    for title in paper_titles_with_order:
        pos_colon = title.index(':')
        if pos_colon >= 0:
            title = title[pos_colon + 1:].strip()
        
        paper_titles.append(title)

    paper_and_url = []
    for paper in paper_titles:
        row = []
        paper_pdf_url = paper_title2url(paper)
        row.append(paper)
        row.append(paper_pdf_url)

        paper_and_url.append(row)
        print(row)

        if paper_pdf_url != '':
            download_pdf_by_webdriver(store_path, paper_pdf_url, paper)
    
if __name__ == '__main__':
    acm_2018 = 'sample.txt'
    store_path_acm_2018 = '/Users/jianbfan/Desktop/github/study/python/downloadpdf/acm2018'
    download_papers_from_conference(acm_2018, store_path_acm_2018)
