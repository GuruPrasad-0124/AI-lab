# Write a program to control the VACCUM Cleaner moves(Intelligent systems design process)
import random

def display(room):
    for row in room:
        print(row)

room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooms are dirty")
display(room)

for i in range(4):
    for j in range(4):
        room[i][j] = random.choice([0, 1])

print("Before cleaning the rooms, I detected random dirt in some locations")
display(room)

a = 0
b = 0
dirty_count = 0

while a < 4:
    while b < 4:
        if room[a][b] == 1:
            print("Vacuum cleaner in this location now[a,b]:", a, b)
            room[a][b] = 0
            print("Cleaned", a, b)
            dirty_count += 1
        b += 1
    a += 1
    b = 0

clean_percentage = (100 - ((dirty_count / 16) * 100))
print("Rooms are clean now. Thanks for using!")
display(room)
print('Performance =', clean_percentage, '%')

