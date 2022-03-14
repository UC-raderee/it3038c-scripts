from emoji import emojize


print('Hello, nice to meet you! What is your name?')

myName = input()   

print('Okay, '+ myName + '. I am a script that can represent your moods with emojis. Could you tell me how you are feeling right now?')

print('Options are as follows:
        Happy
        In love
        Silly
        Flirty
        Sad
        Sick
        Fancy
        Dead')

myMood = input()

if myMood == Happy:
    print('I am glad to hear that! You feel:  ')
    print(emojize(":smile:"))
elif myMood == In love:
    print('Oooooo look at you, I hope the feeling is mutual.  You feel: ')
    print(emojize(":heart_eyes:"))
elif myMood == Silly:
    print('Well that is a fun mood.  I wish I could laugh at one of your jokes, but unfortunately I am just an emotionless script.  You are feeling:')
    print(emojize(":laughing:"))
elif myMood == Flirty:
    print('Ooo lala, look at you! You are feeling:')
    print(emojize(":kissing_heart:"))
elif myMood == Sad
    print('Oh no!  I do not want you to be sad.  Instead of mirroring your emotions with this emoji, I will give you a baby chick.  Please smile.')
    print(emojize(":hatching_chick:")
elif myMood == Sick
    print('I am sorry that you feel sick.  Eat some saltines and soup and get a lot of rest.  You are feeling:')
    print(emojize(":mask:"))
elif myMood == Fancy
    print('Putting on the ritz, baby! Put on your best and keep that feeling rolling. You are feeling:')
    print(emojize(":bowtie:")
elif myMood == Dead
    print('...Oh my.  Um.  Rest in peace, '+ myName +'.  It was nice to meet you.  If you can still see this script, you are feeling:')
    print(emojize(":skull:"))
else:
print('I do not understand that emotion.  Here is a cat for your troubles.')    print(emojize(":cat2:"))


time.sleep(3)

print ('I hope you had a great time exploring your emotions.  I hope to speak again soon.  Goodbye!')
