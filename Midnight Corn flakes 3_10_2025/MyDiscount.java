import java.util.Scanner;

public class MyDiscount{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		double number1 = input.nextDouble();
		double number2 = input.nextDouble();
		double result = MyDsicount(number1, number2);
		System.out.printf("Your discounted price is: %d", result);
	}
	public static double MyDiscount(double input1, double input2){
		double discount = input1 - (input1 * (input2/100));
	}
}