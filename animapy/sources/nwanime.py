from bs4 import BeautifulSoup
import re
from animapy.helpers.common import functions

class nwanime(functions):

    def getVideos(self, offset, items, parent, position):

        episodes = None
        # in case the result is lower than the desired offset returns None
        if len(items) > offset:
            
            metaData = self.__getMetadata(items[offset])
            
            links = self.__getVideoLinks(metaData['link'])

            episodes = self.createObject(metaData['title'], metaData['image'], links['normal'])
            
        if episodes != None:
            parent.setResult(episodes, position)
        parent.count = parent.count + 1
    
    
    def getVideoFromLink(self, link):
        episodes = None
        
        links = self.__getVideoLinks(link)

        episode = self.createObject(normal=links['normal'])
        return episode
    
    
    def getAnimesMetadata(self, items, quant):
        if len(items) < quant:
            quant = len(items)
        result = []
        # in case the result is lower than the desired offset returns None
        for i in range(quant):
            episodes = None
            
            metaData = self.__getMetadata(items[i])

            episode = self.createObject(metaData['title'], metaData['image'], link = metaData['link'])
            if episode != None:
                result.append(episode)
        return result
    
    
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

    
    def __getTitle(self, aTag):
        return aTag.contents[0].encode('ascii','ignore')
    
    
    def __getImage(self, item):
        style = item.find('div')['style']
        return re.findall('url\((.*?)\)', style)[0].encode('ascii','ignore')
    
    
    def __getVideoLinks(self, link):
        # calls to get the movie url
        content = self.calUrl(link)
        newSoup = BeautifulSoup(content)
        normal = ''
        if newSoup.find(id="embed_holder").iframe != None:
            content = self.calUrl(newSoup.find(id="embed_holder").iframe.get('src'))
            newSoup = BeautifulSoup(content)
            scripts = newSoup.body.findAll('script')
            if len(scripts) < 9:
                data = scripts[2].contents[0]
                normal = re.search("'file':\s'([^']+)'", data).group(0)[7:-2]
            else:
                data = scripts[5].contents[0]
                normal = re.search('file:\s"([^"]+)"', data).group(0)[7:-2]
        return {'normal': normal}
    
    
    def __getMetadata(self, item):
        aTag1 = item.a
        children = item.findChildren(recursive=False)
        for child in children:
            if child.name == 'a':
                aTag2 = child
        title = self.__getTitle(aTag2)
        image = self.__getImage(aTag1)
                
        link = aTag2.get('href')
        return {'title': title, 'image': image, 'link': link}