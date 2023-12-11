# Food Truck Map Project

## Overview
The Food Truck Map project is a web application designed to help users discover nearby food trucks based on their current location or specified coordinates. It provides an interactive map interface for users to explore food truck locations and details.

### Features
- Find food trucks by entering latitude and longitude or clicking on the map.
- Interactive map with markers indicating food truck locations.

### Prerequisites
- Python (version 3.6 or higher)
- Django
- Django REST framework
- Leaflet (for maps)
- Docker


1. Clone the repository:
    ```bash
    git clone https://github.com/neeraj0349/food-truck.git
    cd food-truck
    ```

2. Build and run the Docker container:
    ```bash
    docker-compose up --build
    ```

3. Run migrations to set up the database:

    ```bash
    docker-compose exec web python manage.py migrate
    ```
   
4. Import food truck data:
    ```bash
    docker-compose exec web python manage.py import_truck_data
    ```
5. Access the application at http://localhost/foodtrucks/.

#### API Endpoint:
Access the API at http://localhost/api/foodtrucks/?lat=37.788457028828900&lon=-122.39301498669800.


## Usage

1. Open the application in a web browser.
2. Use the search form to enter latitude and longitude or click on the map to find nearby food trucks.
3. Explore the interactive map with food truck markers.
4. Click on food truck markers to view details.
