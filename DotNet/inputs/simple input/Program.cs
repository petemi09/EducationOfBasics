using System;

namespace LearningBasics
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string userInput;
            Console.Write("Enter something: ");
            userInput = Console.ReadLine();
            Console.WriteLine($"You said '{userInput}'");
        }
    }
}
