import urllib2

class functions(object):
    class result: pass

    def calUrl(self, url):
        req = urllib2.Request(url.encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
        return urllib2.urlopen(req).read()

    # creates the returned object
    def createObject(self, title, image, normal='', hd=''):
        epObject = self.result()
        epObject.title = title
        epObject.image = image
        epObject.normal= normal
        epObject.hd = hd
        return epObject