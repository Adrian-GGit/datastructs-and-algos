#include <map>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include "../algorithms/DFS/dfs.cpp"

#ifdef VERBOSE
bool verbose = true;
#else
bool verbose = false;
#endif

bool testNumSCCs_Listcase()
{
    std::map<size_t, std::vector<size_t>> aList;
    for (size_t i = 0; i < 10; i++)
    {
        aList[i] = std::vector<size_t>();
        aList[i].push_back(i + 1);
    }
    aList[10] = std::vector<size_t>();

    auto dfs = DFS::DFS(aList, verbose);
    dfs.process();
    return dfs.getUniqueComponents() == aList.size();
}

bool testNumSCCs_LectureCase()
{
    std::map<size_t, std::vector<size_t>> aList;

    for (size_t i = 0; i < 11; i++)
    {
        aList[i] = std::vector<size_t>();
    }
    aList[0] = {1};
    aList[1] = {2};
    aList[2] = {0};
    aList[3] = {4};
    aList[4] = {5, 6, 7};
    aList[5] = {6};
    aList[6] = {};
    aList[7] = {8};
    aList[8] = {4, 9};
    aList[9] = {2, 10};
    aList[10] = {3};

    auto dfs = DFS::DFS(aList, verbose);
    dfs.process();
    return dfs.getUniqueComponents() == 4;
}

bool testSCCMembers_Tutorialcase()
{
    std::map<size_t, std::vector<size_t>> aList;

    for (size_t i = 0; i < 8; i++)
    {
        aList[i] = std::vector<size_t>();
    }
    aList[0] = {1, 5};
    aList[1] = {2, 4};
    aList[2] = {3};
    aList[3] = {1};
    aList[4] = {1};
    aList[5] = {6, 7};
    aList[6] = {0, 4};
    aList[7] = {};

    auto dfs = DFS::DFS(aList, verbose);
    dfs.process();
    std::vector<size_t> solComponent = {0, 1, 1, 1, 1, 0, 0, 7};
    auto comps = dfs.getComponent();

    for(size_t i = 0; i < std::min(solComponent.size(), comps.size()); i++)
    {
        if (comps[i] != solComponent[i])
        {
            return false;
        }    
    }
    return true;
}

int main()
{
    std::cout << "C++ DFS Testcases:\n  ";
    std::cout << (testNumSCCs_Listcase() ? "P" : "F");
    std::cout << (testNumSCCs_LectureCase() ? "P" : "F");
    std::cout << (testSCCMembers_Tutorialcase() ? "P" : "F");
    std::cout << "\n";
}