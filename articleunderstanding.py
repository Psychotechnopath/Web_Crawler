import requests
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions

#keys
newskey = "4430c65cad4d4b8b9a5660b18c1d0dfe" #powered by newsapi.org
watsonkey = "g-YqWDDroCfNkNDv0RbMhdNNxKUHNeflvivnFqw29V3c"
watsonurl = "https://gateway-lon.watsonplatform.net/natural-language-understanding/api"

#functions
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2019-07-12', iam_apikey=watsonkey, url=watsonurl)

#search news parameters
country = ""
category = "business" #business entertainment general health science sports technology
q = "bitcoin"
sources = "" #or see https://newsapi.org/sources
searchin = "everything" # "top-headlines" or "everything"
maxresults = 4

def search():
    if searchin == "everything":
        if category == True:
            newsurl = ('https://newsapi.org/v2/'+searchin+ "?category="+ category+ "&q="+q+"&apiKey="+newskey +"&pageSize=100")
        else:
            newsurl = ('https://newsapi.org/v2/'+searchin+ "?sources="+ sources+ "&q="+q+"&apiKey="+newskey +"&pageSize=100")
    else:
        if country or category == True:
            newsurl = ('https://newsapi.org/v2/'+searchin+ "?country="+ country+ "&category="+category+"&q="+q+"&apiKey="+newskey +"&pageSize=100")
        else:
            newsurl = ('https://newsapi.org/v2/'+searchin+ "?sources="+ sources+ "&q="+q+"&apiKey="+newskey +"&pageSize=100")
    print("Constructed search url with query: '"+ q + "' in '" + searchin + "' for a maximum results of " + maxresults)
    news = requests.get(newsurl).json()
    print("Found "+ str(len(news["articles"])) + " news articles")
    return news

def understand(news):
    urllist = [news["articles"][i]["url"] for i in range(0, min(maxresults, len(news["articles"])))]
    values = []
    for j, i in enumerate(urllist):
        value = {}
        response = natural_language_understanding.analyze(url=i, features=Features(sentiment=SentimentOptions(),emotion=EmotionOptions())).get_result()
        value['url'] = response['retrieved_url']
        value['sentiment'] = response["sentiment"]["document"]["score"]
        value['sadness'] = response["emotion"]["document"]["emotion"]["sadness"]
        value['joy'] = response["emotion"]["document"]["emotion"]["joy"]
        value['fear'] = response["emotion"]["document"]["emotion"]["fear"]
        value['disgust'] = response["emotion"]["document"]["emotion"]["disgust"]
        value['anger'] = response["emotion"]["document"]["emotion"]["anger"]
        values.append(value)
        print("Analyzed and saved article " + str(j+1))

    return values

def start():
    news = search()
    if news["totalResults"] is 0:
        print("No results found!")
        exit()
    else:
        values = understand(news)
        print(values)

start()