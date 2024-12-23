from utils import Screen, BoxLayout, Button, Label
from kivy.uix.scrollview import ScrollView
from utils.database import pools
from screens.betting_screen import BettingScreen

class PoolListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        self.layout.add_widget(Label(text="Available Pools", font_size=24))

        # Scrollable area for pool buttons
        scroll_view = ScrollView(size_hint=(1, 0.7))
        self.pool_buttons = BoxLayout(orientation="vertical", size_hint_y=None)
        self.pool_buttons.bind(minimum_height=self.pool_buttons.setter("height"))
        scroll_view.add_widget(self.pool_buttons)
        self.layout.add_widget(scroll_view)

        # Button to create a new pool
        create_pool_button = Button(text="Create New Pool", size_hint=(1, 0.2))
        create_pool_button.bind(on_press=self.go_to_create_pool)
        self.layout.add_widget(create_pool_button)

        # Back to home button
        back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back_home)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)
        self.update_pool_list()

    def update_pool_list(self):
        """
        Clear and refresh the list of pools displayed.
        """
        self.pool_buttons.clear_widgets()
        for pool_name in pools:
            button = Button(text=pool_name, size_hint=(1, None), height=40)
            # Bind the button to navigate to the pool's BettingScreen
            button.bind(on_press=lambda instance, pool=pool_name: self.join_pool(pool))
            self.pool_buttons.add_widget(button)

    def join_pool(self, pool_name):
        """
        Navigate to the BettingScreen for the selected pool.
        """
        # Check if the BettingScreen for this pool already exists
        if not self.manager.has_screen(f"bet_{pool_name}"):
            self.manager.add_widget(BettingScreen(pool_name, name=f"bet_{pool_name}"))
        # Navigate to the BettingScreen
        self.manager.current = f"bet_{pool_name}"

    def go_to_create_pool(self, instance):
        """
        Navigate to the screen for creating a new pool.
        """
        self.manager.current = "create_pool"

    def go_back_home(self, instance):
        """
        Navigate back to the home screen.
        """
        self.manager.current = "home"
