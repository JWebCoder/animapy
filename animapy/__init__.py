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
            uri = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        else:
            uri = 'http://www.anitube.se/search/?search_id=' + anime
        content = urllib2.urlopen(uri).read()
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
            
            newSoup = BeautifulSoup(urllib2.urlopen(aTag.get('href').encode('ascii','ignore')).read())
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
            uri = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=adddate &search_key=&search_for=all&videoold=&ordertype=DESC'
        else:
            uri = 'http://www.nwanime.com/search_result.php?&search_type=search_videos&search_id=' + anime + '&sort=title&search_key=&search_for=all&videoold=&ordertype=DESC'
        req = urllib2.Request(uri, headers={'User-Agent' : "Magic Browser"})
        content = urllib2.urlopen(req).read()
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
            req = urllib2.Request(aTag.get('href').encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
            content = urllib2.urlopen(req).read()
            newSoup = BeautifulSoup(content)
            
            data = newSoup.find(id="embed_holder").iframe.get('src')
            req = urllib2.Request(data, headers={'User-Agent' : "Magic Browser"})
            content = urllib2.urlopen(req).read()
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

'''
teste1 = anime.searchAnimes('naruto 382', quant=1)
teste2 = anime.searchAnimes('naruto', quant=1, lang='en')

print teste1[0].title
print teste1[0].image
print teste1[0].hd
print teste2[0].title
print teste2[0].image
print teste2[0].normal
'''