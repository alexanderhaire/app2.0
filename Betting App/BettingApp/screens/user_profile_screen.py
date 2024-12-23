from utils import Screen, BoxLayout, Button, Label
from utils.database import current_user, user_pools

class UserProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="User Profile", font_size=24))

        # Buttons for Details, Pools Generated, and Achievements
        details_button = Button(text="Details", size_hint=(1, 0.2))
        details_button.bind(on_press=self.show_details)
        layout.add_widget(details_button)

        pools_button = Button(text="Pools Generated", size_hint=(1, 0.2))
        pools_button.bind(on_press=self.show_pools)
        layout.add_widget(pools_button)

        achievements_button = Button(text="Achievements", size_hint=(1, 0.2))
        achievements_button.bind(on_press=self.show_achievements)
        layout.add_widget(achievements_button)

        # Back button to return to Home Screen
        back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        # Display area
        self.output_label = Label(text="Select an option above", font_size=18, size_hint=(1, None), height=200)
        layout.add_widget(self.output_label)

        self.add_widget(layout)

    def show_details(self, instance):
        username = current_user.get("username", "Guest")
        self.output_label.text = f"Username: {username}\nAccount Type: Standard"

    def show_pools(self, instance):
        username = current_user.get("username", "")
        pools = user_pools.get(username, [])
        if pools:
            self.output_label.text = "Pools Generated:\n" + "\n".join(pools)
        else:
            self.output_label.text = "Pools Generated:\nNo pools yet."

    def show_achievements(self, instance):
        # Dynamically fetch achievements if needed
        achievements = [
            "1. First Bet Placed",
            "2. High Roller",
            "3. Consistent Winner",
        ]
        self.output_label.text = "Achievements:\n" + "\n".join(achievements)

    def go_back_home(self, instance):
        self.manager.current = "home"
