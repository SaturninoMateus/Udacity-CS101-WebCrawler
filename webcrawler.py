'''
WebCrawler Udacity-CS101 Course
Name: Saturnino Mateus
Email: saturninonataniel@gec.inatel.br
'''
import urllib
 
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ''
 
def get_next_target(page): #seed page
    #This procedure get extract the first url from the page
    start_link = page.find('<a href=')
    #.find() method return -1 if is not in the string
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
 
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
  
def get_all_links(page): #L-30
    #This function have as paramenter the source of
    #the webpage and return a list of all url.
    links = []
    url, endpos  = get_next_target(page)
    while url:
        links.append(url)
        page = page[endpos:]
        url, endpos = get_next_target(page)
    return links
 
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if not(page in crawled):
            content = get_page(page)
            add_page_to_index(index, seed, content)
            union(tocrawl, get_eall_links(content))
            crawled.append(page)
    return index
 
  
def add_to_index(index, keyword, url):
        #Case keyword already in "index"
        for i in index:
            if i[0] == keyword:
                i[1].append(url)
                return
        #Case keyword isn't in "index"
        index.append([keyword,[url]])
 
def lookup(index, keyword):
    #This function return a list of all matched URL with the keyword.
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []
 
def add_page_to_index(index, url, content):
    #Content = Entire text of the text in url
    #Add all words in INDEX
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
