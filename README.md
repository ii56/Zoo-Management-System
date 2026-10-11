# Zoo Management System

A command-line zoo management system written in Python. It keeps track of animals, enclosures and staff, and stores everything in an Excel workbook (`zoo_database.xlsx`).

## Features

- Register animals with a diet (Carnivore, Herbivore or Omnivore), age, health and habitat
- Build enclosures with a maximum capacity and move animals between them
- Feed animals: carnivores only eat meat, herbivores only eat plants
- Hire zookeepers and veterinarians; vets can treat animals back to full health
- All data is saved to and loaded from `zoo_database.xlsx`

## Getting started

Requires Python 3.8+.

```bash
pip install -r requirements.txt
python main.py
```

The repository includes a sample `zoo_database.xlsx` with 10 animals, 7 enclosures and 5 staff members. Delete it to start with an empty zoo.

## Menu

| Option | Action |
| --- | --- |
| 1 | View all animals |
| 2 | Add a new animal |
| 3 | View enclosures |
| 4 | Build a new enclosure |
| 5 | Assign animal to enclosure |
| 6 | Feed an animal |
| 7 | View staff |
| 8 | Hire staff |
| 9 | Have a vet treat an animal |
| 10 | Save and exit |

Changes are only written to the database when you choose **Save and exit**.

## Project structure

| File | Contents |
| --- | --- |
| `main.py` | Menu and user input |
| `zoo_manager.py` | `ZooManager`: loading, saving and all zoo actions |
| `animals.py` | `Animal`, `Carnivore` and `Herbivore` classes |
| `enclosures.py` | `Enclosure` class |
| `staff.py` | `Employee`, `Zookeeper` and `Vet` classes |
| `zoo_database.xlsx` | Sample data (sheets: Animals, Staff, Enclosures) |

## License

MIT, see [LICENSE](LICENSE).
