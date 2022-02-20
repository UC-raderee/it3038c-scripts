#

print ("Hello!  Welcome to Emma's Mad Libs.  As a reminder, nouns are objects, places, or people.  Adjectives are descriptive words.  Verbs are action words.  Have fun, and don't use any dirty/curse words!  Just kidding.  Do what you want.")
play=True
while play:
    adjective = input("Choose an adjective: ")
    adjective2 = input("Choose an adjective: ")
    typeofbird = input("Choose a type of bird: ")
    roominhouse = input("Choose a room in a house: ")
    ptverb = input("Choose a past-tense verb: ")
    verb = input("Choose a verb: ")
    name = input("Choose a relative or friends name: ")
    noun = input("Choose a noun: ")
    liquid = input("Choose a liquid: ")
    verb2 = input("Choose a verb ending with -ing: ")
    bodypart = input("Choose a plural part of the body: ")
    pnoun = input("Choose a plural noun: ")
    verb3 = input("Choose a verb ending with -ing: ")
    noun2 = input("Choose a noun: ")


#Displays the story based on the users input
    print ("------------------------------------------")
    print ("It was a",adjective,", cold November day.")
    print ("I woke up to the ",adjective2," smell of ",typeofbird," roasting in the ",roominhouse," downstairs.")
    print ("I ",ptverb," down the stairs to see if I could help ",verb," the dinner.")
    print ("My mom asked me to see if ",name," needed a fresh ",noun,", so I carried a tray of glasses full of ",liquid," into the ",verb2," room.")
    print ("When I got there, I couldn't believe my ",bodypart,"!")
    print ("There were ",pnoun," ",verb3," on the ",noun2,"!")
    print ("What a day!")
    print ("------------------------------------------")
    count=1
    again=str(input("Would you like to play again? Y/N?"))
    if again == "N":
        play=False

