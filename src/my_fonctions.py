import json

class MyFonctions:
    @staticmethod
    def write_file_real_days(value: str):
        # Open a file in write mode
        try:
            data = {"days": {"rr": value}}

            # Specify the file name
            file_name = "days.json"

            # Open the file in write mode and use json.dump() to write the data as JSON
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print("Data written successfully.")
        except Exception as e:
            print("An error occurred:", e)
    @staticmethod
    def write_file_days_form_file(value: str):
        # Open a file in write mode
        try:
            data = {"days": {"rr": value}}

            # Specify the file name
            file_name = "days.json"

            # Open the file in write mode and use json.dump() to write the data as JSON
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print("Data written successfully.")
        except Exception as e:
            print("An error occurred:", e)