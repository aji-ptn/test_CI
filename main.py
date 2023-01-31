from another_class import AnotherClass


class Main:
    def __init__(self):
        self.another_class = AnotherClass(self)
        self.hello = "hello"

    def welcome(self):
        self.hello = "welcome"
        print(self.hello)
        print(self.another_class.world)


a = Main()
a.welcome()
