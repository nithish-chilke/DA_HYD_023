'''
OOP --> Class,Object,Methods(__init__())
Encapsulation -->Public,Protected,Private
Inheritance -->It is one of key features of oop where we inherit the properties (attributes/methods)
from one clas to another class (base class(parent class) --> derived class (child class))
Whatsapp --> personal user,Business user(catalog),community admin
Features --> Code Reusability,Avoiding Code Duplication,Code maintainability,Polymorphism(method overriding(super()),
method overloading,operator overloading __add__,__str__)

Types : Single Inheritance (Finger Print)
-->One Child class inherting properties from one parent class
Multiple Inheritance(Mother,Father --> Child) -->One child class inheriting propertied from two parent classes
Multiple Inheritance(Grandparent-->parent-->child)
level by level
Hierarchical Inheritance -->multiple child classes inheriting properties from single parent
Hybrid Inheritance --> It can carry one or more type of inheritances

syntax:

single Inheritance:

class baseclass:
    statements(S)...
    ......
class Derivedclass(baseclass):
    ......
    ......

#Whatsapp Scenario -->

class User:
    """single inheritance usage"""
    def send_message(self):
        print('sending_message')
    def voice_call(self):
        print('Making voice call')
    def video_call(self):
        print('making video call')
class BusinessUser(User):
    #pass
    def create_catalog(self):
        print("Displaying Products catalog")
u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog()


#social media login --> users -->update_users
class Users:
    """Single Inheritance usage"""
    company = "codegnan"
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + " " + self.lname
#u1 = Users("Nithish", "Chilke")
#print(u1.full_name())
#print(u1.company)
class update_users(Users):
    def update_name(self):
        return self.fname.title() +" "+self.lname.title().strip()
u1 = update_users("Nithish","Chilke")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2 = Users("saketh","kallepu")
print(u2.full_name())
print(u2.company)

#what if we have constructor in child class also....
#father --> kid (property)

class Father:
    """Usage of Constructor in single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        #self.property = 200000
        self.cash = 200000
    def kid_property(self):
        print(f'Kid property is {self.property}')
obj = Kid()
obj.father_property()
obj.kid_property()
#in this example parent class is having constructor and child class is havimg comstructor so constructor overriding is happening
#to avoid constructor overriding we use super()
-->super() .__init__()
--> super() .__init__(args)
--> super().method()
'''
class Father:
    """Usage of Constructor in single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        super() .__init__()
        self.cash = 200000
    def kid_property(self):
        print(f'Kid property is {self.cash}')
        print(f'kid Final property is {self.cash+self.property}')
obj = Kid()
obj.father_property()
obj.kid_property()