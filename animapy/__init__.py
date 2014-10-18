from bs4 import BeautifulSoup
from sources.anitube import anitube
from sources.nwanime import nwanime
import thread
import urllib2
import time

class anime(object):

    @classmethod
    def searchAnimes(cls, anime, quant, order = None, lang='pt'):
        anime = anime.replace(" ", "+")
        return cls().__getData(anime, quant, order, lang)
    
    
    def __returner(self, data):
        self.count = self.count + 1
        
    
    def setResult(self, episodes, position):
        self.data[position] = episodes

    def __getData(self, anime, quant, order, lang):
        self.count = 0
        self.data = [''] * quant
        if lang == 'pt':
            animes = anitube()
            for i in range(quant):
                thread.start_new_thread( animes.getAnimes, (anime, 1, i, order, self, i,) )

            while self.count != quant:
                pass
            return self.data
            
        else: #if any other language, returns the EN version
            animes = nwanime()
            for i in range(quant):
                thread.start_new_thread( animes.getAnimes, (anime, 1, i, order, self, i,) )

            while self.count != quant:
                pass
            return self.data


#teste = anime.searchAnimes('naruto', 20)
teste2 = anime.searchAnimes('naruto', 5, lang='en')
#print len(teste)

#for val in teste:
#    print val.title
    
for val in teste2:
    if val != '':
        print val.title

#print teste2[0].title
#print teste2[0].image
#print teste2[1].title
#print teste2[1].image
#print teste2[2].title
#print teste2[2].image
#print teste2[3].title
#print teste2[3].image