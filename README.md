Animapy
=======

An anime API for python.

#Installation
Run `pip install Animapy`, or clone the repo and run `python setup.py install`.

#Info
The PT subbed episodes comes from Anitube website.

The EN subbed episodes comes from NWanime website.

#Usage:
```
from animapy import anime

resultsPT = anime.searchAnimes('naruto 382', quant=10)
resultsEN = anime.searchAnimes('naruto', quant=10, lang='en')


print '\nPt Version:\n'
for ep in resultsPT:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print 'Normal: ' + ep.normal
        print 'HD: ' + ep.hd
        print '\n'

print '\n\nEn Version:\n'
for ep in resultsEN:
    if ep != '':
        print 'Title: ' + ep.title
        print 'Image: ' + ep.image
        print 'Normal: ' + ep.normal
        print '\n'
```
