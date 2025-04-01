class HistoryManager:
    def __init__(self):
        self.history = []

    def add_operation(self, operation):
        self.history.append(operation)

    def get_operations(self):
        return self.history
