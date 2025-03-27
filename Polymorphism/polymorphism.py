class Bird:
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

bird = Bird()
penguin = Penguin()
print(bird.fly())
print(penguin.fly())