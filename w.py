from PyDictionary import PyDictionary
import requests
from bs4 import  BeautifulSoup
from game import game

dicc =PyDictionary()


valid_words = []
with open("A.txt")as word_file:
    valid_words = list(word_file.read().split())

Bot =game("bot")
human =game("human")
last_char=" "

while True:
    last_char,word = Bot.get_word(last_char,valid_words )
    print(dicc.meaning(word))
    valid_words.remove(word)
    word_a=human.take_input(last_char).upper()

    human.comapre(word_a,valid_words)
    print(dicc.meaning(word_a))
    print(human)
    last_char=word_a[-1]
    if word_a in valid_words: 
        valid_words.remove(word_a)
    if human.health ==0:
        print("you are dum ! :D  , try again ")
        break
