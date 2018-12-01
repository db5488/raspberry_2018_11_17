a = 7;
b = a;
print(type(a));
print(type(b));
print(type(58));
print(type(99.9));
print(type('abc'));
print(type(9/5));
print(type(9//5));
a = 95
a += 3
print("a=",a);

print((2 + 3) * 4);
print(10);
print(0b10)
print(0o10)
print(0x10)

#type conversion
print(int(True));
print(int(False));
print(int(98.6));
print(int(1.0e4));
#print(int('99 bottles of beer on the wall'));
print(type(4 + 7));
print(True + 2);
googol = 10 **1000
print(type(googol))
print(float('99'));
print("Nay,'said the naysayer");
poem = '''it is a long established fact that a reader will be distracted by the r
eadable content of a page when looking at its layout.
The point of using Lorem I
psum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes
on purpose (injected humour and the like).'''

bottles = 99;
base = '';
base += 'current inventory:';
base += str(bottles);
print(base)

palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome);
print("hello,\"robert\"");

a = "Duck.";
b = a;
c = "Grey Duck!"
print(a + b + c);

letters = "abcdefghijklmnopqrstuvwxyz";
print(letters[0]);
print(letters[1]);
print(letters[2]);
print(letters[-1]);
#print(letters[1000]);

print(letters[:])
print(letters[20:]);
print(letters[10:]);
print(letters[12:15]);
print(letters[-3:]);
print(len(letters));

todos = 'get gloves, get mask, give cat vitamins,call ambulance';

def myFunction():
    pass;

todosList = todos.split(',');
print(todosList);

todosJoin = '||'.join(todosList);
print(todosJoin);
print('poem\'s len:',len(poem));
print(poem.startswith('it was'));
word = 'is';
print(poem.rfind('is'));
print(poem[3:5]);
print(poem.count('is '));
poem = poem.replace('is', 'was');
print(poem);
 

