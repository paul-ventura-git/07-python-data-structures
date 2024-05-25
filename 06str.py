# str : Immutable Arrays of Unicode Characters

# 'str' object does not support item assignment
# 'str' object doesn't support item deletion
arr = "abcdefghijklmno"

print(arr[0:3]) # a b c

mylist= list("abcd")
print(mylist) 

unpackedIntoAList = "".join(list("abcd"))
print (unpackedIntoAList)

# Strings are recursive data structures:
print(type("abc"[0]))