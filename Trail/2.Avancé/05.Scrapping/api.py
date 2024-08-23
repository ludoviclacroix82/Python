import requests
import csv

key='73bbb95f8ecb49b499113a46481b4af1'
url ='https://newsapi.org/v2/top-headlines?sources=lequipe&apiKey='+key
response = requests.get(url)

# # Here the response format is a json file, it is used as a dictionary
dic=response.json()
# for elem in list(dic.keys()):
#     print('##############################################')
#     print("clé: ",elem,"// values: ", dic[elem])
    
# And now we have lists in dictionaries it's json but it's always the same thing
# We will discover the information of the article key
# for elem in enumerate(dic['articles']):
#     print('###############################################')
#     print(elem)

# So if we keep going, it gives us another dictionary!
# for elem in dic['articles'][1].keys():
#     print(' Key : ',elem,'Values : ',dic['articles'][0][elem])

numberArticle = len(dic['articles'])

for i in range(numberArticle-1, 5,-1):
    print(dic['articles'][i])


with open('articles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['Source', 'Author', 'Title', 'Description', 'URL', 'Published At', 'Content'])
    
    # Write data for each article
    for i in range(min(numberArticle, 5)):  # Use min to handle cases with fewer than 5 articles
        article = dic['articles'][i]
        writer.writerow([
            article.get('source', {}).get('name', 'N/A'),
            article.get('author', 'N/A'),
            article.get('title', 'N/A'),
            article.get('description', 'N/A'),
            article.get('url', 'N/A'),
            article.get('publishedAt', 'N/A'),
            article.get('content', 'N/A')
        ])
    