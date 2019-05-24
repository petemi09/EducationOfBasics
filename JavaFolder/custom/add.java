import java.util.Scanner;

class putTogether {
    static void add1(int int1, int int2) {
        int number = int1 + int2;
        System.out.println("your numbers added together: " + number);
    }

    public static void main(String[] args) {	
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer1: ");
        int number1 = input.nextInt();

        Scanner input2 = new Scanner(System.in);
        System.out.print("enter integer2: ");
        int number2 = input2.nextInt();
        
        add1(number1,number2);
    }
}