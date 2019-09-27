using System;
using static System.Console;

namespace RockPaperScissors
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            WriteLine("Welcome to Rock, Paper, Scissors Game!");
            WriteLine();

            int playerScore = 0;
            int computerScore = 0;
            int numberOfGames = 0;

            bool playing = false;
            while (playing != true) {
                Random randInt = new Random();
                String[] plays = { "Rock", "Paper", "Scissors" };
                int playsIndexNum = randInt.Next(plays.Length);
                Write("Pick item: ");
                String item = ReadLine();
                item = item.ToUpper();
                String vsItem = plays[playsIndexNum];
                vsItem = vsItem.ToUpper();
                WriteLine("{0} vs {1}",item, vsItem);
                if (item == vsItem)
                {
                    WriteLine("It's a tie!!!");
                }

                //points go to computer
                else if (vsItem == "ROCK" && item == "SCISSORS")
                {
                    WriteLine("Rock Won, 1pt Computer");
                    computerScore += 1;
                }
                else if (vsItem == "SCISSORS" && item == "PAPER")
                {
                    WriteLine("Scissors won, 1pt Computer");
                    computerScore += 1;
                }
                else if (vsItem == "PAPER" && item == "ROCK")
                {
                    WriteLine("Paper Won, 1pt Computer");
                    computerScore += 1;
                }

                //points go to player
                else if (vsItem == "SCISSORS" && item == "ROCK")
                {
                    WriteLine("Rock Won, 1pt Player");
                    playerScore += 1;
                }
                else if (vsItem == "PAPER" && item == "SCISSORS")
                {
                    WriteLine("Scissors won, 1pt Player");
                    playerScore += 1;
                }
                else if (vsItem == "ROCK" && item == "PAPER")
                {
                    WriteLine("Paper Won, 1pt Player");
                    playerScore += 1;
                }
                else if (item != vsItem)
                {
                    WriteLine("Not an item or mispelled");
                    WriteLine("Game won't be counted");
                    numberOfGames -= 1;
                }

                Write("Do you want to play again? (y/n): ");

                numberOfGames += 1;
                Double gameNum = (double)playerScore / numberOfGames;
                String done = ReadLine();
                if (done == "n")
                {
                    playing = true;
                    WriteLine("Score is {0} player, to {1} computer!", playerScore, computerScore);
                    WriteLine("Number of games played: {0}", numberOfGames);
                    WriteLine("Percentage of games won is {0}", (Math.Round(gameNum,2)));
                    WriteLine("Thanks For playing!");
                }
            }
        }
    }
}
