class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


class Bird(Animal):

    def sound(self):
        print("Tweet")


dog = Dog()
cat = Cat()
bird = Bird()

dog.sound()
cat.sound()
bird.sound()