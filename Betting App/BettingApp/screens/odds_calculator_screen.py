from utils import Screen, BoxLayout, Button, Label, TextInput
from screens.pool_naming_screen import PoolNamingScreen

class OddsCalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="Enter Pool Size", font_size=20))

        # Input for defining the number of participants in the pool
        self.pool_size_input = TextInput(hint_text="Enter number of participants (e.g., 5)", multiline=False)
        layout.add_widget(self.pool_size_input)

        # Button to proceed to the naming screen
        next_button = Button(text="Next", size_hint=(1, 0.2))
        next_button.bind(on_press=self.proceed_to_naming)
        layout.add_widget(next_button)

        # Back to Home button
        back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        # Output message for validation feedback
        self.output = Label(text="", font_size=18)
        layout.add_widget(self.output)

        self.add_widget(layout)

    def proceed_to_naming(self, instance):
        try:
            pool_size = int(self.pool_size_input.text)
            if pool_size <= 0:
                raise ValueError("Pool size must be greater than 0.")
            # Go to the PoolNamingScreen with the specified pool size
            self.manager.add_widget(PoolNamingScreen(pool_size, name="naming"))
            self.manager.current = "naming"
        except ValueError as e:
            # Display error message for invalid input
            self.output.text = f"Error: {str(e)}"
            self.pool_size_input.text = ""  # Clear the input field for better usability

    def go_back_home(self, instance):
        self.manager.current = "home"
