# Hierarchical inheritance
# Base class
class op:
    def func1(self):
        print("We are going to derive 2 lasses from this class")
 
# Derived class1
class op1(op):
    def func2(self):
        print("This class is derived from class op named op1.")
 
# Derivied class2
class op2(op):
    def func3(self):
        print("This class is derived from class op named op2.")
 
 
# Driver's code
object1 = op1()
object2 = op2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()