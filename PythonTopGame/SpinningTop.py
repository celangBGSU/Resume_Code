#   Dev: Corey Lang
#   Purpose: A simple game to show classes and inheritance. The spin speed and weight of each top is random within a range different for each top.
#            The user can pick each top they want, then the program will allocate the new top and ask the use the participate in a tournament like game to beat the other three tops
#   

import random
import time
import keyboard

# The parent class, Spinning_Top, has a Hit Point and material attribute that all tops will inherit
class Spinning_Top:
    def __init__(self, HP, material):
        self.HP = 100
        self.material = material

# The child class, Metal, has a high weight and a low spin speed        
class Metal(Spinning_Top):
    def __init__(self, HP):
        super().__init__(HP, 'Metal')
        self.weight = random.randint(7, 10)
        self.speed = random.randint(1, 3)
        self.AP = (self.weight * self.speed)  

# The child class, Wood, has a mid weight and a mid spin speed comparitivly 
class Wood(Spinning_Top):
    def __init__(self, HP):
        super().__init__(HP, 'Wood')
        self.weight = random.randint(4, 6)
        self.speed = random.randint(4, 7)
        self.AP = (self.weight * self.speed)  

# The child class, Plastic, has the lowest weight and the highest spin speed
class Plastic(Spinning_Top):
    def __init__(self, HP):
        super().__init__(HP, 'Plastic') 
        self.weight = random.randint(1, 3)
        self.speed = random.randint(8, 10)
        self.AP = (self.weight * self.speed)          

# The child class, SuperOP, has the highest weight and the highest spin speed
class SuperOP(Spinning_Top):
    def __init__(self, HP):
        super().__init__(HP, 'Carbon Fiber') 
        self.weight = random.randint(8, 10)
        self.speed = random.randint(8, 10)
        self.AP = (self.weight * self.speed)

# This function allows the tops to "fight" and upate their new HP every round
def attack_phase(Top1, Top2):
    Top1.HP = Top1.HP - Top2.AP
    Top2.HP = Top2.HP - Top1.AP
    

def pause():
    while True:
        if keyboard.read_key() == 'space':
            # If you put 'space' key
            # the program will resume.
            break

# initiation of the default tops the user will be against 
Metal_Top = Metal(Spinning_Top)
Wood_Top = Wood(Spinning_Top)
Plastic_Top = Plastic(Spinning_Top)

print("---------------------------------------------------------------------")
print("-             S P I N N I N G - T O P          G A M E              -")
print("-                                                                   -")
print("---------------------------------------------------------------------")


#Loop to get a top choice from the user so their top can be created
while True:
  try:
    Choice = input("Which TOP would you like to use?\n (a) Metal Top\n (b) Wood Top\n (c) Plastic Top\n (d) Super OP TOP\n\n") 
    if Choice == 'a':
        PlayerTop = Metal(Spinning_Top)  
        print("Your Top is METAL")
        break;
    if Choice == 'b':
        PlayerTop = Wood(Spinning_Top)  
        print("Your Top is WOOD")
        break;
    if Choice == 'c':
        PlayerTop = Plastic(Spinning_Top)  
        print("Your Top is PLASTIC")
        break;   
    if Choice == 'd':
        PlayerTop = SuperOP(Spinning_Top)  
        print("Your Top is CARBON FIBER")
        break;    
    else:
      print("Please choice the options present")      
  except ValueError:
    print("Invalid")
    continue

# display the dict of all the tops in the tournament
print("-----------------------------------------------------------------------------")
print("-             WELCOME YOUR CONTESTENTS!!")
print(f"- PLAYER ->  {PlayerTop.__dict__}  ")
print(f"- CHAMPION ->  {Metal_Top.__dict__}")
print(f"- PRO ->  {Wood_Top.__dict__}      ")
print(f"- ROOKIE ->  {Plastic_Top.__dict__}")
print("-----------------------------------------------------------------------------")

time.sleep(2)
# initiate the int round so the while loop can increment the rounds automaticly
round = 1

# while both tops had health and the round is no more than three the match would continue.
while PlayerTop.HP > 0 and Plastic_Top.HP > 0 and round <=3:
    print("---------------------------------------------------------------------")
    print(f"-                             ROUND {round}!!                        ")
    print(f"-              PLAYER ->  {PlayerTop.HP} HIT POINTS                  ")
    print(f"-                        V                                           ")
    print(f"-                         S                                          ")
    print(f"-              ROOKIE ->  {Plastic_Top.HP} HIT POINTS                ")
    print("---------------------------------------------------------------------")

    print('Hit your space bar to attack!')
    pause()
    attack_phase(PlayerTop, Plastic_Top)
    
    # quick display of what happened in the round
    print(f'You did {PlayerTop.AP} damage to the opposite top!')
    print(f'The opposite top did {Plastic_Top.AP} damage to you!')
    print(f"ROUND {round} OVER!")
    time.sleep(1)
    round += 1

