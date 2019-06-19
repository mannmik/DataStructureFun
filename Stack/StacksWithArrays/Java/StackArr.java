package mann.mike.stack.arrays;

import java.util.ArrayList;

public class StackArr<T> {
	
	private ArrayList<T> stackContainer = new ArrayList<T>();
	
	// push
	public void push (T val)
	{
		this.stackContainer.add(val);
	}
	
	// pop
	public void pop()
	{
		if (!isEmpty()) 
		{
			this.stackContainer.remove(this.stackContainer.size() - 1);
		}
	}
	
	
	// isEmpty
	public boolean isEmpty()
	{
		return this.stackContainer.isEmpty();
	}
	
	// Top
	public T top()
	{
		if (!isEmpty())
		{	
			return this.stackContainer.get(this.stackContainer.size() - 1);
		}
		return null;
	}
	
	
	// Size
	public int size()
	{
		return this.stackContainer.size();
	}
}
