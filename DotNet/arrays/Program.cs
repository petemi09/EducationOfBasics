using System;
using System.Collections.Generic;

namespace list_tutorial
{
    class Program
    {
        static void lists()
        {
            var names = new List<string> { "<name>", "Ana", "Felipe" };
            foreach (var name in names)
            {
                Console.WriteLine($"hello {name.ToLower()}");
                Console.WriteLine($"Hello {name.ToUpper()}!");
            }

            Console.WriteLine($"this is indexing a list {names[1]}");
            
            Console.WriteLine();
            names.Add("Maria");
            names.Add("Bill");
            names.Remove("Ana");
            names.Add("Not Found");
            foreach (var name in names)
            {
                Console.WriteLine($"Hello {name.ToUpper()}!");
            }
            Console.WriteLine($"The list has {names.Count} people in it");



            var index = names.IndexOf("Felipe");
            if (index == -1)
            {
                Console.WriteLine($"When an item is not found, IndexOf returns {index}");
            } else
            {
                Console.WriteLine($"The name '{names[index]}' is at index {index}");
            }

            index = names.IndexOf("Not Found");
            if (index == -1)
            {
                Console.WriteLine($"When an item is not found, IndexOf returns {index}");
            } else
            {
                Console.WriteLine($"The name '{names[index]}' is at index {index}");
            }



            names.Sort();
            foreach (var name in names)
            {
                Console.WriteLine($"Hello {name.ToUpper()}!");
            }

        }

        static void Fib()
        {
            var fibonacciNumbers = new List<int> {1, 1};
            for(int x = 0; x < 20; x++)
            {
                var previous = fibonacciNumbers[fibonacciNumbers.Count - 1];
                var previous2 = fibonacciNumbers[fibonacciNumbers.Count - 2];

                fibonacciNumbers.Add(previous + previous2);
                Console.WriteLine(fibonacciNumbers[x]);
            }
        }
        
        static void Main(string[] args)
        {
            lists();
            Console.WriteLine();
            Fib();
        }
    }
}