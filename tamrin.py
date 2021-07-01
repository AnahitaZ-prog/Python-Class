class Cat:
    name = ""
    age = 0
    color = ""

    def hello(self):
        print("Mio Mio")

Ralf = Cat()
Ralf.name = "Ralf"
Ralf.age = 3
Ralf.color = "Gray"

Mirza = Cat()
Mirza.name = "Mirza"
Mirza.age = 5
Mirza.color = "White"

print(Ralf.name)
Mirza.hello()        
