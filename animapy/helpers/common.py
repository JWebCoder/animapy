import urllib2

class functions(object):
    class result: pass

    def calUrl(self, url):
        req = urllib2.Request(url.encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
        return urllib2.urlopen(req).read()

    # creates the returned object
    def createObject(self, title='', image='', normal='', hd='', link=''):
        epObject = self.result()
        epObject.title = title
        epObject.image = image
        if normal != '':
            epObject.normal= normal
        if hd != '':
            epObject.hd = hd
        if link != '':
            epObject.link = link
        return epObject