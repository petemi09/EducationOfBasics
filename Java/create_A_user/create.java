/*
Created By Mitchell Petellin
A simple program that creates a user and a password
A way to learn how to return values from different functions
and how to get values from a String with random and add them to a new list
*/

import java.util.Scanner;
import java.io.CharArrayReader;
import java.util.Random;

class newUser {

    static void userFinal(String userName, String userPass) {
        // prints out the username and password from the main

        System.out.println();
        System.out.println("Your user name is: " + userName);
        System.out.println("Your password is: " + userPass);
    }

    static String genPass(String lengthInt) {
        //randomly selects and creates a string for a new password

        String list = "";
        Random r = new Random();
        int result = Integer.parseInt(lengthInt);
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i < result; i++) {
            char item = alphabet.charAt(r.nextInt(alphabet.length()));
            list += item;
        }
        return list;
    }

    public static void main(String[] args) {
        Scanner newPerson = new Scanner(System.in);  // Create a Scanner object
        System.out.print("Enter username: ");
        String userName = newPerson.nextLine();  // Read user input
        
        Scanner password = new Scanner(System.in);
        System.out.print("Would you like to generate a random password (y/n): ");
        String pass1 = password.nextLine();  // Read user input
       
        if (pass1.equals("y")) {
            Scanner lengthOfPass = new Scanner(System.in);
            System.out.print("how long do you want your password to be? (enter a int!): ");
            String lengthInt = lengthOfPass.nextLine();
            genPass(lengthInt);
            String userPass = genPass(lengthInt);
            userFinal(userName, userPass);
            
        } else {
            Scanner userPassword = new Scanner(System.in);
            System.out.print("Enter your password: ");
            String userPass = userPassword.nextLine();
            userFinal(userName, userPass);
        }
    }
}