# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # percentage
    
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% ")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Battery: {self.battery}%")

# Subclass: GamingPhone (inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu):
        super().__init__(brand, model, battery)  # Call parent constructor
        self.gpu = gpu
    
    def play_game(self, game):
        if self.battery > 10:
            self.battery -= 10
            print(f"Playing {game} on {self.brand} {self.model} 🎮 (Battery: {self.battery}%)")
        else:
            print("Battery too low! Please charge")
    
    # Overriding method (polymorphism example)
    def info(self):
        print(f"Gaming Phone: {self.brand} {self.model}, GPU: {self.gpu}, Battery: {self.battery}%")
        

# Testing our classes
phone1 = Smartphone("Samsung", "Galaxy S23", 80)
phone2 = GamingPhone("Asus", "ROG Phone 7", 90, "Adreno 740")

phone1.info()
phone1.make_call("+254721234567")
phone1.charge(15)

print("\n---\n")

phone2.info()
phone2.play_game("PUBG Mobile")
phone2.play_game("Genshin Impact")
