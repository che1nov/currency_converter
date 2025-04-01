import json
import os


class HistoryManager:
    def __init__(self, file_path="data/operations.json"):
        self.file_path = file_path
        self.operations = self.load_operations()

    def load_operations(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []

    def save_operations(self):
        with open(self.file_path, "w") as file:
            json.dump(self.operations, file, indent=4)

    def add_operation(self, operation):
        self.operations.append(operation)
        self.save_operations()

    def get_operations(self):
        return self.operations
