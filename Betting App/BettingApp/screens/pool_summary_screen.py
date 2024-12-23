from utils import Screen, BoxLayout, Button, Label
from kivy.uix.scrollview import ScrollView
from utils.database import pools
from screens.betting_screen import BettingScreen

class PoolSummaryScreen(Screen):
    def __init__(self, pool_name, pool_details, **kwargs):
        super().__init__(**kwargs)
        self.pool_name = pool_name
        self.pool_details = pool_details

        # Ensure participants and bets exist
        self.pool_details.setdefault("participants", [])
        self.pool_details.setdefault("bets", {})

        # Main layout
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text=f"Pool Summary: {self.pool_name}", font_size=24))

        # Scrollable area for participants and bets
        scroll_view = ScrollView(size_hint=(1, 0.7))
        participants_layout = BoxLayout(orientation="vertical", size_hint_y=None)
        participants_layout.bind(minimum_height=participants_layout.setter("height"))
        scroll_view.add_widget(participants_layout)

        # Add participants and their bets to the scrollable layout
        for participant, amount in self.pool_details["bets"].items():
            participants_layout.add_widget(
                Label(text=f"{participant}: ${amount:.2f}", font_size=18)
            )

        layout.add_widget(scroll_view)

        # Place Bets button
        bet_button = Button(text="Place Bets", size_hint=(1, 0.2))
        bet_button.bind(on_press=self.go_to_betting)
        layout.add_widget(bet_button)

        # Back to Home button
        back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_betting(self, instance):
        """
        Navigate to the BettingScreen with the current pool's name.
        """
        # Add the BettingScreen for this pool name if it doesn't already exist
        screen_name = f"bet_{self.pool_name}"
        if not self.manager.has_screen(screen_name):
            self.manager.add_widget(BettingScreen(self.pool_name, name=screen_name))
        self.manager.current = screen_name

    def go_back_home(self, instance):
        """
        Navigate back to the HomeScreen.
        """
        self.manager.current = "home"
