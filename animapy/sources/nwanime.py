from bs4 import BeautifulSoup
import re
from animapy.helpers.common import functions

class nwanime(functions):
    
    def getAnimes(self, offset, items, parent, position):

        episodes = None
        # in case the result is lower than the desired offset returns None
        if len(items) > offset:
            
            aTag = items[offset].a
            children = items[offset].findChildren(recursive=False)
            for child in children:
                if child.name == 'a':
                    aTag = child
            title = aTag.contents[0].encode('ascii','ignore')

            # calls to get the movie url
            content = self.calUrl(aTag.get('href'))
            newSoup = BeautifulSoup(content)
            if newSoup.find(id="embed_holder").iframe != None:
                content = self.calUrl(newSoup.find(id="embed_holder").iframe.get('src'))
                newSoup = BeautifulSoup(content)
                scripts = newSoup.body.findAll('script')
                if len(scripts) < 9:
                    data = scripts[2].contents[0]
                    normal = re.search("'file':\s'([^']+)'", data).group(0)[7:-2]
                    image = re.search("//'image':\s'([^']+)'", data).group(0)[12:-1]
                else:
                    data = scripts[5].contents[0]
                    normal = re.search('file:\s"([^"]+)"', data).group(0)[7:-2]
                    image = re.search('img:\s"([^"]+)"', data).group(0)[6:-2]

                episodes = self.createObject(title, image, normal)
        if episodes != None:
            parent.setResult(episodes, position)
        parent.count = parent.count + 1
    
    def getSearchItems(self, anime, order):
        # gets the correct URL
        if order == 'date':
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=adddate&search_key=&search_for=all&videoold=&ordertype=DESC'
        else:
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=title&search_key=&search_for=all&videoold=&ordertype=DESC'
            
        content = self.calUrl(url)
        soup = BeautifulSoup(content)
        # returns all the items
        return soup.findAll('div', { "class" : 'resultstats_large' })