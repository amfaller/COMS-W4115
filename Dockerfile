# Use Python3
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed Python packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install build tools (e.g., g++)
RUN apt-get update && apt-get install -y g++ && apt-get clean

# Define the default command to execute the steps in order
CMD ["sh", "-c", "python main.py test.nvp && g++ SampleClient.cpp tinyxml2/tinyxml2.cpp -std=c++11 -o sample && ./sample"]
