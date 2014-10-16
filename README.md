Animapy
=======

An anime API for python.

#Installation
Run `pip install Animapy`, or clone the repo and run `python setup.py install`.

#Info
The PT subbed episodes comes from Anitube website.

The EN subbed episodes comes comes from NWanime website.

#Usage:
```
from animapy import anime

resultsPT = anime.searchAnimes('naruto', quant=10, order='date', lang='pt')
for result in resultsPT:
    print result.title
    print result.image
    print result.hd
    print result.normal
    
resultsEN = anime.searchAnimes('naruto', quant=10, order='date', lang='en')
for result in resultsEN:
    print result.title
    print result.image
    print result.hd
    print result.normal
```
