# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install GDAL dependencies
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

# Set environment variables
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

#RUN python manage.py migrate

#RUN python manage.py import_truck_data

# Run Gunicorn when the container launches
CMD gunicorn truck.wsgi:application --bind 0.0.0.0:8000
