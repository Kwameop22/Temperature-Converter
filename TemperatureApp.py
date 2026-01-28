from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

class TemperatureBoxLayout(BoxLayout):
    text=StringProperty("Your results will appear here")
    def button(self):
        #print("Button clicked")
        try:
            number = float(self.ids.textinput.text)


            answer = round((number - 32) / 1.8,2)
            self.text = f"CELSIUS  :  {str(answer)}°C"
        except ValueError:
            self.text="ENTER A VALUE"

    def button2(self):
        #print("Button pressed")
        try:
            number = float(self.ids.textinput.text)
            answer = round((number * 1.8) + 32, 2)
            self.text = f"FAHRENHEIT  :  {str(answer)}°F"
        except ValueError:
            self.text="ENTER A VALUE"

    def button3(self):
        print("Button")
        try:
            number = float(self.ids.textinput.text)
            answer = round(number+ 273.15)
            answer2 = round(((number - 32)/1.8)+273.15,2)

            self.text = f"KELVIN  :  {str(answer)}K"
        except ValueError:
            self.text = "ENTER A VALUE"

    def button4(self):
        try:
            number = float(self.ids.textinput.text)
            answer = round(((number - 32)/1.8)+273.15,2)
            self.text = f"KELVIN  :  {str(answer)}K"
        except ValueError:
            self.text="ENTER A VALUE"


class TemperatureApp(App):
    pass

if __name__=="__main__":
    TemperatureApp().run()

