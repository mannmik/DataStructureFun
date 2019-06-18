#include "Bag.hpp"

	// adds a value to our bag container by pushing to our vector
	void Bag::add(int val)
	{
		bagContainer.push_back(val);
	}


	// loops through vector and returns true if it finds a matching val for the function parameter
	bool Bag::contains(int val)
	{
		for (int i = 0; i < bagContainer.size; ++i)
		{
			if (bagContainer[i] == val)
			{
				return true;
			}
		}

		return false;
	}


	// removes any value int the bag container matching the function parameter
	void Bag::remove(int val)
	{
		for (int i = 0; i < bagContainer.size; ++i)
		{
			if (bagContainer[i] == val)
			{
				bagContainer.erase(bagContainer.begin + i);
			}
		}

	}