from bs4 import BeautifulSoup
import urllib2


class anime(object):
    class result: pass
        
    @classmethod
    def searchAnimes(cls, anime, quant = 10, order = None):
        anime = anime.replace(" ", "+")
        if order == 'date':
            uri = 'http://www.anitube.se/search/basic/1/?sort=addate&search_type=&search_id=' + anime
        else:
            uri = 'http://www.anitube.se/search/?search_id=' + anime
        content = urllib2.urlopen(uri).read()
        soup = BeautifulSoup(content)
        links = soup.findAll('li', { "class" : 'mainList' })
        movies = []
        
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
            
            movie = cls.result()
            movie.title = title
            movie.image = image
            movie.normal= normal
            movie.hd = hd
            movies.append(movie)
        return movies