from kivy.uix.scrollview import ScrollView
from utils import Screen, BoxLayout, TextInput, Button, Label  # Import common widgets
from utils.database import user_pools, current_user, pools  # Database imports
from screens.pool_summary_screen import PoolSummaryScreen  # Import PoolSummaryScreen

class PoolNamingScreen(Screen):
    def __init__(self, pool_size=None, **kwargs):
        super().__init__(**kwargs)
        self.pool_size = pool_size or 5  # Default to 5 if no pool_size is provided
        self.participant_names = []

        # Main layout
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        self.layout.add_widget(Label(text="Name Your Participants", font_size=20))

        # Scrollable input area
        scroll_view = ScrollView(size_hint=(1, 0.7))
        input_layout = BoxLayout(orientation="vertical", size_hint_y=None)
        input_layout.bind(minimum_height=input_layout.setter("height"))
        scroll_view.add_widget(input_layout)

        # Dynamically create TextInputs for each participant
        self.name_inputs = []
        for i in range(self.pool_size):
            input_field = TextInput(hint_text=f"Participant {i + 1} Name", multiline=False)
            input_layout.add_widget(input_field)
            self.name_inputs.append(input_field)

        self.layout.add_widget(scroll_view)

        # Submit button
        submit_button = Button(text="Submit", size_hint=(1, 0.2))
        submit_button.bind(on_press=self.submit_names)
        self.layout.add_widget(submit_button)

        # Feedback label
        self.output_label = Label(text="", font_size=16)
        self.layout.add_widget(self.output_label)

        # Back button
        back_button = Button(text="Back to Pool Size", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def submit_names(self, instance):
        # Validate and collect names
        self.participant_names = [
            input_field.text.strip() or f"Participant {i + 1}" 
            for i, input_field in enumerate(self.name_inputs)
        ]

        if len(set(self.participant_names)) != len(self.participant_names):
            self.output_label.text = "Error: Participant names must be unique."
            return

        # Generate pool details
        pool_details = {name: 0 for name in self.participant_names}

        # Generate a unique pool name
        username = current_user.get("username", "Guest")
        if username not in user_pools:
            user_pools[username] = []

        pool_name = f"Pool {len(user_pools[username]) + 1}"
        user_pools[username].append(pool_name)

        # Add to global pools dictionary
        pools[pool_name] = pool_details

        # Navigate to the PoolSummaryScreen
        if not self.manager.has_screen("summary"):
            self.manager.add_widget(PoolSummaryScreen(pool_name, pool_details, name="summary"))
        self.manager.current = "summary"

    def go_back(self, instance):
        self.manager.current = "odds"
