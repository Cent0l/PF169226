from unittest.mock import Mock, MagicMock

magic = MagicMock()
magic.__len__.return_value = 10
magic.__add__.return_value = 'added'
magic.__getitem__.return_value = 'item'
magic.__str__.return_value = 'MagicMock object'

print(len(magic))
print(magic + 5)
print(magic[0])
print(str(magic))

mock = Mock()
try:
    print(len(mock))
except Exception as e:
    print("Mock len error:", e)

with MagicMock() as m:
    print("Inside with:", m)
