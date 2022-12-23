#include <stdio.h>

#include <list>
#include <unordered_set>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <chrono>
#include <algorithm>

constexpr auto NONE = -1;
constexpr auto ORE = 0;
constexpr auto CLAY = 1;
constexpr auto OBSIDIAN = 2;
constexpr auto GEODE = 3;

constexpr auto OREVALUE = 1;
constexpr auto CLAYVALUE = 0.5;
constexpr auto OBSIDIANVALUE = 16;
constexpr auto GEODEVALUE = 100;

typedef struct Blueprint
{
    short int oreRobotCost;
    short int clayRobotCost;
    short int obsidianRobotOreCost;
    short int obsidianRobotClayCost;
    short int geodeRobotOreCost;
    short int geodeRobotObsidianCost;
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

    std::string string()
    {
        std::string str("");
        str.append("{ ");
        str.append(std::to_string(oreRobots));
        str.append(", ");
        str.append(std::to_string(clayRobots));
        str.append(", ");
        str.append(std::to_string(obsidianRobots));
        str.append(", ");
        str.append(std::to_string(geodeRobots));
        str.append(" }");
        return str;
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

    std::string string()
    {
        std::string str("");
        str.append("{ ");
        str.append(std::to_string(ore));
        str.append(", ");
        str.append(std::to_string(clay));
        str.append(", ");
        str.append(std::to_string(obsidian));
        str.append(", ");
        str.append(std::to_string(geodes));
        str.append(" }");
        return str;
    }
} Materials;

class State
{
    public:
        short int minute = 1;
        
        Robots robots;
        Materials materials;

        State(
        Robots robots,
        Materials materials,
        short int min) : 
        robots(1, 0, 0, 0),
        materials(0, 0, 0, 0)
        {
            this->robots = robots;
            this->materials = materials;
            this->minute = min;
        }

        float EstimatedScore()
        {
            float estimate = 0;
            estimate += ((robots.oreRobots * OREVALUE) + materials.ore) * OREVALUE;
            estimate += ((robots.clayRobots * CLAYVALUE) + materials.clay) * CLAYVALUE / (minute / 10);
            estimate += ((robots.obsidianRobots * OBSIDIANVALUE) + materials.obsidian) * OBSIDIANVALUE * (minute / 3);
            estimate += ((robots.geodeRobots * GEODEVALUE) + materials.geodes) * GEODEVALUE * (minute / 2);
            return estimate;
        }

        bool CanBuildRobot(const Blueprint &blueprint, short int type)
        {
            if (type == ORE)
                return this->materials.ore >= blueprint.oreRobotCost;
            if (type == CLAY)
                return this->materials.ore >= blueprint.clayRobotCost;
            if (type == OBSIDIAN)
                return this->materials.ore >= blueprint.obsidianRobotOreCost &&
                    this->materials.clay >= blueprint.obsidianRobotClayCost;
            if (type == GEODE)
                return this->materials.ore >= blueprint.geodeRobotOreCost &&
                    this->materials.obsidian >= blueprint.geodeRobotObsidianCost;
            return false;
        }

        std::vector<short int> Options(const Blueprint& blueprint)
        {
            std::vector<short int> opts;
            opts.push_back(NONE);
            if (CanBuildRobot(blueprint, ORE))
                opts.push_back(ORE);
            if (CanBuildRobot(blueprint, CLAY))
                opts.push_back(CLAY);
            if (CanBuildRobot(blueprint, OBSIDIAN))
                opts.push_back(OBSIDIAN);
            if (CanBuildRobot(blueprint, GEODE))
                opts.push_back(GEODE);
            return opts;
        }
        
        bool StartBuild(const Blueprint &blueprint, short int type)
        {
            if (type == NONE)
                return false;
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
            return true;
        }

        void GatherResources()
        {
            materials.ore += robots.oreRobots;
            materials.clay += robots.clayRobots;
            materials.obsidian += robots.obsidianRobots;
            materials.geodes += robots.geodeRobots;
        }

        void EndBuild(short int typeBuilding)
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
        }

        std::string string()
        {
            std::string str = "";
            str.append("Robots: ");
            str.append(robots.string());
            str.append(", Materials: ");
            str.append(materials.string());
            return str;
        }

        bool operator==(const State& other) const {
            return minute == other.minute &&
                robots.oreRobots == other.robots.oreRobots &&
                robots.clayRobots == other.robots.clayRobots &&
                robots.obsidianRobots == other.robots.obsidianRobots &&
                robots.geodeRobots == other.robots.geodeRobots &&
                materials.ore == other.materials.ore &&
                materials.clay == other.materials.clay &&
                materials.obsidian == other.materials.obsidian &&
                materials.geodes == other.materials.geodes;
        }
};

