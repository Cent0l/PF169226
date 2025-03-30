from unittest.mock import Mock

class Sample:
    def method(self, arg):
        pass

def side_effect_function(arg):
    return f"modified {arg}"

mock_obj = Mock(spec=Sample)

mock_obj.method.side_effect = ['first call', 'second call']
print(mock_obj.method())
print(mock_obj.method())

mock_obj.method.side_effect = side_effect_function
print(mock_obj.method('data'))

mock_obj.method.side_effect = ValueError("An error occurred")
#mock_obj.method()  # odkomentuj, żeby zobaczyć wyjątek
