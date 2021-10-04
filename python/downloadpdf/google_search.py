try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
def find_first_website_contains_paper(paper_title):
    paper_title = 'site:dl.acm.org ' + paper_title
    for j in search(paper_title, tld="co.in", num=10, stop=10, pause=2):
        return j

    return ''

if __name__ == "__main__":
    paper_title = ""
    website_url = find_first_website_contains_paper(paper_title)
    print(website_url)

