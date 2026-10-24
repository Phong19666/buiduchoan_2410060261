import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

key = RSA.generate(2048)
private_key = PKCS1_OAEP.new(key)
public_key = key.publickey().export_key()

def handle_client(client_socket, address):
    print(f"Connected with {address}")
    client_socket.send(public_key)
    
    encrypted_aes_key = client_socket.recv(256)
    aes_key = private_key.decrypt(encrypted_aes_key)
    
    while True:
        try:
            nonce = client_socket.recv(16)
            ciphertext = client_socket.recv(1024)
            if not ciphertext:
                break
                
            cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            message = cipher_aes.decrypt(ciphertext).decode('utf-8')
            print(f"Received from {address}: {message}")
            
            if message.lower() == 'exit':
                print(f"Connection with {address} closed")
                break
        except:
            break
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(5)
print("Server is listening on port 9999...")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client, addr)).start()