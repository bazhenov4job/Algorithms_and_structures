"""
Контроль целостности данных, аутентификация источника
"""

import hashlib


print(hashlib.sha1(b'Hello World!').hexdigest())

print(hashlib.sha1(b'Hello World.').hexdigest())

# допишем в строке дополнительный набор букв, играющий роль пароля, чтобы избежать подмены сообщения

print(hashlib.sha1(b'qwerty' + b'Hello World!').hexdigest())

# чтобы дополнительно обезопасить себя от хэш-мошенника

s = hashlib.sha1(b'Hello World.').hexdigest()

print(s.encode('utf-8'))

print(hashlib.sha1(b'qwerty' + bytes(s.encode('utf-8'))).hexdigest())
