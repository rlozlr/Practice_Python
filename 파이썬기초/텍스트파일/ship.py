ship1 = 3
ship2 = 4
ship3 = 5
maxDay = 0

for i in range(1, (ship1 + 1)):
    if ship1 % i == 0 and ship2 % i == 0:
        maxDay = i
minDay = (ship1 * ship2) // maxDay

newDay = minDay
for i in range(1, (newDay + 1)):
    if newDay % i == 0 and ship3 % i == 0:
        maxDay = i

minDay = (newDay * ship3) // maxDay
print(f'minDay: {minDay}')
print(f'maxDay: {maxDay}')

from datetime import datetime
from datetime import timedelta

n = 1
baseTime = datetime(2021, 1, 1, 10, 0, 0)

with open('C:/pythonEx/arrive.txt', 'a') as f:
    f.write(f'2021년 모든 선박 입항일\n')
    f.write(f'{baseTime}\n')

nextTime = baseTime + timedelta(days=minDay)
while True:
    with open('C:/pythonEx/arrive.txt', 'a') as f:
        f.write(f'{nextTime}\n')

    nextTime = nextTime + timedelta(days=minDay)
    if nextTime.year > 2021:
        break