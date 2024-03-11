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