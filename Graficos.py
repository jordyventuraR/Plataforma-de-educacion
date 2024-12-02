from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
Builder.load_file('mi.kv')


class NuevoPassword(Screen):
    def on_aceptCambios_button_press(self):
        print("Presiono el nuevo password")
        self.manager.current = "LoginScreen"

class RecuperacionPassword(Screen):
    def on_recpass_button_press(self):
        print("Presiono el recuperar password")
        self.manager.current = "NuevoPassword"


class Registro(Screen):
    def on_register_button_press(self):
        print("Presiono el aceptar cambios")
        self.manager.current = "DashBoard"

class DashBoard(Screen):
    pass
    
class LoginScreen(Screen):
    def login_press(self):
        print("Presiono el login")
        self.manager.current = "RecuperacionPassword"
        
    def sigin_press(self):
        print("Presiono el sigin")
        self.manager.current = "DashBoard"
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="LoginScreen"))
        sm.add_widget(DashBoard(name="DashBoard"))
        sm.add_widget(Registro(name="Registro"))
        sm.add_widget(RecuperacionPassword(name="RecuperacionPassword"))
        sm.add_widget(NuevoPassword(name="NuevoPassword"))
        sm.current = "LoginScreen"  # Pantalla inicial
        return sm

if __name__ == '__main__':
    MyApp().run()
