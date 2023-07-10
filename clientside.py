import socket

def send_key(key, server_ip, server_port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)

    try:
        send_key_protocol(client_socket, key)
    except Exception as e:
        print('Error:', e)
    finally:
        # Close the connection
        client_socket.close()

def send_key_protocol(client_socket, key):
    # Get the client's IP address and port
    client_ip = client_socket.getsockname()[0]
    client_port = client_socket.getsockname()[1]

    # Include the client's IP address in the key
    key_with_ip = f"{key} ({client_ip}:{client_port})"

    # Send the key
    client_socket.sendall(key_with_ip.encode('utf-8'))

    # Receive the validation result
    validation_result = client_socket.recv(1024).decode('utf-8')
    print('Validation result:', validation_result)

# Prompt the user to enter a key
key = input('Enter your license key: ')

# Call the function to send the key and receive the validation result
server_ip = "10.10.10.10"
server_port = 10000
send_key(key, server_ip, server_port)