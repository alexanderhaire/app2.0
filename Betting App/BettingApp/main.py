from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Import all screens from the screens module
from screens import *

class BettingApp(App):
    def build(self):
        # Initialize ScreenManager
        sm = ScreenManager()

        # Add main screens
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(CreateAccountScreen(name="create"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(PoolListScreen(name="pool_list"))
        sm.add_widget(CreatePoolScreen(name="create_pool"))
        sm.add_widget(UserProfileScreen(name="profile"))
        sm.add_widget(PoolNamingScreen(name="pool_name"))
        sm.add_widget(OddsCalculatorScreen(name="odds"))

        return sm

if __name__ == "__main__":
    BettingApp().run()
