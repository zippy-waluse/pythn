class Drum:
    def __init__(self, material, size):
        self.material=material
        self.size=size
    def display_property(self):
        print(f"{self.material}, {self.size}")
class Djembe(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)
    def make_sound(self):
        print("tiii")
class TalkingDrum(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)
    def make_sound(self):
        print("Mamaa")
class Bouragbou(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)
    def make_sound(self):
        print("pee pee")
djembe= Djembe("polein", 60.00)
talking_drum=TalkingDrum("cotton", 40.23)
bouragbou=Bouragbou("snakeskin",55.5)

print(f"{djembe.make_sound} {talking_drum.make_sound} {bouragbou.make_sound}")
   


