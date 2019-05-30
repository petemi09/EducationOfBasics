import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.lang.*;

class lolz {
    public static void main(String[] args) {
        int[] numbers = {0,1,0};
        for(int i = 0; i < 200; i++) {
            Random rand2 = new Random();
            int n = rand2.nextInt(100); 

            String binary = "";

            for (int o = 0; o < n; o++) {
                Random rand = new Random();
                int q = rand.nextInt(2);
                binary += numbers[q];
            }

            try {
                Thread.sleep(25);
            } catch (Exception e) {
                System.out.println(e);
            }

            System.out.println(binary);
        }
    }
}