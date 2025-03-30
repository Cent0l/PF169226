from unittest.mock import Mock

mock_obj = Mock()

mock_obj.test_method(1)
mock_obj.test_method(2, key='value')
mock_obj.test_method('abc', 3)

print(mock_obj.test_method.called)
print(mock_obj.test_method.call_count)
print(mock_obj.test_method.call_args_list)
print(mock_obj.test_method.call_args)
