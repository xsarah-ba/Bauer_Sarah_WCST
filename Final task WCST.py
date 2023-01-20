import random
import string

from psychopy import core, event 
from psychopy.visual import Window, TextStim, Circle, Rect, Polygon, Pie
from psychopy.core import wait,Clock
from psychopy.hardware import keyboard                                          #import of the needed modules


def new_card():
    global current_card
    current_card = random.choice(prop_cards)                                    #function that randomly draws a new card from the stack of cards 
    if current_card in previous_cards:                                          #if it's been drawn before a new card will be chosen
        new_card()
    previous_cards.append(current_card)                                         #card will be added to the previously drawn cards

def one_object():
    global current_object
    if current_card[1] == "circle":                                                                                           #checks which shape the card contains
        current_object = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0, -0.6])     #and then generates the object in the right shape and color
    elif current_card[1] == "triangle":
        current_object = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0, -0.6])
    elif current_card[1] == "rectangle":
        current_object = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [0, -0.6])
    else:
        current_object = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.05, -0.65])

def two_objects():
    global current_object2a, current_object2b
    if current_card[1] == "circle":                                                                                          #checks which shape the card contains
        current_object2a = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0, -0.45]) #and then generates two objects in the shape and right color
        current_object2b = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0, -0.75])
    elif current_card[1] == "triangle":
        current_object2a = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0, -0.5])
        current_object2b = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0, -0.7])
    elif current_card[1] == "rectangle":
        current_object2a = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [0, -0.5])
        current_object2b = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [0, -0.7])
    else:
        current_object2a = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.05, -0.55])
        current_object2b = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.05, -0.75])

def three_objects():
    global current_object3a, current_object3b, current_object3c
    if current_card[1] == "circle":                                                                                             #checks which shape the card contains
        current_object3a = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.06, -0.4]) #and then generates three objects in the right shape and color
        current_object3b = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0.06, -0.6])
        current_object3c = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.06, -0.8])
    elif current_card[1] == "triangle":
        current_object3a = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.06, -0.45])
        current_object3b = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0.06, -0.6])
        current_object3c = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.06, -0.75])
    elif current_card[1] == "rectangle":
        current_object3a = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [-0.06, -0.45])
        current_object3b = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [0.06, -0.6])
        current_object3c = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [-0.06, -0.75])
    else:
        current_object3a = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.1, -0.5])
        current_object3b = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [0.01, -0.65])
        current_object3c = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.1, -0.75])

def four_objects():
    global current_object4a, current_object4b, current_object4c, current_object4d
    if current_card[1] == "circle":                                                                                               #checks which shape the card contains
        current_object4a = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.055, -0.47]) #and then generates four objects in the right shape and color
        current_object4b = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0.055, -0.73])
        current_object4c = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0.055, -0.47])
        current_object4d = Circle(test_screen, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.055, -0.73])
    elif current_card[1] == "triangle":
        current_object4a = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.065, -0.5])
        current_object4b = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0.065, -0.7])
        current_object4c = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [0.065, -0.5])
        current_object4d = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = current_card[0], pos = [-0.065, -0.7])
    elif current_card[1] == "rectangle":
        current_object4a = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [-0.065, -0.5])
        current_object4b = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [0.065, -0.7])
        current_object4c = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [0.065, -0.5])
        current_object4d = Rect(test_screen, width = 0.1, height = 0.13, fillColor = current_card[0], pos = [-0.065, -0.7])
    else:
        current_object4a = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.11, -0.54])
        current_object4b = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [0.01, -0.73])
        current_object4c = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [0.01, -0.54])
        current_object4d = Pie(test_screen, radius = 0.1, fillColor = current_card[0], pos = [-0.11, -0.73])

def new_rule():
    global current_rule
    current_rule = random.choice(rules)                                         #function that randomly chooses a rule
    if not len(previous_rules) == 0:                                            #checks whether the list of previous rules is still empty
        if current_rule == previous_rules[-1]:                                  #if the freshly chosen rule is the same as the one a new one will be chosen
            new_rule()
    previous_rules.append(current_rule)                                         #rule will be added to a list of previous rules

def rule_as_number():
    global current_rule_n
    if current_rule == "color":                                                 #this block assigns a number to every possible rule that is currently in use
        current_rule_n = 0
    elif current_rule == "number":
        current_rule_n = 1
    else:
        current_rule_n = 2

def previous_rule_number():
    global previous_rule_n
    if len(previous_rules) > 1:                                                 #checks whether there are already at least two elements in the list (before perseverative errors can't be made)
        if previous_rules[-2] == "color":                                       #this block assigns a number to every possible rule that was in use in the previous block
            previous_rule_n = 0
        elif previous_rules[-2] == "number":
            previous_rule_n = 1
        else:
            previous_rule_n = 2

