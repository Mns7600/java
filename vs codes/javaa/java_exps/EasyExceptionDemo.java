import java.util.Scanner;

public class EasyExceptionDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter numerator:");
            String numStr = sc.nextLine();

            System.out.print("Enter denominator:");
            String denStr = sc.nextLine();

            int numerator = Integer.parseInt(numStr);
            int denominator = Integer.parseInt(denStr);

            int result = numerator / denominator;

            System.out.println("Result: " + result);
        } catch (NumberFormatException e) {
            System.out.println("Please enter valid integers.");
        } catch (ArithmeticException e) {
            System.out.println("Denominator cannot be zero.");
        } finally {
            System.out.println("Program finished.");
            sc.close();
        }
    }
}