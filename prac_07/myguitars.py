import csv
import os
from guitar import Guitar

def load_guitars_from_file(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    if not os.path.exists(filename):
        return guitars
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars_to_file(guitars, filename):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def get_new_guitar():
    """Prompt the user to enter details for a new guitar and return a Guitar object."""
    name = input("Enter guitar name (or 'q' to quit): ").strip()
    if name.lower() == 'q':
        return None

    while True:
        try:
            year = int(input("Enter year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    while True:
        try:
            cost = float(input("Enter cost: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid cost.")

    return Guitar(name, year, cost)

def main():
    """Main function to load, display, add, and save guitars."""
    filename = "guitars.csv"
    guitars = load_guitars_from_file(filename)

    # Sort guitars by year
    guitars.sort()

    # Display guitars
    if guitars:
        print("\nGuitars:")
        for guitar in guitars:
            print(guitar)
    else:
        print("No guitars found.")

    # Add new guitars
    print("\nAdd new guitars:")
    while True:
        new_guitar = get_new_guitar()
        if new_guitar is None:
            break
        guitars.append(new_guitar)

    # Sort guitars again after adding new ones
    guitars.sort()

    # Save guitars to file
    save_guitars_to_file(guitars, filename)

if __name__ == '__main__':
    main()
