from enum import Enum
import random

class Action(Enum):
    ATTACK = "attack"
    DEFEND = "defend"
    HOLD = "hold"
    ASK_FOR_HELP = "ask for help"

class Faction:
    def __init__(self, name,total_troops,game):
        self.name = name
        self.total_troops = total_troops
        self.territories = {}
        self.headquarters = None
        self.game = game
        print(f"Created faction {self.name}")

    def add_territory(self, territory):
        print(f"added {territory.name} from {territory.district.name} to{self.name} in {territory.district.city.name}")
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
            print(f"Headquarters set at {self.headquarters.name} for {self.name} faction")
        else:
            print(f"Territory {territory.name} is not controlled by {self.name}. Cannot set as headquarters.")
    def make_choice(self):
        chosen =random.choice(list(Action))
        print(f"Faction {self.name} decided to make {chosen.value} choice" )
        return chosen
    
    def execute_choice(self, choice):
        # Mapping of choices to faction methods
        action_map = {
            Action.ATTACK: self._attack,
            Action.DEFEND: self._defend,
            Action.HOLD: self._hold,
            Action.ASK_FOR_HELP: self._ask_for_help,
        }
        
        # Get the method based on the choice and call it
        action_method = action_map.get(choice)
        if action_method:
            action_method()
        else:
            print(f"Invalid choice: {choice}")

    def _attack(self):
        # Select a target faction that is not this faction
        target_faction = random.choice([f for f in self.game.factions if f != self])
        # Select a random territory from the target faction
        if target_faction.territories:
            target_territory = random.choice(list(target_faction.territories.keys()))
            print(f"{self.name} decides to ATTACK {target_territory.name} controlled by {target_faction.name}.")
            # Here, you'd add logic to queue up this attack for resolution at the end of the day
            self.game.queue_attack(self, target_faction, target_territory)
        else:
            print(f"{self.name} attempts to ATTACK, but {target_faction.name} has no territories to target.")

    def _defend(self):
        # Check if this faction controls any territories
        if self.territories:
            # Select a random territory from this faction's own territories
            own_territory = random.choice(list(self.territories.keys()))
            print(f"{self.name} decides to DEFEND {own_territory.name}.")
            # Here, you'd add logic to increase the defense of this territory
            # This could involve adding troops, improving fortifications, etc.
            # For example, you could simulate adding troops by increasing the troop count
            # own_territory.troops += some_value
        else:
            print(f"{self.name} has no territories to defend.")

    def _hold(self):
        if self.headquarters is not None:
            total_redeployed_troops = 0
            for territory in self.territories.values():
                if territory != self.headquarters:
                    # Assume each territory has a 'troops' attribute indicating the number of troops present
                    total_redeployed_troops += territory.troops
                    # Reset troops in current territory as they are moved to HQ
                    territory.troops = 0
            # Add all redeployed troops to headquarters
            self.headquarters.troops += total_redeployed_troops
            print(f"{self.name} consolidates forces, redeploying {total_redeployed_troops} troops to HQ at {self.headquarters.name}.")
        else:
            print(f"{self.name} does not have a headquarters set. Cannot redeploy troops.")

    def _ask_for_help(self):
        # Implementation of ask for help action
        print(f"{self.name} decides to ASK FOR HELP.")