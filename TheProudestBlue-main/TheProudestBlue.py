#The Proudest Blue
#Author: Wilson Li


import art
import time
import termcolor
import playsound
from pygame import mixer
import random

def typeEffect(word):
    for i in word:
        print(i,end="")
        time.sleep(0.066)
    print()
#If i want to have the word effect for a piece of text, write typeEffect, and dont write print


def fastTypeEffect(word):
    for i in word:
        print(i,end="")
        time.sleep(0.0012)
    print()

def mediumTypeEffect(word):
    for i in word:
        print(i,end="")
        time.sleep(0.008)

validInput = False
while validInput == False:
    start = (input("Hey there! Do you want to start the game? (type yes if you want to start)\n"))
    if "y" in start:
        validInput = True

mixer.init()
mixer.music.load("piano.mp3")

mixer.music.play()


word1=art.text2art("_____WELCOME   TO_____")
word2=art.text2art("__THE  PROUDEST  BLUE___")


printString = termcolor.colored(word1, 'white','on_blue')
fastTypeEffect (printString)
printString = termcolor.colored(word2, 'white','on_blue')
fastTypeEffect (printString)
time.sleep(1)

smiley = chr (int('1f600',16))

wakeCounter=0
pointCounter=0
def printpoints(point):
    scoreString ="-----------------------------------------------------------------"
    scoreString2="Great Job!!! You currently have %s points out of 100" %(pointCounter) + smiley 
    scoreString3="-----------------------------------------------------------------"
    printString = termcolor.colored(scoreString, 'cyan')
    printString2 = termcolor.colored(scoreString2, 'green')
    printString3 = termcolor.colored(scoreString3, 'cyan')
    time.sleep(1)
    print (printString)
    print (printString2)
    print (printString3)

nameString = "---------------------------------------------------  _                  _ _               _ _ --------------------------------------------------- "
nameString2 ="--------------------------------------------------- | |__ _  _  __ __ _(_| |______ _ _   | (_)--------------------------------------------------- "
nameString3 ="--------------------------------------------------- | '_ | || | \ V  V | | (_-/ _ | ' \  | | |--------------------------------------------------- "
nameString4 ="--------------------------------------------------- |_.__/\_, |  \_/\_/|_|_/__\___|_||_| |_|_|--------------------------------------------------- "
nameString5 ="---------------------------------------------------        |__/                               --------------------------------------------------- "

printNameString = termcolor.colored(nameString, 'magenta','on_white')
fastTypeEffect (printNameString)
printNameString = termcolor.colored(nameString2, 'magenta','on_white')
fastTypeEffect (printNameString)
printNameString = termcolor.colored(nameString3, 'magenta','on_white')
fastTypeEffect (printNameString)
printNameString = termcolor.colored(nameString4, 'magenta','on_white')
fastTypeEffect (printNameString)
printNameString = termcolor.colored(nameString5, 'magenta','on_white')
fastTypeEffect (printNameString)
print ()

validInput = False
while validInput == False:
    intro = (input("Would you like instructions to The Proudest Blue? Type yes if you do. "))
    if "y" in intro:
        typeEffect ("This is a text-based story game inspired by the book The Proudest Blue! In the game, try your best to make the most postive choices that results in good outcomes to earn lots of points!\nPlease follow the type instructions so your input can be valid!\nI hope you have a great time :)\n-Wilson")
        validInput = True
    if "n" in intro:
        validInput = True

time.sleep(1)
Name=(input("Before we get into the game, what is your name?\n"))
print()
print ("Hey", Name, "!")
print ("Welcome to The Proudest Blue!")
print()
time.sleep(2)
word4=art.text2art("_______First Day_______")
printString = termcolor.colored(word4, 'white','on_cyan')
fastTypeEffect (printString)
print()
time.sleep(1)
typeEffect("... ...")
time.sleep(0.5)

