from unittest.mock import Mock, call

mock_obj = Mock()

mock_obj.func(1, 2)
mock_obj.func(a=3, b=4)

expected1 = call(1, 2)
expected2 = call(a=3, b=4)

print("Porównanie pojedynczych wywołań:")
print(expected1 == mock_obj.mock_calls[0])
print(expected2 == mock_obj.mock_calls[1])

expected_calls = call.func.call_list([
    call(1, 2),
    call(a=3, b=4)
])
print("\nLista oczekiwanych wywołań (call_list):")
print(expected_calls)

print("\nStruktura obiektu call:")
print("args:", expected1[1])
print("kwargs:", expected2[2])

print("\nDziałanie call z argumentami pozycyjnymi i nazwanymi:")
print(call(10, x=5))
