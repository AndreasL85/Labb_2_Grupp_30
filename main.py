import file_manager # vi importerar klassen FileManager från file_manager.py

file_mgr = file_manager.FileManager() # vi skapar ett objekt från klassen FileManager

# vi skapar en meny med funktionen show_meny
def show_menu():
    print("1. Read CSV and save to JSON")
    print("2. Add person (to JSON file)")
    print("3. Remove person (from JSON file)")
    print("4. Show all data in JSON file")
    print("5. Save JSON to CSV")
    print("6. Exit")


def main():
    while True: # while sats för de olika alternativen i menyn. Fortsätter loopas tills ett giltigt svar skrivs in
        show_menu() # anropar funktionen????????
        choice = input("Enter your choice: ")

        if choice == "1":
            file_mgr.read_csv_and_save_to_json()
        elif choice == "2":
            file_mgr.add_person()
        elif choice == "3":
            file_mgr.remove_person()
        elif choice == "4":
            file_mgr.show_all_data()
        elif choice == "5":
            file_mgr.save_json_to_csv()
        elif choice == "6":
            print("Program exited.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()