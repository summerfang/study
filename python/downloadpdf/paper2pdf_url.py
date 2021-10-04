from google_search import find_first_website_contains_paper
from website_pdf_urls import get_pdf_urls_from_a_website
import re

def paper_title2url(paper_title):
    website_url = find_first_website_contains_paper(paper_title)
    if re.match(r"^https://dl.acm.org/doi/[1-9|.|/]", website_url):
        # https://dl.acm.org/doi/10.1145/3173574.3173575
        # https://dl.acm.org/doi/pdf/10.1145/3173574.3173575
        return website_url.replace(r'https://dl.acm.org/doi/',r'https://dl.acm.org/doi/pdf/')

    pdf_urls = get_pdf_urls_from_a_website(website_url)
    return pdf_urls

if __name__ == "__main__":
    paper_title = "Deep Thermal Imaging: Proximate Material Type Recognition in the Wild through Deep Learning of Spatial Surface Temperature Patterns"
    paper_pdf_url = paper_title2url(paper_title)