typeEffect ("You are sleeping on a comfortable bed. You looked at the clock and it is 8:00.")
time.sleep(1)
typeEffect ("Your mom comes to your room and says, honeyyy! School is at 8:30! It is time to wake up!")
print()

zero = 0
def zeroroints(point):

    zeroScoreString= "-----------------------------------------------------------------"
    zeroScoreString2="You received zero points"
    zeroScoreString3="-----------------------------------------------------------------"
    zeroScoreString = termcolor.colored(zeroScoreString, 'cyan')
    zeroScoreString2 = termcolor.colored(zeroScoreString2, 'red')
    zeroScoreString3 = termcolor.colored(zeroScoreString3, 'cyan')
    time.sleep(1)
    print(zeroScoreString)
    print(zeroScoreString2)
    print(zeroScoreString3)

#use %s if variable is in the print statement, use %() to say what the variable is
validInput = False
while validInput == False:
    Wakeup=(input("Do you want to wake up now? (type yes or no)\n"))
    if "yes" in Wakeup:
        time.sleep(1)
        typeEffect("You woke up and dressed up! Ready to rock and roll.")
        validInput = True
        pointCounter += 10
        printpoints(pointCounter)
        time.sleep(1)
    elif wakeCounter == 2:
        time.sleep(1)
        typeEffect("You slept too late. It is 8:20 already and you finally woke up for school. Please stay on your schedule next time! ")
        validInput = True
    elif "no" in Wakeup:
        time.sleep(1)
        typeEffect("You continued to sleep for a while.")
        typeEffect ("Your mom comes back to your room and says, it is getting late honey! Time to wake up and go to school! ")
        wakeCounter += 1
    else:
        typeEffect("Your input is invalid! Please try putting yes or no!")

#Note: in this piece of code, I created a while loop for the player to wake up. Your mom tells you to wake up to school, and you can only input yes or no. If the player types yes, they can progress through the game. But if they type no, the player goes back to the start of the loop and has to choose again. There is also a simple point counter in this program. Only if the player wakes up on time, the player would have 5 points. 
#
# There is also a small bonus!! I added a counter to count the number of "no"s the player entered. If the player entered 3 "no"s, the player would have to get up or it is too late for school. This is an effective use of if and elif statements for the choices of players.

typeEffect ("You saw your sister Asiya smiling at you, she said,")
time.sleep(1)
typeEffect ("Good morning, %s! As she put a beautiful blue, silky piece of fabric on her head." %(Name))
time.sleep(1)

typeEffect ("You do not know what it is. And you want to ask her.")
time.sleep(1)
print()
validInput = False
while validInput == False:
    askhijab=(input("You should ask your sister what it is! (Type a question like what are you wearing on your head?)\n"))
    if "w" or "h" in askhijab:
        print()
        typeEffect ("Asiya explained that the silky piece of fabric on her head is called a hijab!")
        time.sleep(1)
        typeEffect("She said it represents a unique aspect of our culture. It is what makes her herself! ")
        pointCounter +=10
        time.sleep (1)
        validInput = True
    else:  
        typeEffect("(Try typing a question!) ")
        time.sleep(3)

typeEffect ("Asiya asked if you want to try it on as well!")
time.sleep(1)
print ()

validInput = False
while validInput == False:
    hijab=(input("Do you want to try it on?(Type yes or no)\n"))
    if "yes" in hijab:
        typeEffect ('"Yes, the hijab is beautiful, I want to wear it today! You said with great excitement."')
        time.sleep(1)
        validInput = True

    elif "no" in hijab:  
        typeEffect ("After considering it, you answered no. You do not want to be judged by other people, and politely declined her request.")
        time.sleep(2)
        typeEffect ("You and your sister are now walking to school!")
        time.sleep(1)
        typeEffect ("On the way to school, you looked at Asiya under the sunshine.")
        time.sleep(1)
        typeEffect ("Even though you did not wear the hijab, you still felt a strong connection with your sister's hijab, the blueness of it speaks to you.")
        time.sleep(1)
        validInput = True
    else:
        print ("Try typing yes or no!")