data = open("data_WCST.txt", "a", encoding = "utf-8")                           #creation of a file and naming of the headers
data.write("\t".join(["subject", "condition", "block_number", "rule", "trial_number", "stimulus", "response_key", "rt", "false/ correct", "perseverative errors so far"]) + "\n")


prop_cards = []                                                                 #list which will contain lists of the properties of all cards
previous_cards = []                                                             #list which will contain the cards that have been drawn before
previous_rules = []                                                             #list which will contain the previous rules
block_nr = 0                                                                    #counts how many times a new rule has been shown (which are the blocks of trials)
pressed_keys = []                                                               #list that will contain the keys that have been pressed
answers_fc = []                                                                 #list that will contain a 0 for every false and an 1 for every correct answer
pers_errors = 0                                                                 #counts the perseverative errors
condition = "no dmg"                                                            #condition can be set to "dmg" if the participant has frontal lobe damage
timer = Clock()

prop_card1 = ["red", "circle", "one"]
prop_card2 = ["green", "triangle", "two"]
prop_card3 = ["blue", "rectangle", "three"]
prop_card4 = ["yellow", "quarter", "four"]                                      #properties of the top 4 cards


rules = ["color", "number", "shape"]                                            #possible rules


colors = ["red", "green", "blue", "yellow"]                                     #list of the possible colors
shapes = ["circle", "triangle", "rectangle", "quarter"]                         #list of the possible shapes
numbers = ["one", "two", "three", "four"]                                       #list of the possible amounts



for color in colors:
    for shape in shapes:
        for number in numbers:
            prop_cards.append([color, shape, number])                           #fills the prop_cards-list with lists that contain the properties of all the cards on the stack
 
prop_cards.remove(["red", "circle", "one"])                                     #and the top four cards are removed from the stack
prop_cards.remove(["green", "triangle", "two"]) 
prop_cards.remove(["blue", "rectangle", "three"]) 
prop_cards.remove(["yellow", "quarter", "four"])


id1 = random.choice(string.ascii_letters)
id2 = random.choice(string.ascii_letters)
id3 = str(random.randint(0,9))
id4 = str(random.randint(0,9))

subject_id = id1 + id2 + id3 + id4                                              #generates a random ID for each subject taking the test


event.globalKeys.add(key = "q", modifiers = ["ctrl"], func = core.quit)         #would allow to quit by pressing q and control, but doesn't work :(


test_screen = Window([1000, 500], color = "black")                                                                                        #creates a window
WCST_text = TextStim(test_screen, text = "Welcome to the\nWisconsin card sorting test.\n\nPress space to read the instructions!")              #text for the welcome screen
WCST_text.draw()
skip_text = TextStim(test_screen, text = "Skip instructions by pressing 's'", pos = [-0.58, -0.85], height = 0.07)                        #instruction to press 's' if the instructions shall be skipped
skip_text.draw()                                                          
test_screen.flip()

keys_start = ["space", "s"]                                                                                                               #list that contains two keys to either get to the instructions or skip them
keys_s = event.waitKeys(keyList = keys_start)

if "space" in keys_s:                                                                                                                     #if the user presses space they get to the instructions
    WCST_text.text ="In this test you will be shown a deck of cards that each have a color, shape and number on them. You will be shown a card and your task will be to sort the card into piles according to one of the attributes (i.e.color, shape, number) but which should be used won't be revealed initially. Instead, you must figure out the correct sorting rule by trial & error. The rule may change during the test.\n\n Press space again to start!"
    WCST_text.alignHoriz = "center"
    WCST_text.draw()
    test_screen.flip()
    keys_s2 = event.waitKeys(keyList = keys_start)
    if "space" in keys_s2:
        WCST_text.text = "Let's go!"
        WCST_text.draw()
        test_screen.flip()
        wait(0.2)
        
elif "s" in keys_s:
    WCST_text.text = "Let's go!"
    WCST_text.draw()
    test_screen.flip()                                                          #if the user presses s they get directly to the experiment
    wait(0.2)


test_card1 = Rect(test_screen, width = 0.25, height = 0.7, fillColor = "white", pos = [-0.8, 0.6])                      #the four card objects
test_card2 = Rect(test_screen, width = 0.25, height = 0.7, fillColor = "white", pos = [-0.27, 0.6])
test_card3 = Rect(test_screen, width = 0.25, height = 0.7, fillColor = "white", pos = [0.27, 0.6])
test_card4 = Rect(test_screen, width = 0.25, height = 0.7, fillColor = "white", pos = [0.8, 0.6])

