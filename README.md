# license_auth

This project consists of a server that listens for messages on a specified port and validates the received messages against a list of valid keys stored in a file. It also includes a client program to send messages to the server for validation.

## Prerequisites

- Python 3.9 or later
- Docker (if running the server in a Docker container)

## Getting Started

1. Clone this repository to your local machine or download the project files.
```
git clone https://github.com/Atropa-Solanaceae/license_auth
```
2. Navigate to the project directory.
```
cd license_auth
```
3. (Optional) If you want to run the server in a Docker container, make sure Docker is installed on your machine. Follow the Docker installation guide for your operating system: [Docker Documentation](https://docs.docker.com/get-docker/)
4. Populate `valid_keys.txt` with a list of valid keys, with each key on a separate line.
5. (If not using Docker) Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```
# Running the Server
## Running natively (without Docker)
1. Start the server by running the following command:
```
python3 server_handler.py
```
The server will start listening for messages on the specified port.
## Running with Docker
1. Build the Docker image by running the following command:
```
docker build -t server_handler .
```
This command will build the Docker image based on the provided Dockerfile.
2. Start the Docker container using the following command:
```
docker run -d --name server_handler -p [containerPORT]:[hostPORT] server_handler
```
This command will start a Docker container named my_server_container, mapping the container's port to the host's port.
The server is now running inside the Docker container.

# Running the Client
1. Open a new terminal window and navigate to the project directory.
2. Run the client program by executing the following command:
```
python clientside.py
```
3. Follow the prompts to enter a message.

The client program will send the message to the server for validation, and the validation result will be displayed in the terminal.
If the message is a valid key, the server will respond with "Valid key". If the message is not a valid key, the server will respond with "Invalid key".

## Customization
*Changing the server address:* If you want to change the IP address or port on which the server listens, modify the appropriate values in the  `server_handler.py` file.

*Updating the valid keys:* To update the list of valid keys, open the `valid_keys.txt` file and add/remove keys as needed.

## License
This project is licensed under the Apache 2.0 License. Feel free to use and modify it according to your needs.
