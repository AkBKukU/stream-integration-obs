#!/usr/bin/python3
from base.api_base import APIbase


class Mod(APIbase):
    """Simple CLI output receiver
    """

    def __init__(self):
        self.service_name = "Base"

    def receive_donate(self,from_name,amount,message):
        """Output message to CLI for donate"""
        print(from_name+" gave "+amount+" and said "+message)
        return

    def receive_interact(self,from_name,kind,message):
        """Output message to CLI for interaction"""
        print(from_name+" did "+kind+" and said "+message)
        return

    def iprint(self):
        return "Yep, it works"
