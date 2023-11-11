from kivy.app import App
from ui.menu import MenuPrincipal

class MyApp(App):
    def build(self):
        return MenuPrincipal()
