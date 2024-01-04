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

actions=[]
print("Loaded Mods:")
print(mods)
for key, mod in enumerate(mods):
    actions.append(getattr(sys.modules[__name__],mods[key]).Mod())


def script_properties():
    props = obs.obs_properties_create()

    a=0
    for action in actions:
        print("Adding: " + action.name()+str(a))
        obs.obs_properties_add_group(
            props,
            action.name()+str(a),
            action.name() + " Settings "+str(a),
            obs.OBS_GROUP_NORMAL,
            action.script_properties()
        )
        obs.obs_properties_add_bool(props, "enable"+str(a), "Enable API?"+action.name())
        a+=1
    return props
