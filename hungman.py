import random


chances = 6


print("Welcome to the Hungman Game")

words_list = [ "Airport",	"Guitar","piano", "Ambulance", "Pillow", "Animals",	"Hamburger",	"Pizza", "Helicopter",	"Planet", "Beach", "Hydrogen", "Rainbow", "Beard", "Raincoat",
"Apple", "Helmet",	"Plastic",  "Honey", "Potato", "Balloon", "Horse", "Queen", "Banana", "Hospital", "Battery", "House", "Rain", "Bed", "Insect",	"Refrigerator"]

#generate random word
chosen_word = random.choice(words_list)
print(chosen_word)

#Generating blanks for each letter of the word
blanks = ""

blanks += "_"*len(chosen_word)
print(blanks)

while chances > 0:
    guess_letter = input("Guess the letter?")

    #Is the guess letter in the word?
    letter_in_word = False
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess_letter:
            letter_in_word = True
            blanks = blanks[:letter] + guess_letter + blanks[letter+1:]
            print(blanks)
    if not letter_in_word:
        print("Lose a life")
        chances -= 1
    if chances == 5:
        print("   O   ")
    elif chances == 4:
        print("   O   ")
        print("   |   ")
    elif chances == 3:
        print("  /O   ")
        print("   |   ")
    elif chances == 2:
        print("  /O\ ")
        print("   |   ")
    elif chances == 1:
        print("  /O\ ")
        print("   |   ")
        print("  /    ")
    else:
        print("  /O\ ")
        print("   |   ")
        print("  / \ ")

        
        

	




	
