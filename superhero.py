class Superhero:
    def __init__(self, name, secret_identity, powers, weakness):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.powers = powers
        self.__weakness = weakness  # Private attribute
        
    def introduce(self):
        print(f"I am {self.name}! My powers include: {', '.join(self.powers)}.")
        
    def reveal_secret(self):
        print(f"My secret identity is {self._secret_identity}.")
        
    def get_weakness(self):
        return self.__weakness
        
    def use_power(self, power):
        if power in self.powers:
            print(f"{self.name} uses {power}!")
        else:
            print(f"{self.name} doesn't have that power.")
            
    def save_civilians(self):
        print(f"{self.name} is saving civilians!")


# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, max_altitude):
        super().__init__(name, secret_identity, powers, weakness)
        self.max_altitude = max_altitude
        
    def fly(self):
        print(f"{self.name} soars through the air at {self.max_altitude} feet!")
        
    def save_civilians(self):  # Overriding parent method
        print(f"{self.name} flies in and rescues civilians from danger!")


# Example usage
if __name__ == "__main__":
    # Create a regular superhero
    spiderman = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["web-slinging", "spider-sense", "wall-crawling"],
        weakness="ethyl chloride"
    )
    
    # Create a flying superhero
    superman = FlyingSuperhero(
        name="Superman",
        secret_identity="Clark Kent",
        powers=["super strength", "heat vision", "freeze breath", "flight"],
        weakness="kryptonite",
        max_altitude=50000
    )
    
    # Demonstrate functionality
    spiderman.introduce()
    spiderman.use_power("web-slinging")
    spiderman.save_civilians()
    
    print("\n")
    
    superman.introduce()
    superman.fly()
    superman.save_civilians()  # Polymorphism in action
    
    # Demonstrate encapsulation
    print(f"\nSpiderman's weakness (accessed via method): {spiderman.get_weakness()}")
    # This would cause an error:
    # print(spiderman.__weakness)
    