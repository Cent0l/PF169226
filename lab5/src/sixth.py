from unittest.mock import Mock, call

mock_obj = Mock()

mock_obj.foo(1)
mock_obj.bar(2)
mock_obj.foo(1)

mock_obj.foo.assert_called()
mock_obj.bar.assert_called_once()
mock_obj.baz.assert_not_called()

mock_obj.foo.assert_called_with(1)
mock_obj.bar.assert_called_once_with(2)

expected_calls = [call.foo(1), call.bar(2), call.foo(1)]
mock_obj.assert_has_calls(expected_calls)
mock_obj.assert_has_calls(expected_calls, any_order=True)

print("mock_calls:", mock_obj.mock_calls)
print("method_calls:", mock_obj.method_calls)
