class LasagneLaskuri:
    def __init__(self):
        self.lasagne_portions = 1
        self.grams_per_portion = 1000
        self.calories_per_portion = 1320
        self.price_per_portion = 3.75

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    key, value = line.strip().split(': ')
                    if key == 'lasagne_portions':
                        self.lasagne_portions = int(value)
                    elif key == 'grams_per_portion':
                        self.grams_per_portion = int(value)
                    elif key == 'calories_per_portion':
                        self.calories_per_portion = int(value)
                    elif key == 'price_per_portion':
                        self.price_per_portion = float(value)
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")
        except ValueError:
            print("Tiedostossa on virheellistä dataa.")
        self.calculate_totals()

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(f"lasagne_portions: {self.lasagne_portions}\n")
            file.write(f"grams_per_portion: {self.grams_per_portion}\n")
            file.write(f"calories_per_portion: {self.calories_per_portion}\n")
            file.write(f"price_per_portion: {self.price_per_portion}\n")

    def add_lasagne_portion(self, additional_portions):
        self.lasagne_portions += additional_portions
        self.calculate_totals()

    def calculate_totals(self):
        self.total_grams = self.lasagne_portions * self.grams_per_portion
        self.total_calories = self.lasagne_portions * self.calories_per_portion
        self.total_price = self.lasagne_portions * self.price_per_portion

    def get_totals(self):
        return {
            'lasagne_portions': self.lasagne_portions,
            'total_grams': self.total_grams,
            'total_calories': self.total_calories,
            'total_price': self.total_price
        }

# Example usage:
# laskuri = LasagneLaskuri()
# laskuri.load_from_file("lasagne.txt")
# laskuri.add_lasagne_portion(1)
# laskuri.save_to_file("lasagne.txt")
