import random
numberOfStreaks = 0
current=1
last=0
sixInRow=0
for experimentNumber in range(100):
    r = random.randint(0,1)
    if r ==0:
        print('H')
    else:
        print('T')
    if r == last:
        current +=1
        if current == 6:
            sixInRow+=1
    else:
        numberOfStreaks = max(numberOfStreaks, current)
        last = r
        current = 0

print ('longest run was', numberOfStreaks)
print('Six in a row is: ', sixInRow)
# Code that creates a list of 100 'heads' or 'tails' values.

# Code that checks if there is a streak of 6 heads or tails in a row.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))

