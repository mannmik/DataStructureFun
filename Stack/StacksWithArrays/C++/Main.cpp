#include "StackADT.hpp"
#include <iostream>
#include <vector>


using namespace std;

int main()
{

	StackADT<int> *myStack = new StackADT<int>;

	myStack->push(1);
	myStack->push(2);
	myStack->push(3);
	cout << myStack->isEmpty() << endl;
	cout << myStack->top() << endl;

	myStack->pop();
	myStack->pop();
	myStack->pop();

	cout << myStack->isEmpty() << endl;
	
	delete myStack;
	myStack = NULL;
	return 0;
}