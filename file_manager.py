import csv
import json

class FileManager:
    csv_file = "studenter_labb2_v25.csv"
    json_file = "studenter.json"

    @staticmethod
    def read_csv_and_save_to_json():
        headers = [] # fråga ullis om headers ska vara med!!!!!!!!!!!!!!!!!!!!!!!!!
        students = []

        with open(FileManager.csv_file, 'r') as csv_file_obj:
            csv_reader = csv.DictReader(csv_file_obj)

            headers = next(csv_reader)

            for row in csv_reader:
                students.append(row)

        with open(FileManager.json_file, 'w', encoding='Latin-1') as json_file_obj:
            json.dump(students, json_file_obj, ensure_ascii=False, indent=4)



    def add_person(self):
        pass

    def remove_person(self):
        pass

    @staticmethod
    def show_all_data():
        try:
            with open(FileManager.json_file, 'r', encoding='Latin-1') as json_file_obj:
                json_data = json.load(json_file_obj)
                print(json.dumps(json_data, indent = 4, ensure_ascii =  False)) # vi skriver ut innehållet snyggt
        except FileNotFoundError:
            print("Fel. Filen existerar inte.")
        except json.JSONDecodeError:
            print("Fel. Det gick inte att avkoda filen")






    def save_json_to_csv(self):
        pass