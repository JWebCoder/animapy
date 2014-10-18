from bs4 import BeautifulSoup
import urllib2
from helpers import functions

class anitube(object):
    
    def getAnimes(self, anime, quant, offset, order, parent):
        # gets the correct URL
        if order == 'date':
            url = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        else:
            url = 'http://www.anitube.se/search/?search_id=' + anime
            
        content = functions.calUrl(url)
        soup = BeautifulSoup(content)
        links = soup.findAll('li', { "class" : 'mainList' })
        episodes = []
        
        # in case the result is lower than the desired quantity
        # quant resets to result count
        if len(links) < quant:
            quant = len(links)
        
        # loops throught the result
        for index in range(quant):
            aTag = links[index + offset].find('div', { "class" : 'videoTitle' }).a
            
            title = aTag.contents[0].encode('ascii','ignore')
            image = links[index + offset].find('img').get('src').encode('ascii','ignore')
            hd = ''
            normal = ''
            
            # calls to get the movie url
            content = functions.calUrl(aTag.get('href'))
            newSoup = BeautifulSoup(content)
            data = newSoup.find(id="videoPlayer").findAll('script')[2].get('src')
            
            response = urllib2.urlopen(data)
            
            # loops throught the javascript lines to get the movie links
            for line in response:
                if 'cdn.anitu.be' in line:
                    if '_hd' in line:
                        hd = line.rstrip()[9:-2]
                    else:
                        normal = line.rstrip()[9:-2]
            
            episodes.append(functions.createObject(title, image, normal, hd))
        parent.setResult(episodes)
        parent.count = parent.count + 1