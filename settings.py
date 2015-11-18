#Server Settings for Alice
#18/11/2015

import os
from keyValue import KeyValueHandler, KeyValue

class Settings:
    def __init__(self):
        self.settings = KeyValueHandler()
        if (os.path.exists("settings.alice")):
            self.settingsFileOnDisk = True;
            self.load()
        else:
            self.settingsFileOnDisk = False;
            self.createFile()
    def load(self):
       if (self.settingsFileOnDisk):
          
           with open("settings.alice", "r") as file:
                for line in file:
                    if ("#" in line):
                        continue
                    self.settings.addItem(line.split("=")[0], line.split("=")[1])

           
    def createFile(self):
        print("Creating settings file")
        if (self.settingsFileOnDisk == False):
            with open("settings.alice", "w") as file:
                file.write("#Alice Settings\n")
                file.write("portNum=8888\n")
            self.load()
        print("Settings file Created")
    def getSetting(self, name):
        return self.settings.getItem(name)
        
        
