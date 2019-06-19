using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace TeleprompterConsole
{
    class Program
    {
        static void Main(string[] args)
        {
			
            // Console.WriteLine("Hello World!");
            // var lines = ReadFrom("sampleQuotes.txt");
			// foreach (var line in lines)
			// {
			// Console.Write(line);
			// if (!string.IsNullOrWhiteSpace(line))
			// {
			// 	var pause = Task.Delay(200);
			// 	// Synchronously waiting on a task is an
			// 	// anti-pattern. This will get fixed in later
			// 	// steps.
			// 	pause.Wait();
			// }
			// }
			ShowTeleprompter().Wait();
	}
	
	static IEnumerable<string> ReadFrom(string file)
	{
		var lineLength = 0;
		string line;
		using (var reader = File.OpenText(file))
		{
			while ((line = reader.ReadLine()) != null)
			{
				//yield return line;
				var words = line.Split(' ');
				foreach (var word in words)
				{
					yield return word + " ";
					lineLength += word.Length + 1;
					if (lineLength > 70)
					{
						yield return Environment.NewLine;
						lineLength = 0;
					}
				}
				yield return Environment.NewLine;
			}
		}
	}

		private static async Task ShowTeleprompter()
		{
			var words = ReadFrom("sampleQuotes.txt");
			foreach (var word in words)
			{
				Console.Write(word);
				if (!string.IsNullOrWhiteSpace(word))
				{
					await Task.Delay(200);
				}
			}
		}

		private static async Task GetInput()
		{
			var delay = 200;
			Action work = () =>
			{
				do {
					var key = Console.ReadKey(true);
					if (key.KeyChar == '>')
					{
						delay -= 10;
					}
					else if (key.KeyChar == '<')
					{
						delay += 10;
					}
					else if (key.KeyChar == 'X' || key.KeyChar == 'x')
					{
						break;
					}
				} while (true);
			};
			await Task.Run(work);
		}
	}
}

namespace TeleprompterConsole
{
    internal class TelePrompterConfig
    {
        public int DelayInMilliseconds { get; private set; } = 200;

        // public void UpdateDelay(int increment) // negative to speed up
        // {
        //     var newDelay = Min(DelayInMilliseconds + increment, 1000);
        //     newDelay = Max(newDelay, 20);
        //     DelayInMilliseconds = newDelay;
        // }

        public bool Done { get; private set; }

        public void SetDone()
        {
            Done = true;
        }
    }
}
