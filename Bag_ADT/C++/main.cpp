#include "Bag.hpp"
#include <iostream>

int main()
{
	// create new instance of bag class
	Bag *myBag = new Bag;

	int firstVal = 3;
	int secondVal = 2;

	// add in two values and print the result of contains
	myBag->add(firstVal);
	cout << myBag->contains(firstVal);
	myBag->add(secondVal);
	cout << myBag->contains(secondVal);

	// remove the first value added and print contains on that value
	myBag->remove(firstVal);
	cout << myBag->contains(firstVal);

	// clear memory created
	delete myBag;
	myBag = NULL;
	return 0;
}