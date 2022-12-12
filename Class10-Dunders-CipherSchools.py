class Person:
    def  _init_(self,name):
        self.name=name
        
    def say_hi(self):
        print('hello, my name is ',self.name)
        
p=Person("loveu")
p.say_hi()




class A:
    def _init_(self):
        print(self)
        print('initialized')
        
    def _del_(self):
        print(self)
        print("I am genious and i am not dying for you")    
a=A()




del a 
a=1
print(type(a))
print(a+5)
print(a._add_(5))
print("loveu singh or " * 20)
print("shivam or saurav or loveu or "._mul_(20))


# class Person:
#     name="loveu"
#     def _add_(self,a):
        
class B:
    a=1
    b=2
    def _add_(self,x):
        return a+b+x