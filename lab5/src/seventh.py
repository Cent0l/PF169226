from unittest.mock import Mock, ANY

mock_obj = Mock()

mock_obj.process(1, 'data', {'key': 'value'})
mock_obj.process.assert_called_with(1, ANY, ANY)

mock_obj.complex_call(user='admin', password='secret', retries=3)
mock_obj.complex_call.assert_called_with(user=ANY, password=ANY, retries=3)

print(ANY == 'anything')
print(ANY == 123)
print(ANY == {'a': 1})
print(ANY == None)

class CustomValidator:
    def __eq__(self, other):
        return isinstance(other, dict) and 'key' in other

mock_obj.check({'key': 123})
mock_obj.check.assert_called_with(CustomValidator())
