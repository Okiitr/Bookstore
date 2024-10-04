## Installation
1. **Set venv**:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate # On Windows use `.\myvenv\Scripts\activate`
   
2. **Clone the repository**:
   ```bash
   git clone https://github.com/Okiitr/Bookstore.git
   cd Bookstore
   
3. **Install requirements and runserver**:
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

4. **Get API**:
   ```bash
   http://127.0.0.1:8000/api/books/
   

5. **Post API**:
    ```bash
     http://127.0.0.1:8000/api/books/create/
    





