from settings import*
print("loading map!")
MAP =[]
MAPCORS = []
MAPDICT = dict()


for y in range(SIZEY*CHUNKX):
    _midmap = []
    for x in range(SIZEX*CHUNKY):
        _midmap.append(0)
    MAP.append(_midmap)

for cy in enumerate(MAP):
    for cx in enumerate(cy[1]):
        MAPCORS.append((cx[0],cy[0]))      

for hx,hy in MAPCORS:

    M = MAP[hy]
    Y = 0
    c = hx,hy
    MAPDICT.update({c: Y})




print("Map is ready!")