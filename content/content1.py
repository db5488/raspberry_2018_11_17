#!/usr/local/bin/python3

a = 2 + 2;
print(a);

for i in  range(1, 10):
    print(i);
    
a = 123;
b = 12.34;
c = "Hello";
d = 'Hello';
e = True;

#x = input("Enter Value:");
#print(type(x));
#print("輸入值為:",x);

tempC = input("Enter temp in C:");
tempF = int(tempC) * 9 / 5 + 32;
print("華氏:",str(tempF),"度C");
