import java.util.Scanner;  // Import the Scanner class

class MyClass {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter username");

    String userName = myObj.nextLine();  // Read user input
    System.out.println("Username is: " + userName);  // Output user input 
    // my stuff
    for (int i = 0; i < userName.length(); i++) {
    //for (int i = 0; i < userName.length(); i++) {
        System.out.print(userName.charAt(i) + " ");
    }
  }
}