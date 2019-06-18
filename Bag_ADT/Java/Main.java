package mann.mike.bagContainer;

public class Main {

	public static void main(String[] args) {
		
		Bag myBag = new Bag();
		
		int firstVal = 2;
		int secondVal = 19;
		
		myBag.add(firstVal);
		System.out.println(myBag.contains(firstVal));
		myBag.add(secondVal);
		System.out.println(myBag.contains(secondVal));
		
		myBag.remove(firstVal);
		System.out.println(myBag.contains(firstVal));

	}

}