test_object1 = Circle(test_screen, radius = 0.1, size = (0.5,1), fillColor = "red", pos = [-0.8, 0.6])                  #red circle thats on the first card
test_object2a = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = "green", pos = [-0.27, 0.7])
test_object2b = Polygon(test_screen, edges = 3, radius = 0.1, size = (0.5, 1), fillColor = "green", pos = [-0.27, 0.5]) #the two green triangles that are on the second card
test_object3a = Rect(test_screen, width = 0.1, height = 0.13, fillColor = "blue", pos = [0.21, 0.74])
test_object3b = Rect(test_screen, width = 0.1, height = 0.13, fillColor = "blue", pos = [0.33, 0.6])
test_object3c = Rect(test_screen, width = 0.1, height = 0.13, fillColor = "blue", pos = [0.21, 0.46])                   #the three blue rectangles that are on the third card
test_object4a = Pie(test_screen, radius = 0.1, fillColor = "yellow", pos = [0.69, 0.68])
test_object4b = Pie(test_screen, radius = 0.1, fillColor = "yellow", pos = [0.81, 0.43])
test_object4c = Pie(test_screen, radius = 0.1, fillColor = "yellow", pos = [0.69, 0.43])
test_object4d = Pie(test_screen, radius = 0.1, fillColor = "yellow", pos = [0.81, 0.68])                                #the for yellow quarters that are on the fourth card

key_card1 = TextStim(test_screen, text = "a", pos = [-0.8, 0.1])                                                        #the four keys that belong to each card
key_card2 = TextStim(test_screen, text = "d", pos = [-0.27, 0.1])
key_card3 = TextStim(test_screen, text = "j", pos = [0.27, 0.1])
key_card4 = TextStim(test_screen, text = "l", pos = [0.8, 0.1])


test_cards = [test_card1, test_card2, test_card3, test_card4]
test_objects = [test_object1, test_object2a, test_object2b, test_object3a, test_object3b, test_object3c, test_object4a, test_object4b, test_object4c, test_object4d]
keys_cards = [key_card1, key_card2, key_card3, key_card4]

trial_card = Rect(test_screen, width = 0.25, height = 0.7, fillColor = "white", pos = [0, -0.6])                        #card object that will contain the stimulus


