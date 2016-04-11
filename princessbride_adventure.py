princess_name = raw_input("Hey there! What's your name? > ")
print "\n"
print "Oh my, hello {}! Or should I say, Princess {}. ^___^ Looks like you just woke up from... fainting. :/".format(princess_name,princess_name)
print "\n"
print "I'm here as your narrator because, well, you kinda need one right now to catch you up on the drama."
print "\n"
print "I'll have you know that you've just been kidnapped by a trio of bandits: a Sicilian boss named Vizzini, a giant named Fezzik, and a Spanish master fencer named Inigo Montoya. You're actually snugly tucked in one of Fezzik's huge arms."
print "\n"
print "Yikes. Well, what can do you do?"
print "1. Nothing..for NOW. No use since Fezzik's a giant :/"
print "2. Fight my way out of their clutches!"
print "3. Give up OTL"

fight_or_flight = int(raw_input("> "))

while (fight_or_flight <= 0) or (fight_or_flight >= 4): # Couldn't figure out how to do NAN
    print "\n"
    print "Oops, I need a response of 1, 2, or 3. Try that again?" # I did several of these throughout, which I realized would probably be better as a function. Not sure how to do python functions yet though.

    fight_or_flight = int(raw_input("> "))

else:
    while fight_or_flight == 3:
        print "\n"
        print "Excuse me but you're Princess {}, you would never give up. Don't you go OTL on me. Let's try that again:".format(princess_name)
        print "1. Nothing..for NOW. no use since Fezzik's a giant  :/"
        print "2. Fight my way out of their clutches!"

        fight_or_flight = int(raw_input("> "))

        while (fight_or_flight <= 0) or (fight_or_flight >= 3):
            print "\n"
            print "Oops, I need a response of 1 or 2. Try that again?"

            fight_or_flight = int(raw_input("> "))

    else:
        if fight_or_flight == 1:
            print "\n"
            print "Alright, nothing for now. Well, Fezzik's giant arms would be hard to get out of anyway."
        else:
            print "\n"
            print "Well.. you thrashed as hard as you could but Fezzik's arms are just too giant for you to escape just yet."

print "\n"
print "Okay, so you've been kidnapped. Yep, it's a big deal but let's see where this story goes."
print "\n"
print "As the trio of bandits journeys with you in tow, they slowly realize that a masked man is following them."
print "\n"
print "For some reason, the trio's letting you choose who will stay behind and tackle the masked man. So who do you think should go first?"
print "1. Inigo, he looks like a great swordfighter with a backstory involving revenge."
print "2. Are you kidding? Fezzik! He's A GIANT!"
print "3. Vizzini, I suppose. He's saying that it's inconceivable for the masked man to beat him mentally."

kidnapper_to_fight = int(raw_input("> "))

#I'd like to be able to use validation in the future so that I can present the options to the user again but without the options that they've already chosen. Also, to validate for string responses!
while (kidnapper_to_fight <= 0) or (kidnapper_to_fight >= 4):
    print "\n"
    print "Oops, that wasn't one of the options. Try that again?"

    kidnapper_to_fight = int(raw_input("> "))

else:
    while kidnapper_to_fight != 3:
        if kidnapper_to_fight == 1:
            print "\n"
            print "Inigo stays behind to swordfight him, but the masked man is seen again."
            print "\n"
            print "Who do you think can beat him now?"
     
            kidnapper_to_fight = int(raw_input("> "))
 
            while (kidnapper_to_fight <= 0) or (kidnapper_to_fight >= 4):
                print "\n"
                print "Oops, that wasn't one of the options. Try that again?"

                kidnapper_to_fight = int(raw_input("> "))
    
        elif kidnapper_to_fight == 2:
            print "\n"
            print "Fezzik stays behind to combat him, but he's knocked unconscious!"
            print "\n"
            print "Who do you think can beat him now?"
     
            kidnapper_to_fight = int(raw_input("> "))

            while (kidnapper_to_fight <= 0) or (kidnapper_to_fight >= 4):
                print "\n"
                print "Oops, that wasn't one of the options. Try that again?"

                kidnapper_to_fight = int(raw_input("> "))
 
    else:
        print "\n"
        print "Vizzini waits for the masked man to come to him at the top of a hill, who challenges him to a mental duel. He produces two cups of wine that Vizzini must choose to drink from, with one of them containing POISON! What would you guess that Vizzini should take?"
        print "\n"
        print "1. The golden cup!"
        print "2. The other cup that looks exactly like the golden cup!"

        cup_choice = int(raw_input("> ")) # no conditional statements in this case since both cups are poisoned!

        while (cup_choice <= 0) or (cup_choice >= 3):
            print "\n"
            print "Oops, I need a response of 1 or 2. Try that again?"

            cup_choice = int(raw_input("> "))
 
        print "\n"
        print "Both Vizzini and the masked man drink their chosen cups.. and Vizzini chokes to death on the poison one!"
        print "\n"
        print "Well actually, the masked man poisoned both, he just built up an intolerance to the poison."

