import random
number = random.randint(1, 20)
for i in range(1, 7):
    print('Guess the number')
    guessedNum = int(input())
    if guessedNum < number :
        print('you are low')
    elif guessedNum > number:
        print('you are high')
    else:
        print('You got it!!')
        break

