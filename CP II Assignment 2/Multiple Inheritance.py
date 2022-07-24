# Multiple Inheritance 
# Base class 1
class A:
    classname = ""
 
    def mother(self):
        print(self.Classname)
 
# Base class2
 
 
class B:
    Secname = ""
 
    def father(self):
        print(self.Secname)
 
# Derived class
 
 
class C(A,B):
    def parents(self):
        print("Class :", self.Classname)
        print("Sec :", self.Secname)
 
 
# Driver's code
s1 = C()
s1.Classname = "I"
s1.Secname = "A"
s1.parents()