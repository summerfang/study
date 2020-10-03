class Temperature:
    def __init__(self):
        self.temp = 50
        
    def get_temperature(self):
        return self.temp
    
    def set_temperature(self, temperature):
        self.temp = temperature

class TemperatureMgr:
    def __init__(self,t):
        self.temperature = t
        
    def get_temperature(self):
        return self.temperature.get_temperature()

    def set_temperature(self, temperature):
        self.temperature.set_temperature(temperature)
        
class CelsiusTemperatureView:
    def __init__(self, tm):
        self.temperature_manager = tm
        
    def print(self):
        print("Celsius: " + str(self.temperature_manager.get_temperature()))
        
class FahrenheitTemperatureView:
    def __init__(self, tm):
        self.temperature_manager = tm
        
    def print(self):
        print("Fahrenheit: " + str(self.temperature_manager.get_temperature()*9/5+32))

t = Temperature()
tm = TemperatureMgr(t)

dc = CelsiusTemperatureView(tm)
dc.print()

tm.set_temperature(0)

df = FahrenheitTemperatureView(tm)
df.print()
dc.print()
