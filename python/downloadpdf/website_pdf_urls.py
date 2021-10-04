# Import libraries
import requests
from bs4 import BeautifulSoup

def get_pdf_urls_from_a_website(url): 
    # Requests URL and get response object
    if url == None:
        return ""
    response = requests.get(url)
    
    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    
    # From all links check for pdf link and
    # if present download file
    for link in links:
        if ('.pdf' in link.get('href', [])):
            url_found = link.get('href');
            if url_found.find('/pdf/') > 0:
                return url_found
 
    return ""
    
if __name__ == "__main__":
    # URL from which pdfs to be downloaded
    url = "https://dl.acm.org/doi/10.1145/3173574.3173593"
    urls = get_pdf_urls_from_a_website(url)