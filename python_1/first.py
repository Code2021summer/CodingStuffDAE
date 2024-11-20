def addNum(firstNum, secondNum): #adds the two inputs
    sum = firstNum + secondNum
    print("The sum of your numbers is" , sum)
def subtractNum(firstNum, secondNum): #subtracts two inputs
    difference = firstNum - secondNum
    print("The difference of your numbers is" , difference) 
def multiplyNum(firstNum, secondNum):#multiplies two inputs
    product = firstNum * secondNum
    print("The product of your numbers is" , product)
def divideNum(firstNum, secondNum): #divides new inputs
    quotient = firstNum / secondNum
    print("The quotient of your numbers is" , quotient)

def displayMenu(): #displays the menu
    print("1. Additon")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def main(): #main program
    allFeatures = ["Addition", "Subtraction", "Multiplication", "Division"]
    print("I shall give you answers for math")
    print("Here are the features in the application")
    for currentFeature in range(len(allFeatures)):
        print(allFeatures[currentFeature])
    print(allFeatures[2])
    userChoice = int(input("Pick one. Just type the number (or else...): "))
    userFirstNum = int(input("Give me a number: "))
    userSecondNum = int(input("Give me another number: "))
    if userChoice == 1:
        addNum(userFirstNum, userSecondNum)
    if userChoice == 2:
        subtractNum(userFirstNum, userSecondNum)
    if userChoice == 3:
        multiplyNum(userFirstNum, userSecondNum)
    if userChoice == 4:
        divideNum(userFirstNum, userSecondNum)
main() #runs the program