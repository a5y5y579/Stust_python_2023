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

class Sports:
    def __init__(self, name):
        self._name = name

    @property
    def sports_name(self):
        return self._name

    @sports_name.setter
    def sports_name(self, value):
        self._name = value

class LandSports(Sports):
    def __init__(self, name, field):
        super().__init__(name)
        self._field = field

    @property
    def landsports_field(self):
        return self._field


class WaterSports(Sports):
    def __init__(self, name, activity):
        super().__init__(name)
        self._activity = activity

    @property
    def watersports_activity(self):
        return self._activity


# Example of usage
if __name__ == "__main__":
   
    baseball = LandSports("baseball", "baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)

    water_skiing = WaterSports("Water Skiing", "Strap on your skis and fly across the water")
    print(water_skiing.sports_name)
    print(water_skiing.watersports_activity)
