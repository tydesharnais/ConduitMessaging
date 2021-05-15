from cryptography.fernet import Fernet
from time import sleep

message = input('Message to Encrypt: ')
messagebytes = message.encode()
key = Fernet.generate_key()
print(f"The Key {key}")
f = Fernet(key)
encrypted = f.encrypt(messagebytes)
print(f'Encrypted message {encrypted}')
decrypted = f.decrypt(encrypted)
sleep(5)
print(f'Decrypted message {decrypted}')
if messagebytes == decrypted:
    print('True')
    sleep(10)
else:
    print('False')
