"""
Tuxemon Launcher (concept/early alpha)
This script currently only asks for mods and map, and starts the game.
"""

from config.get_config import Get_exec_path
from backend.StartTuxemon import StartTuxemon

# Ask for some options (maps, map and save)

want_mods = input("Do you want to use mods? (True/False): ")
if want_mods == "True":
    mod = input("Please enter mod name: ")
    want_mods = True
else:
    mod = None

want_map = input("Do you want to use different starting map? (True/False): ")
if want_map == "True":
    map = input("Enter map filename (must contain \".tmx\" extension at the end): ")
    want_map = True
else:
    map = None


#Start Tuxemon
StartTuxemon(mods=mod, starting_map=map)
