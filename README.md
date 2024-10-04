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
   http://127.0.0.1:8000/api/books/
   

6. **Post API**:
    ```bash
     http://127.0.0.1:8000/api/books/create/
    





