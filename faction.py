from enum import Enum
import random

class Action(Enum):
    ATTACK = "attack"
    DEFEND = "defend"
    HOLD = "hold"
    ASK_FOR_HELP = "ask for help"

class Faction:
    def __init__(self, name,game):
        self.name = name
        self.territories = {}
        self.headquarters = None
        self.game = game
        print(f"Created faction {self.name}")

    def add_territory(self, territory):
        print(f"added {territory.name} from {territory.district.name} to{self.name} in {territory.district.city.name}")
        territory.controlled_by = self
        self.territories[territory] = territory

    def set_headquarters(self, territory, total_troops):
        if self.headquarters is not None:
            print(f"Headquarters already set at {self.headquarters.name}. Cannot reassign headquarters.")
            return
        if territory in self.territories:
            self.headquarters = self.territories[territory]
            self.headquarters.troops = total_troops
            print(f"Headquarters set at {self.headquarters.name} for {self.name} faction")
        else:
            print(f"Territory {territory.name} is not controlled by {self.name}. Cannot set as headquarters.")
    def make_choice(self):
        chosen =random.choice(list(Action))
        print(f"Faction {self.name} decided to make {chosen.value} choice" )
        if chosen == Action.DEFEND and len(self.territories) == 1 and self.headquarters in self.territories.value():
            chosen = Action.HOLD
        return chosen
    
    def execute_choice(self, choice):
        action_map = {
            Action.ATTACK: self._attack,
            Action.DEFEND: self._defend,
            Action.HOLD: self._hold,
            Action.ASK_FOR_HELP: self._ask_for_help,
        }
        
        action_method = action_map.get(choice)
        if action_method:
            action_method()
        else:
            print(f"Invalid choice: {choice}")

    def _attack(self):
        if not self.headquarters:
            print(f"{self.name} has no headquarters to deploy troops from")
            return
        
        target_faction = random.choice([f for f in self.game.factions if f != self])
        if target_faction.territories:
            target_territory = random.choice(list(target_faction.territories.keys()))
            troops_to_commit  =self.headquarters.troops // 3
            
            if troops_to_commit > 0:
                print(f"{self.name} decides to ATTACK {target_territory.name} with {troops_to_commit} troops, controlled by {target_faction.name}")
                self.headquarters.troops -= troops_to_commit
                target_territory.troops += troops_to_commit 
                self.game.queue_attack(self, target_faction, target_territory)
            else:
                print(f"{self.name} does not have enough troops in HQ to launch an attack.")
        else:
            print(f"{self.name} attempts to ATTACK, but {target_faction.name} has no territories to target.")


    def _defend(self):
        if not self.headquarters:
            print(f"{self.name} has no headquarters to deploy troops from")
            return

        territories_to_defend = [t for t in self.territories.keys() if t != self.headquarters]
        if self.territories:
            chosen_territory = random.choice(territories_to_defend)
            troops_to_commit = self.headquarters.troops // 3
            if troops_to_commit > 0:
                print(f"{self.name} decides to DEFEND {chosen_territory.name} with {troops_to_commit} troops.")
                self.headquarters.troops -= troops_to_commit
                chosen_territory.troops += troops_to_commit
            else:
                print(f"{self.name} does not have enough troops in HQ to defend a territory.")               
        else:
            print(f"{self.name} has no territories to defend.")

    def _hold(self):
        if self.headquarters is not None:
            total_redeployed_troops = 0
            for territory in self.territories.values():
                if territory != self.headquarters:
                    total_redeployed_troops += territory.troops
                    territory.troops = 0
            self.headquarters.troops += total_redeployed_troops
            print(f"{self.name} consolidates forces, redeploying {self.headquarters.troops} troops to HQ at {self.headquarters.name}.")
        else:
            print(f"{self.name} does not have a headquarters set. Cannot redeploy troops.")

    def _ask_for_help(self):
        print(f"{self.name} decides to ASK FOR HELP.")
