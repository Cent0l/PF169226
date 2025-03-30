from unittest.mock import Mock

mock_obj = Mock()
mock_obj.a()
mock_obj.b(1)
print("Przed resetowaniem:")
print("call_count:", mock_obj.call_count)
print("mock_calls:", mock_obj.mock_calls)

mock_obj.reset_mock()
print("\nPo resetowaniu:")
print("call_count:", mock_obj.call_count)
print("mock_calls:", mock_obj.mock_calls)

mock_obj.return_value = 'result'
mock_obj()
print("\nZ return_value:", mock_obj())
mock_obj.reset_mock(return_value=False)
print("Po reset_mock(return_value=False):", mock_obj())

mock_obj = Mock()
mock_obj.child = Mock()
mock_obj.child()
print("\nZagnieżdżony mock przed reset:")
print("child.mock_calls:", mock_obj.child.mock_calls)

mock_obj.reset_mock()
print("Zagnieżdżony mock po reset:")
print("child.mock_calls:", mock_obj.child.mock_calls)
