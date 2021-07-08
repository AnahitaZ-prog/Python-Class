class Jentelman:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def show_info(self):
        return self.__salary

info = Jentelman("d",2,25)
print(info.show_info())
