from random import randint

linesOfWords = 267751
phase1, phase2, phase3, phase4, phase5, phase6, phase7 = open("hangManPhases/phase1.txt"), open("hangManPhases/phase2.txt"), open("hangManPhases/phase3.txt"), open("hangManPhases/phase4.txt"), open("hangManPhases/phase5.txt"), open("hangManPhases/phase6.txt"), open("hangManPhases/phase7.txt")
hangManPhases = [phase1.read(), phase2.read(), phase3.read(), phase4.read(), phase5.read(), phase6.read(), phase7.read()]

phase1.close()
phase2.close()
phase3.close()
phase4.close()
phase5.close()
phase6.close()
phase7.close()

def playHangMan():
    ###SETUP###
    dictionary = open("sowpods.txt")
    randomLineNum = randint(1, linesOfWords)
    randomWord = ""
    message = "Error"

    ###FIND WORD###
    index = 1
    for line in dictionary:
        if randomLineNum == index:
            randomWord = line
            break

        index += 1

    dictionary.close()

    ###FAKE WORD###
    solvedWord = "-" * (len(randomWord) - 1)
    mistakes = 0

    ###GAMEPLAY###
    while solvedWord != randomWord:
        ###USER INPUT###
        unlockedLetter = False
        letter = (input("What letter do you think is in the mystery word? "))[0]

        ###FIND LETTERS AND PUT THEM IN###
        for x in range(len(solvedWord)):
            if randomWord[x] == letter:
                solvedWord = list(solvedWord)
                solvedWord[x] = letter
                solvedWord = "".join(solvedWord)
                unlockedLetter = True

        ###ADD MISTAKES###
        if unlockedLetter == False:
            mistakes += 1

        ###OUTPUT###
        print(f"This is your progress on your word: {solvedWord}")
        hangmanPhase = hangManPhases[mistakes]
        print(f"This is your hangman. You made {mistakes} mistakes")
        print(hangmanPhase)

        ###END GAME ACCORDINGLY###
        if mistakes == 6:
            message = "Lost"
            break
        if "-" not in solvedWord:
            message = "Victory"
            break

    ###TELL PLAYER GAME RESULT###
    print(message)

    ###PLAY AGAIN###
    answer = input("Would you like to play again? [y/n] ")

    if answer == "y":
        playHangMan()

playHangMan()


