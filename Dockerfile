# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install the project and its dependencies
RUN pip install .

# Set the entrypoint for the container
ENTRYPOINT ["ddg-cli"]

# Default command to show help (optional)
CMD ["--help"]