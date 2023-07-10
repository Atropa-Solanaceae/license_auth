FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /appdir

# Copy the server-side code and the valid_keys.txt file into the container
COPY server_handler.py /appdir/
COPY valid_keys.txt /appdir/
COPY IP_note.txt /appdir/

# Install the required dependencies
RUN pip install --no-cache-dir socket

# Run the server-side code when the container starts
CMD [ "python", "./server_handler.py" ]