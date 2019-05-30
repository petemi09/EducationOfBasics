import java.util.ArrayList;
import java.util.Scanner;

class reverse {
    static void printStuff(String str) {
        int lengthString = str.length();   
        ArrayList<Character> list = new ArrayList<Character>();
        for (int i = lengthString - 1; i >= 0; i--) {
            char s = str.charAt(i);
            System.out.print(s);
        }     
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner output = new Scanner(System.in);
        System.out.print("enter a string to be reversed: ");
        String str = output.nextLine();
        printStuff(str);
    }
}