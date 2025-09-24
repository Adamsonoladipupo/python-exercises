/*
Pseudocode:
- write a prompt highlighting the use of the app to the user
- declare and initialize a variables that store an input from the user as the:
 	- current year
	- father's current age
	- son's current age
- declare a variable that store the value of when the father is/was twice as old as the son, and initialize it to be 2 multiply by the son's age minus the father's age
- declare a variable that store the year when the father is/was twice as old as the son, initilize it to be currenct year plus the father's twice as old age
- print the number of years ago the father is/was twice as old as the son and the year. 
*/

import java.util.Scanner;

public class fatherTwiceAsOldAsSon{
public static void main(String[] args){
System.out.println("Welcome! This app helps you determine the number of years and year you are twice as old as your son");

Scanner input = new Scanner(System.in);
System.out.print("Enter the current year: ");
int currentYear = input.nextInt();

System.out.print("Enter the father's currecnt age: ");
int currentFatherAge = input.nextInt();

System.out.print("Enter the son's currecnt age:  ");
int currentSonAge = input.nextInt();

int fatherTwiceAsOld = 2*currentSonAge - currentFatherAge;
int yearFatherTwiceAsOld = currentYear + fatherTwiceAsOld;

System.out.printf("Father was/is twice as old as son %d years ago, in the year %d",fatherTwiceAsOld, yearFatherTwiceAsOld);

}
}