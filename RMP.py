import urllib2
from bs4 import BeautifulSoup

site = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1887873'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(site, headers=hdr)
page = urllib2.urlopen(req)
#content = page.read()
#print content
parse = BeautifulSoup(page, 'html.parser')
#gets overall rating of professor
overall_rating_box = parse.find('div', attrs={'class':'breakdown-container quality'}).find('div', attrs={'class':'grade'})
overall_rating = overall_rating_box.text.strip()
#gets would take again rating
take_again_box = parse.find('div', attrs={'class':'breakdown-section takeAgain 100'}).find('div', attrs={'class':'grade'})
take_again = take_again_box.text.strip()
#gets the level of difficulty
level_of_difficulty_box = parse.find('div', attrs={'class':'breakdown-section difficulty'}).find('div', attrs={'class':'grade'})
level_of_difficulty = level_of_difficulty_box.text.strip()
#gets description tags (presented in a list) of professor
description_tag_list = parse.find('div', attrs={'class':'tag-box'}).findAll('span', attrs={'class':'tag-box-choosetags'})
#prints
print("Overall rating: " + overall_rating)
print("Would take again: " + take_again)
print("Level of difficulty: " + level_of_difficulty)
print("Students have said this: ")
for tag in range(5):
    if len(description_tag_list) < 5:
        pass;
    else:
        description = description_tag_list[tag].text.strip()
        print(description)
    