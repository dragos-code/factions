import sys
from logger import Logger
import sys
from game import Game
from city import City

base_troops = 60
city = City("Gloxinia")

sys.stdout = Logger("logs", "file")
game = Game(city)
falcon = game.add_faction("Falcon")
lykkorice = game.add_faction("Lykkorice")
red_neon = game.add_faction("Red Neon")
crashers = game.add_faction("Crashers")


game.city.districts["Central"].add_territories("City Hall", "Purple Wedding Hotel", "Eye of Gorgon Tower", "Starscream Club")
game.city.districts["Midtown"].add_territories( "Hox & Jinsy's Tavern", "Gorgon's Gut Street", "Flimsy's Curses & Trinkets","Red Barb Market")
game.city.districts["Outskirts"].add_territories("Flintstone Graveyard", "Junkyard", "Docks", "Gorgon's Feet Station")


falcon.add_territory(game.city.districts["Central"].territories[0])
falcon.add_territory(game.city.districts["Midtown"].territories[0])
falcon.add_territory(game.city.districts["Outskirts"].territories[0])
falcon.set_headquarters(game.city.districts["Central"].territories[0],base_troops)

crashers.add_territory(game.city.districts["Central"].territories[1])
crashers.add_territory(game.city.districts["Midtown"].territories[1])
crashers.add_territory(game.city.districts["Outskirts"].territories[1])
crashers.set_headquarters(game.city.districts["Outskirts"].territories[1],base_troops)

lykkorice.add_territory(game.city.districts["Central"].territories[2])
lykkorice.add_territory(game.city.districts["Midtown"].territories[2])
lykkorice.add_territory(game.city.districts["Outskirts"].territories[2])
lykkorice.set_headquarters(game.city.districts["Central"].territories[2],base_troops)

red_neon.add_territory(game.city.districts["Central"].territories[3])
red_neon.add_territory(game.city.districts["Midtown"].territories[3])
red_neon.add_territory(game.city.districts["Outskirts"].territories[3])
red_neon.set_headquarters(game.city.districts["Midtown"].territories[3],base_troops)


game.simulate_day()
game.run_simulation(5)

