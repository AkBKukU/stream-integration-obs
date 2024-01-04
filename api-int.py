#!/usr/bin/python3
import sys

from os.path import dirname, basename, isfile, join
import glob
import asyncio
import importlib
from pprint import pprint

try:
    import obspython as obs
    from mods import *
    from base import *
    modules = glob.glob(join(dirname(__file__),"mods/", "*.py"))
    mod_names = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
except ModuleNotFoundError:
    print("This script is meant to be loaded by OBS only")
    modsb=dir()
    from mods import *
    modsa=dir()
    mod_names=list(set(modsb) ^ set(modsa))
    mod_names.remove("modsb")
    #sys.exit(1)

# This is a workaround for how OBS loads modules in a single interpreter
# that doesn't update them after the initial import. This can be removed
# for "release" but should hopefully be safe to be left in.
importlib.reload(api_base)
for key, mod in enumerate(mod_names):
    importlib.reload(sys.modules["mods."+mod])


actions=[]
print("Loaded Mods:")
print(mod_names)
for key, mod in enumerate(mod_names):
    actions.append(getattr(sys.modules[__name__],mod_names[key]).Mod())


def script_properties():
    props = obs.obs_properties_create()
    a=0
    for action in actions:
        print("Adding: " + action.name()+str(a)+str(action.iprint()))
        obs.obs_properties_add_group(
            props,
            action.name()+"group",
            action.name() + " Settings ",
            obs.OBS_GROUP_NORMAL,
            action.script_properties()
        )
        a+=1

    return props

def script_update(settings):
    for action in actions:
        action.script_update(settings)
