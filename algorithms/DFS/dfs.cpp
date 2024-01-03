#include <map>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <stack>

namespace DFS
{
	using AdjacencyList = std::map<size_t, std::vector<size_t>>;
	using NodeList = std::vector<size_t>;
	class DFS
	{
	public:
		DFS(AdjacencyList aList, bool verbose) : mE(aList), mVerbose(verbose)
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

		size_t getUniqueComponents()
		{
			return std::unordered_set<size_t>(mComponent.begin(), mComponent.end()).size();
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
			if (mVerbose)
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
			if (mVerbose)
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
			if (mVerbose)
				std::cout << "TRAVERSE_TREEEDGE("<<v << ", " << w << ")\n"; 

			mOReps.push(w);
			mONodes.push_back(w);
			mDfsNum.insert_or_assign(w, mDfsPos++);
		}

		void mBacktrack(size_t u, size_t v)
		{
			if (mVerbose)
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
		bool mVerbose = false;
	};
} // namespace DFS
