Animapy
=======

An anime API for python.

##Installation
Run `pip install Animapy`, or clone the repo and run `python setup.py install`.

##Info
The PT subbed episodes comes from Anitube website.

The EN subbed episodes comes from NWanime website.

##Usage:

####To get the results of a search:
```
from animapy import anime

teste1 = anime.searchAnimes('naruto 382', quant=10)
teste2 = anime.searchAnimes('naruto', quant=10, lang='en')


print '\nPt Version:\n'
for ep in teste1:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print 'Normal: ' + ep.normal
        if hasattr(ep, 'hd'):
            print 'HD: ' + ep.hd
        print '\n'

print '\n\nEn Version:\n'
for ep in teste2:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        if hasattr(ep, 'normal'):
            print 'Normal: ' + ep.normal
        print '\n'
```

####To get just the title and images of a search:
```
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
```

####To get just the link of the anime file:
```
from animapy import anime

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
```