class Walk():
    
    def __init__(self,name):
        self.name = name
    
    def walk(self):
        return "{} is walking!".format(self.name)