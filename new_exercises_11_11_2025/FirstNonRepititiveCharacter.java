import java.util.Scanner;

public class FirstNonRepititiveCharacter{

	public static void getLetter(String userInput){
		int counting = 0;
		for (int count = 0; count < userInput.length(); count++){
			char letterOne = userInput.charAt(count);
			char checker = letterOne;
			for (int counter = 0; counter < userInput.length(); counter++){
				char letterTwo = userInput.charAt(counter);
				if (letterOne == letterTwo){
					counting++;
				}
			}
			if (counting == 1){
				System.out.print(letterOne);
				break;
			}
			counting = 0;
		}
	}
	
	public static void main(String[] args){
		Scanner inputCollector = new Scanner(System.in);

		System.out.print("Enter a word: ");
		String userInput = inputCollector.nextLine();
		

		getLetter(userInput);
		
	}
}