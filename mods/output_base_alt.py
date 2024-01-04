#!/usr/bin/python3
from base.api_base import APIbase

try:
    import obspython as obs
except ModuleNotFoundError:
    print("This script is meant to be loaded by OBS only")

class Mod(APIbase):
    """Simple CLI output receiver
    """

    def __init__(self):
        super().__init__()
        self.service_name = "Base Alt"

    def receive_donate(self,from_name,amount,message):
        """Output message to CLI for donate"""
        print(from_name+" gave "+amount+" and said "+message)
        return

    def receive_interact(self,from_name,kind,message):
        """Output message to CLI for interaction"""
        print(from_name+" did "+kind+" and said "+message)
        return

    def iprint(self):
        return "This is the alt one"

    def script_properties(self):
        self.props_service = obs.obs_properties_create()
        obs.obs_properties_add_bool(self.props_service, self.service_name+"enable", "Enable "+self.service_name+" API?")
        self.props_service = self.prop_apikeys(self.props_service)

        # Hide/Show API Keys
        # TODO - This requires a reload of the script and is not proper
        p=obs.obs_properties_get(self.props_service, self.service_name+"client_id")
        obs.obs_property_set_visible(p,self.gui_apienable)
        p=obs.obs_properties_get(self.props_service, self.service_name+"client_secret")
        obs.obs_property_set_visible(p,self.gui_apienable)
        p=obs.obs_properties_get(self.props_service, self.service_name+"connect")
        obs.obs_property_set_visible(p,self.gui_apienable)
        return self.props_service
