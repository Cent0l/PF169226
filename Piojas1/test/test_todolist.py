import unittest
from src.todolist import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        self.todo.add_task("Kup mleko")
        self.assertIn("Kup mleko", self.todo.tasks)
        self.assertFalse(self.todo.tasks["Kup mleko"])

    def test_add_invalid_task(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("")
        with self.assertRaises(ValueError):
            self.todo.add_task(None)

    def test_complete_task(self):
        self.todo.add_task("Umyć samochód")
        self.todo.complete_task("Umyć samochód")
        self.assertTrue(self.todo.tasks["Umyć samochód"])

    def test_complete_nonexistent_task(self):
        with self.assertRaises(KeyError):
            self.todo.complete_task("Nieistniejące zadanie")

    def test_get_active_tasks(self):
        self.todo.add_task("Zrobić zakupy")
        self.todo.add_task("Wynieść śmieci")
        self.todo.complete_task("Wynieść śmieci")
        self.assertEqual(self.todo.get_active_tasks(), ["Zrobić zakupy"])

    def test_get_completed_tasks(self):
        self.todo.add_task("Nauczyć się Pythona")
        self.todo.add_task("Przeczytać książkę")
        self.todo.complete_task("Nauczyć się Pythona")
        self.assertEqual(self.todo.get_completed_tasks(), ["Nauczyć się Pythona"])

if __name__ == "__main__":
    unittest.main()
