"""
Tuxemon starting module for Tuxemon Launcher.

It requires 2 original folders: "tuxemon" (main engine) and "mods" (Content)
"""
from tuxemon.core import prepare, main

def StartTuxemon(mods=None, starting_map=None, slot=None):
    """Usage: StartTuxemon(mods="tuxemon", starting_map="player_house_bedroom.tmx", slot=False)
    Start the game from a specified path.
    If mods is not in mods folder, or it's other type than str, it will be ignored, the same is for starting_map."""
    
    '''parser = ArgumentParser()
    parser.add_argument('-m', '--mod', dest='mod', metavar='mymod', type=str, nargs='?',
                        default=None, help='The mod directory used in the mods directory')
    parser.add_argument('-l', '--load', dest='slot', metavar='1,2,3', type=int, nargs='?',
                        default=None, help='The index of the save file to load')
    parser.add_argument('-s', '--starting-map', dest='starting_map', metavar='map.tmx', type=str, nargs='?',
                        default=None, help='The starting map')
    args = parser.parse_args()'''
    
    if type(mods) == str:
        prepare.CONFIG.mods.insert(0, mods)
    if type(starting_map) == str:
        prepare.CONFIG.starting_map = starting_map
    
    main.main(load_slot=slot)
    