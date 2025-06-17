# Pizza API Challenge

## Overview
This project implements a RESTful API for a Pizza Restaurant using Flask. It follows the MVC (Model-View-Controller) architecture and includes models for restaurants, pizzas, and a join table for restaurant-pizza relationships.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/pizza-api-challenge.git
   cd pizza-api-challenge
   ```

2. **Create a virtual environment and install dependencies:**
   ```
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```

3. **Set up the database:**
   ```
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. **Seed the database:**
   Write your seed data in `server/seed.py` and run:
   ```
   python server/seed.py
   ```

## Route Summary

### Restaurants
- **GET /restaurants**
  - Returns a list of all restaurants.
  
- **GET /restaurants/<int:id>**
  - Returns details of a single restaurant and its pizzas.
  - Error response if not found: `{ "error": "Restaurant not found" }` (404)

- **DELETE /restaurants/<int:id>**
  - Deletes a restaurant and all related RestaurantPizzas.
  - Success response: `204 No Content`
  - Error response if not found: `{ "error": "Restaurant not found" }` (404)

### Pizzas
- **GET /pizzas**
  - Returns a list of pizzas.

### Restaurant Pizzas
- **POST /restaurant_pizzas**
  - Creates a new RestaurantPizza.
  - Request body:
    ```json
    { "price": 5, "pizza_id": 1, "restaurant_id": 3 }
    ```
  - Success response:
    ```json
    { "id": 4, "price": 5, "pizza_id": 1, "restaurant_id": 3, "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" }, "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "address3" } }
    ```
  - Error response:
    ```json
    { "errors": ["Price must be between 1 and 30"] }
    ```
    (400 Bad Request)

## Validation Rules
- The `price` for RestaurantPizza must be between 1 and 30.

## Postman Usage Instructions
1. Open Postman.
2. Import the Postman collection:
   - Click on "Import" → "Upload" and select `challenge-1-pizzas.postman_collection.json`.
3. Test each route using the provided examples in the collection.

## License
This project is licensed under the MIT License.