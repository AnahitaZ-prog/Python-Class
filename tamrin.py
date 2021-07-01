class Cat:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def hello(self):
        print('hello my name is {}.'.format(self.name))
# Ralf = Cat("Ralf",2,"black")
# print(Ralf.color)

rex = Cat("rex",2,"gray")
Ralf = Cat("Ralf",2,"black")
rex.name = "ralf"
rex.hello()
