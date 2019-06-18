
#ifndef STACKADT_HPP
#define STACKADT_HPP

#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <stdexcept>


using namespace std;

template <class T>
class StackADT
{
	private:
		vector<T> stackContainer;

	public:


		void push(T val)
		{
			stackContainer.push_back(val);
		}


		void pop()
		{
			stackContainer.pop_back();
		}

		T top()
		{
			return stackContainer.back();
		}

		bool isEmpty() {
			return stackContainer.empty();
		}

};
#endif




