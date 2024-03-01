class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f"Hi, This is {self.name}")
        
    def roll_call(self,roll):
        print(f"Hi, This is {self.name} and my roll number is {self.roll}")
        


class Student(Person):
        def __init__(self,name,roll):
            super().__init__(name)
            self.roll = roll
         

names = input("Enter your name: ")
roll = int(input("Enter your roll number: "))


Person1 = Student(names,roll)

Person1.talk()
Person1.roll_call(roll)

        
        
    