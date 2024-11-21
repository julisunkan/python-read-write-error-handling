# Smartphone Class with Inheritance:
# Base class for Smartphone

class Smartphone:
    def __init__(self, model, brand, battery_level):
        self.model = model
        self.brand = brand
        self.battery_level = battery_level  # Battery percentage

    def charge(self):
        if self.battery_level < 100:
            self.battery_level = 100
            print(f"{self.model} is fully charged!")
        else:
            print(f"{self.model} already has a full charge!")

    def use(self):
        if self.battery_level > 0:
            self.battery_level -= 10
            print(f"Using {self.model}. Battery is now at {self.battery_level}%")
        else:
            print(f"{self.model} needs charging!")

    def get_battery(self):
        return self.battery_level


# Derived class for GamingPhone (inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, model, brand, battery_level, is_gaming_mode):
        super().__init__(model, brand, battery_level)
        self.is_gaming_mode = is_gaming_mode  # A specific attribute for gaming phones

    def play_game(self):
        if self.battery_level > 0:
            if self.is_gaming_mode:
                self.battery_level -= 15
                print(f"Playing game on {self.model} in gaming mode. Battery is now at {self.battery_level}%")
            else:
                self.battery_level -= 5
                print(f"Playing a simple game on {self.model}. Battery is now at {self.battery_level}%")
        else:
            print(f"{self.model} has no battery left to play!")

# Example usage
phone1 = Smartphone("Galaxy S21", "Samsung", 80)
phone1.use()
phone1.charge()

gaming_phone = GamingPhone("Razer Phone 2", "Razer", 100, True)
gaming_phone.play_game()
gaming_phone.use()


# Activity 2: Polymorphism Challenge!
# Base class for Animal
class Animal:
    def move(self):
        pass  # Polymorphic method to be implemented by subclasses

# Dog class inherits from Animal
class Dog(Animal):
    def move(self):
        print("The dog runs.")

# Fish class inherits from Animal
class Fish(Animal):
    def move(self):
        print("The fish swims.")

# Bird class inherits from Animal
class Bird(Animal):
    def move(self):
        print("The bird flies.")

# Example usage
def test_movement(animal):
    animal.move()

# Create instances
dog = Dog()
fish = Fish()
bird = Bird()

# Testing polymorphism: Each class defines move() differently
test_movement(dog)   # Output: The dog runs.
test_movement(fish)  # Output: The fish swims.
test_movement(bird)  # Output: The bird flies.
