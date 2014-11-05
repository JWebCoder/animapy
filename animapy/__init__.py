from bs4 import BeautifulSoup
from animapy.sources.anitube import anitube
from animapy.sources.nwanime import nwanime
import thread
import urllib2
import time

class anime(object):

    @classmethod
    def searchAnimes(cls, anime, quant, order = '', lang='pt'):
        return cls().__getData(anime, quant, order, lang)


    @classmethod
    def searchAnimesMetadata(cls, anime, quant, order = '', lang='pt'):
        return cls().__getData(anime, quant, order, lang, False)


    @classmethod
    def getAnimeLinks(cls, link, lang='pt'):
        obj = cls()
        obj.__setTarget(lang)
        return obj.animes.getVideoFromLink(link)


    def setResult(self, episodes, position):
        self.data[position] = episodes


    #defines the target object according to the language set
    def __setTarget(self, lang):
        if lang == 'pt':
            self.animes = anitube()
        else: #if any other language, returns the EN version
            self.animes = nwanime()


    def __getData(self, anime, quant, order, lang, video=True):
        anime = anime.replace(" ", "+")
        self.__setTarget(lang)
        items = self.animes.getSearchItems(anime, order)
        
        if video:
            self.data = [''] * quant
            self.__getVideos(items, quant)
        else:
            self.data = self.animes.getAnimesMetadata(items, quant)
        return self.data


    def __getVideos(self, items, quant):
        self.count = 0
        for i in range(quant):
            thread.start_new_thread( self.animes.getVideos, (i, items, self, i,) )

        while self.count != quant:
            pass