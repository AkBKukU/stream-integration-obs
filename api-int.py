#!/usr/bin/python3
import sys

from os.path import dirname, basename, isfile, join
import glob

try:
    import obspython as obs
    modules = glob.glob(join(dirname(__file__),"mods/", "*.py"))
    mods = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
except ModuleNotFoundError:
    print("This script is meant to be loaded by OBS only")
    modsb=dir()
    from mods import *
    modsa=dir()
    mods=list(set(modsb) ^ set(modsa))
    mods.remove("modsb")
    #sys.exit(1)

# Production Imports
#from stream.api_twitch import APItwitch

# Test Imports
#from stream.api_twitch_test import APItwitchTest as APItwitch
#from stream.output_base import OUTBase as OUTDectalk

import asyncio



print("Loaded Mods:")
print(mods)
#temp = mods.output_base.OUTBase()
#temp.iprint()
