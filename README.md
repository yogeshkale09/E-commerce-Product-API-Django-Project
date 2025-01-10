# E-commerce-Product-API-Django-Project
This project is a simple e-commerce backend API built using Django and Django REST Framework. It allows you to manage products, including adding, retrieving, updating, and deleting them. The API also includes features like filtering, sorting, pagination, and token-based authentication.

Django REST Framework is a wrapper over the default Django Framework, basically used to create APIs of various kinds. There are three stages before creating an API through the REST framework, Converting a Model’s data to JSON/XML format (Serialization), Rendering this data to the view, and Creating a URL for mapping to the views.

---

## Features

### 1] Product Management:

- Add a product

- Retrieve all products with optional filtering and sorting

- Update product details

- Delete a product

---

### 2] Additional Features:

- Pagination for product listings

- Error handling for invalid inputs

- Token-based authentication (JWT)

- Retrieve low-stock products.

---

## API Endpoints

### Authentication

- *POST /api/token/:* Obtain JWT token.

- *POST /api/token/refresh/:* Refresh JWT token.

### Products

- *POST /products/:* Add a new product.

  - *Input:* name, description, price, stock, category.

- *GET /products/:* Retrieve all products with optional filters and sorting.

  - *Filters:* category, price (ascending/descending).

- *PUT /products/{id}/:* Update product details (except id).

- *DELETE /products/{id}/:* Delete a product.

- *GET /products/low-stock/:* Retrieve products with low stock.

---

## Data Validation

- *Name:* Must be unique and required.

- *Price:* Must be a positive number.

- *Stock:* Must be a non-negative integer.

---
## Installation

1. *Clone the Repository:*

- git clone <repository-url>
- cd ecommerce

2. *Create and Activate a Virtual Environment:*

- python -m venv ecommerceenv
- ecommerceenv\Scripts\activate

3. *Install Dependencies:*

- pip install -r requirements.txt

4. *Apply Migrations:*

- python manage.py migrate
- python manage.py makemigrations

5. *Run the Server:*

- python manage.py runserver

---

## Running Tests

Unit tests are included for critical functionality. Run them using:

- python manage.py test

---

## Technologies Used

- Python

- Django

- Django REST Framework

- JWT for authentication

- SQLite
---

## Future Improvements

- Add support for multiple users with role-based permissions.

- Enhance the filtering and searching capabilities.

- Add support for product images.
![Screenshot 2025-01-10 123649](https://github.com/user-attachments/assets/93892813-bb08-4fd3-abc7-f18776ff84e2)
![Screenshot 2025-01-10 123720](https://github.com/user-attachments/assets/ea10fbb8-0451-4ccf-80ea-4d3d6ced4e52)
![Screenshot 2025-01-10 123850](https://github.com/user-attachments/assets/26174e73-6792-49e3-9077-cf7cf87035fd)
![Screenshot 2025-01-10 124059](https://github.com/user-attachments/assets/d8c93bb7-7efc-447f-9466-a33d0ae7944e)
