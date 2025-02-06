import csv # vi importerar CSV-modulen
import json #vi importerar JSON-modulen

class FileManager: # vi skapar en klass
    # tilldelar klassvariabler till filerna
    csv_file = "studenter_labb2_v25_Ny.csv"
    json_file = "studenter.json"

    @staticmethod # vi använder static för att läsa CSV och spara till JSON
    def read_csv_and_save_to_json():
        students = [] # lista för studenter

        # vi öppnar CSV-filen i läsläge och lagras i variabeln csv_file_obj
        with open(FileManager.csv_file, "r", encoding = "utf-8-sig") as csv_file_obj:
            csv_reader = csv.DictReader(csv_file_obj) # CSV läses in som en ordlista (rad för rad)

            # vi hoppar över rubrikerna
            next(csv_reader)

            # vi loopar igenom varje rad i CSV-filen
            for row in csv_reader:
                students.append(row) # för varje loopvarv läggs en ny rad till (som en dictionary) i listan för studenter med hjälp av "append"

        # vi öppnar JSON-filen i skrivläge
        # vi tecken-kodar för att vi ska kunna skriva ut "åöä"
        with open(FileManager.json_file, "w", encoding = "utf-8-sig") as json_file_obj:
            json.dump(students, json_file_obj, ensure_ascii = False, indent = 4) # vi sparar ner datan i json filen
        print("File saved to JSON")


    @staticmethod
    # vi använder en metod för att lägga till en person i JSON-filen
    def add_person():
            try:
                with open(FileManager.json_file, "r", encoding = "utf-8-sig") as json_file_obj: # vi öppnar filen i läsläge
                    data = json_file_obj.read() # vi läser filen

                    # om filen är tom skapar vi en tom lista
                    if not data.strip():
                        students = []
                    else:
                        students = json.loads(data) # vi laddar in json-filen som en lista i python

            # saknas filen eller inte funkar, så skapar vi en tom lista
            except (FileNotFoundError, json.JSONDecodeError):
                students = []

            print("Add info about student")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            user_name = input("Username: ")

            # vi skapar en dictionary för den nya studenten
            new_person = {
                "efternamn": last_name,
                "förnamn": first_name,
                "användarnamn": user_name
            }

            students.append(new_person) # vi lägger till ny student på slutet av listan

            # vi öppnar JSON-filen i skrivläge
            with open(FileManager.json_file, "w", encoding = "utf-8-sig") as json_file_obj:
                # vi sparar ner datan i json filen
                json.dump(students, json_file_obj, ensure_ascii = False, indent = 4)

            print("New student added")




    @staticmethod
    # vi använder denna metod för att ta bort person från JSON-filen
    def remove_person():
        try:
            with open(FileManager.json_file, "r", encoding = "utf-8-sig") as json_file_obj:

                data = json_file_obj.read()  # vi läser filen

                # om filen är tom återvänder till menyn
                if not data.strip():
                    print("File is empty")
                    return
                else:
                    students = json.loads(data)  # vi laddar in json-filen som en lista i python

            print("Enter student username that you want to remove")
            erase_student = input("Username: ")

            student_found = False # vi kollar om studenten finns
            # vi loopar igenom listan med studenter
            for student in students:
                # om studenten finns, tar vi bort den
                if student["användarnamn"] == erase_student:
                    students.remove(student)
                    student_found = True
                    break # vi stoppar loopen när studenten hittats och tagits bort

            # om inte studenten kan hittas
            if not student_found:
                print(f"Error. Could not find student {erase_student}")
                return

            with open(FileManager.json_file, "w", encoding = "utf-8-sig") as json_file_obj:
                json.dump(students, json_file_obj, ensure_ascii = False, indent = 4)

            print("Student removed")
        except FileNotFoundError:
            print("Error. File does not exist.") # finns inte filen skriver vi ut felmeddelande
        except json.JSONDecodeError:
            print("Error. Could not decode file") # felmeddelande vid avkodning




    # vi lägger till en metod som är statisk för att visa all data från JSON-filen
    @staticmethod
    def show_all_data():
        try: # vi försöker exekvera koden i try-blocket
            with open(FileManager.json_file, "r", encoding = "utf-8-sig") as json_file_obj:
                json_data = json.load(json_file_obj) # load läser in python filen samt konverterar den till en lista av dictionaries

                if not json_data:
                    print("The list is empty")
                    return

                print(json.dumps(json_data, indent = 4, ensure_ascii =  False)) # vi skriver ut innehållet snyggt
        except FileNotFoundError:
            print("Fel. Filen existerar inte.") # finns inte filen skriver vi ut felmeddelande
        except json.JSONDecodeError:
            print("Fel. Det gick inte att avkoda filen") # felmeddelande vid avkodning

    @staticmethod
    def save_json_to_csv():
        try:
            with open(FileManager.json_file, "r", encoding = "utf-8-sig") as json_file_obj:
                json_data = json.load(json_file_obj)  # load läser in python filen samt konverterar den till en lista av dictionaries

                if not json_data:
                    print("The list is empty")
                    return

        except FileNotFoundError:
            print("Fel. Filen existerar inte.")  # finns inte filen skriver vi ut felmeddelande

        except json.JSONDecodeError:
            print("Fel. Det gick inte att avkoda filen")  # felmeddelande vid avkodning

        # vi hämtar rubrikerna från första studenten
        headers = json_data[0].keys()

        with open(FileManager.csv_file, "w", newline = "", encoding = "utf-8-sig") as csv_file_obj:
            csv_writer = csv.DictWriter(csv_file_obj, fieldnames = headers)

            # vi skriver rubrikerna
            csv_writer.writeheader()
            # vi skriver ner alla studenter
            csv_writer.writerows(json_data)

        print("The CSV-file is updated with the latest JSON-data")