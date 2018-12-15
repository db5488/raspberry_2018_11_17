def do_nothing():
    pass;

do_nothing();

def make_a_sound():
    print('quack');

make_a_sound();

def agree():
    return True;

if agree():
    print("agree");

def echo(anything):
    return anything + ' ' + anything;

print(echo("robert"));

thing = None;
if thing is None:
    print("it's some thing");
else:
    print("no thing");

def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert};

print(menu('chardonnay', 'chicken', 'cake'));

#keyword arguments

print(menu(entree='beef', dessert='bagel', wine='bordeaux'));

print(menu('frontenac', dessert='flan', entree='fish'));

def menu1(wine, entree, dessert='pudding'):
    'prints first ment'
    return {'wine': wine, 'entree':entree, 'dessert':dessert}

print(menu1('chardonnay','chicken'));
print(menu1('dunkelfelder', 'duck', dessert='doughnut'));
print(menu1.__doc__);