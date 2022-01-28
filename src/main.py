import random
print('Welcome in GUESS the number game')
try_num = 0
max = 100
min = 0
num = 0
guess = False
try_max = 0
ans = ''
print('Choose your number from ', min, ' to ', max, ' . (Don\'t tell us!)')
try_max = int(input("How many tries I have? Please don't tell 0 :) "))
while (not guess and try_num != try_max):
    try_num += 1
    num = random.randint(min, max)
    print('Is it ', num, ' ? Yes or No ')
    ans = (input('')).upper()
    if(ans == 'YES'):
        guess = True
    elif (try_num != try_max):
        print('Is YOUR number higher or lower? ')
        ans = (input('')).upper()
        if (ans == 'HIGHER'):
            min = num + 1
        else:
            max = num - 1

print('-'*10)
if(not guess):
    print('I lost :( I run of guess number.')
else:
    print('I won! I\'m much clever than you! LOL')
    print('I just needed ', try_num, ' of ',
          try_max, ' tries to guess your num.')
input('Enter to close the console')
