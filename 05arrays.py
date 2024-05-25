# array.array : They're type arrays constrained to a single data type

import array

# array of only floats
arr = array.array("f", (1.0, 1.5, 2.0, 2.5))

print(arr[1])

print(arr)

del arr[1]

print(arr)

arr.append(42.88)

print(arr)