
class Restaurant:
    def __init__(self, restaurant_name, cousine_type) -> None:
        self.name = restaurant_name
        self.cuisine_type = cousine_type
    
    def describe_restaurant(self) -> str:
         print(f'{self.name} serves wonderful {self.cuisine_type}.')

    def open_restaurant(self) -> str:
        print(f'{self.name} is open. Come on in!')
