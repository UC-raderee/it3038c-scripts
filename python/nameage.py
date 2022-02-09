import time
start_time = time.time()


print('What is your name?')

myName = input()

while myName != 'Emma':
    if myName == 'your name':
        print('Ha ha, very funny. Seriously, who are you?')
        myName = input()
    
    else:
        print('That is not your name.  Please, tell me your real name.')

        myName = input()
    

print('Hello, '+ myName + '. That is a good name. How old are you?')

myAge = int(input())

if myAge < 13:
    print('Learning young, thats good')
elif myAge == 13:
    print('Youre a teenager now... thats cool, I guess')
elif myAge > 13 and myAge < 30:
    print('Still young, still learning...')
elif myAge >= 30 and myAge < 65:
    print('Now youre adulting.')
else:
    print('...youve lived a long time?')


programAge = int(time.time() - start_time)

print('%s? Thats funny, Im only %s seconds old.' % (myAge, programAge))

print('I wish I was %s  years old' % str(int(myAge) * 2))

time.sleep(3)

print ('Im tired. I go sleep sleep now.')
