import sys

from .dependency_container import DepedencyContainer

def main():
    controller = DepedencyContainer.get_memory_controller()
    
    while True:
        print("\nMemory CLI")
        print("1. Store Data")
        print("2. Read Data")
        print("3. Display Memory")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            raw_data = input("Enter the data to store: ")
            success = controller.store(raw_address, raw_data)
            raw_address = input("\nEnter the address to store data: ")
            if success:
                print("Data stored successfully.")
            # else:
            #     print("Failed to store data.")

        elif choice == '2':
            raw_address = input("\nEnter the address to read data from: ")
            data_value = controller.read(raw_address)
            if data_value:
                print(f"Data read successfully: {data_value}")
            # else:
            #     print("No data found at the specified address.")

        elif choice == '3':
            print("Current Memory State:")
            print(controller.display())

        elif choice == '4':
            print("Exiting CLI.")
            sys.exit(0)

        else:
            print("Invalid choice. Please select a valid option.")