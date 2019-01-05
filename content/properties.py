class Duck:
    def __init__(self,input_name):
        self._hidden_name = input_name;
        
    @property
    def name(self):
        print("inside the getter");
        return self._hidden_name;
    
    @property
    def nick(self):
        print("nick the getter");
        return self._hidden_name;
    
    @name.setter
    def name(self, input_name):
        print("inside the setter");
        self._hidden_name = input_name;
    
    @nick.setter
    def nick(self,input_name):
        print("inside the setter");
        self._hidden_name = input_name;
        

fowl = Duck("robert");
print(fowl.nick);
fowl.nick = "alice";
print(fowl.nick);