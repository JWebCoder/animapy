import urllib2

class result: pass

def calUrl(url):
    req = urllib2.Request(url.encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
    return urllib2.urlopen(req).read()

# creates the returned object
def createObject(title, image, normal='', hd=''):
    epObject = result()
    epObject.title = title
    epObject.image = image
    epObject.normal= normal
    epObject.hd = hd
    return epObject