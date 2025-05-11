import os
import json

class ApiCheck:
    def __init__(self, file_path='Api_check.json'):
        self.file_path = file_path
        self.api_data = self.load_api_data()

        if not self.api_data.get("api") or not self.api_data.get("userid"):
            self.ask_and_save_data()
        else:
            print("API and User ID already exist.")

    def load_api_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("JSON file is corrupted. Recreating...")
        return {}

    def ask_and_save_data(self):
        api = input("Enter your API: ").strip()
        userid = input("Enter your User ID: ").strip()
        self.api_data = {"api": api, "userid": userid}

        with open(self.file_path, 'w') as file:
            json.dump(self.api_data, file, indent=4)

        print("API and User ID saved successfully.")

# Usage
if __name__ == "__main__":
    try:
        api_checker = ApiCheck()
    except Exception as e:
        print(f"An error occurred: {e}")
