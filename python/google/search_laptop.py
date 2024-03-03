
# params = {
#     "q": "laptop",  # Your search query
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# print(results)
# # Extract relevant data from 'results'
# # (e.g., product titles, prices, and links)


from googlesearch import search

query = "laptop"
for result in search(query):
    print(result)

from googlesearch.googlesearch import GoogleSearch

response = GoogleSearch().search("something")
for result in response.results:
    print("Title:", result.title)
    print("Content:", result.getText())
