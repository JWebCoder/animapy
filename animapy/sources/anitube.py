from bs4 import BeautifulSoup
import urllib2
from animapy.helpers.common import functions

class anitube(functions):
    
    '''
        thread function
        gets:
            offset: point in the list
            items: search item list
            parent: function caller
            position: where to set the result in a list owned by the caller
        does:
            sets the complete data of an episode in a list owned by the caller
    '''
    def getVideos(self, offset, items, parent, position):
        episodes = None
        # in case the result is lower than the desired offset returns None
        if len(items) > offset:
            metaData = self.__getMetadata(items[offset])
            
            links = self.__getVideoLinks(metaData['link'])

            episodes = self.createObject(metaData['title'], metaData['image'], links['normal'], links['hd'])
        if episodes != None:
            parent.setResult(episodes, position)
        parent.count = parent.count + 1
    
    
    '''
        gets:
            link: page link where the video plays
        returns:
            the episode normal and hd link
    '''
    def getVideoFromLink(self, link):
        episodes = None
        
        links = self.__getVideoLinks(link)

        episode = self.createObject(normal=links['normal'],hd=links['hd'])
        return episode

    
    '''
        gets:
            items: search item list
            quant: quantity of items to get the metadata
        returns:
            a list with episodes metadata
    '''
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
    
    
    '''
        gets:
            anime: name of the anime to search
            order: orders the search
        returns:
            item list
    '''
    def getSearchItems(self, anime, order):
        # gets the correct URL
        if order == 'date':
            url = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        elif order == 'title':
            url = 'http://anitube.xpg.uol.com.br/search/basic/1/?sort=title&search_type=&search_id=' + anime
        elif order == 'viewnum':
            url = 'http://anitube.xpg.uol.com.br/search/basic/1/?sort=viewnum&search_type=&search_id=' + anime
        elif order == 'rate':
            url = 'http://anitube.xpg.uol.com.br/search/basic/1/?sort=rate&search_type=&search_id=' + anime
        else:
            url = 'http://www.anitube.se/search/?search_id=' + anime
            
        content = self.calUrl(url)
        soup = BeautifulSoup(content)
        # returns all the items
        return soup.findAll('li', { "class" : 'mainList' })
    
    
    '''
        gets:
            tag: html tag
        returns:
            the content
    '''
    def __getContent(self, tag):
        return tag.contents[0].encode('ascii','ignore')

    
    '''
        gets:
            tag: html tag
        returns:
            the src attribute
    '''
    def __getSrc(self, tag):
        return tag.find('img').get('src').encode('ascii','ignore')
    
    
    '''
        gets:
            link: page link where the video plays
        returns:
            the episode normal and hd link
    '''
    def __getVideoLinks(self, link):
        hd = ''
        normal = ''
        
        # calls to get the movie url
        content = self.calUrl(link)
        newSoup = BeautifulSoup(content)
        data = newSoup.find(id="videoPlayer").findAll('script')[2].get('src')

        response = urllib2.urlopen(data)

        # loops throught the javascript lines to get the movie links
        for line in response:
            if ('cdn.anitu.be' in line) or ('vid.anitu.be' in line):
                if '_hd' in line:
                    hd = line.rstrip()[9:-2]
                else:
                    normal = line.rstrip()[9:-2]
        return {'hd': hd, 'normal': normal}
    
    
    '''
        gets:
            item: episode
        returns:
            the episode metadata
    '''
    def __getMetadata(self, item):
        aTag = item.find('div', { "class" : 'videoTitle' }).a
        title = self.__getContent(aTag)
        image = self.__getSrc(item)
        link = aTag.get('href')
        return {'title': title, 'image': image, 'link': link.encode('ascii','ignore')}
