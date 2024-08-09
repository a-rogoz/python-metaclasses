# metaclasses are used to create classes;
# classes are used to create objects;
# the type of the metaclass type is type

# __name__ – inherent for classes; contains the name of the class;
# __class__ – inherent for both classes and instances; contains information about the class to which a class instance belongs;
# __bases__ – inherent for classes; it’s a tuple and contains information about the base classes of a class;
# __dict__ – inherent for both classes and instances; contains a dictionary (or other type mapping object) of the object's attributes.

# The same information stored in __class__could be retrieved by calling a type() function with one argument

# When the type() function is called with three arguments, then it dynamically creates a new class.
Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

# 1 the argument specifies the class name; this value becomes the __name__ attribute of the class;
# 2 the argument specifies a tuple of the base classes from which the newly created class is inherited; this argument becomes the __bases__ attribute of the class;
# 3 the argument specifies a dictionary containing method definitions and variables for the class body; the elements of this argument become the __dict__ attribute of the class and state the class namespace.

def bark(self):
    print("Woof, woof")

class Animal:
    def feed(self):
        print("It is feeding time!")

Dog = type("Dog", (Animal, ), {"age": 0, "bark": bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()


# after the class instruction has been identified and the class body has been executed, the class = type(, , ) code is executed;
# the type is responsible for calling the __call__ method upon class instance creation; this method calls two other methods:
# __new__(), responsible for creating the class instance in the computer memory; this method is run before __init__();
# __init__(), responsible for object initialization.


class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = "Added by My_Meta"
        return obj
    

class My_Object(metaclass=My_Meta):
    pass


print(My_Object.__dict__)


#####


def greetings(self):
    print("just a greeting function, but it could be something more serious like a check sum")


class My_Meta2(type):
    def __new__(mcs, name, bases, dictionary):
        if "greetings" not in dictionary:
            dictionary["greetings"] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj
    

class My_Class1(metaclass=My_Meta2):
    pass


class My_Class2(metaclass=My_Meta2):
    def greetings(self):
        print("We are ready to greet you!")

myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()