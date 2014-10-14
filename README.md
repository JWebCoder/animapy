Animapy
=======

An anime API for python.

#Installation
Run `pip install Animapy`, or clone the repo and run `python setup.py install`.

#Info
The data comes from Anitube website.

#Usage:
```
from animapy import anime

results = anime.searchAnimes('naruto', quant=10, order='date')
for result in results:
    print result.title
    print result.image
    print result.hd
    print result.normal
```
