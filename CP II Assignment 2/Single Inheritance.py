#Single Inheritance
# Base class
class A:
    def C(self):
        print("This is base class A")
 
# Derived class
class B(A):
    def D(self):
        print("This class derived from base class A")
        
o = B()
o.C()
o.D()