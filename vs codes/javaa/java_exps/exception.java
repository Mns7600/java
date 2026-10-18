
import java.util.*;

public class exception {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter age: ");
            int age = sc.nextInt();

            if (age < 0) {
                throw new IllegalArgumentException(
                    "Age cannot be negative"
                );
            }

            System.out.println("Age: " + age);
        }
        catch (InputMismatchException e) {
            System.out.println("Enter a number!");
        }
        catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        finally {
            sc.close();
        }
    }
}
