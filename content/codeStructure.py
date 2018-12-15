alphabet = 'abcdefg' + \
'hijklmnop' + \
'efg' + \
'wxyz';
print(alphabet);

color ="puce";
if color == "red":
    print("tomato");
elif color == "green":
    print("pepper");
elif color == "bee purple":
    print("bees");
else:
    print(color);

x = 7;
print((5<x) and (x < 10))

count = 1;
while count <= 5:
    print(count);
    count += 1;

while True:
    stuff = input("STring to capitalize");
    if stuff == "q":
        break;
    print(stuff.capitalize());

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter'];
current = 0;
while current < len(rabbits):
    print(rabbits[current]);
    current += 1;

for letter in rabbits:
    print(letter);
    
accusation = {'room':'ballroom',
              'weapon':'lead pipe',
              'person':'Col. mustard'};

for card in accusation:
    print(card);

for value in accusation.values():
    print(value);
    
for item in accusation.items():
    print(item);

for x in range(0,3):
    print(x);

for x in range(2, -1, -1):
    print(x);

