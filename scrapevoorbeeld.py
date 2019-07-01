from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import random

df_recipes = pd.DataFrame(columns=['url','title', 'category'])

urllist = ['https://www.ah.nl/allerhande/recepten/R-L1383828431711/hollandse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828431711/hollandse-recepten?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828431711/hollandse-recepten?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828431711/hollandse-recepten?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828431711/hollandse-recepten?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828430124/italiaanse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828430124/italiaanse-recepten?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828430124/italiaanse-recepten?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828430124/italiaanse-recepten?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828430124/italiaanse-recepten?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828781864/mexicaanse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828458526/japanse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828458643/indonesische-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828781762/indiase-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828506789/chinese-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828460640/thaise-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828458094/marokkaanse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828460527/surinaamse-recepten',
           'https://www.ah.nl/allerhande/recepten/R-L1383828460866/turkse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828429045/spaanse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828431512/franse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828428646/griekse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828781038/scandinavische-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828588164/midden-oosterse-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828458591/aziatische-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383829430168/ontbijtrecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465533/brunch?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465556/lunch?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383829801823/lunchbox?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828639304/pauzehap?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504612/lenterecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504612/lenterecepten?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504612/lenterecepten?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828470720/winterrecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828470720/winterrecepten?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828470720/winterrecepten?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828470720/winterrecepten?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828470720/winterrecepten?Nrpp=1024?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504670/herfstrecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504670/herfstrecepten?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504670/herfstrecepten?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504670/herfstrecepten?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504670/herfstrecepten?Nrpp=1024?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504587/zomerrecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504587/zomerrecepten?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504587/zomerrecepten?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504587/zomerrecepten?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828504587/zomerrecepten?Nrpp=1024?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828663918/wildrecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383829388692/eieren?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828474580/snelle-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828474580/snelle-recepten?Nrpp=1024?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828474580/snelle-recepten?Nrpp=1024?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828474580/snelle-recepten?Nrpp=1024?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828514811/bbq-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465208/saladerecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465208/saladerecepten?Nrpp=1024?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465208/saladerecepten?Nrpp=1024?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465208/saladerecepten?Nrpp=1024?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828465208/saladerecepten?Nrpp=1024?Ns=totalTime%7C0&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828474528/verjaardagsrecepten',
           'https://www.ah.nl/allerhande/recepten/R-L1383828432046/kerstrecepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828432046/kerstrecepten?Nrpp=1024?Nrpp=1024&Ns=recipeId%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828432046/kerstrecepten?Nrpp=1024?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
           'https://www.ah.nl/allerhande/recepten/R-L1383828432046/kerstrecepten?Nrpp=1024?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828522053/recepten-voor-pasen?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828474453/moederdag-recepten?Nrpp=1024',
           'https://www.ah.nl/allerhande/recepten/R-L1383828914065/vaderdag?Nrpp=1024'
           ]

urllist2 = ['https://www.ah.nl/allerhande/recepten/R-L1383829430168/ontbijtrecepten',
            'https://www.ah.nl/allerhande/recepten/R-L1383828431928/recepten-allerhande?Nrpp=1024&Ns=recipeId%7C1',
            'https://www.ah.nl/allerhande/recepten/R-L1383828431928/recepten-allerhande?Ns=totalTime%7C0&Nrpp=1024',
            'https://www.ah.nl/allerhande/recepten/R-L1383828431928/recepten-allerhande?Nrpp=1024&Ns=ratings%7C1%7C%7CnumberOfRatings%7C1',
            'https://www.ah.nl/allerhande/recepten/R-L1383828431928/recepten-allerhande?Ns=numberOfTimeInShoppingListLastWeek%7C1&Nrpp=1024',
            ]
urllist3 = ['https://www.ah.nl/allerhande/recepten/R-L1383829430168/ontbijtrecepten?Nrpp=0',
            'https://www.ah.nl/allerhande/recepten/R-L1383828465556/lunch']
# df_recipes = pd.read_csv(r'C:\Users\david.berenstein\PycharmProjects\GHGtf\standardUseCases\recipes.csv', encoding='latin-1').reset_index(drop=True)
for url in urllist:
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    recipes = page_soup.findAll('section', {'class': 'item recipe'})
    category = url.split('/')[6].split('?')[0]
    for recipe in recipes:
        url = 'https://www.ah.nl' + str(recipe.a['href'])
        title = recipe.a.span.span['data-recipe-title']
        df_recipes = df_recipes.append(pd.DataFrame([[url, title, category]], columns=['url', 'title', 'category']))

df_recipes = df_recipes.reset_index(drop=True)
df_recipes.to_csv('recipes_total.csv')
exit()

#drop the duplicate recipes from allerhande.nl
# df_recipes = pd.read_csv(r'C:\Users\david.berenstein\PycharmProjects\GHGtf\standardUseCases\recipes.csv', encoding='latin-1').reset_index(drop=True)
# df_recipes = df_recipes.drop(df_recipes.columns[0], axis=1)
# df_recipes = df_recipes.drop_duplicates(['url']).reset_index(drop=True)
# df_recipes.to_csv('recipes.csv')

# df_recipes = pd.read_csv(r'C:\Users\david.berenstein\PycharmProjects\GHGtf\standardUseCases\recipes.csv', encoding='latin-1').reset_index(drop=True)
# df_recipes = df_recipes.drop(df_recipes.columns[0:2], axis=1).reset_index(drop=True)
df_recipes['ingredients'] = 0
# df_recipes.to_csv('recipes.csv')