while block_nr < 3:                                                             #amount of rules that will be chosen
    new_rule()
    rule_as_number()
    previous_rule_number()
    block_nr += 1
    trial_count = random.randint(2,5)                                           #each time a new rule is chosen it's randomly decided how many cards have to be drawn till another rule will be chosen
    count = 0                                                                   #(re)sets the count to 0
    
    while count <= trial_count:                                                 #a new card will be drawn for as many times as it was decided above
        new_card()
        count += 1
        
        for card in test_cards:
            card.draw()                                                         #draws the test cards
        for obj in test_objects:
            obj.draw()                                                          #and the test objects 
        for key in keys_cards:
            key.draw()                                                          #and the keys that belong to the cards
        
        trial_card.draw()                                                       #and the trial card to the screen
        
        
        if current_card[2] == "one":                                            #checks if there is one object on the current card
            one_object()
            current_object.draw()                                               #draws the object to the screen

        elif current_card[2] == "two":                                          #checks if there are two objects on the current card
            two_objects()
            objects2 = [current_object2a, current_object2b]                     #list that contains the two objects
            for obj in objects2:
                obj.draw()                                                      #draws the two objects to the screen

        elif current_card[2] == "three":                                        #checks if there are three objects on the current card
            three_objects()
            objects3 = [current_object3a, current_object3b, current_object3c]   #list that contains the three objects
            for obj in objects3:
                obj.draw()                                                      #draws the three objects to the screen

        else:                                                                   #if there are four objects on the current card
            four_objects()
            objects4 = [current_object4a, current_object4b, current_object4c, current_object4d]  #list that contains the four objects
            for obj in objects4:
                obj.draw()                                                      #draws the four objects to the screen
        
        
        test_screen.flip()                                                      #the test screen is flipped
            
        keys_trial = ["a", "d", "j", "l"]                                       #keys that belong to each card
        keys_t = event.waitKeys(keyList = keys_trial)
        
        cor = TextStim(test_screen, text = "Correct")                           #texts that will be used as feedback
        inc = TextStim(test_screen, text = "Incorrect")
        
        rt = timer.reset
        
        if "a" in keys_t:                                                             #checks whether 'a' has been pressed
            rt = timer.getTime()
            pressed_keys.append("a")                                                  #adds it to the list of previously pressed keys
            if prop_card1[current_rule_n] == current_card[current_rule_n]:            #checks whether the card has been sorted according the rules by comparing the property of the chosen card with the current card
                cor.draw()
                answers_fc.append(1)                                                  #adds a 1 to indicate a correct answer
            else:
                inc.draw()
                answers_fc.append(0)                                                  #adds a 0 to indicate a wrong answer
                if len(previous_rules) > 1:                                           #checks whether the first rule is the only rule that's been added to the list of previous rules (there can't be any perseverative errors yet)
                    if prop_card1[previous_rule_n] == current_card[previous_rule_n]:  #checks whether the error has been a perseverative one
                        pers_errors += 1                                              #if so, the count for perseverative errors is increased by one
            
        elif "d" in keys_t:                                                           #checks whether 'd' has been pressed
            rt = timer.getTime()
            pressed_keys.append("d")                                                  #adds it to the list of previously pressed keys
            if prop_card2[current_rule_n] == current_card[current_rule_n]:            #checks whether the card has been sorted according the rules by comparing the property of the chosen card with the current card
                cor.draw()
                answers_fc.append(1)                                                  #adds a 1 to indicate a correct answer
            else:
                inc.draw()
                answers_fc.append(0)                                                  #adds a 0 to indicate a wrong answer
                if len(previous_rules) > 1:                                           #checks whether the first rule is the only rule that's been added to the list of previous rules (there can't be any perseverative errors yet)
                    if prop_card2[previous_rule_n] == current_card[previous_rule_n]:  #checks whether the error has been a perseverative one
                        pers_errors += 1                                              #if so, the count for perseverative errors is increased by one
            
        elif "j" in keys_t:                                                           #checks whether 'j' has been pressed
            rt = timer.getTime()
            pressed_keys.append("j")                                                  #adds it to the list of previously pressed keys
            if prop_card3[current_rule_n] == current_card[current_rule_n]:            #checks whether the card has been sorted according the rules by comparing the property of the chosen card with the current card
                cor.draw()
                answers_fc.append(1)                                                  #adds a 1 to indicate a correct answer
            else:
                inc.draw()
                answers_fc.append(0)                                                  #adds a 0 to indicate a wrong answer
                if len(previous_rules) > 1:                                           #checks whether the first rule is the only rule that's been added to the list of previous rules (there can't be any perseverative errors yet)
                    if prop_card3[previous_rule_n] == current_card[previous_rule_n]:  #checks whether the error has been a perseverative one
                        pers_errors += 1                                              #if so, the count for perseverative errors is increased by one
            
        elif "l" in keys_t:                                                           #checks whether 't' has been pressed
            rt = timer.getTime()
            pressed_keys.append("l")                                                  #adds it to the list of previously pressed keys
            if prop_card4[current_rule_n] == current_card[current_rule_n]:            #checks whether the card has been sorted according the rules by comparing the property of the chosen card with the current card
                cor.draw()
                answers_fc.append(1)                                                  #adds a 1 to indicate a correct answer
            else:
                inc.draw()
                answers_fc.append(0)                                                  #adds a 0 to indicate a wrong answer
                if len(previous_rules) > 1:                                           #checks whether the first rule is the only rule that's been added to the list of previous rules (there can't be any perseverative errors yet)
                    if prop_card4[previous_rule_n] == current_card[previous_rule_n]:  #checks whether the error has been a perseverative one
                        pers_errors += 1                                              #if so, the count for perseverative errors is increased by one
        
        rt_r = round(rt, 4)
        test_screen.flip()
        wait(0.5)
            
        data.write("\t".join([subject_id, condition, str(block_nr), str(current_rule), str(count), str(current_card), pressed_keys[-1], str(rt_r), str(answers_fc[-1]), str(pers_errors)]) + "\n")


WCST_text.text = "Thank you for your participation! \nYou can now quit by pressing any button."
WCST_text.draw()
test_screen.flip()

keyb = keyboard.Keyboard()
keyb.waitKeys()

divisor = len(answers_fc)                                                       #indicates how many answers the user has given
count_cor = answers_fc.count(1)                                                 #counts how many of these answers have been correct
count_inc = answers_fc.count(0)                                                 #counts how many of these answers have been false
percent_cor = round((count_cor/divisor *100), 2)                                #calculates the percentage of correct answers
percent_inc = round((count_inc/divisor *100), 2)                                #calculates the percentage of incorrect answers
percent_pers = round((pers_errors/count_inc *100), 2)                           #calculates the percentage of perseverative errors in the incorrect answers

data.write("\t".join(["\n(amount / percentage) \nCorrect answers:", str(count_cor), str(percent_cor), "\nIncorrect answers:", str(count_inc), str(percent_inc), "\nPerseverative errors:", str(pers_errors), str(percent_pers), "\n\n  ### \n\n"]))

data.close()