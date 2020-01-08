import sys
import ctypes
import struct

a = 59
x = y = a
b = 125.54
c = 'Hello World!'

print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))

print('*' * 50)
print(id(b))
print(sys.getsizeof(b))

z = b
b = 122.99
print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))
print(id(float))

print('*' * 50)
print(id(c))
print(sys.getsizeof(c))

print(ctypes.string_at(id(c), sys.getsizeof(c)))
print(struct.unpack('LLLLLLLLLLli' + 'c'*13, ctypes.string_at(id(c), sys.getsizeof(c))))
print(id(str))

print('*' * 50)
print(id(lst))
print(sys.getsizeof(lst))

print(ctypes.string_at(id(lst), sys.getsizeof(lst)))
print(struct.unpack('LLLL' + 'L'*5*4, ctypes.string_at(id(lst), sys.getsizeof(lst))))
print(id(list))