# temp = df_recipes['url'][0]
# uClient = uReq(temp)
# page_html = uClient.read()
# uClient.close()
#
# page_soup = soup(page_html, 'html.parser')
# calories = page_soup.findAll('span',{'itemprop':'calories'})
# proteinContent = page_soup.findAll('span', {'itemprop':'proteinContent'})
# carbohydrateContent = page_soup.findAll('span', {'itemprop':'carbohydrateContent'})
# sodiumContent = page_soup.findAll('span', {'itemprop':'sodiumContent'})
# fiberContent = page_soup.findAll('span', {'itemprop':'fiberContent'})
# fatContent = page_soup.findAll('span', {'itemprop': 'fatContent'})
# saturatedFatContent = page_soup.findAll('span', {'itemprop':'saturatedFatContent'})
# category = page_soup.findAll('ul', {'class': 'short'})
# print(category[0].li.span.text)
#
# print(proteinContent[0].text)
# df_recipes['calories'][j] = calories[0].text
# df_recipes['proteinContent'][j] = proteinContent[0].text
# df_recipes['carbohydrateContent'][j] = carbohydrateContent[0].text
# df_recipes['sodiumContent'][j] = sodiumContent[0].text
# df_recipes['fiberContent'][j] = fiberContent[0].text
# df_recipes['fatContent'][j] = fatContent[0].text
# df_recipes['saturatedFatContent'][j] = saturatedFatContent[0].text
#
# if(len(page_soup.findAll('div', {'class':'icon icon-star star-5 active'}))==2):
#     df_recipes['rating'][j] = 1
# elif(len(page_soup.findAll('div', {'class':'icon icon-star star-4 active'}))==2):
#     df_recipes['rating'][j] = 2
# elif(len(page_soup.findAll('div', {'class':'icon icon-star star-3 active'}))==2):
#     df_recipes['rating'][j] = 3
# elif(len(page_soup.findAll('div', {'class':'icon icon-star star-2 active'}))==2):
#     df_recipes['rating'][j] = 4
# else:
#     df_recipes['rating'][j] = 5
#
#
#
# print(len(page_soup.findAll('div', {'class':'icon icon-star star-5 active'})))
#
# # load the placeholders and create placeholders for the necessary information
# df_recipes = pd.read_csv(r'C:\Users\david.berenstein\PycharmProjects\GHGtf\standardUseCases\recipes.csv', encoding='latin-1').reset_index(drop=True)
df_recipes['calories'] = 0
print(df_recipes['url'].str.split(' '))
df_recipes['proteinContent'] = 0
df_recipes['carbohydrateContent'] = 0
df_recipes['sodiumContent'] = 0
df_recipes['fiberContent'] = 0
df_recipes['fatContent'] = 0
df_recipes['saturatedFatContent'] = 0
df_recipes['rating'] = 0
df_recipes['course'] = 0

j = 0
for url in df_recipes['url']:
    # get the url webpage
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    #find the necessary information from the webpage
    calories = page_soup.findAll('span', {'itemprop': 'calories'})
    proteinContent = page_soup.findAll('span', {'itemprop': 'proteinContent'})
    carbohydrateContent = page_soup.findAll('span', {'itemprop': 'carbohydrateContent'})
    sodiumContent = page_soup.findAll('span', {'itemprop': 'sodiumContent'})
    fiberContent = page_soup.findAll('span', {'itemprop': 'fiberContent'})
    fatContent = page_soup.findAll('span', {'itemprop': 'fatContent'})
    saturatedFatContent = page_soup.findAll('span', {'itemprop': 'saturatedFatContent'})
    htmlIngredient = page_soup.findAll('li', {'itemprop': 'ingredients'})
    category = page_soup.findAll('ul', {'class': 'short'})

    # fill in the nutritional values
    try:
        df_recipes['calories'][j] = calories[0].text
    except:
        df_recipes['calories'][j] = 0
    try:
        df_recipes['proteinContent'][j] = proteinContent[0].text
    except:
        df_recipes['proteinContent'][j] = 0
    try:
        df_recipes['carbohydrateContent'][j] = carbohydrateContent[0].text
    except:
        df_recipes['carbohydrateContent'][j] = 0
    try:
        df_recipes['sodiumContent'][j] = sodiumContent[0].text
    except:
        df_recipes['sodiumContent'][j] = 0
    try:
        df_recipes['fiberContent'][j] = fiberContent[0].text
    except:
        df_recipes['fiberContent'][j] = 0
    try:
        df_recipes['fatContent'][j] = fatContent[0].text
    except:
        df_recipes['fatContent'][j] = 0
    try:
        df_recipes['saturatedFatContent'][j] = saturatedFatContent[0].text
    except:
        df_recipes['saturatedFatContent'][j] = 0

    #grap the rating of the recipes
    if (len(page_soup.findAll('div', {'class': 'icon icon-star star-5 active'})) == 2):
        df_recipes['rating'][j] = 1
    elif (len(page_soup.findAll('div', {'class': 'icon icon-star star-4 active'})) == 2):
        df_recipes['rating'][j] = 2
    elif (len(page_soup.findAll('div', {'class': 'icon icon-star star-3 active'})) == 2):
        df_recipes['rating'][j] = 3
    elif (len(page_soup.findAll('div', {'class': 'icon icon-star star-2 active'})) == 2):
        df_recipes['rating'][j] = 4
    else:
        df_recipes['rating'][j] = 5

    #grap the ingredients from the webpage
    vector = []
    for i in range(len(htmlIngredient)):
        vector.append(htmlIngredient[i].a['data-default-label'])
    df_recipes['ingredients'][j] = vector

    #grap the course from the webpage
    df_recipes['course'][j] = category[0].li.span.text
    j = j + 1
    print(j, len(df_recipes['url']))
    break

df_recipes.to_csv('recipesInfoExtended.csv')
print(df_recipes)