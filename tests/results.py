from animapy import anime

teste1 = anime.searchAnimes('naruto 382', quant=10)
#teste2 = anime.searchAnimes('naruto', quant=10, lang='en')


print '\nPt Version:\n'
for ep in teste1:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print 'Normal: ' + ep.normal
        print 'HD: ' + ep.hd
        print '\n'

print '\n\nEn Version:\n'
for ep in teste2:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print 'Normal: ' + ep.normal
        print '\n'