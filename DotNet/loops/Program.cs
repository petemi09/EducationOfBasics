using System;

namespace ConditionsPT2
{
    class Program
    {
        static void loops()
        {
            int counter = 0;
            while (counter < 10)
            {
                Console.WriteLine($"Hello World! The counter is {counter}");
                counter++;
            }
            counter = 0;
            Console.WriteLine("$$$$$$$$$$$$$");
            do
            {
                Console.WriteLine($"Hello World! The counter is {counter}");
                counter++;
            } while (counter < 10);
        }

        static void moreLoops()
        {
            for(int index = 0; index < 10; index++)
                {
                    Console.WriteLine($"The index is {index}");
                }
        }

        static void tutorialCode()
        {
            int total = 0;
            for(int num = 0; num <= 20; num++)
            {
                if ((num % 3) == 0) 
                {
                    Console.WriteLine($"yes {num}");
                    total += num;
                }
            }
            Console.WriteLine($"the total is {total}");
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            loops();
            moreLoops();
            tutorialCode();
        }
    }
}
