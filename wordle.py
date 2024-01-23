# PYTHON WORDLE
import random
import linecache
# decide on word by choosing a random line number with a word on it
def chooseword():
    lineno = random.randint(1,14855)
    global word
    word = linecache.getline('wordbank.txt', lineno)
    word = str(word)
    print(word)

# check if input is valid
def validation():
    with open('wordbank.txt') as f:
        # checking whether guessed word is in word database
        if userinput in f.read():
            valid = True
            print("Your word is valid")
        else:
            print('Your word is invalid. Try guessing again')
            valid = False
            found = False
        # checking whether you have guessed the correct word
        if valid == True:
            print('is it even getting here')
            if userinput == word:
                print("You've guessed the correct word!")
                found = True

chooseword()
# take in input
found = False
valid = False
while found==False:
    userinput = str(input("What is your word?"))
    validation()
print("You've guesed the correct word! The word was ", word)
# check input in comparison to word


# output how close you were compared to word (graphically)
