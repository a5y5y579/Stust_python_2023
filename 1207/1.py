class Sports:
    
    def water(self):
        print("AT THE WATER.")
    
    def land(self):
        print("AT THE LAND.")

class water(Sports):

    def Pool(self):
        print("In the pool.")
    
    def Sea(self):
        print("In the sea.")

class land(Sports):

    def Ball(self):
        print("Use Ball.")
    
    def NBall(self):
        print("Not Use Ball.")

scoer = land()
scoer.Ball()
