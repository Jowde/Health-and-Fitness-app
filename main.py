from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import os 

Window.clearcolor = (1, 1, 1, 1)
class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation = "vertical")
        
        text_input = TextInput(background_color = "white", 
                                  foreground_color="white", 
                                  multiline = False, 
                                  halign="right")
        
        
        c_layout = BoxLayout()
        text_label =  Label(text="Age",font_color = 'black')
        c_layout.add_widget(text_label)
        c_layout.add_widget(text_input)
        main_layout.add_widget(c_layout)
        
        c_layout = BoxLayout()
        text_label =  Label(text="Height")
        c_layout.add_widget(text_label)
        text_input = TextInput(background_color = "black", 
                                  foreground_color="white", 
                                  multiline = False, 
                                  halign="right")
        c_layout.add_widget(text_input)
        main_layout.add_widget(c_layout)
        
        c_layout = BoxLayout()
        text_label =  Label(text="Weight")
        c_layout.add_widget(text_label)
        text_input = TextInput(background_color = "black", 
                                  foreground_color="white", 
                                  multiline = False, 
                                  halign="right")
        c_layout.add_widget(text_input)
        main_layout.add_widget(c_layout)
        
        return main_layout
    
if __name__ == "__main__":
    app = MainApp()
    app.run()       