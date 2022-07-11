from basic_tile import Basic_tile
from land_enum import Land
from time import time
import random

class Tile_generator:
    names = {"OUTER": ["village", "town", "city", "fortress","mountains", "caves", "fields", "crossroads",
     "sentinel", "hills", "plains", "grasslands", "woods", "graveyard", 
     "shrine", "highlands", "farmlands", "forest", 
     "coast", "riverside", "spring"],
     "INNER": ["oasis", "desert", "steppe", "vampire's lair", 
     "warcamp", "desolation", "chapel", "exotic market", "sanctuary",
      "cult of pleasure", "black knight", "jungle", "ancient ruins", "dervishes patrol", "swamp", "grassy plateou"],
      "ENDGAME": ["crown of command", "crypt of fiends", "devil's playground", "dice with Death", "trial of ordeal",
       "succubus", "fallen angel", "the great necromancer"]}
    tiles = {"OUTER": [],
    "INNER": [],
    "ENDGAME": []}

    

    def generate(self):
        for land in Land:
            land = str(land).split(".")[1]
            match land:
                case "OUTER":
                    edges = list(set(self.names[land][:4]))
                    self.tiles[land] = [Basic_tile(edge, 0, 1) for edge in edges]
                    previous = Basic_tile(self.names[land][random.randint(4,len(self.names[land]) -1)],random.randint(1,2), random.randint(0,4))
                    self.tiles[land].append(previous)
                    for i in range(20):
                        current = Basic_tile(self.names[land][random.randint(4,len(self.names[land]) -1)],random.randint(1,2), random.randint(0,4))
                        while abs(previous.height - current.height) > 1 or current.name == previous.name:
                            current = Basic_tile(self.names[land][random.randint(4,len(self.names[land]) -1)],random.randint(1,2), random.randint(0,4))
                        previous = current
                        self.tiles[land].append(current)
                case "INNER":
                    self.tiles[land] = list(map((lambda x: Basic_tile(x, random.randint(2,3), random.randint(0,3))), list(set(self.names[land]))))
                case "ENDGAME":
                    end_map = self.names[land][1:5] + self.names[land][5:]
                    end_map.append(self.names[land][0])
                    self.tiles[land] = list(map((lambda x: Basic_tile(x, 0, random.randint(0,3))), end_map))
    

    def save_res(self):
        fname = f"gen_{time()}.txt"
        f = open(fname, "x")
        for land in Land:
            land = str(land).split(".")[1]
            f.write(f"{land}:")
            for x in self.tiles[land]:
                f.write(f"({x.name},{x.cards_drawn},{x.height});")
            f.write("\n")
        f.close
        return fname
            