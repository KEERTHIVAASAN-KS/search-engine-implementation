import requests

def links(url):
    queue=[]
    
    request=requests.get(url)
    try:
        content=(request.content).decode("utf-8")
    except UnicodeError:
        return []
    content=content.split("href=")
    content.pop(0)

    for i in content:
        l=i.split(">")
        l=l[0]
        link=""
        if "'" in l:
            l=list(l)
            l.remove("'")
            if "'" in l:
                l.remove("'")
        elif '"' in l:
            l=list(l)
            l.remove('"')
            if '"' in l:
                l.remove('"')
        for j in l:
            link=link+j

        queue.append(link)
    q=[]
    for i in queue:
        if " " in i:
            link=i.split()
            link=link[0]
            q.append(link)
        else:
            q.append(i)

    for i in q:
        file=open("links.txt","a")
        file.write(i+"\n")
        file.close()
    return q

def crawl():
    while True:
        file=open("crawllist.txt","r+")
        ln=file.readlines()
        for i in range(len(ln)):
            ln[i]=ln[i].rstrip("\n")
        for url in ln:
            try:
                if url[:6]!="https:" and url[:2]=="//":
                    url="https:"+url
                q=links(url)
                for i in q:
                    if i not in ln:
                        file.write(i+"\n")
            except (requests.exceptions.InvalidSchema,requests.exceptions.MissingSchema,requests.exceptions.ReadTimeout,requests.exceptions.SSLError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ConnectionError):
                continue
        file.close()


crawl()
        

    
            



