#Created bby: Mitchell Petellin
#Goal: To randomly select a language to code in for projects
import random

def pick():
    languages = ['Python','Java','C++','JS','DotNet','HTML','Swift']
    select = random.choice(languages)
    print(select)

def main():
    pick()

#main()
if __name__ == "__main__":
    main()