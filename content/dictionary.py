empty_dict = {};
print(empty_dict);
bierce = {
    "day":"A period",
    "positive":"Mistaken",
    "misfortune":"The Kin"
    };
print(bierce);

lol = [['a','b'],['c','d'],['e','f']];
print(dict(lol));

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
    };

print(pythons);
pythons['Gilliam'] = 'Gerry';
print(pythons);
pythons['Gilliam'] = 'Terry';
print(pythons);

others = {'Marx': 'Groucho', 'Howard':'Moe'};
pythons.update(others);
print(pythons);
del pythons['Marx'];
print(pythons);
#pythons.clear();
#print(pythons);
print('Chapman1' in pythons);
#print(pythons['Marx']);
if 'Marx' in pythons:
    pythons['Marx'];
else:
    print('no key')

print(pythons.get('Marx', 'Not a python'));

print(list(pythons.keys()));
print(list(pythons.values()));
print(list(pythons.items()));

newPythons = pythons.copy();
print(newPythons);