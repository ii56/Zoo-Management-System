class Enclosure:
    def __init__(self, name, biome, capacity):
        self.name = name
        self.biome = biome
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        if animal in self.animals:
            return f"Failure: {animal.name} is already in {self.name}."
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            return f"Success: {animal.name} the {animal.species} was added to {self.name}."
        else:
            return f"Failure: {self.name} is at maximum capacity ({self.capacity}). Cannot add {animal.name}."

    def remove_animal(self, animal_id):
        for animal in self.animals:
            if str(animal.id) == str(animal_id):
                self.animals.remove(animal)
                return f"Success: Animal ID {animal_id} removed from {self.name}."

        return f"Failure: Animal ID {animal_id} not found in {self.name}."

    def get_occupants(self):
        if not self.animals:
            return f"{self.name} is currently empty."

        occupants_list = [f"[{a.id}] {a.name} ({a.species})" for a in self.animals]
        return f"Occupants of {self.name}: " + ", ".join(occupants_list)

    def get_summary(self):
        return f"{self.name} | Biome: {self.biome} | {len(self.animals)}/{self.capacity} occupied"
