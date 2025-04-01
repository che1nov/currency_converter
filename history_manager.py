class HistoryManager:
    def __init__(self):
        """
        Инициализация менеджера истории операций.
        """
        self.history = []

    def add_operation(self, operation):
        """
        Добавление операции в историю.
        :param operation: Словарь с данными операции.
        """
        self.history.append(operation)

    def get_operations(self):
        """
        Получение списка всех операций.
        :return: Список операций.
        """
        return self.history
