from Engine import *
from nodes import *

for ymap in range(nbChunkY):
    map.append([])
    for xmap in range(nbChunkX):
        # définition des chuks
        #tmpChunkTemplate = []
        #for ychunk in range(nbBlocksY):
        #    tmpChunkTemplate.append([])
        #    for xchunk in range(nbBlocksX):
        #        tmpChunkTemplate[-1].append(Wall)
        #map[ymap].append(Chunk(tmpChunkTemplate))
        
        map[ymap].append(Chunk([[BrickWall(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()],
                                [BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickFloor(), BrickWall()]
                                ]))

testPlayer = Player([1, 1, 1, 1])
testPlayer.move(0.1, 0)


        
        
    
    







    