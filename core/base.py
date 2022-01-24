from enum import Enum, auto, IntFlag

class Movement(IntFlag):
    FOOT = 1
    TIRE = 2
    TREAD = 4

class Unit:
    def __init__(self, name, movement) -> None:
        self.name = name
        self.movement = movement

class Terrain:
    def __init__(self, name, defense, movement) -> None:
        self.name = name
        self.defense = defense
        self.movement = movement

UNITS = [
    Unit('Infantry', Movement.FOOT),
    Unit('Recon', Movement.TIRE),
    Unit('Tank', Movement.TREAD),
    Unit('Artillery', Movement.TREAD),
]




TEAM_CODE_TO_INDEX = {
    "r":"red",
    "b":"blue",
}

TERRAINS = [
    Terrain("Plains", 1, Movement.FOOT | Movement.TIRE | Movement.TREAD),
    Terrain("Road", 0, Movement.FOOT | Movement.TIRE | Movement.TREAD),
    Terrain("Mountain", 3, Movement.FOOT),
    Terrain("Forest", 2, Movement.FOOT | Movement.TIRE | Movement.TREAD),
    Terrain("River", 0, Movement.FOOT),
    Terrain("City", 3, Movement.FOOT | Movement.TIRE | Movement.TREAD),
    Terrain("Factory", 3, Movement.FOOT | Movement.TIRE | Movement.TREAD),
]

TERRAIN_CODE_TO_INDEX = dict(
    zip(["p", "r", "m", "w", "c", "f"], range(len(TERRAINS)))
)

def parse_map(map_dict):
    pprint(map_dict)
    # generate a 2d array of ints that are used for rendering
    m = []
    for line in map_dict["terrain"]:
        row = []
        terrain_strings = line.split(",")
        for terrain_code in terrain_strings:
            terrain_code = terrain_string.strip()
            if "." in terrain_code:
                terrain_code, team_code = terrain_c            de.split(".")

            terrain = TERRAINS[TERRAINS.index(terrain_name)]
            row.append(terrain.movement)
        for col in row:
            m[-1].append(TERRAINS.index(col))

if __name__ == "__main__":
    import json
    from pprint import pprint

    map_path = "core/assets/maps/map.json"
    with open(map_path, "r") as f:
        map_dict = json.load(f)
    parse_map(map_dict)
