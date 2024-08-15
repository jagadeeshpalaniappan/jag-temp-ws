# Use an official Python runtime as a base image
FROM phidata/python:3.11.5

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Install PHIDATA dependency
# RUN pip install phidata

# Expose port 8501 and map it to port 8501 on the host machine
EXPOSE 8501


# Run the Streamlit app when the container starts
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]