from unittest.mock import Mock

mock_obj = Mock(name='MyMock')
mock_obj.get_data.return_value = 'mocked result'
result = mock_obj.get_data('user')
mock_obj.get_data.assert_called_with('user')
print(mock_obj.get_data.call_args)
