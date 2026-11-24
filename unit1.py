class Resident:
    def __init__(self, name, flat_number, maintenance_fee, status):
        self.name = name
        self.flat_number = flat_number
        self.maintenance_fee = maintenance_fee
        self.status = status

    def display(self):
        print("Resident Name:", self.name)
        print("Flat Number:", self.flat_number)
        print("Maintenance Fee:", self.maintenance_fee)
        print("Payment Status:", self.status)
        print("------------------------")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self):
        name = input("Enter resident name: ")
        flat_number = input("Enter flat number: ")
        maintenance_fee = int(input("Enter maintenance fee: "))
        status = input("Enter payment status (Paid/Pending): ")

        resident = Resident(name, flat_number, maintenance_fee, status)
        self.residents.append(resident)

        print("Resident added successfully!")

    def display_all(self):
        if len(self.residents) == 0:
            print("No resident records found.")
        else:
            for resident in self.residents:
                resident.display()


society = Society()

while True:
    print("\n--- Apartment Maintenance System ---")
    print("1. Add Resident")
    print("2. Display All Residents")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        society.add_resident()

    elif choice == "2":
        society.display_all()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")