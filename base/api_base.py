#!/usr/bin/python3

import sys, os
import asyncio
from datetime import datetime
try:
    import obspython as obs
except ModuleNotFoundError:
    print("This script is meant to be loaded by OBS only")

class APIbase(object):
    """API Base for signal emitters

    Manages loading API keys, logging, and registering signal recievers
    """

    def __init__(self,key_path=None,log=False):
        """Init with file path"""
        self.service_name = "Base"
        self.gui_apienable = False
        self.client_id = None
        self.client_secret = None
        self.callbacks_donate=[]
        self.callbacks_interact=[]

    def log(self,filename,text):
        """logging output for data"""
        log_path="log/"+self.service_name
        # Make log dir if not there
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        # Build filename
        filepath=log_path+"/"+str(datetime.now().isoformat()).replace(":","-")+"_"+filename+".log"
        # Write data
        with open(filepath, 'w', encoding="utf-8") as output:
            output.write(text)
        return

    def name(self):
        """Return name of service"""
        return self.service_name

    def connect(self):
        """Dummy service connection"""
        print("No service to connect to.")
        return

    def disconnect(self):
        """Dummy service disconnect"""
        print("No service to disconnect from.")
        return

    def script_properties(self):
        self.props_service = obs.obs_properties_create()
        obs.obs_properties_add_bool(self.props_service, self.service_name+"enable", "Enable "+self.service_name+" API?")
        return self.props_service

    def prop_apikeys(self,props):
        obs.obs_properties_add_text(props,self.service_name+"client_id", "Client ID",obs.OBS_TEXT_PASSWORD)
        obs.obs_properties_add_text(props,self.service_name+"client_secret", "Client Secret",obs.OBS_TEXT_PASSWORD)
        obs.obs_properties_add_bool(self.props_service, self.service_name+"connect", "Connect to API?")
        return props

    def script_update(self,settings):
        self.gui_apienable = obs.obs_data_get_bool(settings, self.service_name+"enable")

    def register_donate(self,callback):
        """Store callback receiver for donation"""
        self.callbacks_donate.append(callback)
        return

    def emit_donate(self,from_name,amount,message):
        """Call stored receivers for donation"""
        for callback in self.callbacks_donate:
            callback(from_name,amount,message)
        return

    def register_interact(self,callback):
        """Store callback receiver for interation"""
        print("register_interact")
        self.callbacks_interact.append(callback)
        return

    def emit_interact(self,from_name,kind,message):
        """Call stored receivers for interaction"""
        for callback in self.callbacks_interact:
            callback(from_name,kind,message)
        return

    def receive_donate(self,from_name,amount,message):
        """Output message to CLI for donate"""
        print(from_name+" gave "+amount+" and said "+message)
        return

    def receive_interact(self,from_name,kind,message):
        """Output message to CLI for interaction"""
        print(from_name+" did "+kind+" and said "+message)
        return
