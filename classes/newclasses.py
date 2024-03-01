class People:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def name(self,full_name):
        print(full_name)
        
    def age(self,people_age):
        print(people_age)

man = People(10,20)
print(man.x)
man.name("pratik")
man.age(20)