import random

class game:



    def __init__(self,name):
        self.name=name
        self.health = 3
        self.score = 0
    def __str__(self):
        return ("{%s %s %s}")%(self.name,self.health,self.score)

    def take_input(self,last_char):
        player_input =input("player have to start "+last_char+" ="  )
        return player_input

    def comapre(self,enetrd_word ,list):
        if enetrd_word in list:
            self.score += 1
        else:
            self.health -= 1

    def get_word(self,last,list):
        if last ==" ":
            bot_word = random.choice(list)
            last = bot_word[-1]
            print(bot_word)

            return last,bot_word
        else:
            while True:
                w= random.choice(list)
                if w[0].lower() == last.lower():
                    print( w)
                    f=w[-1]

                    return f,w









