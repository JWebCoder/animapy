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
        else:
            return cls().__getENMetaData(anime, quant, order)
        

    def __getPTMetaData(self, anime, quant, order):
        if order == 'date':
            url = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        else:
            url = 'http://www.anitube.se/search/?search_id=' + anime
            
        content = self.__calUrl(url)
        soup = BeautifulSoup(content)
        links = soup.findAll('li', { "class" : 'mainList' })
        movies = []
        
        if len(links) < quant:
            quant = len(links)
        for index in range(quant):
            aTag = links[index].find('div', { "class" : 'videoTitle' }).a
            
            title = aTag.contents[0].encode('ascii','ignore')
            image = links[index].find('img').get('src').encode('ascii','ignore')
            hd = ''
            normal = ''
            
            content = self.__calUrl(aTag.get('href'))
            newSoup = BeautifulSoup(content)
            data = newSoup.find(id="videoPlayer").findAll('script')[2].get('src')
            
            response = urllib2.urlopen(data)
            
            for line in response:
                if 'cdn.anitu.be' in line:
                    if '_hd' in line:
                        hd = line.rstrip()[9:-2]
                    else:
                        normal = line.rstrip()[9:-2]
            
            movie = self.result()
            movie.title = title
            movie.image = image
            movie.normal= normal
            movie.hd = hd
            movies.append(movie)
        return movies


    def __getENMetaData(self, anime, quant, order):
        # full link http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=naruto+200&sort=title&search_key=&search_for=all&videoold=&ordertype=DESC
        if order == 'date':
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=adddate &search_key=&search_for=all&videoold=&ordertype=DESC'
        else:
            url = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=title&search_key=&search_for=all&videoold=&ordertype=DESC'
        
        content = self.__calUrl(url)
        soup = BeautifulSoup(content)
        items = soup.findAll('div', { "class" : 'resultstats_large' })
        movies = []
        
        if len(items) < quant:
            quant = len(items)
        for index in range(quant):
            aTag = items[index].a
            children = items[index].findChildren(recursive=False)
            for child in children:
                if child.name == 'a':
                    aTag = child
            title = aTag.contents[0].encode('ascii','ignore')
            normal = ''
            image = ''

            content = self.__calUrl(aTag.get('href'))
            newSoup = BeautifulSoup(content)
                                    
            content = self.__calUrl(newSoup.find(id="embed_holder").iframe.get('src'))
            newSoup = BeautifulSoup(content)
                                    
            data = newSoup.body.findAll('script')[5].contents[0]
            
            normal = re.search('file:\s"([^"]+)"', data).group(0)[7:-2]
            image = re.search('img:\s"([^"]+)"', data).group(0)[6:-2]
            
            movie = self.result()
            movie.title = title
            movie.image = image
            movie.normal= normal
            movies.append(movie)
        return movies


    def __calUrl(self, url):
        req = urllib2.Request(url.encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
        return urllib2.urlopen(req).read()

'''
teste1 = anime.searchAnimes('naruto 382', quant=1)
teste2 = anime.searchAnimes('naruto', quant=1, lang='en')

print '\nPt Version:'
print 'Title: ' + teste1[0].title
print 'Image: ' + teste1[0].image
print 'HD: ' + teste1[0].hd
print 'Normal: ' + teste1[0].normal
print '\nEn Version:'
print 'Title: ' + teste2[0].title
print 'Image: ' + teste2[0].image
print 'Normal: ' + teste2[0].normal
'''