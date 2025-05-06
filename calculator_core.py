import json
import os

class Calculator:
    def __init__(self, history_file="history.json"):
        self.history_file = history_file
        self.history = self.load_history()

    def add(self, a, b):
        return self._calculate("add", a, b, a + b)

    def subtract(self, a, b):
        return self._calculate("subtract", a, b, a - b)

    def multiply(self, a, b):
        return self._calculate("multiply", a, b, a * b)

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return self._calculate("divide", a, b, a / b)

    def _calculate(self, operation, a, b, result):
        record = {"operation": operation, "a": a, "b": b, "result": result}
        self.history.append(record)
        self.save_history()
        return result

    def create_record(self, operation, a, b, result):
        self.history.append({"operation": operation, "a": a, "b": b, "result": result})
        self.save_history()

    def read_history(self):
        return self.history

    def update_record(self, index, new_data):
        if 0 <= index < len(self.history):
            self.history[index].update(new_data)
            self.save_history()
            return True
        return False

    def delete_record(self, index):
        if 0 <= index < len(self.history):
            del self.history[index]
            self.save_history()
            return True
        return False

    def save_history(self):
        with open(self.history_file, "w") as f:
            json.dump(self.history, f, indent=4)

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                return json.load(f)
        return []