mixer.music.stop()
mixer.init()
mixer.music.load("piano.mp3")
1
mixer.music.play()

if "yes" in hijab:
    validInput = False
    while validInput == False:
        hijabcolor=(input("Do you want your hijab to be pink, yellow, or blue?\n"))
        if "p" in hijabcolor:
            typeEffect ("You chose the pink hijab! Asiya helped you put it on. You really liked how it looked.")
            validInput = True
        elif "y" in hijabcolor:
            typeEffect ("You chose the yellow hijab! Asiya helped you to put it on. You really liked how it looked.")
            validInput = True
        elif "b" in hijabcolor:
            typeEffect ("You chose the blue hijab! Asiya said she knew you would pick the blue one! And helped you to put it on. You really liked how it looked.")
            pointCounter += 5
            #This is 5 bonus points, from choosing the blue hijab at the first, and the player's final score would become 105 if they get everything else right. If the player choose other colors, its still gonna be 100.
            time.sleep(1)
            validInput = True
        else:
            print("There are only pink, yellow and blue hijabs on the shelf! ")

if "yes" in hijab:
    typeEffect ("You and your sister are now walking to school.")
    time.sleep(1)
    typeEffect ("On the way to school, you looked at Asiya under the sunshine. Her blue hijab looks very pretty. The blueness of it speaks to you.")
    time.sleep(1)

typeEffect("...")
time.sleep (1)
print("                _ _.-'`-._ _")
print("                ;.'________'.;")
print("     _________n.[____________].n_________")
print("    |""_""_""_""||==||==||==||""_""_""_""]")
print('    |"""""""""""||..||..||..||"""""""""""|')
print("    |LI LI LI LI||LI||LI||LI||LI LI LI LI|")
print("    |.. .. .. ..||..||..||..||.. .. .. ..|")
print("    |LI LI LI LI||LI||LI||LI||LI LI LI LI|")
print(" ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,")
print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
print()
time.sleep(1)
print ("You arrived at school! Your sister said goodbye and went to the sixth grade area.")
time.sleep(1)
print()

if "yes" in hijab:

    typeEffect ("Your friend Lucy saw your hijab, she told you it looks really nice! You felt a bit less nervous about wearing it.\n")
time.sleep(1)

if "yes" in hijab:
    typeEffect ('When you were walking to your class, another student in your grade saw your hijab, but did not know what it was. They said,')
    time.sleep(1)
    typeEffect ('"Haha, are you wearing a towel on your head? That looks so funny"')
    time.sleep(1)
if "no" in hijab:
    typeEffect ('A student in your grade saw her hijab, they did not know what it was, and said,')
    time.sleep(1)   
    typeEffect ('"Haha, is your sister wearing a towel on her head? That looks so funny"')
    print()
mixer.music.stop()
mixer.init()
mixer.music.load("intense.mp3")

mixer.music.play()
validInput = False
while validInput == False:
    time.sleep(1)
    typeEffect ("What do you want to do?\n\n")
    choice=(input("Type 1 If you want to stand up to them and explain what the hijab is\nType 2 If you want to shout at them\nType 3 If you want to run away from them\n"))
    print (" ")
    if "1" in choice:
        typeEffect ("You explained to them what you believed is right, that the hijab represents your culture, your beliefs and what makes you unique.\nThey then said sorry for joking about it!")
        pointCounter += 20
        printpoints(pointCounter)
        time.sleep (1)
        validInput = True
    elif "2" in choice:
        typeEffect("You shouted at that student! The student shouted back at you, you were both unhappy about the situation.")
        zeroroints(zero)
        time.sleep(1)
        validInput = True
    elif "3" in choice:
        typeEffect("You ran away from the student, feeling sad and irritated about the situation.")
        zeroroints(zero)
        time.sleep(1)
        validInput = True
    else:
        print ("Please enter 1, 2, or 3")

