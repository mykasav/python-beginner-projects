
import random

class RPS:
    ROCK="r"
    PAPER="p"
    SCISSORS="s"
    listrps=[ROCK, PAPER, SCISSORS]
    def randomize(self):
        listrpsrad=random.choice(self.listrps)
        return listrpsrad
    
    def validateR(self,guess):
        if guess=="r":
            return "Stalemate!"
        elif guess=="p":
            return "You won!!"
        elif guess=="s":
            return "You lost!!"
        
    def validateP(self,guess):
        if guess=="p":
            return "Stalemate!"
        elif guess=="r":
            return "You lost"
        elif guess=="s":
            return "you won"
        
    def validateS(self,guess):
        if guess=="s":
            return "Stalemate!"
        elif guess=="p":
            return "You lost!!"
        elif guess=="r":
            return "You won"
        
    def start(self):
            while True:
                autorized=["r","s","p"]
                guess=str(input("Chose Rock,Paper,Scissors or /leave: (r/p/s.)").lower())
                if guess=="/leave":
                    print("thx for playing")
                    break
                if guess not in autorized:
                    print("Invalid input, try again")
                    continue
                
                a=self.randomize()
                print("o robo escolheu",a)
                if a=="r":
                    print( self.validateR(guess))
                        
                elif a=="p":
                    print( self.validateP(guess))
                    
                elif a=="s":
                    print( self.validateS(guess))
           
                
            
gamerps=RPS()
resultado=gamerps.start()
print(resultado)
