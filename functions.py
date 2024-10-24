import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the log base 2 of a particular number
def log2(num):
    return math.log2(num)

## takes in an age from the user via parameters
## responds based on a couple of criteria
def ageResponse(age):
    if(age < 18):
        print("You're a minor!")

    elif(age >= 18 or age < 21):
        print("You're kind of in a weird legal gray area of ages.")

    else:
        print("You're 21 or older!")
        print("You can now drink alcohol AND get married without parental consent in MS. Congrats.")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])

## takes in two parameters: start and end
## totals the numbers together so if 1 and 3 are start and end should be:
## 1 + 2 + 3 = 6 to return
def total(start, end):
    total = 0

    for i in range(start, end):
        total += i

    return total


## calls to the functions if you want to run them to test things out can be placed below here
## please make sure they're not actually in the code (uncommented out) when running pytest --
## it can break things
