#IGNORE THIS PROJECT
def presentSituation(scenario, optionOne, optionTwo, optionThree): #creates a reusable format for presenting each scenario
    print(scenario)
    firstChoice = "1. " + optionOne
    secondChoice = "2. " + optionTwo
    thirdChoice = "3. " + optionThree
    options = [firstChoice, secondChoice, thirdChoice]
    for currentOption in options:
        print(currentOption)
    global userChoice
    userChoice = int(input("What do you do? ")) #asks the reader for input
    print(" ") #adds a space between options in order 
    if userChoice == 1: #tells the user what happened
        print("You chose to " + optionOne)
    if userChoice == 2:
        print("You chose to " + optionTwo)
    if userChoice == 3:
        print("You chose to " + optionThree)
#def deadEndSituation(scenario) #defines what happens when a game ending scenario is chosen
    #print(scenario)
    #print("GAME OVER")
    #doesGameContinue = input("Do you want to try again? (yes/no)")
    #if doesGameContinue == "yes":
    #    defineSituation(1)
    #if doesGameContinue == "no":
     #   print("What are you still doing here then?")
        
def defineSituation(situationNumber): #defines the circumstances and options for every scenario so they can be easily retrived by the code
    if situationNumber == 1: #initial situation
        presentSituation("You wake up. Your vision is hazy. So are your memories. You're lying on cold stone, with a bag of food by your side.", "go back to sleep", "get up", "sleep")
    if situationNumber == 2: #sleeping more
        presentSituation("While you were sleeping, a pack of hummingbirds stole your food. You are well rested, but very hungry.", "sleep even more", "explore the area", "yell for help")
    if situationNumber == 3: #get up at the start
        presentSituation("You rub the last of sleep from your eyes as you sit up. There is a pack of food containing 4 jars of pickles, 1 potato, and a stick of butter. The butter has completely melted, and the potato is rotten.", "eat all of it at once", "eat half a pickle for breakfast", "wait until you find something better")
    if situationNumber == 4: #choose a tunnel
        presentSituation("You look around at your surroundings. You are in a cave with a few branching tunnels. You hear a bleat from one tunnel, but there is a glow from the other.", "go down the tunnel where you heard the bleat", "go down the glowing tunnel", "scream for help")
    if situationNumber == 5: #hamster start
        presentSituation("An army of hamsters rushes in an attacks you", "offer them food", "fight them", "offer to braid their hair")
    if situationNumber == 6: #glowing tunnel
        presentSituation("As you walk, the glow becomes brighter and brighter. At the very end of the tunnel, you find a computer with a screen that just says, Do You Want To Play?", "say yes", "dance on the keyboard", "scream for help")
    if situationNumber == 7: #bleat tunnel
        presentSituation("You walk for what seems like miles. You suddenly arrive at a cliff. You turn back, but lose your footing and fall. Thankfully, a sheep is there, and it saves your life. However, it drops you off in a new cave, at the bottom of the cliff. You are grateful, but annoyed", "offer the sheep half a pickle", "use the sheep as a trampoline to get out", "ask it for help")
    if situationNumber == 8: #braid hair
        presentSituation("You did such a good job braiding the hamsters hair, that you are now their leader, however, the old leader is mad at you for this. They are obscured in darkness, but they are watching you", "offer them the crown back", "command your new legion of hamsters to help you run away", "pretend they don't exist")
def terminateGame(scenario):
    print(scenario)
    print("GAME OVER")

def chooseSituation(): #this takes into account what the user chose as their answer, and then it loads the next situation based on their answer
    global food
    global hunger
    defineSituation(1) #intial situation
    if userChoice == 2:
        defineSituation(3) #getting up first
        if userChoice == 1:
            terminateGame("You ate so much that you exploded.")
        if userChoice == 2:
            hunger = 2
            food = 2
        if (userChoice == 3) or (userChoice == 2):
            defineSituation(4)
    if (userChoice == 1) or (userChoice == 3):
        defineSituation(2) #sleep
        food = 0
        if userChoice == 1:
            terminateGame("You slept for too long, and fell asleep forever.")
def main():
    print(" ")
    print("Welcome!")
    print("Instructions: Type the number to choose your response")
    chooseSituation()
userChoice = 0 #a few variables that are important for the game
food = 4
hunger = 0
situationNumber = 1
main()