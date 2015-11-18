#KeyValue Class for Alice
#18/11/2015

class KeyValue():
    def __init__(key, value):
        self.key = key
        self.value = value
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value

class KeyValueHandler():
    def __init__():
        self.keyValues = []
    def addItem(key, value):
        self.keyValues.append(KeyValue(key, value))
