import random
# Point of no return
from logger import Logger
import sys
# They've all fallen into the powers of darkness
base_troops = 60
class _C:
    """
    This class offers quick color coding for terminal text with predefined color attributes.
    """
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'  # Resets the color to default.

class Territory:
    def __init__(self, district, name):
        self.name = name
        self.district = district
        self.controlled_by = None
        self.troops = 0

class District:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        #self.territories = self.create_territories()
        self.territories = []
    def add_territories(self, t1,t2,t3,t4):
        territories = []
        territories.append(Territory(self,t1))
        territories.append(Territory(self,t2))
        territories.append(Territory(self,t3))
        territories.append(Territory(self,t4))
        self.territories = territories
    def create_territories(self):
        territories = []
        for i in range(4):
            territory_name = input(f"Enter name for territory {i+1} in {self.name}:")
            territories.append(Territory(self, territory_name))
        return territories  # Fix: return the list of territories.
    

class City:
    city_id_counter = 1
    
    def __init__(self, name):
        self.id = City.city_id_counter
        City.city_id_counter += 1
        self.name = name
        self.districts = {
            "Central": District("Central", self),
            "Midtown": District("Midtown", self),
            "Outskirts": District("Outskirts", self)
        }
class Faction:
    def __init__(self, name,total_troops):
        self.name = name
        print(f"Created faction {_C.MAGENTA}{self.name}{_C.RESET}")
        self.total_troops = total_troops
        self.territories = {}
        self.headquarters = None

    def add_territory(self, territory):
        print(f"added {_C.RED}{territory.name}{_C.RESET} from {_C.BLUE}{territory.district.name}{_C.RESET} to {_C.YELLOW}{self.name}{_C.RESET} in {_C.GREEN}{territory.district.city.name}{_C.RESET}")
        territory.controlled_by = self
        self.territories[territory] = territory

    def set_headquarters(self, territory):
        # Check if headquarters is already set
        if self.headquarters is not None:
            print(f"Headquarters already set at {self.headquarters.name}. Cannot reassign headquarters.")
            return
        # Check if the territory is controlled by this faction
        if territory in self.territories:
            self.headquarters = self.territories[territory]
            print(f"Headquarters set at {_C.RED}{self.headquarters.name}{_C.RESET} for {_C.YELLOW}{self.name}{_C.RESET} faction")
        else:
            print(f"Territory {_C.RED}{territory.name}{_C.RESET} is not controlled by {_C.YELLOW}{self.name}{_C.RESET}. Cannot set as headquarters.")
    def make_choice(self):
        choices = ["attack", "defend", "hold", "ask_for_help"]
        return random.choice(choices)

    def execute_choice(self, choice):
        # Placeholder for executing the choice
        print(f"{self.name} decides to {choice}.")
        # Implementation will depend on the choice logic
class Game:
    def __init__(self, factions, territories):
        self.factions = factions
        self.territories = territories
        self.day = 0

    def simulate_day(self):
        self.day += 1
        print(f"Day {self.day}:")
        for faction in self.factions:
            choice = faction.make_choice()
            faction.execute_choice(choice)
            # Additional logic to apply the choice effects

    def run_simulation(self, number_of_days):
        for _ in range(number_of_days):
            self.simulate_day()
            # Further logic to check for game end conditions, etc.

if __name__ == "__main__":
    sys.stdout = Logger("logs", "file")
    city = City("Gloxinia")
    falcon = Faction("Falcon",base_troops)
    lykkorice = Faction("Lykkorice",base_troops)
    red_neon = Faction("Red Neon",base_troops)
    crashers = Faction("Crashers",base_troops)
    factions = [falcon, lykkorice, red_neon, crashers]


    city.districts["Central"].add_territories("City Hall", "Purple Wedding Hotel", "Eye of Gorgon Tower", "Starscream Club")
    city.districts["Midtown"].add_territories( "Hox & Jinsy's Tavern", "Gorgon's Gut Street", "Flimsy's Curses & Trinkets","Red Barb Market")
    city.districts["Outskirts"].add_territories("Flintstone Graveyard", "Junkyard", "Docks", "Gorgon's Feet Station")
    
    
    # Collecting all territories into a single list
    # territories = []
    # for district in city.districts:
    #     territories.extend(district.territories)


    falcon.add_territory(city.districts["Central"].territories[0])
    falcon.add_territory(city.districts["Midtown"].territories[0])
    falcon.add_territory(city.districts["Outskirts"].territories[0])
    falcon.set_headquarters(city.districts["Central"].territories[0])

    crashers.add_territory(city.districts["Central"].territories[1])
    crashers.add_territory(city.districts["Midtown"].territories[1])
    crashers.add_territory(city.districts["Outskirts"].territories[1])
    crashers.set_headquarters(city.districts["Outskirts"].territories[1])

    lykkorice.add_territory(city.districts["Central"].territories[2])
    lykkorice.add_territory(city.districts["Midtown"].territories[2])
    lykkorice.add_territory(city.districts["Outskirts"].territories[2])
    lykkorice.set_headquarters(city.districts["Central"].territories[2])

    red_neon.add_territory(city.districts["Central"].territories[3])
    red_neon.add_territory(city.districts["Midtown"].territories[3])
    red_neon.add_territory(city.districts["Outskirts"].territories[3])
    red_neon.set_headquarters(city.districts["Midtown"].territories[3])
    territories = []
    game = Game(factions, territories)

    game.simulate_day()
    game.run_simulation(30)

