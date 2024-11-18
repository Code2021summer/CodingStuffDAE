def presentSituation(scenario, optionOne, optionTwo, optionThree): #creates a reusable format for presenting each scenario
    print(scenario)
    firstChoice = "1. " + optionOne
    secondChoice = "2. " + optionTwo
    thirdChoice = "3. " + optionThree
    options = [firstChoice, secondChoice, thirdChoice]
    for currentOption in options:
        print(currentOption)
    global userChoice
    userChoice = int(input("What do you do? "))
    if userChoice == 1:
        print("You chose to " + optionOne)
    if userChoice == 2:
        print("You chose to " + optionTwo)
    if userChoice == 3:
        print("You chose to " + optionThree)
        
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
def chooseSituation():
    global food
    defineSituation(1)
    if userChoice == 2:
        defineSituation(3)

    if (userChoice == 1) or (userChoice == 3):
        defineSituation(2)
        food = 0
def main():
    print(" ")
    print("Welcome!")
    print("Instructions: Type the number to choose your response")
    chooseSituation()
userChoice = 0
food = 4
hunger = 0
situationNumber = 1
main()