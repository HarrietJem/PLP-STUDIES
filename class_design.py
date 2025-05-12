# Parent class: Superhero
class Superhero:
    def __init__(self, name, superpower, weakness):
        self.name = name
        self.superpower = superpower
        self.weakness = weakness

    def use_power(self):
        return f"{self.name} uses {self.superpower}!"

# Child class: FlyingSuperhero (inheritance & encapsulation)
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, weakness, flight_speed):
        super().__init__(name, superpower, weakness)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies at {self.flight_speed} km/h!"

# Creating objects
hero1 = Superhero("Thunderbolt", "Lightning Strike", "Water")
hero2 = FlyingSuperhero("Sky Guardian", "Wind Manipulation", "Darkness", 500)

# Using methods
print(hero1.use_power())  # Thunderbolt uses Lightning Strike!
print(hero2.fly())  # Sky Guardian flies at 500 km/h!
