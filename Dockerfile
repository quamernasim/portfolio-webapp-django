# Use the desired version of Ubuntu as the base image
FROM ubuntu:latest

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3.12-distutils \
    && rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.12
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.12 get-pip.py && \
    rm get-pip.py

# Set up a working directory for your project
WORKDIR /app

# Copy the current directory containing your Django project into the container at /app
COPY . /app

# # Install Django and any other dependencies required for your project
# RUN pip3.12 install --no-cache-dir -r requirements.txt

# # Expose the port on which your Django app will run
# EXPOSE 8000

# # Command to run your Django app using Gunicorn (adjust as needed)
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
