import tkinter
from tkinter import Tk

#Sets windows to Tk
window = Tk()
#Gives the size of the box
window.geometry('300x500')
#Changes the windows name
window.title("Word class definer")
#Changes the background color
window.configure(background = 'light blue')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def Adjectives():
     print("Adjectives")
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("An Adjective is a word nameing an attribute of a noun")
     print("")
     print("Such as They live in a Beautiful house")
     print("")
     print("In this  sentences Beautiful is the Adjective")
     print("")
     print("Here are some adjectives, red, meaningless")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Denominal adjective")
     print()
     print("A mathematical puzzle")
     print()
     print("the denominal adjective is mathematical")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Order of adjectives")
     print()
     print("I love the really  - big - old - blue  -  antique - car there")
     print("")
     print("           quality - size - age - color - qualifier")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("comparing adjectives")
     print("The house is bigger than that one")
     print("")
     print("Bigger is the comparing word")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Compound adjectives")
     print()
     print("This is a four foot table")
     print()
     print("Four foot is the compond adjective")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Adjectival phrase")
     print()
     print("The doctor is very late")
     print()
     print("Very late is the adjectival phrase")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")

adjet = tkinter.Button(window, text='Adjectives',command=Adjectives)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def Noun():
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Noun")
     print()
     print("A word orther then a pro-noun used to identify a class of people, a place or a thing")
     print("")
     print("An Example would be He is the person to see")
     print()
     print("In this  sentences the noun's are He and person")
     print("")
     print("Here are some nouns Dog  John Beach")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Nouns are subjects")
     print()
     print("Every sentence has a subject witch is a noun that tells us what")
     print("what thatsentence is all about")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Nouns are direct objects")
     print()
     print("These nouns receive actions from verbs. john swung the baseball bat")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Nouns are indirect objects")
     print("")
     print("Thesw nouns receive the direct object brad. threw the ball")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Nouns are objects of prepositions")
     print("")
     print("these nouns follow the prepositions in prepositional phrases.")
     print("John swung the base ball bat at Greg")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Nouns are predicate nominatvies")
     print("")
     print("These nouns follow linking verbs and rename the subject.")
     print("John is a baseball player")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Nouns are objectives complements")
     print()
     print("These nouns complete the direct object.")
     print("they named their dog Max")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     
nou = tkinter.Button(window, text='Noun',command=Noun)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#     
def Verb():
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("verb")
     print()
     print("A word used to describe an action or an state occurrence and forming")
     print("")
     print("You cant have a sentence or a question without a verb")
     print("")
     print("Here a list of all the types of verbs")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Physical verb")
     print()
     print("Lets run to the conner and back")
     print()
     print("Run is the verb orther verbs like this are call, hear")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Mental Verb")
     print()
     print("I know the answer")
     print("")
     print("Know was the verb but orhter verbs like this are believe ,recongnized")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("States of being verbs")
     print()
     print("I am a student")
     print()
     print("Student was the verb orther verbs like this are is and are")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Action Verbs")
     print()
     print("Verbs used to express specific actions these are used")
     print("-any time you want to show actions whanting to be done")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Transtitve Verbs")
     print()
     print("Transitive verbs are action verbs, that always exprees")
     print("- double activities these verbs will always have direct objects")
     print("meanings someone or something receives actions from it")
     print("")
     print("Im belive this commands where you are told what to do in")
     print("detail")
     print("An example clean the blue car with a blue sponge")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Intransitive verbs")
     print("")
     print("Intranstive verbs are action verbs that again show do activiities")
     print("but with no direct objects to follow")
     print("")
     print("This is a command given but whith no context or details")
     print("Like go clean the car")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Auxilliary verbs")
     print("Auxiliary verbs are also known as helping verbs")
     print("and are used together with a main verb to show the verb’s tense or to")
     print("from question or negative")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Stative verb")
     print("")
     print("Stative verb can be recongnized because they express a state rather")
     print("than an action they typically relate to thoughts, emmtion relationships")
     print("Senses, states of being measurments")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Modal Verb")
     print("")
     print("Modal verbs are auxiliary verbs that are used to express abilites")
     print("possibiliities, permissions, and obligations")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Phrasal Verbs")
     print()
     print("Phrasal Verbs aren't single words; instead they are combinations")
     print("of words that are used together to take a diffrent meaninng over the original verb")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Irregular Verbs")
     print()
     print("Irregular verbs are those that dont take on the reqular spelling patterns")
     print("of past simple and past participle verbs")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     
     

ver = tkinter.Button(window, text='Verb', command=Verb)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
def Imagery():
          print("_____________________________________________________________")
          print("_____________________________________________________________")
          print("Imagery")
          print("")
          print("This is where the the writeing creates a images in your head")
          print("")
          print("_____________________________________________________________")
          print("_____________________________________________________________")
          print("_____________________________________________________________")
Imy = tkinter.Button(window, text='Imagery',command=Imagery)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
def hyp():
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Hyperbole")
     print()
     print("A hyperbole is like the pub so busy no one gose there")
     print()
     print("Exggerated statements or claims not to be taken literally")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")
hyp = tkinter.Button(window, text='Hyperbole', command=hyp)

#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def oxy():
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Oxymorons")
     print()
     print("A figure of speech in witch apparently contradictory term appear")
     print("conjunction")
     print("")
     print("Here are some examples Big baby Awfully lucky open secret dark light")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")

oxy = tkinter.Button(window, text='Oxymorons', command =oxy)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dion():
      print("_____________________________________________________________")
      print("_____________________________________________________________")
      print("")
      print("Dramatic irony")
      print("")
      print("This is where the audnice know some the charcters dont")
      print("")
      print("Like some onne every one thinks some on is dead but we know")
      print("that there not")
      print()
      print("_____________________________________________________________")
      print("_____________________________________________________________")
      print("_____________________________________________________________")

dion = tkinter.Button(window, text='Dramatic Irony', command =dion)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def iro():
      print("_____________________________________________________________")
      print("_____________________________________________________________")
      print()
      print("Irony")
      print()
      print("The exppression of one's meaning by using language that normally")
      print("Signifies the opposite typically for humorous or emphatic effect")
      print()
      print("For example gettting hit by an ambulance")
      print()
      print("_____________________________________________________________")
      print("_____________________________________________________________")
      print("_____________________________________________________________")
      
iro = tkinter.Button(window, text='Irony', command = iro)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pronoun():
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print()
     print("Pro Noun")
     print()
     print("A pro-Noun is a noun phrase used by itself that refers to either")
     print("to the particpiants in the discoerse or someone or something")
     print("")
     print("Here are some pro nouns: You, IT ,The, he, you")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")

pronoun = tkinter.Button(window, text='Pro Noun', command= pronoun)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def repe():
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("Repetition")
     print()
     print("This is where you repete something muiltply times")
     print()
     print("For example i will i will i will ")
     print()
     print("_____________________________________________________________")
     print("_____________________________________________________________")
     print("_____________________________________________________________")

repe = tkinter.Button(window, text='Repetition', command=repe)
#Programing for the button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~#
#this is the layout of the buttons so i can chose the order they appear
adjet.pack()
nou.pack()
pronoun.pack()
ver.pack()
Imy.pack()
hyp.pack()
oxy.pack()
dion.pack()
iro.pack()
repe.pack()
#~~~~~~~~~~~~~~#
window.mainloop()
mainloop()

    
