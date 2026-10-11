from zoo_manager import ZooManager


def get_int(prompt, min_value=None, max_value=None):
    """Keeps asking until the user enters a whole number in the allowed range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number of at least {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"Please enter a number no greater than {max_value}.")
        else:
            return value


def get_choice(prompt, options):
    """Keeps asking until the user picks one of the given options (case-insensitive)."""
    lookup = {o.lower(): o for o in options}
    while True:
        value = input(prompt).strip().lower()
        if value in lookup:
            return lookup[value]
        print(f"Please choose one of: {', '.join(options)}")


def main():
    # This automatically triggers load_data() from your __init__
    manager = ZooManager()

    print("\n=== Welcome to the Zoo Management System ===")

    while True:
        print("\n--- Main Menu ---")
        print("1. View all animals")
        print("2. Add a new animal")
        print("3. View enclosures")
        print("4. Build a new enclosure")
        print("5. Assign animal to enclosure")
        print("6. Feed an animal")
        print("7. View staff")
        print("8. Hire staff")
        print("9. Have a vet treat an animal")
        print("10. Save and Exit")

        choice = input("\nSelect an option (1-10): ").strip()

        if choice == '1':
            print("\n--- Current Zoo Animals ---")
            if not manager.animals:
                print("No animals in the zoo right now.")
            else:
                for animal in manager.animals:
                    # Uses the get_status method from animals.py
                    print(animal.get_status())

        elif choice == '2':
            print("\n--- Add New Animal ---")
            a_id = input("Enter Animal ID (e.g., 101): ")
            name = input("Enter Name: ")
            species = input("Enter Species: ")
            kingdom = input("Enter Kingdom: ")
            age = get_int("Enter Age: ", min_value=0)
            health = get_int("Enter Health (0-100): ", min_value=0, max_value=100)
            habitat = input("Enter Habitat type: ")
            diet = get_choice("Enter Diet (Carnivore/Herbivore/Omnivore): ", ["Carnivore", "Herbivore", "Omnivore"])

            result = manager.add_animal(a_id, name, species, kingdom, age, health, habitat, diet)
            print(result)

        elif choice == '3':
            print("\n--- Enclosures ---")
            if not manager.enclosures:
                print("No enclosures have been built yet.")
            else:
                for enclosure in manager.enclosures:
                    print(enclosure.get_summary())
                    print("   " + enclosure.get_occupants())

        elif choice == '4':
            print("\n--- Build Enclosure ---")
            name = input("Enter Enclosure Name: ")
            biome = input("Enter Biome (e.g., Savannah, Aquatic): ")
            capacity = get_int("Enter Maximum Capacity: ", min_value=1)

            result = manager.add_enclosure(name, biome, capacity)
            print(result)

        elif choice == '5':
            print("\n--- Assign Animal ---")
            animal_id = input("Enter the ID of the animal to move: ")
            enclosure_name = input("Enter the name of the destination enclosure: ")

            result = manager.assign_animal_to_enclosure(animal_id, enclosure_name)
            print(result)

        elif choice == '6':
            print("\n--- Feed Animal ---")
            animal_id = input("Enter the ID of the animal to feed: ")
            food_type = input("Enter the food (e.g., meat, fruit, plants): ")

            result = manager.feed_animal(animal_id, food_type)
            print(result)

        elif choice == '7':
            print("\n--- Staff ---")
            if not manager.staff:
                print("No staff have been hired yet.")
            else:
                for member in manager.staff:
                    print(member.get_details())

        elif choice == '8':
            print("\n--- Hire Staff ---")
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            role = get_choice("Enter Role (ZooKeeper/Veterinarian): ", ["ZooKeeper", "Veterinarian"])
            salary = get_int("Enter Salary: ", min_value=0)

            result = manager.hire_staff(emp_id, name, role, salary)
            print(result)

        elif choice == '9':
            print("\n--- Treat Animal ---")
            vet_id = input("Enter the vet's Employee ID: ")
            animal_id = input("Enter the ID of the animal to treat: ")

            result = manager.treat_animal(vet_id, animal_id)
            print(result)

        elif choice == '10':
            print("\nSaving database...")
            manager.save_data()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