struct hash_fn
{
    std::size_t operator() (const State& state) const
    {
        std::size_t m = std::hash<short int>()(state.minute);
        std::size_t r1 = std::hash<int>()(state.robots.oreRobots);
        std::size_t r2 = std::hash<int>()(state.robots.clayRobots);
        std::size_t r3 = std::hash<int>()(state.robots.obsidianRobots);
        std::size_t r4 = std::hash<int>()(state.robots.geodeRobots);
        std::size_t m1 = std::hash<int>()(state.materials.ore);
        std::size_t m2 = std::hash<int>()(state.materials.clay);
        std::size_t m3 = std::hash<int>()(state.materials.obsidian);
        std::size_t m4 = std::hash<int>()(state.materials.geodes);

        return m ^ r1 << 1 ^ r2 << 2 ^ r3 << 3 ^ r4 << 4 ^ m1 << 5 ^ m2 << 6 ^ m3  << 7 ^ m4 << 8;
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

short int strToInt(std::string str) 
{
    std::stringstream ss;
    int c = 0;
    ss << str;
    ss >> c;
    return c;
}

std::string durationString(std::chrono::duration<long long, std::nano> dur)
{
    std::stringstream ss;
    ss << dur.count() / (float)1000000000;
    std::string s;
    ss >> s;
    return s;
}

bool GreaterScore(State state1, State state2)
{
    float score1 = state1.EstimatedScore();
    float score2 = state2.EstimatedScore();
    return score1 > score2;
}

int main()
{
    std::ifstream input_file("day19test.txt");
    std::vector<Blueprint> blueprints;

    while (input_file)
    {
        std::string line;
        std::getline(input_file, line);
        std::vector<std::string> words = split(line, ' ');
        short int o;
        short int c;
        short int oo;
        short int oc;
        short int go;
        short int gob;

        if (words.size())
        {
            o = strToInt(words[6]);
            c = strToInt(words[12]);
            oo = strToInt(words[18]);
            oc = strToInt(words[21]);
            go = strToInt(words[27]);
            gob = strToInt(words[30]);

            blueprints.push_back(Blueprint{ o, c, oo, oc, go, gob });
        }
    }

    for (auto bp : blueprints)
    {
        std::unordered_set<State, hash_fn>* states = new std::unordered_set<State, hash_fn>;//(1048576); //1048576 = 4^10
        std::unordered_set<State, hash_fn>* newStates = new std::unordered_set<State, hash_fn>;//(1048576); //1048576 = 4^10
        std::vector<State>* finalStates = new std::vector<State>;//(1048576);
        states->emplace(Robots(1, 0, 0, 0), Materials{ 0, 0, 0, 0 }, 1);

        int i = 0;
        std::chrono::high_resolution_clock clock;
        std::chrono::high_resolution_clock::time_point start = clock.now();
        while (!states->empty() || !newStates->empty())
        {
            if (states->empty()) {
                states = newStates;
                newStates = new std::unordered_set<State, hash_fn>;
                std::cout << "now on minute " << states->begin()->minute << ", last minute took " << durationString(clock.now() - start) << std::endl;
                start = clock.now();
            }

            State state = *(states->begin());
            states->erase(state);
            std::vector<short int> options = state.Options(bp);

            for (auto choice : options)
            {
                State newState = state;
                bool isBuilding = newState.StartBuild(bp, choice);
                newState.GatherResources();
                if (isBuilding)
                    newState.EndBuild(choice);
                newState.minute++;
                //std::cout << newState.minute << std::endl;
                if (newState.minute == 24)
                {
                    //std::cout << "finished state with mats " << newState.materials.string() << std::endl;
                    finalStates->push_back(newState);
                }
                else
                {
                    /*                  if (newState.minute > i)
                                        {
                                            std::cout << "now on minute " << newState.minute << ", last minute took " << durationString(clock.now() - start) << std::endl;
                                            start = clock.now();
                                            i++;
                                            if (i >= 10)
                                            {
                                                std::sort(states->begin(), states->end(), GreaterScore);
                                                std::cout << "sorted" << std::endl;
                                                std::list<State>::iterator halfway = states->begin();
                                                std::advance(halfway, states->size() * 2.0/3.0);
                                                states->erase(halfway, states->end());
                                                std::cout << "erased, new len is " << states->size() << std::endl;
                                            }
                                        }*/
                    newStates->insert(newState);
                }
            }
        }

        State bestState = (*finalStates)[0];
        int best = bestState.materials.geodes;
        for (const auto &candidate : (*finalStates))
        {
            if (candidate.materials.geodes > best)
            {
                best = candidate.materials.geodes;
                bestState = candidate;
            }
        }
        std::cout << "best geode score was " << best << std::endl;
        std::cout << "winning state: " << bestState.string() << std::endl;
    }

    std::cin.get();
    return 0;
}