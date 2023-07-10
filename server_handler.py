import socket

def validate_message(message):
    # Extract the client's IP address from the message
    client_ip = message.split()[1][1:-1]

    # Read the valid keys from the file
    with open('valid_keys.txt', 'r') as file:
        valid_keys = file.read().splitlines()

    if message.split()[0] in valid_keys:
        return validation_noting(client_ip, message, valid_keys)
    else:
        return f'Invalid key {message.split()[0]}.'

def validation_noting(client_ip, message, valid_keys):
    # Read existing IP addresses from the IP_note.txt file
    with open('IP_note.txt', 'r') as ip_file:
        existing_ips = ip_file.read().splitlines()

    # Check if the IP is already present
    ip_entry = next((entry for entry in existing_ips if entry.startswith(client_ip)), None)

    # Determine the validation result
    validation_result = '[VALID]' if message.split()[0] in valid_keys else '[INVALID]'

    # Update the IP entry with the validation result if IP is already present
    if ip_entry:
        ip_entry = f'{client_ip} {validation_result}'
    else:
        # Add a new IP entry with the validation result
        ip_entry = f'{client_ip} {validation_result}'
        existing_ips.append(ip_entry)

    # Save the IP addresses to the IP_note.txt file, one IP per line
    with open('IP_note.txt', 'w') as ip_file:
        ip_file.write('\n'.join(existing_ips))

    if validation_result == '[VALID]':
        return f'Valid key {message.split()[0]}.'
    else:
        return f'Invalid key {message.split()[0]}.'


def handle_connection(connection):
    try:
        # Receive the data
        data = connection.recv(1024).decode('utf-8')
        print('Received message:', data)

        # Validate the message
        validation_result = validate_message(data)

        # Send the validation result back to the client
        connection.sendall(validation_result.encode('utf-8'))
        print('Validation result sent:', validation_result)
    except Exception as e:
        print('Error:', e)
    finally:
        # Close the connection
        connection.close()

def start_server(server_ip, server_port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port
    server_address = (str(server_ip), int(server_port))
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print('Server started. Waiting for a message...')

    while True:
        # Accept a connection
        connection, client_address = server_socket.accept()

        # Handle the connection
        handle_connection(connection)


# Start the server
try:
    server_ip = "10.10.10.10"
    server_port = 10000
    start_server(server_ip, server_port)
except KeyboardInterrupt:
    print('Server stopped.')