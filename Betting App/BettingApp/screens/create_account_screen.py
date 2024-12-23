from utils import Screen, BoxLayout, TextInput, Button, Label
from utils.database import user_db, user_pools

class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="Create an Account", font_size=24))
        
        self.new_username = TextInput(hint_text="New Username", multiline=False)
        self.new_password = TextInput(hint_text="New Password", password=True, multiline=False)
        layout.add_widget(self.new_username)
        layout.add_widget(self.new_password)
        
        create_button = Button(text="Create Account", size_hint=(1, 0.2))
        create_button.bind(on_press=self.create_account)
        layout.add_widget(create_button)
        
        back_button = Button(text="Back to Login", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        self.message_label = Label(text="", color=(0, 1, 0, 1))
        layout.add_widget(self.message_label)
        self.add_widget(layout)
    
    def create_account(self, instance):
        username = self.new_username.text.strip()
        password = self.new_password.text.strip()
        if username and password:
            if username not in user_db:
                user_db[username] = password
                user_pools[username] = []  # Initialize pools for new user
                self.message_label.text = "Account created successfully!"
            else:
                self.message_label.text = "Username already exists."
        else:
            self.message_label.text = "Username and password cannot be empty."
    
    def go_back(self, instance):
        self.manager.current = "login"
