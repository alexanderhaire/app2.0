from utils import Screen, BoxLayout, Button, Label

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="Welcome!", font_size=24))
        
        create_pool_button = Button(text="Create Pool", size_hint=(1, 0.2))
        create_pool_button.bind(on_press=self.go_to_pool_name)
        layout.add_widget(create_pool_button)
        
        user_profile_button = Button(text="Go to User Profile", size_hint=(1, 0.2))
        user_profile_button.bind(on_press=self.go_to_user_profile)
        layout.add_widget(user_profile_button)
        
        self.add_widget(layout)
    
    def go_to_pool_name(self, instance):
        # Navigate to the pool naming screen
        self.manager.current = "pool_name"
    
    def go_to_user_profile(self, instance):
        # Navigate to the user profile screen
        self.manager.current = "profile"
