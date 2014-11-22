import urllib2

'''
    helper class
'''
class functions(object):
    '''
        object used to create the return objects
    '''
    class result: pass

    
    '''
        gets:
            url: web link
        returns:
            page html
    '''
    def calUrl(self, url):
        req = urllib2.Request(url.encode('ascii','ignore'), headers={'User-Agent' : "Magic Browser"})
        return urllib2.urlopen(req).read()

    
    '''
        creates the returned object
    '''
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