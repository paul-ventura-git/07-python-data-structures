# Mutable Arrays of Single Bytes

arr = bytearray((0, 1, 2, 3))

arr[1] = 23
print(arr[1])

del arr[1]
print(arr)

arr.append(42)
print(arr)

mybytes = bytes(arr)
print(mybytes)