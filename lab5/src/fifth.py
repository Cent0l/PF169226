from unittest.mock import Mock

def custom_side_effect(arg):
    if arg == 'a':
        return 'A result'
    elif arg == 'b':
        return 'B result'
    return 'default'

mock_obj = Mock()
mock_obj.return_value = 'return value'
mock_obj.side_effect = custom_side_effect

print(mock_obj('a'))
print(mock_obj('x'))

mock_obj = Mock()
mock_obj.return_value = 'return value'
mock_obj.side_effect = lambda x: f"side {x}"
print(mock_obj('test'))  # side_effect ma priorytet nad return_value

mock_obj = Mock()
mock_obj.child = Mock()
mock_obj.child.method = Mock(return_value='nested result')
print(mock_obj.child.method())

nested = Mock()
nested.configure_mock(**{
    'x': 5,
    'y': Mock(return_value='hello'),
    'z.attr': 'nested value'
})
print(nested.x)
print(nested.y())
print(nested.z.attr)
