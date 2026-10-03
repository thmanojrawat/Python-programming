# Binary data types

data_bytes = b"Hello"
data_bytearray = bytearray(b"Hello")
data_memoryview = memoryview(b"Hello")

print(data_bytes, type(data_bytes))
print(data_bytearray, type(data_bytearray))
print(data_memoryview, type(data_memoryview))
