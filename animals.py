class Animal:
    diet = "Omnivore"

    def __init__(self, id, name, species, kingdom, age, health, habitat, is_hungry=True):
        self.id = str(id)
        self.name = name
        self.species = species
        self.kingdom = kingdom
        self.age = age
        self.health = health
        self.habitat = habitat
        self.is_hungry = is_hungry

    # Function for feeding (food_type is optional so all subclasses share the same signature)
    def feeding(self, food_type=None):
        if not self.is_hungry:
            return f"{self.name} is not hungry right now."
        self.is_hungry = False
        return f"{self.name} has been fed and is no longer hungry."

    # Function for health check
    def heal(self):
        self.health = 100
        return f"{self.name} has been treated and is now fully healthy."

    # Function to summarise everything in this class
    def get_status(self):
        if self.is_hungry:
            hunger_state = "Hungry"
        else:
            hunger_state = "Full"

        return f"[{self.id}] {self.name} the {self.species} ({self.diet}) | Health: {self.health} | Status: {hunger_state}"


class Carnivore(Animal):
    diet = "Carnivore"

    def feeding(self, food_type=None):
        if not self.is_hungry:
            return f"{self.name} is not hungry right now."
        if food_type is None:
            return f"{self.name} needs to be given some meat."
        if food_type.lower() == "meat":
            self.is_hungry = False
            return f"{self.name} happily ate its meal."
        return f"{self.name} refuses to eat {food_type}. It needs meat!"


class Herbivore(Animal):
    diet = "Herbivore"
    accepted_foods = ["plant", "plants", "vegetable", "vegetables", "fruit", "fruits", "grass", "hay", "leaves"]

    def feeding(self, food_type=None):
        if not self.is_hungry:
            return f"{self.name} is not hungry right now."
        if food_type is None:
            return f"{self.name} needs to be given some plants."
        if food_type.lower() in self.accepted_foods:
            self.is_hungry = False
            return f"{self.name} happily ate the {food_type}."
        return f"{self.name} refuses to eat {food_type}. It needs plants!"


# Maps the diet name (as stored in the database) to the class that should be created
DIET_CLASSES = {
    "carnivore": Carnivore,
    "herbivore": Herbivore,
    "omnivore": Animal,
}


def create_animal(diet, *args, **kwargs):
    """Creates the correct Animal subclass for the given diet."""
    animal_class = DIET_CLASSES.get(str(diet).strip().lower(), Animal)
    return animal_class(*args, **kwargs)
