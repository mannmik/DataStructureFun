#ifndef BAG_HPP
#define BAG_HPP
#include <iostream> 
#include <vector> 
using namespace std;

class Bag
{
    private:
        vector<int> bagContainer;

    public:
        // adds value to our bag container
		void add(int val);
        // returns true if the bag container contains the specified value
		bool contains(int val);
        // removes the value sent in as parameter
		void remove(int val);

};
#endif