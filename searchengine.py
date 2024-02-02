import requests
import sys

def findtitle(url):
    request=requests.get(url)
    content=request.content
    content=content.decode("utf-8")
    content=content.split("<title>")
    if len(content)<2:
        return ""
    content=content[1]
    content=content.split("</title>")
    title=content[0]
    return title

def findrank(titles,search):
    ranklist=[]
    for title in titles:
        rank=0
        if len(title)>=len(search):
            title=title.split()
            for j in title:
                if j in search:
                    rank+=1         
        else:
            search=search.split()
            for j in search:
                if j in title:
                    rank+=1 
        ranklist.append(rank)
    return ranklist


def rank(titles,search):
    ranklist=findrank(titles,search)
    for i in range(len(titles)):
        for j in range(len(titles)-1):
            if ranklist[j]<ranklist[j+1]:
                ranklist[j],ranklist[j+1]=ranklist[j+1],ranklist[j]
                titles[j],titles[j+1]=titles[j+1],titles[j]
    index=0
    for i in range(len(ranklist)):
        if ranklist[i]==0:
            index=i
            break
    ranklist=ranklist[:index]
    titles=titles[:index]
    return titles          



    
def search(search):
    titles={}
    file=open("crawl_bot\links.txt","r")
    links=file.read()
    links=links.split("\n")
    for link in links:
        try:
            if link[:6]!="https:" and link[:2]=="//":
                link="https:"+link
                          

            title=findtitle(link)
            titles[title]=link
        except (requests.exceptions.MissingSchema,requests.exceptions.InvalidSchema,requests.exceptions.SSLError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ConnectionError):
            continue
    rankedtitles=rank(list(titles.keys()),search)
    for title in rankedtitles:
        print(title,":",titles[title])

 
if len(sys.argv)!=2:
    print("INCORRECT USAGE OF ARGUMENTS TRY AGAIN")
else:
    search(sys.argv[1])