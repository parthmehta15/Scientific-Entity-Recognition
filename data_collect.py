import urllib, urllib.request
import requests

def get_data(search_query, no_of_results):
    url = 'http://export.arxiv.org/api/query?search_query=all:<<query>>&start=0&max_results=<<no_of_results>>'
    search_query = search_query.replace(' ','%20')
    url = url.replace('<<query>>',search_query)
    url = url.replace('<<no_of_results>>',no_of_results)
    data = urllib.request.urlopen(url)
    master_data = data.read().decode('utf-8')
    return master_data


def download_file(download_url, doc_no):
    response = requests.get(download_url)
    file = open("document"+str(doc_no)+".pdf", 'wb')
    file.write(response.content)
    file.close()
    print("Completed")