# once the while loop had broke, the programs reads the HP of the tops and declares a winner    
else:
    # if the user has less health at the end of the bracket, then the user loses and terminates the program
    if PlayerTop.HP < Plastic_Top.HP:

        print(f'The HP of your top is now {PlayerTop.HP} and the HP of your opponent is {Plastic_Top.HP} at the end of round {round-1}. Sorry you lost')
        time.sleep(2)
        quit()

    # if the user won the bracket then the program continues to the next match
    else:
        print(f"Congragulations, AT THE END OF ROUND {round} YOU WON! YOU ARE PROCEDDING TO THE NEXT LEVEL")
        time.sleep(2)

# the user's top get restored with 100 HP before the beginning of each bracket
PlayerTop.HP = 100    
print(f'The HP of your top is now at full health! {PlayerTop.HP}HP ')
print('Hit your space bar to move on to the next battle!')
pause()

# Each bracket is similar to the first braket in terms of code comprehension...
round = 1

while PlayerTop.HP > 0 and Wood_Top.HP > 0 and round <=3:
    print("---------------------------------------------------------------------")
    print(f"-                             ROUND {round}!!                        -")
    print(f"-              PLAYER ->  {PlayerTop.HP} HIT POINTS                  -")
    print(f"-                        V                                           -")
    print(f"-                         S                                          -")
    print(f"-              PRO ->  {Wood_Top.HP} HIT POINTS                      -")
    print("---------------------------------------------------------------------")

    print('Hit your space bar to attack!')
    pause()
    attack_phase(PlayerTop, Wood_Top)
    print(f'You did {PlayerTop.AP} damage to the opposite top!')
    print(f'The opposite top did {Wood_Top.AP} damage to you!')
    print(f"ROUND {round} OVER!")
    time.sleep(1)
    round += 1
    
else:
    if PlayerTop.HP < Wood_Top.HP:
        print(f'The HP of your top is now {PlayerTop.HP} and the HP of your opponent is {Wood_Top.HP} at the end of round {round-1}.. Sorry you lost')
        time.sleep(2)
        quit()

    else:
        print("Congragulations, YOU WON! YOU ARE PROCEDDING TO THE NEXT LEVEL")
        time.sleep(2)
        
PlayerTop.HP = 100    
print(f'The HP of your top is now at full health! {PlayerTop.HP}HP ')
print('Hit your space bar to move on to the next battle!')
pause()

round = 1

while PlayerTop.HP > 0 and Metal_Top.HP > 0 and round <=3:
    print("---------------------------------------------------------------------")
    print(f"-                             ROUND {round}!!                        -")
    print(f"-              PLAYER ->  {PlayerTop.HP} HIT POINTS                  -")
    print(f"-                        V                                           -")
    print(f"-                         S                                          -")
    print(f"-              CHAMPION ->  {Metal_Top.HP} HIT POINTS                -")
    print("---------------------------------------------------------------------")

    print('Hit your space bar to attack!')
    pause()
    attack_phase(PlayerTop, Metal_Top)
    print(f'You did {PlayerTop.AP} damage to the opposite top!')
    print(f'The opposite top did {Metal_Top.AP} damage to you!')
    print(f"ROUND {round} OVER!")
    time.sleep(1)
    round += 1
    
else:
    if PlayerTop.HP < Metal_Top.HP:
        print(f'The HP of your top is now {PlayerTop.HP} and the HP of your opponent is {Metal_Top.HP} at the end of round {round-1}.. Sorry you lost')
        time.sleep(2)
        quit()

    else:
        print("Congragulations, YOU WON! YOU ARE THE NEW CHAMPION!!!!")
        time.sleep(2)
        
PlayerTop.HP = 100    

print('Hit your space bar to countinue!')
pause()


# when the user has defeated all the other tops they are welcomed with congratuations and title of new champIon
print(f'GOOD JOB! YOU BEAT MY GAME. THANKS FOR PLAYING')
print(f'OUR NEW CHAMPION! {PlayerTop.__dict__}') 