import socket
import threading
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9999))

server_public_key = RSA.import_key(client_socket.recv(1024))
cipher_rsa = PKCS1_OAEP.new(server_public_key)

aes_key = get_random_bytes(16)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)
client_socket.send(encrypted_aes_key)

def encrypt_message(key, msg):
    cipher_aes = AES.new(key, AES.MODE_EAX)
    nonce = cipher_aes.nonce
    ciphertext, tag = cipher_aes.encrypt_and_digest(msg.encode('utf-8'))
    return nonce + ciphertext

def receive_messages():
    while True:
        try:
            pass
        except Exception as e:
            print(f"\nError receiving message: {e}")
            break

receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

while True:
    message = input("Enter message ('exit' to quit): ")
    encrypted_msg = encrypt_message(aes_key, message)
    
    client_socket.send(encrypted_msg[:16])
    client_socket.send(encrypted_msg[16:])
    
    if message == "exit":
        break

client_socket.close()
sys.exit()