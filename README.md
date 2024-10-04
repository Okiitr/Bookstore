## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Okiitr/Bookstore.git
   cd Bookstore
   
2. **Set venv**:
   python -m venv myvenv
   source myvenv/bin/activate # On Windows use `myvenv\Scripts\activate`
   
3. **Install requirements and runserver**:
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
