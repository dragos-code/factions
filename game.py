from faction import Faction

class Game:
    def __init__(self, city):
        self.city = city
        self.day = 0
        self.factions = []
        self.territories = []
        self.attack_queue = []
    
    def add_faction(self,name):
        faction = Faction(name, self)
        self.factions.append(faction)
        return faction
    def add_district_territories(self, district_name, territory_names):
        if district_name in self.city.districts:
            self.city.districts[district_name].add_territories(*territory_names)
        else:
            print(f"District '{district_name}' does not exist in the city '{self.city.name}'.")


    def queue_attack(self, attacker, defender, territory):
        self.attack_queue.append((attacker,defender, territory))
    
    def resolve_attacks(self):
        for attack in self.attack_queue:
            attacker, defender, territory = attack;
            print(f"Resolving attack: {attacker.name} attacks {territory.name} controlled by {defender.name}")
        self.attack_queue.clear()
    def simulate_day(self):
        self.day += 1
        print(f"Day {self.day}:")
        for faction in self.factions:
            choice = faction.make_choice()
            faction.execute_choice(choice)
        self.resolve_attacks()

        for district_name, district in self.city.districts.items():
            for territory in district.territories:
                print(f"{territory.name} in {district_name} has {territory.troops} troops.")

    def run_simulation(self, number_of_days):
        for _ in range(number_of_days):
            self.simulate_day()
