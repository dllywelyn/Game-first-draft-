import random 

passwords = ["password", "rosebud", "inconceivable", "please", "bird", "opensesame", "prettyplease"]
excuses = ["I'm sorry I don't speak Welsh", "Oh I know the password, but I think I just heard my mum \
shouting tea is ready!", "Forgive me, but I've just right this second grown a moral compass and cannot \
enter.", "What did you just call me? You've just lost a customer, good day sir!", "Wait, wait, is this \
not a church? I think I'm in the wrong place."]

# Double the alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + cipherKey
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    # put encrypted message here, take from list
    secretword = random.choice(passwords)
    shiftAmount = random.randint(-5,-1)
    if shiftAmount == -1:
        print(f"You hear a single loud knock on the door.")
    else:
        print(f"You hear {shiftAmount*-1} loud knocks on the door.")
    #print(secretword)
    myEncryptedMessage = encryptMessage(secretword, shiftAmount, myAlphabet2)
    print(f"After a pause, the voice on the other side bellows, \n '\033[33m{myEncryptedMessage}\033[0m'")
    while True:
        choice = input("What would you like to do? Guess the secret word [1] \
or make a polite excuse and leave [2]?\n")
        if choice == "1":
            guess = input("What's the secret word?\n")
            if guess == secretword:
                print("Correct!")
                break
            else:
                print("\033[31mWrong! Guess again...\033[0m")
        if choice =="2":
            print("\033[31m",(random.choice(excuses)),"\033[0m")
            break

runCaesarCipherProgram()