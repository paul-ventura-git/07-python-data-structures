# Immutable types like strings and numbers are hashable and work well as dictionary keys.
# You can also use tuple objects as dictionary keys as long as they contain only hashable types themselves.

phonebook = {
  "bob": 7387,
  "alice": 3719,
  "jack": 7052,
}

print(phonebook)

squares = {x: x * x for x in range(6)}

print(squares)