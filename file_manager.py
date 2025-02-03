import csv # vi importerar CSV-modulen
import json #vi importerar JSON-modulen

class FileManager: # vi skapar en klass
    # tilldelar klassvariabler till filerna
    csv_file = "studenter_labb2_v25.csv"
    json_file = "studenter.json"

    @staticmethod # vi använder static för att läsa CSV och spara till JSON
    def read_csv_and_save_to_json():
        headers = [] # fråga ullis om headers ska vara med!!!!!!!!!!!!!!!!!!!!!!!!! lista för kolumn rubriker (används ej just nu) - chat gpt
        students = [] # lista för studenter

        # vi öppnar CSV-filen i läsläge och lagras i variabeln csv_file_obj
        with open(FileManager.csv_file, 'r') as csv_file_obj:
            csv_reader = csv.DictReader(csv_file_obj) # CSV läses in som en ordlista (rad för rad)

            headers = next(csv_reader)

            # vi loopar igenom varje rad i CSV-filen
            for row in csv_reader:
                students.append(row) # för varje loopvarv läggs en ny rad till (som en dictionary) i listan för studenter med hjälp av "append"

        # vi öppnar JSON-filen i skrivläge
        # vi tecken kodar för att vi ska kunna skriva ut "åöä"
        with open(FileManager.json_file, 'w', encoding='Latin-1') as json_file_obj:
            json.dump(students, json_file_obj, ensure_ascii=False, indent=4) # vi sparar ner datan i json filen


    # vi använder en metod för att lägga till en person i JSON-filen
    def add_person(self):
        pass
    # vi använder denna metod för att ta bort person från JSON-filen
    def remove_person(self):
        pass

    # vi lägger till en metod som är statisk för att visa all data från JSON-filen
    @staticmethod
    def show_all_data():
        try: # vi försöker exekvera koden i try-blocket
            with open(FileManager.json_file, 'r', encoding='Latin-1') as json_file_obj:
                json_data = json.load(json_file_obj) # load läser in python filen samt konverterar den till en lista av dictionaries
                print(json.dumps(json_data, indent = 4, ensure_ascii =  False)) # vi skriver ut innehållet snyggt
        except FileNotFoundError:
            print("Fel. Filen existerar inte.") # finns inte filen skriver vi ut felmeddelande
        except json.JSONDecodeError:
            print("Fel. Det gick inte att avkoda filen") # felmeddelande vid avkodning






    def save_json_to_csv(self):
        pass