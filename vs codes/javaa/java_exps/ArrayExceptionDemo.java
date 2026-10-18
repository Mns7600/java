import java.util.Scanner;

public class ArrayExceptionDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numbers = {10, 20, 30, 40}; // Fixed array of size 4

        try {
            System.out.print("Enter an array index (0 to 3): ");
            String inputStr = sc.nextLine();

            // Might throw NumberFormatException
            int index = Integer.parseInt(inputStr);

            // Might throw ArrayIndexOutOfBoundsException
            int value = numbers[index];

            System.out.println("Value at index " + index + " is: " + value);

        } catch (NumberFormatException e) {
            System.out.println(
                "Error: Invalid input format. Please enter a valid integer index."
            );

        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println(
                "Error: Index out of bounds. Please enter an index between 0 and 3."
            );

        } finally {
            System.out.println("Array lookup operation completed.");
            sc.close();
        }
    }
}