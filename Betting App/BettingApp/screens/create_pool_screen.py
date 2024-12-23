from utils import Screen, BoxLayout, TextInput, Button, Label
from utils.database import pools

class CreatePoolScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="Create a New Pool", font_size=24))

        # Input for pool name
        self.pool_name_input = TextInput(hint_text="Enter Pool Name", multiline=False)
        layout.add_widget(self.pool_name_input)

        # Input for number of participants
        self.participant_count_input = TextInput(hint_text="Enter Number of Participants", multiline=False)
        layout.add_widget(self.participant_count_input)

        # Create pool button
        create_button = Button(text="Create Pool", size_hint=(1, 0.2))
        create_button.bind(on_press=self.create_pool)
        layout.add_widget(create_button)

        # Back button
        back_button = Button(text="Back to Pool List", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Feedback message label
        self.message_label = Label(text="", font_size=16)
        layout.add_widget(self.message_label)
        self.add_widget(layout)

    def create_pool(self, instance):
        pool_name = self.pool_name_input.text.strip()
        try:
            participant_count = int(self.participant_count_input.text.strip())
            if pool_name and participant_count > 0:
                if pool_name not in pools:
                    # Add the pool to the global dictionary
                    pools[pool_name] = {
                        "participants": [f"Participant {i + 1}" for i in range(participant_count)],
                        "bets": {},
                    }
                    self.message_label.text = "Pool created successfully!"
                    # Update the pool list
                    self.manager.get_screen("pool_list").update_pool_list()
                else:
                    self.message_label.text = "Pool name already exists. Please choose another."
            else:
                self.message_label.text = "Invalid pool name or participant count."
        except ValueError:
            self.message_label.text = "Participant count must be a valid number."

    def go_back(self, instance):
        # Navigate back to the pool list screen
        self.manager.current = "pool_list"
