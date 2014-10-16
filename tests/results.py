from animapy import anime

teste1 = anime.searchAnimes('naruto 382', quant=2)
teste2 = anime.searchAnimes('naruto', quant=3, lang='en')

print '\nPt Version:\n'
print 'Title: ' + teste1[0].title
print 'Image: ' + teste1[0].image
print 'HD: ' + teste1[0].hd
print 'Normal: ' + teste1[0].normal
print '\nTitle: ' + teste1[1].title
print 'Image: ' + teste1[1].image
print 'HD: ' + teste1[1].hd
print 'Normal: ' + teste1[1].normal
print '\n\nEn Version:\n'
print 'Title: ' + teste2[0].title
print 'Image: ' + teste2[0].image
print 'Normal: ' + teste2[0].normal
print '\nTitle: ' + teste2[1].title
print 'Image: ' + teste2[1].image
print 'Normal: ' + teste2[1].normal