mixer.music.stop()
mixer.init()
mixer.music.load("piano.mp3")
mixer.music.play()

validInput = False
while validInput == False:
    typeEffect ("It is 9:00, the bell rang and the period began!")
    class1 = (input("Press enter to listen to class. "))
    if "w" or "h" in class1:
        print ("You are now listening to class!")
        time.sleep(1)
        validInput = True
    else:
        print ("Please press 1. Try again.")
#learn how to use press enter
print("...")
time.sleep(1)
print("                     ____________________________________________________________________")
print("                    |  __________________________________________________________________  |")
print("                    | |  THE PROUDEST BLUE                                               | |")
print("                    | |                                                                  | |")
print("                    | |                                                                  | |")
print("                  .------------------------------------------------------------------------. ")
print("                 | So what did we learn from reading The Proudest Blue?                     | ")
print("                 | You should be kind and accepting to other people's cultures and differences")
print("                 | And everyone should be treated equally no matter what their background is!|")
print("                   '-,----------------------------------------------------------------------' ")
print("       ___     _/   | |                                                                  | |")
print("     .� __)         | |__________________________________________________________________| |")
print("    ( /_ _(\        |______________________________________________________________________|")
print("   ( _|  > ))")
print("  ( ( (---'-.")
print("  (_ `)\-``  )")
print("    `/-/   ) \ ")
print("----(__.�--------------.")
print("\                       \ ")
print("\\_______________________\ ")
print("|,------------------------'")
print ("gnv")
print ("...")
time.sleep(2)
typeEffect ("...")
time.sleep(2)
typeEffect ("...")
time.sleep(2)
typeEffect ("It is now 10:15, You learned a lot from English class! The class ended.")
pointCounter+=10
validInput = False
while validInput == False:
    sister = (input("You see your sister at the exit of a building, do you want to go to see her?\n"))
    if "y" in sister:
        typeEffect ("She waved at you with a big smile!")
        typeEffect ("You walked to see your sister, you wanted to see if she is doing well.")
        time.sleep (1)
        validInput = True
    elif"n" in sister:
        typeEffect ("You saw your sister with her friends, so you did not want to bother her.")
        time.sleep(1)
        typeEffect ("Your sister saw you in the distantce, and she waved at you with a big smile!")
        typeEffect ("You waved back to her!")
        time.sleep(1)
        typeEffect ("She came to talk to you! With her beautiful blue hijab swaying from the wind")
        typeEffect ("")
        validInput = True
    else:
        print("Please type yes or no.")
validInput = False
while validInput == False:
    typeEffect ("What do you want to say to Asiya?\n\n")
    say = (input('Type 1 to say "Hey Asiya! How are you doing? How do you feel about the first day of Hijab?"\n'))
    if "1" in say:
        typeEffect ('"You greeted Asiya and asked how she was doing!"')
        time.sleep(1)
        print ()
        typeEffect ('Asiya said,"Hey %s ! I am doing great :) How are you?"'%(Name))
        validInput = True
    else:
        typeEffect("Please type 1 to say that.")

validInput = False
while validInput == False:
    time.sleep(1)
    mood = input('Tell Asiya how you are doing! (Type "Great", "Okay", or "Not that good")\n')
    if "Great" in mood:
        typeEffect ('"That is awesome! Glad to hear it!"Asiya said with another beautiful smile.')
        validInput = True
    if "Okay" in mood:
        typeEffect ('Asiya said, "Alright! Sounds good, let me know if I could help you!"')
        validInput = True
    if "Not that good" in mood:
        typeEffect ('"Aww, what happened? I hope you will be better later!" Asiya said, with another beautiful smile.')
        validInput = True

typeEffect ("You said thank you to Asiya for saying that!")

typeEffect ("...")
typeEffect ("...")
typeEffect ("Suddenly, you heard someone laughing from nearby.\nA boy on the basketball court pointed at Asiya, with an unkind face. He said,\n")
typeEffect ('"What is this kid wearing? It looks so stupid!"Closely followed by laughters of other kids.')  


