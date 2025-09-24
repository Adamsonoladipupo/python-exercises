/*
Pseudocode
- write a prompt highlighting the use of the app to the user
- Collect three inputs from the user, store them each in a variable as score1, score2 and score3.
- declare and initialize a variable as the average of the scores, initialize it to be the sum of the three score, and divide it by 3.
- check if the average is less than equals to 100 and greater than equals to 90, print "A", if not,
- check if the average is less than 90 and greater than equals to 80, print "B", if not,
- check if the average is less than 80 and greater than equal to 70, print "C", if not
- check if the average is less than 70 and greater than equal to 60, print "D", if not
- print "F"
*/

import java.util.Scanner;

public class averageOfScores{
public static void main(String[] args){
System.out.println("Welcome! This app helps you grade a student based on their score");

Scanner input = new Scanner(System.in);
System.out.print("Enter score 1: ");
int score1 = input.nextInt();

System.out.print("Enter score 2: ");
int score2 = input.nextInt();

System.out.print("Enter score 3: ");
int score3 = input.nextInt();

int averageScore = (score1+score2+score3)/3;

if (90<= averageScore && averageScore <=100){
System.out.print("your grade is A");
} else if (80<= averageScore && averageScore <90){
System.out.print("your grade is B");
} else if (70<= averageScore && averageScore <80){
System.out.print("your grade is C");
} else if (60<= averageScore && averageScore <70){
System.out.print("your grade is D");
} else if (0<= averageScore && averageScore <60){
System.out.print("your grade is F");
} else {System.out.print("INVALID result, not within the scope of the grading system");}


}
}