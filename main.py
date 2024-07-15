from person import Person
from stack import Stack
import csv

def read_people_from_csv(filename):
    # Reads data from a CSV file and creates a list of person objects.
    people = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Skip header row if there is one
        next(reader)
        for row in reader:
            if len(row) < 4:  # Check if the row has less than 4 columns
                continue
            nickname, name, family, age = row
            people.append(Person(nickname, name, family, int(age)))
        return people

def main():
    # The main function that reads people from CSV,
    # creates a stack, interacts with the user, and pops elements.
    people_data = read_people_from_csv('people.csv')
    people_stack = Stack()

    for person in people_data:
        people_stack.push(person)

    while not people_stack.is_empty():
        try:
            num_to_pop = int(input('Enter a number (1-4) to pop that many people from the stack: '))
            if num_to_pop < 1 or num_to_pop > 4:
                print('Invalid input. Please enter a number between 1 and 4.')
                continue

            for _ in range(num_to_pop):
                if people_stack.is_empty():
                    print('Stack is empty.')
                    break
                people_stack.pop()

            if not people_stack.is_empty():
                print(f'Remaining person: {people_stack.peek().name}')
            else:
                print('The stack is empty now.')
                break
        except ValueError:
            print('Invalid input. Please enter a number.')

if __name__ == "__main__":
    main()


