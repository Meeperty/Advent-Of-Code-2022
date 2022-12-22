import time
from queue import Queue

NONE = -1
ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

class Blueprint:
    def __init__(self, o : int, c : int, oo : int, oc : int, gob : int, go : int) -> None:
        self.oreRobotCost = o
        self.clayRobotCost = c
        self.obsidianRobotOreCost = oo
        self.obsidianRobotClayCost = oc
        self.geodeRobotOreCost = go
        self.geodeRobotObsidianCost = gob
        
class Factory:
    def __init__(self, bp : Blueprint) -> None:
        self.is_building = False
        self.type_building = NONE

class State:
    def __init__(self, fac : Factory, bp : Blueprint, robots : list[int], mats : list[int], min : int = 1) -> None:
        self.factory = fac
        self.blueprint = bp
        self.robots = robots
        self.materials = mats
        self.minute = min
    
    def can_build(self, type : int) -> bool:
        if type == ORE:
            return self.materials[ORE] >= self.blueprint.oreRobotCost
        if type == CLAY:
            return self.materials[ORE] >= self.blueprint.clayRobotCost
        if type == OBSIDIAN:
            return (self.materials[ORE] >= self.blueprint.obsidianRobotOreCost) and (self.materials[CLAY] >= self.blueprint.obsidianRobotClayCost)
        if type == GEODE:
            return (self.materials[ORE] >= self.blueprint.geodeRobotOreCost) and (self.materials[OBSIDIAN] >= self.blueprint.geodeRobotObsidianCost)
        return False

    def gather_materials(self) -> None:
        for bot in self.robots:
            self.materials[bot] += 1
    
    def options(self) -> list[int]:
        options = [NONE]
        if self.can_build(ORE):
            options.append(ORE)
        if self.can_build(CLAY):
            options.append(CLAY)
        if self.can_build(OBSIDIAN):
            options.append(OBSIDIAN)
        if self.can_build(GEODE):
            options.append(GEODE)
        return options
    
    def start_build(self, type : int) -> None:
        if type == -1:
            return
        if type == 0:
            self.materials[ORE] -= self.blueprint.oreRobotCost
        if type == 1:
            self.materials[ORE] -= self.blueprint.clayRobotCost
        if type == 2:
            self.materials[ORE] -= self.blueprint.obsidianRobotOreCost
            self.materials[CLAY] -= self.blueprint.obsidianRobotClayCost
        if type == 3:
            self.materials[ORE] -= self.blueprint.geodeRobotOreCost
            self.materials[OBSIDIAN] -= self.blueprint.geodeRobotObsidianCost
        self.factory.type_building = type
        self.factory.is_building = True
    
    def end_build(self) -> int:
        bot : int = self.factory.type_building
        self.factory.is_building = False
        self.factory.type_building = NONE
        return bot

input_file = open("day19test.txt")
blueprints : list[Blueprint] = list()
for line in input_file:
    sections = line.split()
    o = int(sections[6])
    c = int(sections[12])
    oo = int(sections[18])
    oc = int(sections[21])
    go = int(sections[27])
    gob = int(sections[30])
    blueprints.append(Blueprint(o, c , oo, oc, go, gob))
    
def main():
    for blueprint in blueprints:
        states : list[State] = []
        final_states : list[State] = []
        factory = Factory(blueprint)
        states.append(State(factory, blueprint, [ORE], [0, 0, 0, 0]))
        i = 0
        start_time = time.time()
        while len(states) > 0:
            #order: start build, collect, end build
            state = states.pop(0)
            options = state.options()
            
            for choice in options:
                new_state = State(factory, blueprint, state.robots.copy(), state.materials.copy(), state.minute)
                new_state.start_build(choice)
                new_state.gather_materials()
                if new_state.factory.is_building:
                    new_state.robots.append(new_state.end_build())
                new_state.minute += 1
                if new_state.minute == 24:
                    final_states.append(new_state)
                else:
                    states.append(new_state)
                    if new_state.minute > i:
                        print(f"now on minute {i}, last minute took {time.time() - start_time}s")
                        start_time = time.time()
                        i += 1
                        
        print("blueprint finished")
        
main()