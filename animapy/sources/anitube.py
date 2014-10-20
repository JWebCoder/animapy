from bs4 import BeautifulSoup
import urllib2
from animapy.helpers.common import functions

class anitube(functions):

    def getAnimes(self, offset, items, parent, position):

        episodes = None
        # in case the result is lower than the desired offset returns None
        if len(items) > offset:
            
            aTag = items[offset].find('div', { "class" : 'videoTitle' }).a

            title = aTag.contents[0].encode('ascii','ignore')
            image = items[offset].find('img').get('src').encode('ascii','ignore')
            hd = ''
            normal = ''

            # calls to get the movie url
            content = self.calUrl(aTag.get('href'))
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

            episodes = self.createObject(title, image, normal, hd)
        if episodes != None:
            parent.setResult(episodes, position)
        parent.count = parent.count + 1
        
    def getSearchItems(self, anime, order):
        # gets the correct URL
        if order == 'date':
            url = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        else:
            url = 'http://www.anitube.se/search/?search_id=' + anime
            
        content = self.calUrl(url)
        soup = BeautifulSoup(content)
        # returns all the items
        return soup.findAll('li', { "class" : 'mainList' })