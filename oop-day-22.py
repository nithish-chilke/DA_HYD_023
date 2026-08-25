'''
Constructor--> Instance methods -->public Attributes
Encapsulation

which will automatically initialize the attributes and the ,met to the

'''
'''
class Cars:
    """"Understanding the usage of constructir in oop"""
    def __init__(self,brand,name,price,color):
        self.brand = brand
        self.name = name
        self.price =  price
        self.color = color 
    #Methods (behaviour)
    def Details(self):
        print(f'car brand is {self.brand}')
        print(f'Car name is {self.name}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1 = Cars("Landrover","Defender","5000000","black")
u1.Details()
print(u1.__dict__)
u2 = Cars("Toyata","Fortuner","10000000","maroon")
u2.Details()
print(u2.__dict__)
'''
#Non parameterised 
'''
class Cars:
    """"Understanding the usage of constructir in oop"""
    def __init__(self):
        self.brand = "BMW"
        self.name = "Sedans"
        self.price = "25lakhs"
        self.color = "black"
    #Methods (behaviour)
    def Details(self):
        print(f'car brand is {self.brand}')
        print(f'Car name is {self.name}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1 = Cars()
print(u1.brand,u1.name,u1.price,u1.color)
u1.Details()
print(u1.__dict__)
'''

#encapsulation --> it is one of the main feature of oop
#It binds (bundles) the data (attributes) and the methods (behaviours)
#into a single unit (class) --> multiple objects
#-->Attributes --> public,protected,private
#public attributes --> Attributes define inside the class()
#and  can be modified outside the class
'''
class CodegnanPortal:
    """Codegnan Portal with users"""
    def __init__(self,username):
        self.user = username#Public attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
u1 = CodegnanPortal("Nithishchilke")
u1.display()
u1.user = "Nithish chilke"
u1.display()
print(u1.__dict__)#returns the key-value pairs for attributes
u2 = CodegnanPortal("jayachandra")
u2.display()
print(u2.__dict__)
'''

#protected attributes --> we use single underscore before an
#attribute moreover it can be modified also outside the class
#and even accessible in subclasses...
'''
class CodegnanPortal:
    """Codegnan Portal with users"""
    def __init__(self,username,_otp,):
        self.user = username#Public attribute
        self._otp = _otp
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has recieved OTP as {self._otp}')
u1 = CodegnanPortal("nithish",2345)
u1.display()
u1._otp = 3456
u1.display()
'''
#private attributes --> we use sepcial notations as doubleunderscore
#such as __password
#accessile
'''
class CodegnanPortal:
    """Codegnan Portal with users"""
    def __init__(self,username,_otp,password):
        self.user = username#Public attribute
        self._otp = _otp
        self.__password = password
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has recieved OTP as {self._otp}')
        print(f'Studnet password is {self.__password}')
u1 = CodegnanPortal("nithish",2345,"admin@122")
print(u1.__dict__)
print(u1._CodegnanPortal__password)#NameMangLing
'''

class CodegnanPortal:
    """Codegnan Portal with users"""

    def __init__(self, username, _otp, password):
        self.user = username
        self._otp = _otp
        self.__password = password

    # Getter method
    def get_password(self):
        return "******"

    # Setter method
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Wrong Password, not satisfied 6 characters")
        else:
            self.__password = new_password
            print("Now password is updated")


u1 = CodegnanPortal("nithis", 23455, "admmin@123")

print(u1.get_password())

u1.set_password("nithis")
u1.set_password("saketh123")

print(u1.get_password())