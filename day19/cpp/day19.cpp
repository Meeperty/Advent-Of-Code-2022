#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

#define NONE -1
#define ORE 0
#define CLAY 1
#define OBSIDIAN 2
#define GEODE 3

typedef struct Blueprint
{
    char oreRobotCost;
    char clayRobotCost;
    char obsidianRobotOreCost;
    char obsidianRobotClayCost;
    char geodeRobotOreCost;
    char geodeRobotObsidianCost;
} Blueprint;

typedef struct Robots
{
    int oreRobots;
    int clayRobots;
    int obsidianRobots;
    int geodeRobots;
    
    Robots(int o, int c, int ob, int g)
    {
        oreRobots = o;
        clayRobots = c;
        obsidianRobots = ob;
        geodeRobots = g;
    }
} Robots;

typedef struct Materials
{
    int ore = 0;
    int clay = 0;
    int obsidian = 0;
    int geodes = 0;

    Materials(int o, int c, int ob, int g)
    {
        ore = o;
        clay = c;
        obsidian = ob;
        geodes = g;
    }
} Materials;

class State
{
    public:
        char minute = 1;

        bool isBuilding = false;
        char typeBuilding = NONE;

        Blueprint blueprint;
        Robots robots;
        Materials materials;

        State(Blueprint& blueprint, 
        Robots robots,
        Materials materials,
        char min) : 
        robots(1, 0, 0, 0),
        materials(0, 0, 0, 0)
        {
            this->blueprint = blueprint;
            this->robots = robots;
            this->materials = materials;
            this->minute = min;
        }

        bool CanBuildRobot(char type)
        {
            if (type == ORE)
                return this->materials.ore >= this->blueprint.oreRobotCost;
            if (type == CLAY)
                return this->materials.ore >= this->blueprint.clayRobotCost;
            if (type == OBSIDIAN)
                return this->materials.ore >= this->blueprint.obsidianRobotOreCost &&
                    this->materials.clay >= this->blueprint.obsidianRobotClayCost;
            if (type == GEODE)
                return this->materials.ore >= this->blueprint.geodeRobotOreCost &&
                    this->materials.obsidian >= this->blueprint.geodeRobotObsidianCost;
            return false;
        }

        std::vector<char> Options()
        {
            std::vector<char> opts;
            opts.push_back(NONE);
            if (CanBuildRobot(ORE))
                opts.push_back(ORE);
            if (CanBuildRobot(CLAY))
                opts.push_back(CLAY);
            if (CanBuildRobot(OBSIDIAN))
                opts.push_back(OBSIDIAN);
            if (CanBuildRobot(GEODE))
                opts.push_back(GEODE);
            return opts;
        }
        
        void StartBuild(char type)
        {
            if (type == NONE)
                return;
            if (type == ORE)
                materials.ore -= blueprint.oreRobotCost;
            if (type == CLAY)
                materials.ore -= blueprint.clayRobotCost;
            if (type == OBSIDIAN)
            {
                materials.ore -= blueprint.obsidianRobotOreCost;
                materials.clay -= blueprint.obsidianRobotClayCost;
            }
            if (type == GEODE)
            {
                materials.ore -= blueprint.geodeRobotOreCost;
                materials.obsidian -= blueprint.geodeRobotObsidianCost;
            }
            typeBuilding = type;
            isBuilding = true;
        }

        void GatherResources()
        {
            materials.ore += robots.oreRobots;
            materials.clay += robots.clayRobots;
            materials.obsidian += robots.obsidianRobots;
            materials.geodes += robots.geodeRobots;
        }

        void EndBuild()
        {
            switch (typeBuilding)
            {
                case ORE:
                    robots.oreRobots++;
                    break;
                
                case CLAY:
                    robots.clayRobots++;
                    break;

                case OBSIDIAN:
                    robots.obsidianRobots++;
                    break;

                case GEODE:
                    robots.geodeRobots++;
                    break;
            }
            typeBuilding = NONE;
            isBuilding = false;
        }
};

//these are copied from https://stackoverflow.com/questions/236129/how-do-i-iterate-over-the-words-of-a-string
template <typename Out>
void split(const std::string &s, char delim, Out result) {
    std::istringstream iss(s);
    std::string item;
    while (std::getline(iss, item, delim)) {
        *result++ = item;
    }
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}

char strToCharNumber(std::string str) 
{
    std::stringstream ss;
    int c = 0;
    ss << str;
    ss >> c;
    return (char)c;
}

int main() 
{
    std::ifstream input_file("day19.txt");
    std::vector<Blueprint> blueprints;

    while (input_file)
    {
        std::string line;
        std::getline(input_file, line);
        std::vector<std::string> words = split(line, ' ');
        char o;
        char c;
        char oo;
        char oc;
        char go;
        char gob;

        if (words.size())
        {
            o = strToCharNumber(words[6]);
            c = strToCharNumber(words[12]);
            oo = strToCharNumber(words[18]);
            oc = strToCharNumber(words[21]);
            go = strToCharNumber(words[27]);
            gob = strToCharNumber(words[30]);
        }
        blueprints.push_back(Blueprint{o, c, oo, oc, go, gob});
    }
    
    for (auto bp : blueprints)
    {
        std::vector<State>* states = new std::vector<State>;//(1048576); //1048576 = 4^10
        std::vector<State>* finalStates = new std::vector<State>;//(1048576);
        states->push_back(State(bp, Robots(1, 0, 0, 0), Materials{0, 0, 0, 0}, 1));

        while (states->size())
        {
            State state = (*states)[states->size()];
            std::vector<char> options = state.Options();
            std::cout << "state at " << &state << " has " << state.materials.ore << " ore"<< std::endl;

            for (auto choice : options)
            {
                State newState = state;
                newState.StartBuild(choice);
                newState.GatherResources();
                if (newState.isBuilding)
                    newState.EndBuild();
                newState.minute++;
                //std::cout << newState.minute << std::endl;
                if (newState.minute == 24)
                    finalStates->push_back(newState);
                else
                    states->push_back(newState);
            }
            states->pop_back();
        }

        int best = 0;
        for (auto final : (*finalStates))
        {
            if (final.materials.geodes > best)
            {
                best = final.materials.geodes;
            }
        }
        std::cout << "best geode score was " << best << std::endl;
    }

    return 0;
}