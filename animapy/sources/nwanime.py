from bs4 import BeautifulSoup
import re
from helpers import functions

class nwanime(object):
    
    def getAnimes(self, anime, quant, offset, order, parent):
        # gets the correct URL
        if order == 'date':
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=adddate&search_key=&search_for=all&videoold=&ordertype=DESC'
        else:
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=title&search_key=&search_for=all&videoold=&ordertype=DESC'
        
        content = functions.calUrl(url)
        soup = BeautifulSoup(content)
        items = soup.findAll('div', { "class" : 'resultstats_large' })
        episodes = []
        
        # in case the result is lower than the desired quantity
        # quant resets to result count
        
        if len(items) >= (quant + offset):
            
            # loops throught the result
            for index in range(quant):
                aTag = items[index + offset].a
                children = items[index + offset].findChildren(recursive=False)
                for child in children:
                    if child.name == 'a':
                        aTag = child
                title = aTag.contents[0].encode('ascii','ignore')

                # calls to get the movie url
                content = functions.calUrl(aTag.get('href'))
                newSoup = BeautifulSoup(content)
                if newSoup.find(id="embed_holder").iframe != None:
                    content = functions.calUrl(newSoup.find(id="embed_holder").iframe.get('src'))
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

                    

                    episodes.append(functions.createObject(title, image, normal))
        parent.setResult(episodes)
        parent.count = parent.count + 1