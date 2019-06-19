package mann.mike.stack.arrays;

public class Main {

	public static void main(String[] args) {
		
		StackArr<Integer> myStack = new StackArr<Integer>();
		
		int firstVal = 1;
		int secondVal = 2;
		int thirdVal = 3;
		
		System.out.println(myStack.isEmpty());
		
		myStack.push(firstVal);
		System.out.println(myStack.top());
		myStack.push(secondVal);
		System.out.println(myStack.top());
		myStack.push(thirdVal);
		System.out.println(myStack.top());
		
		System.out.println(myStack.isEmpty());
		
		myStack.pop();
		System.out.println("Size of stack is " + myStack.size());
		myStack.pop();
		System.out.println("Size of stack is " + myStack.size());
		myStack.pop();
		System.out.println("Size of stack is " + myStack.size());
		
		System.out.println(myStack.isEmpty());
	
		
	}

}
