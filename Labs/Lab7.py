import emoji
from emoji import emojize


print('Hello, nice to meet you!')

print('I am a script that can represent your moods with emojis. Could you tell me how you are feeling right now?')

print('Options are as follows: Happy, Love, and Silly')

myMood = input()

if myMood == "Happy":
    print('I am glad to hear that! You feel:  ')
    print(emoji.emojize(":grinning_face_with_big_eyes:"))
elif myMood == "Love":
    print('How sweet!')
    print(emoji.emojize(":heart_with_arrow:"))
elif myMood == "Silly":
    print('What a fun mood!')
    print(emoji.emojize(":rolling_on_the_floor_laughing:"))

print('I hope you enjoyed exploring your emotions.  Goodbye!')

quit()
