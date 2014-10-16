from bs4 import BeautifulSoup
import urllib2
import re

class anime(object):
    class result: pass


    @classmethod
    def searchAnimes(cls, anime, quant = 10, order = None, lang='pt'):
        anime = anime.replace(" ", "+")
        if lang == 'pt':
            return cls().__getPTMetaData(anime, quant, order)
        else: #if any other language, returns the EN version
            return cls().__getENMetaData(anime, quant, order)
        
    # function for anitube, PT version
    def __getPTMetaData(self, anime, quant, order):
        
        # gets the correct URL
        if order == 'date':
            url = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        else:
            url = 'http://www.anitube.se/search/?search_id=' + anime
            
        content = self.__calUrl(url)
        soup = BeautifulSoup(content)
        links = soup.findAll('li', { "class" : 'mainList' })
        episodes = []
        
        # in case the result is lower than the desired quantity
        # quant resets to result count
        if len(links) < quant:
            quant = len(links)
        
        # loops throught the result
        for index in range(quant):
            aTag = links[index].find('div', { "class" : 'videoTitle' }).a
            
            title = aTag.contents[0].encode('ascii','ignore')
            image = links[index].find('img').get('src').encode('ascii','ignore')
            hd = ''
            normal = ''
            
            # calls to get the movie url
            content = self.__calUrl(aTag.get('href'))
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
            
            episodes.append(self.__createObject(title, image, normal, hd))
        return episodes


    # function for nwanime, EN version
    def __getENMetaData(self, anime, quant, order):
        
        # gets the correct URL
        if order == 'date':
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=adddate&search_key=&search_for=all&videoold=&ordertype=DESC'
        else:
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=title&search_key=&search_for=all&videoold=&ordertype=DESC'
        
        content = self.__calUrl(url)
        soup = BeautifulSoup(content)
        items = soup.findAll('div', { "class" : 'resultstats_large' })
        episodes = []
        
        # in case the result is lower than the desired quantity
        # quant resets to result count
        
        if len(items) < quant:
            quant = len(items)
            
        # loops throught the result
        for index in range(quant):
            aTag = items[index].a
            children = items[index].findChildren(recursive=False)
            for child in children:
                if child.name == 'a':
                    aTag = child
            title = aTag.contents[0].encode('ascii','ignore')
            
            # calls to get the movie url
            content = self.__calUrl(aTag.get('href'))
            newSoup = BeautifulSoup(content)
            if newSoup.find(id="embed_holder").iframe != None:
                content = self.__calUrl(newSoup.find(id="embed_holder").iframe.get('src'))
                newSoup = BeautifulSoup(content)
                data = newSoup.body.findAll('script')[5].contents[0]

                normal = re.search('file:\s"([^"]+)"', data).group(0)[7:-2]
                image = re.search('img:\s"([^"]+)"', data).group(0)[6:-2]

                episodes.append(self.__createObject(title, image, normal))
        return episodes


    # calls a link in "browser" mode
    def __calUrl(self, url):
        req = urllib2.Request(url.encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
        return urllib2.urlopen(req).read()


    # creates the returned object
    def __createObject(self, title, image, normal='', hd=''):
        epObject = self.result()
        epObject.title = title
        epObject.image = image
        epObject.normal= normal
        epObject.hd = hd
        return epObject