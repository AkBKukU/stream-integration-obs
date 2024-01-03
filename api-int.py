#!/usr/bin/python3
import sys

from os.path import dirname, basename, isfile, join
import glob
import asyncio

try:
    import obspython as obs
    from mods import *
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






print("Loaded Mods:")
print(mods)
temp = getattr(sys.modules[__name__],mods[mods.index("output_base")]).OUTBase()
temp.iprint()