validInput = False
while validInput == False:
    mood = input('Do you want to stand up to the bully for your sister? (Type yes or no)\n')
    if "yes" in mood:
        typeEffect ("Disappointed about the boy's disrespectful comment, you are very angry about it.\nYou told your sister that you want to stand up to the bully.\nYour sister told you to be calm and collected, rather than to shout because you would be as immature as him.\nAnd at last she encouraged you with a big smile.")
        typeEffect ("You said,\n")
        time.sleep(2)
        speech = termcolor.colored("Asiya's hijab is not a laugh. Asiya's hijab is like the ocean waving to the sky. The blueness, it's always there, strong and friendly.\nIt represents our unique culture, so please respect it.\nI hope you will undertand soon, soon enough you do not mock anyone else.")
        printString= termcolor.colored(speech, 'blue')
        typeEffect (printString)
        typeEffect ("You saw the bully leave just now, with a regretful expression. Your sister gave you another smile, this time it was a proud smile. ")
        pointCounter+=30
        printpoints (pointCounter)
        validInput = True
    if "no" in mood:
        typeEffect ("You chose not to stand up to the bully. Asiya walked away from the bully ignoring him. You noticed she was not that happy, and you really wished that next time you could stand up to the bully for her.")
        pointCounter +10
        
'''
decided to stand up to the bully next time
'''

'''
blue text
'''
mixer.music.load("piano.mp3")
mixer.music.play()

print()
time.sleep(2)
word4=art.text2art("______Second Day______")
printString = termcolor.colored(word4, 'white','on_cyan')
fastTypeEffect (printString)
print()
print ("Your mom comes to your room... And as usual, she came to wake you up.")
validInput= False
while validInput == False:
    wakeup2=(input("Do you want to wake up now? (type yes or no)\n"))
    if "yes" in Wakeup:
        time.sleep(1)
        typeEffect("You woke up and dressed up! Ready to take on whatever is ahead.")
        validInput = True
        pointCounter += 5
        time.sleep(1)
        printpoints(pointCounter)
        time.sleep(1)
    elif "no" in Wakeup:
        time.sleep(1)
        typeEffect("You continued to sleep for a while.")
        typeEffect ("Your mom comes back to your room and says, it is getting late honey! Time to wake up and go to school! ")
        wakeCounter += 1
    elif wakeCounter == 3:
        time.sleep(1)
        typeEffect("You slept too late. It is 9:00 already and you finally woke up. Please stay on your schedule next time! ")
        validInput = True
    else:
        typeEffect("Your input is invalid! Try putting yes or no!")

hijablist =["the yellow hijab!", "the blue hijab!", "the pink hijab!"]

validInput = False
while validInput == False:     
    typeEffect ("You saw the shelf with 3 different hijabs on it again. You were thinking about wearing one of them today, perhaps to be no longer afraid of other people's comments?")
    hijabchoice = (input("Do you want to wear a hijab to school today? "))
    if "yes" in hijabchoice:
        time.sleep(1)
        typeEffect ("You chose to wear a hijab!! Despite of the direspectful comments you might face, you wanted to proudly represent your culture.")
        time.sleep(1)
        print("You reached your hand and randomly picked", random.choice(hijablist))
        time.sleep(1)
        pointCounter +=10
        printpoints (pointCounter)
        validInput = True
    if "no" in hijabchoice:
        time.sleep(1)
        typeEffect ("You chose to not wear the hijab today! But you are still determined to support your sister and your beliefs.")
        validInput = True
    if "no" in hijab and "no" in hijabchoice:
        time.sleep(1)
        typeEffect ("You still chose to not wear the hijab today! But you are still determined to support your sister and your beliefs.")
        validInput = True
#list of yellow, blue, pink hijabs, the player would get a random one if they say yes

typeEffect ("You headed to school with your sister!")

