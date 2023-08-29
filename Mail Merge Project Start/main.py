#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

for n in range(len(names)):
    names[n] = names[n].strip()

for i in range(len(names)):
    with open("./Input/Letters/starting_letter.txt") as file:
        letter = file.read()
        letter = letter.replace("[name]", f"{names[i]}")
    with open(f"./Output/ReadyToSend/letter_for_{names[i]}.txt", 'w') as mail:
        mail.write(letter)

