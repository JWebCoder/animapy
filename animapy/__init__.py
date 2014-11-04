from bs4 import BeautifulSoup
from animapy.sources.anitube import anitube
from animapy.sources.nwanime import nwanime
import thread
import urllib2
import time

class anime(object):

    @classmethod
    def searchAnimes(cls, anime, quant, order = None, lang='pt'):
        anime = anime.replace(" ", "+")
        return cls().__getData(anime, quant, order, lang)
    
    
    @classmethod
    def searchAnimesNoVideo(cls, anime, quant, order = None, lang='pt'):
        anime = anime.replace(" ", "+")
        return cls().__getData(anime, quant, order, lang, False)
    
    
    def __returner(self, data):
        self.count = self.count + 1
        
    
    def setResult(self, episodes, position):
        self.data[position] = episodes

    def __getData(self, anime, quant, order, lang, video=True):
        self.count = 0
        self.data = [''] * quant
        if lang == 'pt':
            animes = anitube()
            items = animes.getSearchItems(anime, order)
            
        else: #if any other language, returns the EN version
            animes = nwanime()
            items = animes.getSearchItems(anime, order)
        
        if video:
            for i in range(quant):
                thread.start_new_thread( animes.getAnimes, (i, items, self, i,) )

            while self.count != quant:
                pass
        else:
            animes.getAnimesMetadata(items, quant, self)
        return self.data