typeEffect ("On the way to school, your sister's blue hijab, looked exactly the same as yesterday... But something was different. \nShe looked prouder, and the blueness of it seemed to only brighten, you don't exactly know the reason, but it shined, prouder.")


typeEffect("...")
time.sleep (1)
print("                 _ _.-'`-._ _")
print("                ;.'________'.;")
print("     _________n.[____________].n_________")
print("    |""_""_""_""||==||==||==||""_""_""_""]")
print('    |"""""""""""||..||..||..||"""""""""""|')
print("    |LI LI LI LI||LI||LI||LI||LI LI LI LI|")
print("    |.. .. .. ..||..||..||..||.. .. .. ..|")
print("    |LI LI LI LI||LI||LI||LI||LI LI LI LI|")
print(" ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,")
print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
print()

if "yes" in hijabchoice:
    typeEffect ("Today, the students at school seemed to have became more respectful when they see your hijab!\nYour actions yesterday must have changed their views. ")
if "no" in hijabchoice:
    typeEffect ("Today, the students at school seemed to have became more respectful when they see your sister's hijab!\nYour actions yesterday must have changed their views. ")

typeEffect ("Even though some students glanced, they were all very accepting! They asked about the hijab politely when they did not know what it was.")
if "yes" in hijabchoice:
    typeEffect ("You wore your hijab throughout the day at school, you no longer feel the insecureness of wearing it. You showed your culture to other people. Your hijab swayed left and right in the wind, it was the proudest you have ever felt.")
if "no" in hijabchoice:
    typeEffect ("You saw your sister wear her hijab throughout the day at school, your sister no longer feels the insecureness of wearing it, and showed her culture to other people. You see her blue hijab swaying left and right in the wind, it was the proudest blue you've ever seen.")

pointCounter +=5
print ()


word2=art.text2art("__THE  PROUDEST  BLUE___")
printString = termcolor.colored(word2, 'white','on_blue')
mediumTypeEffect (printString)

typeEffect ("Congratulations!!!\nYou have completed the game!\nHaving a score of %s points!"%(pointCounter))

validInput = False
while validInput == False:
    if pointCounter >= 100:
        typeEffect ("You did a perfect job!")
        typeEffect ("You achieved the legendary badge!")
        print (    "__     __")
        print ("   |  \   /  |")
        print ("   ||| \_/ |||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print (" __|||||||||||__")
        print ("\ \--.||||||.--/ /")
        print (" \ \__\____/__/ /")
        print ("  \ LEGENDARY/")
        print ("    ---------")
        validInput = True
    if pointCounter >= 90 and pointCounter < 100:
        typeEffect ("You did a wonderful job!")
        typeEffect ("You achieved the true master badge!")
        print (    "__     __")
        print ("   |  \   /  |")
        print ("   ||| \_/ |||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print (" __|||||||||||__")
        print ("\ \--.||||||.--/ /")
        print (" \ \__\____/__/ /")
        print ("  \TRUE MASTER/")
        print ("    ---------")
        validInput = True
    if pointCounter >= 80 and pointCounter < 90:
        typeEffect ("You did a great job job!")
        typeEffect ("You achieved the master badge!")
        print (    "__     __")
        print ("   |  \   /  |")
        print ("   ||| \_/ |||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print (" __|||||||||||__")
        print ("\ \--.|||.--/ /")
        print (" \ \__\__/__/ /")
        print ("  \ \MASTER/ /")
        print ("     ------")
        validInput = True
    if pointCounter >= 60 and pointCounter < 80:
        typeEffect ("You did well! Try to get a better score next time!")
        typeEffect ("You achieved the expert badge!")
        print (    "__     __")
        print ("   |  \   /  |")
        print ("   ||| \_/ |||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print ("   |||||||||||")
        print (" __|||||||||||__")
        print ("\ \--.|||.--/ /")
        print (" \ \__\__/__/ /")
        print ("  \ \EXPERT/ /")
        print ("     ------")
        validInput = True
mixer.music.stop()