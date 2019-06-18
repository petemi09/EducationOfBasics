using System;

namespace ConditionsPT1
{
    class Program
    {
        static void ifAndElse()
        {
            int a = 5;
            int b = 3;
            if (a + b > 10)
                Console.WriteLine("The answer is greater than 10");
            else
                Console.WriteLine("The answer is not greater than 10");

            int c = 4;
            Console.WriteLine("----------");
            if ((a + b + c > 10) && (a == b))
            {
                Console.WriteLine("The answer is greater than 10");
                Console.WriteLine("And the first number is equal to the second");
            }
            else
            {
                Console.WriteLine("The answer is not greater than 10");
                Console.WriteLine("Or the first number is not equal to the second");
}           Console.WriteLine("------------");
            int d = 4;
            if (c == d)
            Console.WriteLine("they are the same");

            if ((a + b + c > 10) || (a == b))
            {
                Console.WriteLine("The answer is greater than 10");
                Console.WriteLine("Or the first number is equal to the second");
            }
            else
            {
                Console.WriteLine("The answer is not greater than 10");
                Console.WriteLine("And the first number is not equal to the second");
            }
        }
        static void Conditions()
        {
            Console.WriteLine("Hello World!");
            int a = 5;
            //int b = 6;
            int b = 3;
            if (a + b > 10) {
                Console.WriteLine("a = 5");
                Console.WriteLine("b = 6");
                Console.WriteLine("The answer is greater than 10.");
            }
        }
        static void Main(string[] args)
        {
            Conditions();
            ifAndElse();
        }
    }
}
