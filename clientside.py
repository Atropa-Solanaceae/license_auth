import socket
import os

def send_key(key, server_ip, server_port):
    try:
        client_socket = socket.create_connection((server_ip, server_port), timeout=5)
    except ConnectionRefusedError:
        print('Server authentication failed: Connection refused')
        input('\nPress Enter to exit...')
        return
    except TimeoutError:
        print('Server authentication failed: Connection timed out')
        input('\nPress Enter to exit...')
        return

    try:
        send_key_protocol(client_socket, key)
    except Exception as e:
        print('Error:', e)
        print('Server authentication failed')
        input('\nPress Enter to exit...')
    finally:
        client_socket.close()

def send_key_protocol(client_socket, key):
    try:
        client_socket.sendall(key.encode())
        response = client_socket.recv(1024).decode()
        print('Server response:', response)
    except socket.timeout:
        print('Server authentication failed: Connection timed out')
        input('\nPress Enter to exit...')
    except Exception as e:
        print('Error:', e)
        print('Server authentication failed')
        input('\nPress Enter to exit...')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# Prompt the user to enter a key
key = input('Enter your license key: ')
print("\nSending key to server...\n")

# Call the function to send the key and receive the validation result
server_ip = "10.10.10.10"
server_port = 10000
send_key(key, server_ip, server_port)
