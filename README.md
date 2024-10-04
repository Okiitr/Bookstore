## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Okiitr/Bookstore.git
   cd Bookstore
   
2. **Set venv**:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate # On Windows use `.\myvenv\Scripts\activate`
   
4. **Install requirements and runserver**:
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

5. **Get API**:
   ```bash
   curl -u username:password "http://127.0.0.1:8000/api/books/
   curl -u username:password "http://127.0.0.1:8000/api/books/?author=J.K. Rowling&published_date=2024-10-04

6. **Post API**:
    ```bash
    curl -u username:password -X POST \
   -H "Content-Type: application/json" \
   -d '{
          "title": "The Great Gatsby",
          "author": "F. Scott Fitzgerald",
          "published_date": "1925-04-10",
          "price": 10.99,
          "stock": 50
      }' \
   http://127.0.0.1:8000/api/books/create/
    





