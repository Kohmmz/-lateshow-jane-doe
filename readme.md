# Late Show API

## Description
The Late Show API is a Flask-based RESTful API that manages episodes, guests, and their appearances on a late-night talk show. It uses **Flask-RESTful**, **SQLAlchemy**, and **Flask-Migrate** to handle database interactions and migrations.

## Features
- Retrieve a list of episodes
- Retrieve details of a specific episode
- Retrieve a list of guests
- Add a new guest appearance with a rating
- Enforce data validations (e.g., ratings must be between 1 and 5)

## Technologies Used
- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- SQLAlchemy-Serializer

## Installation
### Prerequisites
Ensure you have **Python 3.7+** and **Pipenv** installed.

### Setup Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Kohmmz/-lateshow-jane-doe.git
   cd -lateshow-jane-doe
   ```
2. Install dependencies using Pipenv:
   ```sh
   pipenv install
   ```
3. Activate the virtual environment:
   ```sh
   pipenv shell
   ```
4. Initialize the database:
   ```sh
   flask db upgrade
   ```
5. Run the Flask app:
   ```sh
   python app.py
   ```

## API Endpoints
### **Episodes**
#### **GET /episodes**
Returns a list of all episodes.

#### **GET /episodes/<id>**
Returns details of a specific episode by ID.

### **Guests**
#### **GET /guests**
Returns a list of all guests.

### **Appearances**
#### **POST /appearances**
Creates a new guest appearance with a rating.

**Request Body:**
```json
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}
```

**Response Body:**
```json
{
  "id": 1,
  "rating": 5,
  "episode": {
    "id": 1,
    "date": "2023-04-01",
    "number": 100
  },
  "guest": {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
}
```

## Validations
- **Rating** must be between **1 and 5**.
- **episode_id** and **guest_id** must reference existing records.

## License
This project is licensed under the MIT License.

