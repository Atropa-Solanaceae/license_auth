import socket
from os import name, system

def send_key(key, server_ip, server_port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = (server_ip, server_port)

    try:
        client_socket.connect(server_address)
    except ConnectionRefusedError:
        print('Server authentication failed: Connection refused')
        return
    except TimeoutError:
        print('Server authentication failed: Connection timed out')
        return

    try:
        send_key_protocol(client_socket, key)
    except Exception as e:
        print('Error:', e)
        print('Server authentication failed')
    finally:
        # Close the connection
        client_socket.close()

def send_key_protocol(key, server_ip, server_port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Set a timeout for the connection attempt
        client_socket.settimeout(5)  # Adjust the timeout value as needed

        # Connect to the server
        server_address = (server_ip, server_port)
        client_socket.connect(server_address)
    except (socket.timeout, TimeoutError):
        print('Server authentication failed: Connection timed out')
        return

    try:
        send_key_protocol(client_socket, key)
    except Exception as e:
        print('Error:', e)
        print('Server authentication failed')
    finally:
        # Close the connection
        client_socket.close()

system('cls' if name == 'nt' else 'clear')

# Prompt the user to enter a key
key = input('Enter your license key: ')
print("\nSending key to server...\n")

# Call the function to send the key and receive the validation result
server_ip = "10.10.10.10"
server_port = 10000
send_key(key, server_ip, server_port)
