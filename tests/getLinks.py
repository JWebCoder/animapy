from animapy import anime

#Test
teste1 = anime.getAnimeLinks('http://www.anitube.se/video/79734/Ai-Tenchi-Muyo--22')
teste2 = anime.getAnimeLinks('http://www.nwanime.com/one-piece-episode-668/video/69a0b530b6b09a092bf0/', lang='en')


print '\nPt Version:\n'
print 'Normal: ' + teste1.normal
if hasattr(teste1, 'hd'):
    print 'HD: ' + teste1.hd
print '\n'

print '\n\nEn Version:\n'
print 'Normal: ' + teste2.normal
print '\n'