class Animal:
    def __init__(self,name):
        self.__name = name;
    
    @property
    def name1(self):
        return self.__name;
    
    @name1.setter
    def name1(self,name):
        self.__name = name;

a1 = Animal('animal');
print(a1.name1);
a1.name1 = 'cat';
print(a1.name1);