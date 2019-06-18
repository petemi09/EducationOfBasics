using System;

namespace NumbersInCSharp2
{
    class Program
    {
        static void Remainders() 
        {
            Console.WriteLine("Remainders");
            int a = 7;
            int b = 4;
            int c = 3;
            int d = (a  + b) / c;
            int e = (a + b) % c;
            Console.WriteLine($"quotient: {d}");
            Console.WriteLine($"remainder: {e}");
            Console.WriteLine("------");
            double aa = 5;
            double ba = 4;
            double ca = 2;
            double da = (aa  + ba) / ca;
            Console.WriteLine(da);
            double ee = 19;
            double f = 23;
            double g = 8;
            double h = (ee + f) / g;
            Console.WriteLine(h);
            Console.WriteLine("this is the new part");
            double num1 = 15;
            double num2 = num1 / 2.4;
            Console.WriteLine($"this is the number {num2}");
        }

        static void maxes() 
        {
            Console.WriteLine("maxes");
            int max = int.MaxValue;
            int min = int.MinValue;
            Console.WriteLine($"The range of integers is {min} to {max}");
            Console.WriteLine("-------");
            int what = max - 3;
            Console.WriteLine($"An example of overflow: {what}");
            Console.WriteLine("-------");
            double max1 = double.MaxValue;
            double min1 = double.MinValue;
            Console.WriteLine($"The range of double is {min1} to {max1}");
            double third = 1.0 / 3.0;
            Console.WriteLine($"third {third}");
        }

        static void FixedPoint()
        {
            Console.WriteLine("This is fixed Point section");
            decimal min = decimal.MinValue;
            decimal max = decimal.MaxValue;
            Console.WriteLine($"The range of the decimal type is {min} to {max}");
            double a = 1.0;
            double b = 3.0;
            Console.WriteLine(a / b);

            decimal c = 1.0M;
            decimal d = 3.0M;
            Console.WriteLine(c / d);
        }

        static void Circles()
        {
            Console.WriteLine("Calculate Cirlces!");
            double pi = Math.PI;
            //given radius by tutorial
            double radius = 2.50;
            Console.WriteLine(pi);
            Console.WriteLine(Math.PI);
            Console.WriteLine($"The calculation of a circle is {(radius * radius) * pi}");
        }
        static void Main(string[] args)
        {
            Remainders();
            maxes();
            FixedPoint();
            Circles();

            
        }
    }
}
