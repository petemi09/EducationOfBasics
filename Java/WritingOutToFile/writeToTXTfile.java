// Created by Mitchell Petellin
//
// Purpose is to have a simple input write out to a file


import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;


class OutPut {
    // public static void nameOfFile() {
    //     Scanner str1 = new Scanner(System.in);
    //     String fileName = str1.nextLine();
    // }

    public static void nothing() throws IOException {
        String fileContent = "hello fucker";
        FileWriter fileWriter = new FileWriter("/Users/Mpetellin11/Desktop/Bitches.txt");
        fileWriter.write(fileContent);
        fileWriter.close();
    }
    public static void main(String[] args) throws IOException {
        System.out.println("hello");
        nothing();
    }
}