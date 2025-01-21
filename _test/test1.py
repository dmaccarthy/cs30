"""
This program checks if the pygame, sc8pr, and Thonny software is installed.
"""

try:
    import pygame
    try: import sc8pr
    except: print("sc8pr not installed!")
except:
    from sys import version_info as v
    print(f"Python {v.major}.{v.minor}")
    print("pygame not installed!")
    print("sc8pr requires pygame!")

try:
    import thonny
    print(f"Thonny {thonny.get_version()}")
except: print("Thonny not installed!")
