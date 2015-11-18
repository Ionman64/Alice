#Server Settings for Alice
#18/11/2015

import os
import keyValue

class Settings:
    def __init__(self):
        self.settings = KeyValueHandler()
        if (os.path.exists("settings.alice")):
            self.settingsFileOnDisk = True;
            with open("settings.alice", "r") as file:
                for line in file:
                    self.settings.addItem(line.split("=")[0], line.split("=")[1])
        else:
            self.settingsFileOnDisk = False;
    def getSetting(name):
        return 8888
        
        
