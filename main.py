class vehicles:
    def __init__(self,name,fuel,topspeed):
        self.name=name
        self.fuel=fuel
        self.topspeed=topspeed
    def details(self):
        print("Vehicle name is :",self.name)
        print("Vehicle fuel type is: ",self.fuel)
        print("Vehicle topspeed is :",self.topspeed)
class car(vehicles):
    def __init__(self, name, fuel, topspeed,enginecapacity):
        super().__init__(name, fuel, topspeed)
        self.enginecapacity=enginecapacity
    def  wheels(self):
        print("Cars have four wheels.")
        print("It depends on model of car whether it is two wheel drive or fourwheel drive.")
    def details(self):
        super().details()
        print("Engine capacity of car is ",self.enginecapacity)
class bikes(vehicles):
    def __init__(self,name,fuel,topspeed,engine):
        super().__init__(name,fuel,topspeed)
        self.engine=engine
    def wheel(self):
        print("bikes have two wheels")
    def details(self):
        super().details()
        print("Engine capacity of bike is ",self.engine)
class trucks(vehicles):
    def __init__(self,name,fuel,topspeed,load):
        super().__init__(name,fuel,topspeed)
        self.load=load
    def wheels(self):
        print("wheels on trucks generally depends upon the load they are carrying.")
    def details(self):
        super().details()
        print("Load capacity of the truck is",self.load)
harrier=car("TATA HARRIER","diesel","200 km/hr","2000cc")
harrier.details()
harrier.wheels()
pulsar=bikes("BAJAJ PULSAR","petrol","130km/hr","200cc")
pulsar.details()
pulsar.wheel()
bharatbenz=trucks("BHARAT BENZ","diesel","100km/hr","two to three tons")
bharatbenz.details()
bharatbenz.wheels()


