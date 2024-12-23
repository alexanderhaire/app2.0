from utils import Screen, BoxLayout, TextInput, Button, Label
from utils.database import user_db, current_user, user_pools

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="Login to Betting App", font_size=24))
        
        self.username = TextInput(hint_text="Username", multiline=False)
        self.password = TextInput(hint_text="Password", password=True, multiline=False)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        
        login_button = Button(text="Login", size_hint=(1, 0.2))
        login_button.bind(on_press=self.validate_login)
        layout.add_widget(login_button)
        
        create_account_button = Button(text="Create Account", size_hint=(1, 0.2))
        create_account_button.bind(on_press=self.go_to_create)
        layout.add_widget(create_account_button)
        
        self.error_label = Label(text="", color=(1, 0, 0, 1))
        layout.add_widget(self.error_label)
        self.add_widget(layout)
    
    def validate_login(self, instance):
        if self.username.text in user_db and self.password.text == user_db[self.username.text]:
            current_user["username"] = self.username.text
            if self.username.text not in user_pools:
                user_pools[self.username.text] = []  # Initialize user pools
            self.manager.current = "home"
        else:
            self.error_label.text = "Invalid username or password."
    
    def go_to_create(self, instance):
        self.manager.current = "create"
