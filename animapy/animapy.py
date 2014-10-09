from bs4 import BeautifulSoup
import urllib2
import json

class animapy:
    def searchAnimes(self, anime):
        uri = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        content = urllib2.urlopen(uri).read()
        soup = BeautifulSoup(content)
        links = soup.findAll('div', { "class" : 'videoTitle' })
        for link in links:
            newSoup = BeautifulSoup(urllib2.urlopen(link.a.get('href').encode('ascii','ignore')).read())
            data = newSoup.find(id="videoPlayer").findAll('script')[2].get('src')
            response = urllib2.urlopen(data)
            for line in response:
                if '_hd' in line:
                    print line.rstrip()[9:-2]

x = animapy()
x.searchAnimes('naruto')