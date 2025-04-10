class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        pass  # To be overridden by subclasses
        
    def speak(self):
        pass  # To be overridden by subclasses


class Dog(Animal):
    def move(self):
        return f"{self.name} runs happily! 🐕"
        
    def speak(self):
        return "Woof! Woof!"


class Fish(Animal):
    def move(self):
        return f"{self.name} swims gracefully! 🐟"
        
    def speak(self):
        return "Blub blub..."


class Bird(Animal):
    def move(self):
        return f"{self.name} flies high in the sky! 🦅"
        
    def speak(self):
        return "Tweet tweet!"


class Snake(Animal):
    def move(self):
        return f"{self.name} slithers silently! 🐍"
        
    def speak(self):
        return "Hiss..."


# Demonstration
if __name__ == "__main__":
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Sky"),
        Snake("Viper")
    ]
    
    for animal in animals:
        print(animal.move())
        print(animal.speak())
        print()  # Blank line for separation