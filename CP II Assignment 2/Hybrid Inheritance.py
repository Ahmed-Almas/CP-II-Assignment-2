# hybrid inheritance
class A:
    def func1(self):
        print("This class is A.")
 
 
class B(A):
    def func2(self):
        print("This class derived from A ")
 
 
class C(A):
    def func3(self):
        print("This class derived from A ")
 
 
class D(B, A):
    def func4(self):
        print("This class derived from A and B ")
 
 
# Driver's code
object = D()
object.func1()
object.func2()