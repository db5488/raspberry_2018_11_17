class Person:
    
    def __init__(self,name):
        self.name = name;

class MDPerson(Person):
    def __init__(self,name):
        self.name = "Doctor" + name;

class JPPerson(Person):
    def __init__(self,name):
        self.name = name + ", Esquire";


person1 = Person("alice");
print(person1.name);
print(type(person1));

class Car():
    def exclaim(self):
        print("I am Car");


class Yugo(Car):
    def exclaim(self):
        print("I am Yugo");
    
    def need_a_push(self):
        print("A little help here?");

give_me_a_car = Car();
give_me_a_yugo = Yugo();
give_me_a_car.exclaim();
give_me_a_yugo.exclaim();

person = Person("Fudd");
doctor = MDPerson("Fudd");
lawyer = JPPerson("Fudd");

give_me_a_yugo.need_a_push();

print(person.name);
print(doctor.name);
print(lawyer.name);


class EmailPerson(Person):
    def __init__(self,name,email):
        super().__init__(name);
        self.email = email;

bob = EmailPerson("Bob Frapples", "bob@gmail.com");
print(bob.name);
print(bob.email);