print "\n"
print "With Vizzini dead, Inigo and Fezzik flee!"
print "\n"
print "You finally get a closer look at the masked man and realize -- He's got to be the Dread Pirate Roberts! The pirate who killed the love of your life, Westley."
print "\n"
print "What do you do??"
print "1. Ask him who he is, just to clarify."
print "2. Tell him what you just realized."
print "3. Push him down the hill!!!"

masked_man_confrontation = int(raw_input("> "))

while (masked_man_confrontation <= 0) or (masked_man_confrontation >= 4):
    print "\n"
    print "Oops, I need a response of 1, 2, or 3. Try that again?"

    masked_man_confrontation = int(raw_input("> "))
else:

    if masked_man_confrontation == 1:
        print "\n"
        print "You ask the masked man who he is. He explains that these days, he goes by the name DREAD PIRATE ROBERTS, but that's his pirate stage name seeing as how the title had been passed down to him from his life aboard the previous Roberts' ship."
        print "\n"
        print "Now what?"
        print "1. Well he just confirmed that he's the Dread Pirate Roberts, so push him down the hill now!"
        print "2. Be a little less dramatic and tell him to take off the mask. You want to see the face of the man who killed your love."

        princess_drama_reaction = int(raw_input("> "))

        while (princess_drama_reaction <= 0) or (princess_drama_reaction >= 3):
            print "\n"
            print "Oops, I need a response of 1 or 2. Try that again?"

            princess_drama_reaction = int(raw_input("> "))

        if princess_drama_reaction == 1:
            print "\n"
            print "You dramatically yell to him 'You killed my Westley! You can die for all I care!' and push him."
            print "\n"
            print "As he tumbles down the hill, he manages to say 'As..you...wish...!'"
            print "\n"
            print "As you slowly manage to understand him, you realize that was the phrase that Westley used to say when he meant I LOVE YOU. You then tumble right after him down the hill. At the bottom, you find that his mask flew off to reveal that he is indeed Westley!"
            print "\n"
            print "You two can now live happily ever after (well, if you manage to escape Prince Humperdink, who's looking for you now so you can get married)!!!!"
            print "\n"
        elif princess_drama_reaction == 2:
            print "\n"
            print "You yell at him 'You killed my Westley!' You demand he takes off his mask so you can look at the face of the man who killed your love."
            print "\n"
            print "As he slowly takes off his mask, he says 'as you wish,' which was the phrase that Westley used to say when he meant 'I love you.'"
            print "\n"
            print "Just as you realize it, he reveals that he has indeed been Westley all along! You two can now live happily ever after (well, if you manage to escape Prince Humperdink, who's looking for you now so you can get married)!!!!"
            print "\n"
        else:
            print "You dramatically yell to him 'You killed my Westley! You can die for all I care!' and push him. As he tumbles down the hill, he manages to say As..you...wish...!'"
            print "\n"
            print "You slowly manage to understand him and realize that was the phrase that Westley used to say when he meant 'I love you.'"
            print "\n"
            print "You then tumble right after him down the hill. At the bottom, you find that his mask flew off to reveal that he is indeed Westley! You two can now live happily ever after (well, if you manage to escape Prince Humperdink, who's looking for you now so you can get married)!!!!"
            print "\n"

    elif masked_man_confrontation == 2:
        print "\n"
        print "You tell him you realized he's the Dread Pirate Roberts, which he confirms 'Yes, but--' BUT you don't care what he has to say, he's the one who killed your love!"
        print "\n"
        print "You yell at him 'You killed my Westley! You can die for all I care!' and push him. As he tumbles down the hill, he manages to say As..you...wish...!'"
        print "\n"
        print "You slowly manage to understand him and realize that was the phrase that Westley used to say when he meant 'I love you.'"
        print "\n"
        print "You then tumble right after him down the hill. At the bottom, you find that his mask flew off to reveal that he is indeed Westley! You two can now live happily ever after (well, if you manage to escape Prince Humperdink, who's looking for you now so you can get married)!!!!"
        print "\n"

    else:
        print "\n"
        print "You yell at him 'You killed my Westley! You can die for all I care!' and push him. As he tumbles down the hill, he manages to say As..you...wish...!'"
        print "\n"
        print "You slowly manage to understand him and realize that was the phrase that Westley used to say when he meant 'I love you.'"
        print "\n"
        print "You then tumble right after him down the hill. At the bottom, you find that his mask flew off to reveal that he is indeed Westley! You two can now live happily ever after (well, if you manage to escape Prince Humperdink, who's looking for you now so you can get married)!!!!"
        print "\n"
        
print "\n"
restart = raw_input("Would you like to play this again, 'Yes' or 'No'? > ")
        
if restart == "Yes":
    print "\n"
    print "As you wish!"
    print "\n"
    execfile("slojewski_adventure.py")
else:
    print "\n"
    print "As you wish, have fun storming the castle!"
    print "\n"
