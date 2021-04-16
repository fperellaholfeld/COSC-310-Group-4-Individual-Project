from mediawiki import MediaWiki
import mediawiki
from requests.models import Response

def getArticle(movie):
    wiki = MediaWiki()
    result = wiki.search(movie, results=3)
    page = wiki.page(result[0])
    return page

def getSummary(movie):
    page = getArticle(movie)
    print('IMDBot:', page.summarize())
    return

def getCritical(movie):
    page = getArticle(movie)
    check = False
    for sec in page.sections:
        if (('critical' in sec.lower() or 'reception' in sec.lower() or 'response' in sec.lower()) and page.section(sec) != ''):
            print('IMDBot:', page.section(sec))
            check = True
            break
    if (check == False):
        print('IMDBot: I\'m not able to find the critical reception for this movie, sorry.')
    return

def getPlot(movie):
    page = getArticle(movie)
    check = False
    for sec in page.sections:
        if ('plot' in sec.lower()):
            print('IMDBot:', page.section(sec))
            check = False
            break
    if (check == False):
        print()