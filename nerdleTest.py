import random, pygame, sys
from pygame.locals import *
pygame.init()
import random

white = (255,255,255)
yellow = (255,255,102)
grey = (211, 211, 211)
black = (0,0,0)
green=(0,255,0)
lightGreen=(153,255,204)
red = (255, 0, 0)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!",       True, lightGreen)
youLose = bigFont.render("You Lose!",     True, lightGreen)
playAgain = bigFont.render("Play Again?", True, lightGreen)
incorrectAnswer = bigFont.render("Sum is incorrect, Press ENTER", True, red)

def sumGenerator():

    sumList = ["","","",""]
    additionfile = open("addition.txt","r")
    lines = additionfile.readlines()
    sumList[0] = lines[random.randint(0,len(lines))][:-1]
    additionfile.close()

    dividefile = open("divide.txt","r")
    lines = dividefile.readlines()
    sumList[1] = lines[random.randint(0, len(lines))][:-1]
    dividefile.close()

    subtractfile = open("subtract.txt","r")
    lines = subtractfile.readlines()
    sumList[2] = lines[random.randint(0, len(lines))][:-1]
    subtractfile.close()

    multiplyfile = open("multiply.txt","r")
    lines = multiplyfile.readlines()
    sumList[3] = lines[random.randint(0, len(lines))][:-1]
    multiplyfile.close()

    chosenSum = sumList[random.randint(0,3)]
    return chosenSum

    
def checkGuess(turns, nerdleSum, userGuess, window):
    renderList = ["","","","","","","",""]
    spacing = 0
    guessColourCode = [grey,grey,grey,grey,grey,grey,grey,grey]
    count = 0
    for x in range(0,8):
        if userGuess[x] in nerdleSum:
            guessColourCode[x] = yellow

        if userGuess[x] == nerdleSum[x]:
            guessColourCode[x] = green

    list(userGuess)

    for x in range(0,8):
        renderList[x] = font.render(userGuess[x], True, black)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(60 +spacing, 50+(turns*80), 50, 50))
        window.blit(renderList[x],(70 + spacing, 50 + (turns*80)))
        spacing+=80

    if guessColourCode == [green,green,green,green,green,green,green,green]:
        return True

def main():
    nerdleSum = sumGenerator()
    mySum = nerdleSum.split("=")

    gameSum = mySum[0]
    answer = mySum[1]

    print(answer)
    print(nerdleSum)

    height = 600
    width = 800

    FPS = 30

    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    for x in range (0,8):
        for y in range (0,6):
            pygame.draw.rect(window, grey, pygame.Rect(60+(x*80), 50+(y*80), 50, 50),2)

    pygame.display.set_caption("NERDLE!")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess+=event.unicode.upper()

                if event.key == K_RETURN and win == True:
                    main()

                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 8:
                    guess = guess[:-1]

                if event.key == K_RETURN and len(guess) > 7:
                    userGuess = guess.split("=")
                    if eval(userGuess[0]) == int(userGuess[1]):
                        win = checkGuess(turns, nerdleSum, guess, window)
                        turns+=1
                        guess = ""
                        window.fill(black,(0,500,800,200))

        window.fill(black,(0,500,800,200))
        renderGuess = font.render(guess,True,grey)
        window.blit(renderGuess,(180,530))

        if win == True:
            window.blit(youWin,(90,200))
            window.blit(playAgain,(60,300))

        if turns == 6 and win != True:
            window.blit(youLose,(90,200))
            window.blit(playAgain,(60,300))
        pygame.display.update()
        clock.tick(FPS)

main()

        








                    
                    












                












    
            




    
        
                    








        








        





   
