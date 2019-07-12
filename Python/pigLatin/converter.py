# Created by: Mitchell Petellin
# this is a program to convert a sentence into a pig latin sentence
# created: 7/5/2019
from gtts import gTTS 
import os 

def convert(x):
    list1 = x.split(" ")
    new_sentence = ""
    for word in list1:
        firstLetter = word[0]
        x = word[1:]
        pigLatin = "ay"
        newWord = x + firstLetter + pigLatin
        new_sentence += (newWord.lower()) + " "
    return new_sentence

def user():
    userInput = input(str("enter a sentence: "))
    return userInput

def main():
     
    x = user()
    y = convert(x)
    print(y)
    language = 'en'
    myobj = gTTS(text=y, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3") 
main()