# OOP --> Object Oriented Programming 
'''
# An Object Oriented Programming is a Mechanism or a Process which revolves around creating objects.
# It Consists 2 Important Properties --> Attributes (Data), Methods (Behaviour)
# --> Attributes or Variables --> which Carry data to the Class
# --> Methods --> It is a Function defined inside a Class
'''

# Features of OOP -->
'''
# Modularity
# Scalibilty
# Encapsulation ( binding the data(Attributes),features to the class) (Objects)
# Abstraction --> Show only relevant 
# Inheritence --> Acquiring Properties (Attributes, Methods) --> Types -->
# --> Single --> Fingerprint
# --> Multiple --> Parents (Mother, Father) --> Child
# --> Multilevel --> GrandParent -> Parent -> Child
# Polymorphism --> Method Overloading, Method Overriding, Operator Overriding
'''

# Syntax for class creation:
'''
class Class_Name:
    """Doc String"""
    attributes (charecteristics)
    .........
    def func(self):      (behaviour)
        .....
        ......
    ......
obj = Class_Name()
'''

# Student Class with basic details
'''
class Student:
    """Understanding the usage of OOP"""
    name = "Varun"
    id = "CGH3937"
    gender = "Male"
    email_id = "varunsairamjoolapalli2005@gmail.com"
    # Methods(behaviour)
    def display(self):
        print(f"Student Name is {self.name}")
        print(f"Student ID is {self.id}")
        print(f"Student Mail id is {self.email_id}")
U1 = Student()
print(U1)
#print(dir(U1))   # directory (returns all available methods/attributes)
print(U1.display())

U2 = Student()
U2.display()
'''

# Now Student class for Multiple Objects
'''
class Students:
    """Understanding the usage of OOP"""
    name = input("Enter the Name:")
    id = input("Enter the ID No:")
    gender = input("Enter the Gender:")
    email_id = input("Enter the Mail id:")
    # Methods(behaviour)
    def display(self):
        print(f"Student Name is {self.name}")
        print(f"Student ID is {self.id}")
        print(f"Student Mail id is {self.email_id}")
U1 =Students()
U1.display()
U2 = Students()
U2.display()
print(U1.__dict__)    # it returns empty dictionary
print(U2.__dict__)    # it returns empty dictionary
'''

# Students details with Multiple Objects:
'''
class Students:
    """Understanding the usage of OOP"""
    def data(self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    # Methods(behaviour)
    def display(self):
        print(f"Student Name is {self.name}")
        print(f"Student ID is {self.id}")
        print(f"Student Mail id is {self.email_id}")
U1 = Students()
U1.data("Varun","CGH3937","Male","varun@gmail.com")
U1.display()
print(U1.__dict__)
U2 = Students()
U2.data("Sai","CGH4000","Male","sai@gmail.com")
U2.display()
print(U2.__dict__)
'''

# TASK --> Create a Class with Car Brand Name, Price, Colour --> display()

class Cars:
    """Understanding the usage of OOP"""
    def car_data(self,Brand,Name,Price,Colour):
        self.Brand = Brand
        self.Name = Name
        self.Price = Price
        self.Colour = Colour
    #Methods(behaviour)
    def details(self):
        print(f"Car Brand is {self.Brand}")
        print(f"Car Model Name is {self.Name}")
        print(f"Car Price is {self.Price}")
        print(f"Car Colour is {self.Colour}")
U1 = Cars()
U1.car_data("BMW","Sedans",Colour="White",Price="50 Lakhs")
U1.details()
U2 = Cars()
U2.car_data("Maruthi Suzuki","Swift",Colour="Blue",Price="8 Lakhs")
U2.details()