from utils import Screen, BoxLayout, Button, Label, TextInput
from utils.database import pools
from utils.helpers import calculate_odds
from kivy.uix.scrollview import ScrollView

class BettingScreen(Screen):
    def __init__(self, pool_name, **kwargs):
        super().__init__(**kwargs)
        self.pool_name = pool_name
        self.pool_details = pools.get(pool_name, {})

        # Ensure the pool details contain "participants"
        if "participants" not in self.pool_details:
            self.pool_details["participants"] = []

        # Main layout with scrollable content
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text=f"Place Bets for {pool_name}", font_size=24))

        scroll_view = ScrollView(size_hint=(1, 0.7))
        self.bet_inputs = BoxLayout(orientation="vertical", size_hint_y=None)
        self.bet_inputs.bind(minimum_height=self.bet_inputs.setter("height"))
        scroll_view.add_widget(self.bet_inputs)

        # Dynamically add participant labels and TextInput fields for bets
        self.bets = {}  # Store bets for participants
        for participant in self.pool_details["participants"]:
            participant_label = Label(text=f"Bet on {participant} ($):", font_size=18)
            bet_input = TextInput(hint_text="Enter bet amount", multiline=False)
            self.bet_inputs.add_widget(participant_label)
            self.bet_inputs.add_widget(bet_input)
            self.bets[participant] = bet_input

        layout.add_widget(scroll_view)

        # Submit button
        submit_button = Button(text="Submit Bets", size_hint=(1, 0.2))
        submit_button.bind(on_press=self.submit_bets)
        layout.add_widget(submit_button)

        # Labels for pool details
        self.output_label = Label(text="")
        layout.add_widget(self.output_label)

        self.total_money_label = Label(text="Total Money in Pool: $0")
        layout.add_widget(self.total_money_label)

        self.odds_label = Label(text="Odds Multiplier: N/A")
        layout.add_widget(self.odds_label)

        # Back button
        back_button = Button(text="Back to Pool List", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_bets(self, instance):
        try:
            total_bets = 0
            new_bets = {}

            # Validate and collect bets
            for participant, input_field in self.bets.items():
                bet = float(input_field.text.strip() or 0)
                if bet < 0:
                    raise ValueError("Bets cannot be negative.")
                new_bets[participant] = bet
                total_bets += bet

            if total_bets == 0:
                raise ValueError("At least one bet is required.")

            # Update pool's bet details
            if "bets" not in self.pool_details:
                self.pool_details["bets"] = {}
            self.pool_details["bets"].update(new_bets)

            # Calculate total pool money and odds
            total_pool = sum(self.pool_details["bets"].values())
            self.total_money_label.text = f"Total Money in Pool: ${total_pool:.2f}"

            odds = calculate_odds(self.pool_details["bets"])
            odds_text = "\n".join([f"{k}: {v}" for k, v in odds.items()])
            self.odds_label.text = f"Odds Multiplier:\n{odds_text}"

            self.output_label.text = "Bets placed successfully!"
        except ValueError as e:
            self.output_label.text = f"Error: {str(e)}"

    def go_back(self, instance):
        self.manager.current = "pool_list"
