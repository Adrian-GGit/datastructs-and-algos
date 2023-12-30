#include <map>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <stack>

#ifdef VERBOSE
bool verbose = true;
#else
bool verbose = false;
#endif

namespace DFS
{
	using AdjacencyList = std::map<size_t, std::vector<size_t>>;
	using NodeList = std::vector<size_t>;
	class DFS
	{
	public:
		DFS(AdjacencyList aList) : mE(aList)
		{
			for (auto it = mE.begin(); it != mE.end(); it++)
			{
				mV.push_back(it->first);
			}
			mComponent.resize(mV.size());
		}

		void process()
		{
			for (size_t v : mV)
			{
				if (mVisited.contains(v))
				{
					continue;
				}
				mVisited.insert(v);
				mRoot(v);
				mDfs(v, v);
			}
		}

		std::vector<size_t> getComponent()
		{
			return mComponent;
		}

	private:
		void mRoot(size_t v)
		{
			mOReps.push(v);
			mONodes.push_back(v);
			mDfsNum.insert_or_assign(v, mDfsPos++);
		}

		void mDfs(size_t u, size_t v)
		{
			if (verbose)
				std::cout << "DFS("<<u << ", " << v << ")\n"; 

			for (size_t w : mE.at(v))
			{
				if (mVisited.contains(w))
				{
					mTraverseNonEdgeTree(v, w);
					continue;
				}
				mTraverseTreeEdge(v, w);
				mVisited.insert(w);
				mDfs(v, w);
			}
			mBacktrack(u, v);
		}
		void mTraverseNonEdgeTree(size_t v, size_t w)
		{
			if (verbose)
				std::cout << "TRAVERSE_NONTREEEDGE("<<v << ", " << w << ")\n"; 
			for (size_t x : mONodes)
			{
				if( x == w)
				{
					while (mDfsNum[w] < mDfsNum[mOReps.top()])
					{
						mOReps.pop();
					}
					break;
				}
			}
		}

		void mTraverseTreeEdge(size_t v, size_t w)
		{
			if (verbose)
				std::cout << "TRAVERSE_TREEEDGE("<<v << ", " << w << ")\n"; 

			mOReps.push(w);
			mONodes.push_back(w);
			mDfsNum.insert_or_assign(w, mDfsPos++);
		}

		void mBacktrack(size_t u, size_t v)
		{
			if (verbose)
				std::cout << "BACKTRACK("<<u << ", " <<v  << ")\n"; 

			if (v != mOReps.top())
			{
				return;
			}

			mOReps.pop();

			while (1)
			{
				size_t w = mONodes.back();
				mONodes.pop_back();
				mComponent[w] = v;
				if (w == v)
				{
					break;
				}
			}
		}

		AdjacencyList mE;
		NodeList mV;
		std::unordered_set<size_t> mVisited;
		std::stack<size_t> mOReps;
		std::vector<size_t> mONodes;
		std::unordered_map<size_t, size_t> mDfsNum;
		std::vector<size_t> mComponent;
		size_t mDfsPos = 0;
	};
} // namespace DFS

int main()
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

	auto dfs = DFS::DFS(aList);
	dfs.process();

	std::cout << "SCCs after DFS:\n";
	for (size_t c : dfs.getComponent())
	{
		std::cout << c << ", ";
	}
	std::cout << std::endl;
}