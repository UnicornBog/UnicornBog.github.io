
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();

        int secretNumber = random.nextInt(250) + 1;
        System.out.println("Think of a number between 1 and 250");
        System.out.println("After each guess let the computer know if the guess is too high, too low, or correct");
        System.out.println("Higher(H)");
        System.out.println("Lower(L)");
        System.out.println("Correct(C)");
        System.out.println("Loading, is your number " + secretNumber + "?");

        Scanner scanner = new Scanner(System.in);
        String response = scanner.nextLine();
        
        while (!response.equalsIgnoreCase("C")) {
            if (response.equalsIgnoreCase("L")) {
                secretNumber = random.nextInt(secretNumber + 1) + 1;
                System.out.println("Is your number " + secretNumber + "?");
            }
            else if (response.equalsIgnoreCase("H")) {
                secretNumber = random.nextInt(250 - secretNumber) + secretNumber + 1;
                System.out.println("Is your number " + secretNumber + "?");
            }
            else if (response.equalsIgnoreCase("C")) {
                System.out.println("Yay! I guessed your number!");
            }
            response = scanner.nextLine();
        }
        scanner.close();
    }
}