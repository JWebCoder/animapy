from animapy import anime

teste1 = anime.searchAnimesMetadata('naruto 382', quant=3)
teste2 = anime.searchAnimesMetadata('naruto', quant=3, lang='en')


print '\nPt Version:\n'
for ep in teste1:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print '\n'

print '\n\nEn Version:\n'
for ep in teste2:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print '\n'