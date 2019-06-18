package mann.mike.bagContainer;
import java.util.*;


public class Bag 
{
	private ArrayList bagContainer = new ArrayList();
	
	
	
	public void add(int val)
	{
		this.bagContainer.add(val);
	}
	
	
	
	public boolean contains(int val)
	{
		return this.bagContainer.contains(val);
	}
	
	
	public void remove(int val)
	{
		for (int i = 0; i < this.bagContainer.size(); ++i)
		{	
			
			if ((int)this.bagContainer.get(i) == val)
			{
				this.bagContainer.remove(i);
				return;
			}
		}
		
	}
		
}
