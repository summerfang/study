import urllib.request

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

if __name__ == '__main__': 
    pdf_path = 'https://arxiv.org/pdf/1808.01861.pdf'
    download_file(pdf_path, "1808.01861.pdf")